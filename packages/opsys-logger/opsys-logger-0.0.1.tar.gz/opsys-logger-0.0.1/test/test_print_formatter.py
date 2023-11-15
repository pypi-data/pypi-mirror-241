import unittest
from unittest.mock import patch, MagicMock
from opsys_logger.print_formatter import PrintFormatter, MessageType


class Test(unittest.TestCase):
    @ classmethod
    def setUp(self):
        pass

    @ classmethod
    def setUpClass(cls):
        pass

    @ classmethod
    def tearDownClass(cls):
        pass

    @ patch.object(PrintFormatter, 'set_cb')
    def test_set_cb(self, print_formatter_mock: MagicMock):
        print_format = PrintFormatter()
        render_html_cb = None 
        log_callback = None
        is_manuf = False
        print_format.set_cb(render_html_cb, log_callback, is_manuf)
        print_formatter_mock.assert_called_once_with(None, None, False)
        
    @ patch.object(PrintFormatter, 'callback')
    def test_callback(self, print_formatter_mock: MagicMock):
        print_format = PrintFormatter()
        message = 'log message'
        message_type = MessageType.Log.value
        print_format.callback(message, message_type)
        print_formatter_mock.assert_called_once_with('log message', (3,))
        
    @ patch.object(PrintFormatter, 'is_log_cb')
    def test_is_log_cb(self, print_formatter_mock: MagicMock):
        print_format = PrintFormatter()
        print_format.is_log_cb()
        print_formatter_mock.assert_called_once_with()
        
    @ patch.object(PrintFormatter, 'print_dict')
    def test_print_dict(self, print_formatter_mock: MagicMock):
        print_format = PrintFormatter()
        message = "print dict"
        print_format.print_dict(message)
        print_formatter_mock.assert_called_once_with("print dict")
        
    @ patch.object(PrintFormatter, 'print_short')
    def test_print_short(self, print_formatter_mock: MagicMock):
        print_format = PrintFormatter()
        message = "print short"
        print_format.print_short(message)
        print_formatter_mock.assert_called_once_with("print short")
        
    @ patch.object(PrintFormatter, 'print_message')
    def test_print_message(self, print_formatter_mock: MagicMock):
        print_format = PrintFormatter()
        message = "print message"
        print_format.print_message(message)
        print_formatter_mock.assert_called_once_with("print message")
        
    @ patch.object(PrintFormatter, 'print_short_blue')
    def test_print_short_blue(self, print_formatter_mock: MagicMock):
        print_format = PrintFormatter()
        message = "print short blue"
        print_format.print_short_blue(message)
        print_formatter_mock.assert_called_once_with("print short blue")
        
    @ patch.object(PrintFormatter, 'print_short_green')
    def test_print_short_green(self, print_formatter_mock: MagicMock):
        print_format = PrintFormatter()
        message = "print short green"
        print_format.print_short_green(message)
        print_formatter_mock.assert_called_once_with("print short green")
        
    @ patch.object(PrintFormatter, 'print_error_message')
    def test_print_error_message(self, print_formatter_mock: MagicMock):
        print_format = PrintFormatter()
        message = "print error message"
        print_format.print_error_message(message)
        print_formatter_mock.assert_called_once_with("print error message")
        
    @ patch.object(PrintFormatter, 'reset_color')
    def test_reset_color(self, print_formatter_mock: MagicMock):
        print_format = PrintFormatter()
        print_format.reset_color()
        print_formatter_mock.assert_called_once_with()


if __name__ == '__main__':
    unittest.main()
