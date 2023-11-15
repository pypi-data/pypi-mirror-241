from typing import Callable, Any
from abc import ABC, abstractmethod


class FormatterAbstract(ABC):
    @abstractmethod
    def set_cb(self, render_html_cb: Callable[[str], None], log_callback: Callable[[str], None], is_manuf: bool):
        pass

    @abstractmethod
    def callback(self, message: Any, message_type: Any):
        pass

    @abstractmethod
    def is_log_cb(self):
        pass

    @abstractmethod
    def print_dict(self, message: dict):
        pass

    @abstractmethod
    def print_short(self, message: str):
        pass

    @abstractmethod
    def print_message(self, message: str):
        pass

    @abstractmethod
    def print_short_blue(self, message: str):
        pass

    @abstractmethod
    def print_error_message(self, message: str):
        pass
