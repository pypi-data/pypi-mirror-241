from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Generic, Optional, Sequence, TypeVar

T = TypeVar('T')


@dataclass(frozen=True)
class Request(Generic[T]):
    """An object that contains data to be processed by :class:`Provider`.

    Generic argument indicates which object should be
    returned after request processing.

    Request must be always a hashable object
    """


class CannotProvide(Exception):
    is_terminal: bool

    def __init__(
        self,
        msg: Optional[str] = None,
        sub_errors: Sequence['CannotProvide'] = (),
        is_terminal: bool = False
    ):
        """
        :param msg: Human-oriented description of error
        :param sub_errors: Errors caused this error
        """
        self.msg = msg
        self.sub_errors = sub_errors
        self.is_terminal = is_terminal or any(sub_error.is_terminal for sub_error in sub_errors)
        self._self_is_terminal = is_terminal
        super().__init__(self.msg, self.sub_errors, self.is_terminal)

    def __repr__(self):
        return (
            f"{type(self).__name__}"
            f"(msg={self.msg!r}, sub_errors={self.sub_errors!r}, is_terminal={self.is_terminal})"
        )


V = TypeVar('V')


class Mediator(ABC, Generic[V]):
    """Mediator is an object that gives provider access to other providers
    and that stores state of the current search.

    Mediator is a proxy to providers of retort.
    """

    @abstractmethod
    def provide(self, request: Request[T], *, extra_stack: Sequence[Request[Any]] = ()) -> T:
        """Get response of sent request.

        :param request: A request instance
        :param extra_stack: Additional stack that will be added to :attr:`.request_stack` before passed request
        :return: Result of the request processing
        :raise CannotProvide: A provider able to process the request does not found
        """

    @abstractmethod
    def provide_from_next(self) -> V:
        """Forward current request to providers
        that placed after current provider at the recipe.
        """

    @property
    @abstractmethod
    def request_stack(self) -> Sequence[Request[Any]]:
        """Call stack, but consisting of requests.
        Last element of ``request_stack`` is current request.
        """


class Provider(ABC):
    """An object that can process Request instances"""

    @abstractmethod
    def apply_provider(self, mediator: Mediator[T], request: Request[T]) -> T:
        """Handle request instance and return a value of type required by request.
        Behavior must be the same during the provider object lifetime

        :raise CannotProvide: provider cannot process passed request
        """
