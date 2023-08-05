import itertools
import warnings

import sheraf.exceptions
from sheraf.models.base import BaseModel, BaseModelMetaclass
from sheraf.models.indexmanager import (
    SimpleIndexManager,
    MultipleDatabaseIndexManager,
)


class BaseIndexedModelMetaclass(BaseModelMetaclass):
    def __new__(cls, name, bases, attrs):
        klass = super().__new__(cls, name, bases, attrs)
        klass.indexes = {}

        def add_index(name, index, attributes, add_to_attribute=True):
            # Get the real attributes objects when string have been passed as attributes
            # in the index.

            index.key = index.key or name
            if not index.attributes:
                raise sheraf.exceptions.SherafException(
                    f"The {index.key} index must have at least one attribute."
                )

            new_attrs = []
            for a in index.attributes:
                if isinstance(a, str):
                    try:
                        a = attributes[a]
                    except KeyError:
                        raise sheraf.exceptions.SherafException(
                            f"The {index.key} index has a wrong attribute with name '{a}'."
                        )
                if not isinstance(a, sheraf.Attribute):
                    raise sheraf.exceptions.SherafException(
                        f"The {index.key} index has a wrong attribute."
                    )

                new_attrs.append(a)
            index.attributes = new_attrs

            # Get the attributes from the attribute names
            index.values_funcs = {
                func: [
                    [
                        attributes[attr] if isinstance(attr, str) else attr
                        for attr in attrs
                    ]
                    for attrs in attrs_groups
                ]
                for func, attrs_groups in index.values_funcs.items()
            }

            for attribute in index.attributes:
                if add_to_attribute:
                    attribute.indexes[index.key] = index

                attribute.lazy = False

            # Assign the default values func to attributes without
            # values func.
            attrs_with_func = [
                attr
                for func, attr_groups in index.values_funcs.items()
                if func is not index.default_values_func
                for attrs in attr_groups
                for attr in attrs
            ]

            index.values_funcs[index.default_values_func] = [
                [attribute]
                for attribute in index.attributes
                if attribute not in attrs_with_func
            ]

            klass.indexes[index.key] = klass.index_manager(index)

        for name, index in attrs.items():
            if isinstance(index, sheraf.attributes.index.Index):
                add_index(name, index, klass.attributes)

        for attribute in klass.attributes.values():
            for index_key, index in attribute.indexes.items():
                add_index(attribute.key(klass), index, klass.attributes, False)

        return klass


class BaseIndexedModel(BaseModel, metaclass=BaseIndexedModelMetaclass):
    """
    This class handles the whole indexation mechanism. The mechanisms
    for reading or iterating over models in the database are handled
    here.
    """

    _primary_key = None
    _is_first_instance = None

    def __init__(self, *args, **kwargs):
        self._identifier = None
        super().__init__(*args, **kwargs)

    @classmethod
    def primary_key(cls):
        if cls._primary_key is None:
            for index_name, index in cls.indexes.items():
                if not index.details.primary:
                    continue

                if cls._primary_key is None:
                    cls._primary_key = index_name

                else:
                    raise sheraf.exceptions.PrimaryKeyException(
                        "A model can have only one primary key. '{}' has '{}' and '{}'".format(
                            cls.__class__.__name__,
                            cls._primary_key,
                            index_name,
                        )
                    )

        return cls._primary_key

    @classmethod
    def all(cls):
        """
        :return: A :class:`~sheraf.queryset.QuerySet` containing all the
            registered models.
        """
        return sheraf.queryset.QuerySet(model_class=cls)

    @classmethod
    def create(cls, **kwargs):
        if not cls.primary_key():
            raise sheraf.exceptions.PrimaryKeyException(
                "{} inherit from IndexedModel but has no primary key. Cannot create.".format(
                    cls.__name__
                )
            )

        return super().create(**kwargs)

    def initialize(self, **kwargs):
        if self.primary_key() in kwargs:
            identifier = kwargs[self.primary_key()]
            del kwargs[self.primary_key()]
        else:
            identifier = self.attributes[self.primary_key()].create(self)

        self.__setattr__(self.primary_key(), identifier)

        super().initialize(**kwargs)

    @classmethod
    def _check_args(cls, *args, **kwargs):
        if len(args) + len(kwargs) != 1:
            raise TypeError(
                "BaseIndexedModel.read (and variants) take only one positionnal or named parameter"
            )

        if args:
            index_name = cls.primary_key()
            key = args[0]

        else:
            index_name, key = list(kwargs.items())[0]

        try:
            index = cls.indexes[index_name]
        except KeyError:
            raise sheraf.exceptions.InvalidIndexException(
                "'{}' is not a valid index".format(index_name)
            )

        return index, key

    @classmethod
    def read(cls, *args, **kwargs):
        """
        Get a model instance from its identifier. If the model identifier is not valid, a
        :class:`~sheraf.exceptions.ModelObjectNotFoundException` is raised.

        The function takes only one parameter which key is the index where to
        search, and which value is the index identifier. If the index is
        multiple, a :class:`~sheraf.exceptions.MultipleIndexException` is
        raised.
        By default the index used is the `id` index.

        :param *args*: The ``identifier`` of the model. There can be only one positionnal or
                      keyword argument.
        :param *kwargs*: The ``identifier`` of the model. There can be only one positionnal or
                        keyword argument.
        :return: The :class:`~sheraf.models.indexation.BaseIndexedModel` matching the id.

        >>> class MyModel(sheraf.Model):
        ...     table = "my_model"
        ...     unique = sheraf.SimpleAttribute().index(unique=True)
        ...     multiple = sheraf.SimpleAttribute().index()
        ...
        >>> with sheraf.connection():
        ...     m = MyModel.create(unique="A", multiple="B")
        ...     assert MyModel.read(m.id) == m
        ...     assert MyModel.read(unique="A") == m
        ...
        >>> with sheraf.connection():
        ...     MyModel.read("invalid")
        Traceback (most recent call last):
            ...
        ModelObjectNotFoundException
        >>> with sheraf.connection():
        ...     MyModel.read(multiple="B")
        Traceback (most recent call last):
            ...
        MultipleIndexException
        """

        index, key = cls._check_args(*args, **kwargs)

        if not index.details.unique:
            raise sheraf.exceptions.MultipleIndexException(
                "'{}' is a multiple index and cannot be used with 'read'".format(
                    index.details.key
                )
            )

        return cls._decorate(cls._read_model_index(key, index))

    @classmethod
    def read_these(cls, *args, **kwargs):
        """
        Get model instances from their identifiers. Unlike
        :func:`~sheraf.models.indexation.BaseModel.read_these`,If an instance
        identifiers does not exist, a :class:`~sheraf.exceptions.ModelObjectNotFoundException`
        is raised.

        The function takes only one parameter which key is the index where to
        search, and which values are the index identifier.
        By default the index used is the `id` index.

        :return: A generator over the models matching the keys.

        >>> class MyModel(sheraf.IntIndexedNamedAttributesModel):
        ...     table = "my_model"
        ...
        >>> with sheraf.connection():
        ...     m1 = MyModel.create(id=1)
        ...     m2 = MyModel.create(id=2)
        ...
        ...     assert [m1, m2] == list(MyModel.read_these([m1.id, m2.id]))
        ...     list(MyModel.read_these(["invalid"]))
        Traceback (most recent call last):
            ...
        sheraf.exceptions.ModelObjectNotFoundException: Id 'invalid' not found in MyModel, 'id' index
        """

        index, keys = cls._check_args(*args, **kwargs)

        if index.details.unique:
            return (cls._decorate(cls._read_model_index(key, index)) for key in keys)

        else:
            return itertools.chain.from_iterable(
                (
                    cls._decorate(mapping)
                    for mapping in cls._read_model_index(key, index)
                )
                for key in keys
            )

    @classmethod
    def read_these_valid(cls, *args, **kwargs):
        """
        Return model instances from an index. Unlike :func:`~sheraf.models.indexation.BaseModel.read_these`,
        invalid index values are ignored.

        The function takes only one parameter which key is the index where to
        search, and which values are the index identifier.
        By default the index used is the `id` index.

        :return: A generator over the models matching the keys.

        >>> class MyModel(sheraf.IntIndexedNamedAttributesModel):
        ...     table = "my_model"
        ...
        >>> with sheraf.connection():
        ...     m1 = MyModel.create(id=1)
        ...     m2 = MyModel.create(id=2)
        ...
        ...     assert [m1, m2] == list(MyModel.read_these_valid([m1.id, m2.id]))
        ...     assert [m1, m2] == list(MyModel.read_these_valid([m1.id, 42, m2.id]))
        """

        index, keys = cls._check_args(*args, **kwargs)

        if index.details.unique:
            return (
                cls._decorate(index.get_item(key))
                for key in keys
                if index.has_item(key)
            )

        else:
            return itertools.chain.from_iterable(
                (cls._decorate(mapping) for mapping in index.get_item(key))
                for key in keys
                if index.has_item(key)
            )

    @classmethod
    def _read_model_index(cls, key, index):
        try:
            return index.get_item(key)
        except KeyError:
            raise sheraf.exceptions.ModelObjectNotFoundException(
                cls, key, index.details.key
            )

    @classmethod
    def index_table_rebuild(cls, index_names=None):
        """
        Resets a model indexation tables.

        This method should be called if an attribute became indexed in an already
        populated database.

        :param index_names: A list of index names to reset. If `None`, all the
                            indexes will be reseted. The primary index cannot be
                            resetted.
        """
        if not index_names:
            indexes = cls.indexes.values()
        else:
            indexes = [
                index
                for index_name, index in cls.indexes.items()
                if index_name in index_names
            ]

        for index in indexes:
            if index.details.primary:
                continue

            index.delete()

        for m in cls.all():
            for index in indexes:
                if not index.details.primary:
                    index.add_item(m)

    @classmethod
    def filter(cls, predicate=None, **kwargs):
        """Shortcut for :func:`sheraf.queryset.QuerySet.filter`.

        :return: :class:`sheraf.queryset.QuerySet`
        """
        return sheraf.queryset.QuerySet(model_class=cls).filter(
            predicate=predicate, **kwargs
        )

    @classmethod
    def search(cls, *args, **kwargs):
        """
        Shortcut for :func:`sheraf.queryset.QuerySet.search`.

        :return: :class:`sheraf.queryset.QuerySet`
        """
        return sheraf.queryset.QuerySet(model_class=cls).search(*args, **kwargs)

    @classmethod
    def order(cls, *args, **kwargs):
        """Shortcut for :func:`sheraf.queryset.QuerySet.order`.

        :return: :class:`sheraf.queryset.QuerySet`
        """
        return sheraf.queryset.QuerySet(model_class=cls).order(*args, **kwargs)

    @classmethod
    def get(cls, *args, **kwargs):
        """Shortcut for :func:`sheraf.queryset.QuerySet.filter` and
        :func:`sheraf.queryset.QuerySet.get`. ``Cowboy.get(name="Peter")`` and
        ``Cowboy.filter(name="Peter").get()`` are equivalent.

        :return: The instance of the model if the filter matches exactly one
            instance. Otherwise, it raises a
            :class:`~sheraf.exceptions.QuerySetUnpackException`.

        >>> class Cowboy(sheraf.Model):
        ...     table = "people"
        ...     name = sheraf.SimpleAttribute()
        ...     age = sheraf.SimpleAttribute()
        ...
        >>> with sheraf.connection(commit=True):
        ...     peter = Cowboy.create(name="Peter", age=30)
        ...     steven = Cowboy.create(name="Steven", age=30)
        ...     assert peter == Cowboy.get(name="Peter")
        ...
        >>> with sheraf.connection():
        ...     Cowboy.get()
        Traceback (most recent call last):
            ...
        sheraf.exceptions.QuerySetUnpackException: Trying to unpack more than 1 value from a QuerySet
        >>> with sheraf.connection():
        ...     Cowboy.get(age=30)
        Traceback (most recent call last):
            ...
        sheraf.exceptions.QuerySetUnpackException: Trying to unpack more than 1 value from a QuerySet
        >>> with sheraf.connection():
        ...     Cowboy.get(name="Unknown cowboy")
        Traceback (most recent call last):
            ...
        sheraf.exceptions.EmptyQuerySetUnpackException: Trying to unpack an empty QuerySet
        """
        return cls.filter(*args, **kwargs).get()

    def __repr__(self):
        try:
            identifier = (
                self.identifier
                if self.mapping is not None and self.primary_key() in self.mapping
                else None
            )
        except:
            identifier = "???"

        return "<{} {}={}>".format(
            self.__class__.__name__, self.primary_key(), identifier
        )

    def __hash__(self):
        return hash(self.identifier)

    def __eq__(self, other):
        return (
            hasattr(self, self.primary_key())
            and hasattr(other, self.primary_key())
            and self.identifier == other.identifier
        )

    def __setattr__(self, name, value):
        attribute = self.attributes.get(name)
        if attribute:
            was_created = attribute.is_created(self)
            if was_created:
                prev_value = getattr(self, name)
            old_values = self.before_index_edition(attribute)

        super().__setattr__(name, value)

        if attribute:
            try:
                self.after_index_edition(attribute, old_values)
            except sheraf.SherafException:
                if not was_created:
                    super().__delattr__(name)
                else:
                    super().__setattr__(name, prev_value)
                raise

    def __delattr__(self, name):
        attribute = self.attributes.get(name)
        if attribute:
            old_values = self.before_index_edition(attribute)

        super().__delattr__(name)

        if attribute:
            self.after_index_edition(attribute, old_values)

    def before_index_edition(self, attribute):
        old_index_values = {}
        for index in attribute.indexes.values():
            if not self._is_indexable(index):
                warnings.warn(
                    "New index in an already populated table. %s.%s will not be indexed. "
                    'Consider calling %s.index_table_rebuild(["%s"]) to initialize the indexation table.'
                    % (
                        self.__class__.__name__,
                        index.key,
                        self.__class__.__name__,
                        index.key,
                    ),
                    sheraf.exceptions.IndexationWarning,
                    stacklevel=5,
                )
                continue

            old_index_values[index] = index.get_model_values(self)
        return old_index_values

    def after_index_edition(self, attribute, old_index_values):
        for index in attribute.indexes.values():
            if not self._is_indexable(index):
                continue

            new_index_values = index.get_model_values(self)

            index_manager = self.indexes[index.key]
            index_manager.update_item(self, old_index_values[index], new_index_values)

    @property
    def identifier(self):
        """
        The identifier is the value of the primary_key for the current instance.
        If the primary_key is 'id', then the identifier might be an UUID.
        """
        if not self._identifier:
            self._identifier = getattr(self, self.primary_key())

        return self._identifier

    def _is_indexable(self, index):
        """
        To have its entries updated, an index must have its table previously
        initialized, with the exception of the very first model instance in
        the database.
        """
        if self._is_first_instance is None:
            self._is_first_instance = not self.index_manager().initialized()

        index_manager = self.indexes[index.key]
        index_table_exists = index_manager.table_initialized()
        return self._is_first_instance or index_table_exists

    def copy(self, **kwargs):
        r"""
        Copies a model.
        The attributes carrying an unique index wont be copied, they will be
        resetted instead.

        :param \*\*kwargs: Keywords arguments will be passed to
                         :func:`~sheraf.models.BaseModel.create` and thus
                         wont be copied.

        :return: a copy of this instance.
        """

        unique_attributes = (
            attribute
            for index in self.indexes.values()
            for attribute in index.details.attributes
            if index.details.unique
        )

        for attribute in unique_attributes:
            kwargs.setdefault(attribute.key(self), attribute.create(self))

        return super().copy(**kwargs)

    def delete(self):
        """Delete the current model instance.

        >>> class MyModel(sheraf.Model):
        ...     table = "my_model"
        ...
        >>> with sheraf.connection():
        ...    m = MyModel.create()
        ...    assert m == MyModel.read(m.id)
        ...    m.delete()
        ...    m.read(m.id)
        Traceback (most recent call last):
            ...
        sheraf.exceptions.ModelObjectNotFoundException: Id '...' not found in MyModel
        """
        for attr_name in self.attributes.keys():
            delattr(self, attr_name)

    @classmethod
    def count(cls, index_name=None):
        """
        Counts the number of elements in an index.
        :param index_name: The name of the index to count. By default
            the primary index is used
        """
        return cls.indexes[index_name or cls.primary_key()].count()


class IndexedModelMetaclass(BaseIndexedModelMetaclass):
    """
    Contains the mapping of tables (name of models) to their
    corresponding model definitions
    """

    tables = {}

    def __new__(cls, name, bases, attrs):
        klass = super().__new__(cls, name, bases, attrs)

        if "table" in attrs:
            table_name = attrs["table"]
            qualname = attrs["__module__"] + "." + attrs["__qualname__"]

            unique_table_name = attrs.get("unique_table_name", True)
            if (
                unique_table_name
                and table_name in IndexedModelMetaclass.tables
                and name != IndexedModelMetaclass.tables[table_name][0].split(".")[-1]
            ):
                message = "Table named '{table_name}' used twice: {first_class} and {second_class}".format(
                    table_name=table_name,
                    first_class=IndexedModelMetaclass.tables[table_name][0],
                    second_class=qualname,
                )
                raise sheraf.exceptions.SameNameForTableException(message)
            IndexedModelMetaclass.tables[table_name] = (qualname, klass)
        return klass


def model_from_table(table_name):
    if table_name not in IndexedModelMetaclass.tables:
        return None
    return IndexedModelMetaclass.tables[table_name][1]


class IndexedModel(BaseIndexedModel, metaclass=IndexedModelMetaclass):
    """
    :class:`~sheraf.models.indexation.IndexedModel` are the top-level
    models in the database. They come with one or several indexes,
    stored in a *table* at the root of the database. They must
    have a **table** parameter defined and an **id** attribute.

    They can have a **database_name** attribute. If it is set, then in a
    default connection context:

    - :func:`~sheraf.models.indexation.IndexedModel.create` will store the\
    new model instances in this database;
    - :func:`~sheraf.models.indexation.IndexedModel.read` and\
    :func:`~sheraf.models.indexation.IndexedModel.all` (etc.) will read in\
    priority in this database, and then in the default database.
    - :func:`~sheraf.models.indexation.IndexedModel.delete` will try to delete\
    the model from this database, and by default in the default database.

    However, if a **database_name** is explicitly passed to
    :func:`sheraf.databases.connection`, then every action will be
    performed on this database, ignoring the model **database_name** attribute.
    """

    database_name = None
    table = None

    id = sheraf.attributes.simples.SimpleAttribute().index(primary=True)

    @classmethod
    def index_manager(cls, index=None):
        return MultipleDatabaseIndexManager(cls.database_name, cls.table, index)

    @classmethod
    def create(cls, *args, **kwargs):
        if "id" not in cls.attributes:
            raise sheraf.exceptions.PrimaryKeyException(
                "{} inherit from IndexedModel but has no id attribute. Cannot create.".format(
                    cls.__name__
                )
            )

        return super().create(*args, **kwargs)


class SimpleIndexedModel(BaseIndexedModel, metaclass=BaseIndexedModelMetaclass):
    @classmethod
    def index_manager(cls, index=None):
        return SimpleIndexManager(index)
