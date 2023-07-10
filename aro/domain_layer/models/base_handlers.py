from abc import ABC
from dataclasses import dataclass, field
from typing import Dict, Literal, Optional

from aro.presentation_layer.mappings import CreateOffersRequestMapping


handler_result_literal = Literal['APPROVED', 'DENIED']


class Handler(ABC):
    def __init__(self) -> None:
        self.next = None

    def set_next(self, next_handler: "Handler") -> None:
        self.next = next_handler

    def _run(self, *args, **kwargs):
        raise NotImplementedError

    def handle(self, *args, **kwargs):
        if result := self._run(*args, **kwargs):
            return result

        if self.next:
            return self.next.handle(*args, **kwargs)


class ContextWithHistory(ABC):
    handlers_history: Dict[str, handler_result_literal] = field(
        default_factory=dict, init=False
    )
    deny_description: Optional[str] = field(default=None, init=False)
    deny_code: Optional[str] = field(default=None, init=False)

    @property
    def deny_step(self) -> Optional[str]:
        step = filter(lambda i: i[1] == "DENIED",
                      self.handlers_history.items())

        try:
            k, _ = next(step)

            return k
        except StopIteration:
            return None

    def set_step_result(self, step_name: str, result: handler_result_literal) -> None:
        self.handlers_history[step_name] = result


@dataclass
class CreateOffersContext(ContextWithHistory):
    request_data: CreateOffersRequestMapping
