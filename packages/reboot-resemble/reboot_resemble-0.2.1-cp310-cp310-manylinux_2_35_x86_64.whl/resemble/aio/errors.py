from google.protobuf.message import Message
from google.rpc import status_pb2
from resemble.aio.types import assert_type
from resemble.v1alpha1.errors_pb2 import (
    ActorAlreadyConstructed,
    ActorNotConstructed,
    UnknownService,
)
from typing import Optional, TypeVar, Union


class Aborted(Exception):
    """Base class of all RPC specific code generated errors used for
    aborting an RPC."""

    def __init__(self):
        super().__init__()

    @property
    def detail(self):
        # TODO(benh): better way to do this?
        return NotImplementedError

    @property
    def message(self):
        # TODO(benh): better way to do this?
        return NotImplementedError


AbortedT = TypeVar('AbortedT', bound=Aborted)


def _from_status(
    cls: type[AbortedT],
    status: status_pb2.Status,
) -> Optional[AbortedT]:
    # TODO(rjh, benh): think about how to handle cases where there are
    # multiple errors (since there are multiple details).
    assert issubclass(cls, Aborted)

    for any in status.details:
        for detail_type in cls.DETAIL_TYPES:
            if any.Is(detail_type.DESCRIPTOR):
                detail = detail_type()
                any.Unpack(detail)

                # TODO(benh): figure out why we need to ignore this type.
                return cls(detail, message=status.message)  # type: ignore

    return None


class Error(Aborted):
    """Common errors."""

    # Type alias for the union of possible error details.
    Detail = Union[
        ActorAlreadyConstructed,
        ActorNotConstructed,
        UnknownService,
    ]

    DETAIL_TYPES: list[type[Detail]] = [
        ActorAlreadyConstructed,
        ActorNotConstructed,
        UnknownService,
    ]

    _detail: Detail
    _message: str

    def __init__(self, detail: Detail, *, message: Optional[str] = None):
        super().__init__()

        assert_type(detail, self.DETAIL_TYPES)

        self._detail = detail
        self._message = message or detail.DESCRIPTOR.name

    @property
    def detail(self) -> Detail:
        return self._detail

    @property
    def message(self) -> str:
        return self._message

    @classmethod
    def from_status(cls, status: status_pb2.Status):
        return _from_status(cls, status)
