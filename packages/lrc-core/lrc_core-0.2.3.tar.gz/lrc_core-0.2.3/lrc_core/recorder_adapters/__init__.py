"""Abstract base classes for recording adapters.
Such as TelnetAdapter, RecorderAdapter, etc.
"""
import importlib
import inspect
import pkgutil
import telnetlib  # pylint: disable=deprecated-module
from abc import ABC, abstractmethod
from pprint import pprint

from lrc_core.exception import LrcException
from lrc_core.config import SMP_IP, SMP_PW

DEFINED_RECORDER_ADAPTERS = None

# monkey patching of telnet lib
original_read_until = telnetlib.Telnet.read_until
original_write = telnetlib.Telnet.write


def new_read_until(self, match, timeout=None):
    """
    Monkey Patch!
    Reads data from the connection until the specified match is found.

    Args:
        match (str or bytes): The string or bytes object to search for in the data.
        timeout (float, optional): The maximum amount of time to wait for the match to be found.

    Returns:
        bytes: The data read from the connection up to and including the match.
    """
    if isinstance(match, str):
        return original_read_until(self, match.encode("ascii"), timeout)
    else:
        return original_read_until(self, match, timeout)


def new_write(self, buffer):
    """
    Monkey Patch!
    Writes the given buffer to the underlying stream.

    If the buffer is a string, it is first encoded as ASCII before being written.

    Args:
        buffer: The buffer to write to the stream.

    Returns:
        The number of bytes written to the stream.
    """
    if isinstance(buffer, str):
        return original_write(self, buffer.encode("ascii"))
    else:
        return original_write(self, buffer)


telnetlib.Telnet.read_until = new_read_until
telnetlib.Telnet.write = new_write


def read_line(self, timeout=2):
    """
    Reads a line from the input stream.

    Args:
        timeout (float): The maximum amount of time to wait for input, in seconds.

    Returns:
        str: The line of text read from the input stream.
    """
    return self.read_until("\n", timeout)


telnetlib.Telnet.read_line = read_line


def read_until_non_empty_line(self):
    """
    Reads lines from the input stream until a non-empty line is found.
    Returns the first non-empty line found, or None if the end of the stream is reached.
    """
    line = self.read_line()
    if line is None:
        return None
    while len(line.rstrip()) <= 0:
        line = self.read_line()
    return line


telnetlib.Telnet.read_until_non_empty_line = read_until_non_empty_line


def assert_string_in_output(self, string, timeout=2):
    """
    Asserts that the given string is present in the output of the recorder adapter.

    Args:
        string (str): The string to search for in the output.
        timeout (int, optional): The maximum number of seconds
            to wait for the string to appear in the output. Defaults to 2.

    Returns:
        tuple: A tuple containing a boolean indicating whether the string
            was found in the output, and the output itself.
    """
    resp = self.read_until(string, timeout)
    if resp is None:
        return (
            False,
            resp,
        )
    resp = resp.decode("ascii")
    if string in resp:
        return True, resp
    return False, resp


telnetlib.Telnet.assert_string_in_output = assert_string_in_output


class TelnetAdapter(ABC):
    """
    Abstract base class for Telnet adapters.

    Attributes:
        address (str): The IP address or hostname of the device to connect to.
        tn (telnetlib.Telnet): The Telnet connection object.
        esc_char (str): The escape character to use for the Telnet connection.
    """

    def __init__(self, address, esc_char="W"):
        self.address = address
        self.tn = None
        self.esc_char = esc_char

    @abstractmethod
    def _login(self):
        pass

    def _run_cmd(self, cmd, _timeout=1, auto_connect=True):
        if self.tn is None and not auto_connect:
            raise LrcException("Not connected!")
        elif self.tn is None:
            self._login()
        self.tn.write(cmd)
        out = self.tn.read_until_non_empty_line()
        res = out
        while out is not None and out != "":
            out = self.tn.read_until_non_empty_line()
            print(out)
            res += out
        return res

    @staticmethod
    def _get_response_str(tn_response):
        if isinstance(tn_response, bytes):
            return str(tn_response.decode("ascii").rstrip())
        else:
            return str(tn_response).rstrip()


class RecorderAdapter:
    """
    Abstract base class for recorder adapters.

    Attributes:
        address (str): The address of the recorder.
        user (str): The username for the recorder.
        password (str): The password for the recorder.
    """

    def __init__(self, address: str, user: str, password: str):
        self.address = address
        self.user = user
        self.password = password

    @classmethod
    @abstractmethod
    def get_recorder_params(cls) -> dict:
        """
        Returns a dictionary of parameters for the recorder.

        Returns:
            dict: A dictionary of parameters for the recorder.
        """

    @abstractmethod
    def _get_name(self):
        """
        Returns the name of the recorder.

        Returns:
            str: The name of the recorder.
        """

    @abstractmethod
    def _get_version(self):
        """
        Returns the version of the recorder.

        Returns:
            str: The version of the recorder.
        """

    @abstractmethod
    def is_recording(self) -> bool:
        """
        Returns True if the recorder is currently recording, False otherwise.

        Returns:
            bool: True if the recorder is currently recording, False otherwise.
        """

    def get_recording_status(self) -> str:
        """
        Returns the recording status of the recorder.

        Returns:
            str: The recording status of the recorder.
        """


def get_defined_recorder_adapters() -> list:
    """
    Returns a list of recorder adapter models defined in the recorder_adapters package.

    Each model is represented as a dictionary with the following keys:
    - id: The unique identifier of the model.
    - name: The name of the model.
    - commands: A dictionary of commands supported by the model, where each key 
        is the name of the command and the value is a dictionary of parameter names and types.
    - path: The file path of the module defining the model.
    - requires_user: (Optional) A boolean indicating whether the model requires 
        a user to be authenticated.
    - requires_password: (Optional) A boolean indicating whether the model requires 
        a password to be authenticated.
    """
    rec_adapters_module = importlib.import_module(
        ".recorder_adapters", package="backend"
    )
    rec_adapter_class = getattr(
        rec_adapters_module, "RecorderAdapter"
    )  # needed, otherwise subclass check may fail
    models = []
    found_packages = list(pkgutil.iter_modules(rec_adapters_module.__path__))
    for f_p in found_packages:
        importer = f_p[0]
        rec_model_module = importer.find_module(f_p[1]).load_module(f_p[1])
        rec_model = {
            "id": f_p[1],
            "name": f_p[1],
            "commands": {},
            "path": rec_model_module.__file__,
        }
        if hasattr(rec_model_module, "RECORDER_MODEL_NAME"):
            rec_model["name"] = rec_model_module.RECORDER_MODEL_NAME
        if hasattr(rec_model_module, "REQUIRES_USER"):
            rec_model["requires_user"] = rec_model_module.REQUIRES_USER
        if hasattr(rec_model_module, "REQUIRES_PW"):
            rec_model["requires_password"] = rec_model_module.REQUIRES_PW
        for name, obj in inspect.getmembers(rec_model_module, inspect.isclass):
            if issubclass(obj, rec_adapter_class) and name != "RecorderAdapter":
                rec_model["id"] = rec_model["id"] + "." + obj.__name__
                rec_model["class"] = obj
                commands = {}
                for method_name, method in inspect.getmembers(
                    obj, predicate=inspect.isfunction
                ):
                    if len(method_name) > 0 and "_" == method_name[0]:
                        continue
                    signature = inspect.signature(method)
                    parameters = {}
                    for params in signature.parameters:
                        if params == "self":
                            continue
                        param_type = signature.parameters[params].annotation.__name__
                        param_type = (
                            "_unknown_type" if param_type == "_empty" else param_type
                        )
                        parameters[signature.parameters[params].name] = param_type
                    if len(parameters) <= 0:
                        parameters = None
                    commands[method_name] = parameters
                rec_model["commands"] = commands
        models.append(rec_model)
    return models


def get_recorder_adapter_by_id(rec_id: str, **kwargs):
    """
    Returns a recorder adapter instance based on the given ID.

    Args:
        rec_id (str): The ID of the recorder adapter to retrieve.
        **kwargs: Additional keyword arguments to pass to the recorder adapter constructor.

    Returns:
        An instance of the recorder adapter with the given ID, or None if no such adapter exists.
    """
    global DEFINED_RECORDER_ADAPTERS  # pylint: disable=global-statement
    if DEFINED_RECORDER_ADAPTERS is None:
        DEFINED_RECORDER_ADAPTERS = get_defined_recorder_adapters()
    for rec_adapter in DEFINED_RECORDER_ADAPTERS:
        if rec_id in rec_adapter.get("id", "").split("."):
            return rec_adapter["class"](**kwargs)
    return None


if __name__ == "__main__":
    print(get_defined_recorder_adapters())
    get_recorder_adapter_by_id("SMP35x", address=SMP_IP, password=SMP_PW)
    exit()
