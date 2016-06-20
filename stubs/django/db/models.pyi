from six import text_type
from typing import overload, Any, Generator, Generic, Iterable, Mapping, Optional, Sequence, Sized, Tuple, TypeVar

class Model(object):
    def save(self, update_fields=[]):
        # type: (Iterable[text_type]) -> None
        ...

def BooleanField(name=None, default=None, blank=False, null=False, *args, **kwargs):
    # type: (Optional[text_type], Optional[bool], bool, bool, *Any, **Any) -> bool
    ...
def CharField(name=None, default=None, max_length=None, blank=False, null=False, *args, **kwargs):
    # type: (Optional[text_type], Optional[bool], Optional[int], bool, bool, *Any, **Any) -> text_type
    ...
def TextField(name=None, default=None, blank=False, null=False, *args, **kwargs):
    # type: (Optional[text_type], Optional[bool], bool, bool, *Any, **Any) -> text_type
    ...
def ForeignKey(field, blank=False, null=False, *args, **kwargs):
    # type: (Any, bool, bool, *Any, **Any) -> Any
    ...

ModelT = TypeVar('ModelT', bound=Model)

class ModelIterable(Generic[ModelT], Iterable):
    def __init__(self, qset):
        # type: (QuerySet[ModelT]) -> None
        ...
    def __iter__(self) -> Generator[ModelT, None, None]: ...

class ValuesIterable(Generic[ModelT], Iterable):
    def __init__(self, qset):
        # type: (QuerySet[ModelT]) -> None
        ...
    def __iter__(self) -> Generator[Dict[str, Any], None, None]: ...

class ValuesListIterable(Generic[ModelT], Iterable):
    def __init__(self, qset):
        # type: (QuerySet[ModelT]) -> None
        ...
    def __iter__(self) -> Generator[Any, None, None]: ...

class QuerySet(Generic[ModelT], Sequence):
    def filter(self, **kwargs):
        # type: (**Any) -> QuerySet[ModelT]
        ...
    def order_by(self, *fields):
        # type: (*text_type) -> QuerySet[ModelT]
        ...
    def exclude(self, **kwargs):
        # type: (**Any) -> QuerySet[ModelT]
        ...
    def all(self) -> QuerySet[ModelT]: ...
    def get(self, **kwargs):
        # type: (**Any) -> ModelT
        ...
    def first(self) -> ModelT: ...
    def count(self) -> int: ... # type: ignore
    def exists(self) -> bool: ...
    def delete(self) -> None: ...
    def select_related(self) -> QuerySet[ModelT]: ...
    def values(self, *args):
        # type: (*text_type) -> ValuesIterable[ModelT]
        ...
    def values_list(self, *args, **kwargs):
        # type: (*text_type, **Any) -> ValuesListIterable[ModelT]
        ...
    def __iter__(self) -> Generator[ModelT, None, None]: ...

    @overload
    def __getitem__(self, i: int) -> ModelT: ...
    @overload
    def __getitem__(self, s: slice) -> QuerySet[ModelT]: ...

    def __len__(self) -> int: ...
    def update(self, **kwargs):
        # type: (**Any) -> None
        ...

class Manager(Generic[ModelT], QuerySet):
    def create(self, **kwargs):
        # type: (**Any) -> ModelT
        ...
    def get_or_create(self, **kwargs):
        # type: (**Any) -> Tuple[ModelT, bool]
        ...