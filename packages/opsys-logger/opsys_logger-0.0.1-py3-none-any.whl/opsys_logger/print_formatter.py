from enum import Enum
import shutil
from colorama import Fore, Style

from .print_formatter_abstract import FormatterAbstract


class MessageType(Enum):
    """
    Callback Message Type
    """
    CommRead = (0,)
    CommWrite = (1,)
    System = (2,)
    Log = (3,)
    UserInstruction = (4,)
    ExecutionLog = (5,)
    Error = (6,)


class PrintFormatter(FormatterAbstract):
    """
    Formatted prints class
    """
    def set_cb(self, render_html_cb=None, log_callback=None, is_manuf=False):
        """
        Set callback parameters (constructor)

        Args:
            render_html_cb (Callable[[str], None], optional): Web App output callback object. Defaults to None.
            log_callback (Callable[[str], None], optional): Logger callback object. Defaults to None.
            is_manuf (bool, optional): Server callback flag. Defaults to False.
        """
        self._render_html_cb = render_html_cb
        self._log_callback = log_callback
        self._is_manuf = is_manuf

    def callback(self, message, message_type):
        """
        Callback message wrapper

        Args:
            message (str): output message
            message_type (MessageType): Enum object with message type code
        """
        try:
            if self.is_log_cb():
                self._log_callback(message, message_type)
        except:
            pass

    def is_log_cb(self):
        """
        Check if callback initialized 

        Returns:
            Callable[[str]: Output callback object if initialized.
                            Otherwise, return None.
        """
        return self._log_callback is not None

    def print_dict(self, message):
        """
        Print dictionary content

        Args:
            message (str): output message
        """
        self.callback(message, MessageType.Log.value)
        for i in message:
            print(f'{i}: {message[i]}')

    def print_short(self, message):
        """
        Print unformatted message

        Args:
            message (str): output message
        """
        self.callback(message, MessageType.Log.value)
        print(message)

    def print_message(self, message):
        """
        Print formatted message in green color (MSG)

        Args:
            message (str): output message
        """
        self.callback(message, MessageType.ExecutionLog.value)
        print(Fore.GREEN + "-" * 200)
        print((Fore.GREEN + message).center(shutil.get_terminal_size().columns))
        print(Fore.GREEN + "-" * 200)
        self.reset_color()

    def print_short_blue(self, message):
        """
        Print regular message in blue color

        Args:
            message (str): output message
        """
        self.callback(message, MessageType.Log.value)
        print((Fore.BLUE + message))
        self.reset_color()

    def print_short_green(self, message):
        """
        Print regular message in green color

        Args:
            message (str): output message
        """
        self.callback(message, MessageType.Log.value)
        print((Fore.GREEN + message))
        self.reset_color()

    def print_error_message(self, message):
        """
        Print formatted message in red color (ERR)

        Args:
            message (str): output message
        """
        self.callback(message, MessageType.Error.value)
        print(Fore.RED + "-" * 200)
        print((Fore.RED + message).center(shutil.get_terminal_size().columns))
        print(Fore.RED + "-" * 200)
        self.reset_color()

    @ staticmethod
    def reset_color():
        """
        Reset color formatting to white color - default
        """
        print(Style.RESET_ALL)
