# pylint: disable=too-many-lines
"""
Recorder Adapter for SMP
"""
from collections import defaultdict
import enum
import logging
import re
import threading
from typing import Dict, List, TypeVar, Union

from lrc_core.exception import LrcException, exception_decorator
from lrc_core.recorder_adapters import telnetlib, TelnetAdapter, RecorderAdapter

logger = logging.getLogger("lrc.recorder_adapters.extron_smp")

RECORDER_MODEL_NAME = "Recorder Adapter for SMP 351 and 352"
VERSION = "0.9.0"
REQUIRES_USER = False
REQUIRES_PW = True

ALLOWED_HOSTNAME_RE = re.compile(r"(?!-)[A-Z\d-]{1,63}(?<!-)$", re.IGNORECASE)

ACTIVE_ALARMS_RE = re.compile(
    r"<[-_a-zA-Z]+\:(?P<name>[-_a-zA-Z]+),[-_a-zA-Z]+\:(?P<level>[-_a-zA-Z]+)>",
    re.IGNORECASE,
)

FILE_LISTING_RE = re.compile(
    r"(?P<file>.*) (?P<date>\S+, \d+ \S+ \d+ \d+:\d+:\d+ \S+) (?P<size>\d+)"
)


class SMP35x(TelnetAdapter, RecorderAdapter):
    """
    A class representing the Extron SMP recorder.
    """

    locks = defaultdict(threading.Lock)

    @classmethod
    def get_recorder_params(cls) -> dict:
        return {"_requires_user": False, "_requires_password": True}

    S = TypeVar("S", bound=enum.IntEnum)

    def _get_number_from_enum(
        self, number_or_enum: Union[S, int], enum_class: S
    ) -> int:
        if isinstance(number_or_enum, enum.IntEnum):
            return number_or_enum.value
        elif isinstance(number_or_enum, int):
            if number_or_enum in iter(enum_class):
                return number_or_enum
            raise ValueError(
                f"number must be a {enum_class} or one of "
                f"{','.join([str(x.value) for x in iter(enum_class)])}, "
                f"but was {number_or_enum}"
            )
        else:
            raise TypeError(f"channel_number must be a {enum_class} or int")

    class InputNumber(enum.IntEnum):
        """
        An enumeration representing the input numbers for an Extron SMP recorder.

        Attributes:
            Input_1 (int): The input number for Input 1.
            Input_2 (int): The input number for Input 2.
            Input_3 (int): The input number for Input 3.
            Input_4 (int): The input number for Input 4.
            Input_5 (int): The input number for Input 5.
        """

        INPUT_1 = 1
        INPUT_2 = 2
        INPUT_3 = 3
        INPUT_4 = 4
        INPUT_5 = 5

    class OutputChannel(enum.IntEnum):
        """
        Enum representing the output channels of an Extron SMP recorder.

        Attributes:
            A (int): The first output channel.
            B (int): The second output channel.
        """

        A = 1  # channel A
        B = 2  # channel B

    class UserEncoderLayoutPresetNumber(enum.IntEnum):
        """
        An enumeration representing the available user encoder layout preset numbers.

        Attributes:
            PRESET_1 (int): The preset number for layout 1.
            PRESET_2 (int): The preset number for layout 2.
            PRESET_3 (int): The preset number for layout 3.
            PRESET_4 (int): The preset number for layout 4.
            PRESET_5 (int): The preset number for layout 5.
            PRESET_6 (int): The preset number for layout 6.
            PRESET_7 (int): The preset number for layout 7.
            PRESET_8 (int): The preset number for layout 8.
            PRESET_9 (int): The preset number for layout 9.
            PRESET_10 (int): The preset number for layout 10.
            PRESET_11 (int): The preset number for layout 11.
            PRESET_12 (int): The preset number for layout 12.
            PRESET_13 (int): The preset number for layout 13.
            PRESET_14 (int): The preset number for layout 14.
            PRESET_15 (int): The preset number for layout 15.
            PRESET_16 (int): The preset number for layout 16.
        """

        PRESET_1 = 1
        PRESET_2 = 2
        PRESET_3 = 3
        PRESET_4 = 4
        PRESET_5 = 5
        PRESET_6 = 6
        PRESET_7 = 7
        PRESET_8 = 8
        PRESET_9 = 9
        PRESET_10 = 10
        PRESET_11 = 11
        PRESET_12 = 12
        PRESET_13 = 13
        PRESET_14 = 14
        PRESET_15 = 15
        PRESET_16 = 16

    class AudioChannels(enum.IntEnum):
        """
        Enum representing the available audio channels on the Extron SMP recorder.

        Attributes:
            ANALOG_INPUT_A_LEFT (int): The left analog input channel A.
            ANALOG_INPUT_A_RIGHT (int): The right analog input channel A.
            DIGITAL_INPUT_A_LEFT (int): The left digital input channel A.
            DIGITAL_INPUT_A_RIGHT (int): The right digital input channel A.
            ANALOG_INPUT_B_LEFT (int): The left analog input channel B.
            ANALOG_INPUT_B_RIGHT (int): The right analog input channel B.
            DIGITAL_INPUT_B_LEFT (int): The left digital input channel B.
            DIGITAL_INPUT_B_RIGHT (int): The right digital input channel B.
            OUTPUT_LEFT (int): The left output channel.
            OUTPUT_RIGHT (int): The right output channel.
        """

        ANALOG_INPUT_A_LEFT = 40000
        ANALOG_INPUT_A_RIGHT = 40001
        DIGITAL_INPUT_A_LEFT = 40002
        DIGITAL_INPUT_A_RIGHT = 40003
        ANALOG_INPUT_B_LEFT = 40004
        ANALOG_INPUT_B_RIGHT = 40005
        DIGITAL_INPUT_B_LEFT = 40006
        DIGITAL_INPUT_B_RIGHT = 40007
        OUTPUT_LEFT = 60000
        OUTPUT_RIGHT = 60001

    class AudioInput(enum.IntEnum):
        """Enum representing the different audio inputs of an Extron SMP recorder."""

        INPUT_1 = 1
        INPUT_2 = 2
        INPUT_3 = 3
        INPUT_4 = 4
        INPUT_5 = 5  # for SDI models (only)

    class VerboseMode(enum.IntEnum):
        """
        Enum class representing the different verbose modes for Extron SMP devices.

        Attributes:
            CLEAR_NONE (int): Default mode for telnet connections, clears non-essential information.
            VERBOSE (int): Default mode for USB and RS-232 control, provides verbose information.
            TAGGED (int): Provides tagged responses for queries.
            VERBOSE_TAGGED (int): Provides verbose information and tagged responses for queries.
        """

        CLEAR_NONE = 0
        VERBOSE = 1
        TAGGED = 2
        VERBOSE_TAGGED = 3

    class FrontPanelLockMode(enum.IntEnum):
        """
        Enumeration of the front panel lock modes for an Extron SMP recorder.

        Attributes:
            OFF (int): No front panel lock.
            COMPLETE_LOCKOUT (int): Complete front panel lockout.
            MENU_LOCKOUT (int): Lockout of front panel menu controls.
            RECORDING_CONTROLS_ONLY (int): Lockout of all front panel controls except
            for recording controls.
        """

        OFF = 0
        COMPLETE_LOCKOUT = 1
        MENU_LOCKOUT = 2
        RECORDING_CONTROLS_ONLY = 3

    class ConfigurationType(enum.IntEnum):
        """
        An enumeration of the types of configurations on an Extron SMP device.

        Attributes:
            IP_CONFIG (int): The configuration type for IP settings.
            BOX_SPECIFIC_CONFIG (int): The configuration type for device-specific settings.
        """

        IP_CONFIG = 0
        BOX_SPECIFIC_CONFIG = 2

    def __init__(self, address, password, auto_login=True, **_kwargs):
        """
        Initializes a new instance of the SMP35x class.

        Args:
            address (str): The IP address of the recorder.
            password (str): The password for the recorder.
            auto_login (bool): Whether to automatically login to the recorder. Defaults to True.
            **kwargs: Additional keyword arguments.
        """
        RecorderAdapter.__init__(self, address, "", password)
        TelnetAdapter.__init__(self, address)
        if auto_login:
            self._login()

    def _login(self):
        """
        Logs in to the recorder.
        """
        logger.debug("Connecting to %s ...", self.address)
        with SMP35x.locks[self.address]:
            try:
                self.tn = telnetlib.Telnet(self.address)
            except TimeoutError as e:
                raise LrcException(str(e)) from e
            except ConnectionRefusedError as e:
                raise LrcException(str(e)) from e
            self.tn.read_until("\r\nPassword:")
            # password = getpass.getpass()
            password = self.password
            self.tn.write(password + "\n\r")

            out = self.tn.assert_string_in_output("Login Administrator")
            if not out[0]:
                print(out[1])
                if "Password:" in out[1]:
                    logger.warning(
                        "Could not login (as admin) with given password! %s",
                        self.address,
                    )
                    print("re-enter pw")
                    self.tn.write(self.password + "\n\r")
                    self.tn.assert_string_in_output("Login Administrator")
                logger.error("WRONG (admin) password!! Exiting! %s", self.password)
                self.tn = None
                logger.error(
                    "Could definitely not login (as admin) with given password! %s",
                    self.address,
                )
                raise LrcException("Could not login as administrator with given pw!")
            logger.info("OK, we have admin rights!")

    def _get_name(self):
        """
        Gets the name of the recorder.

        Returns:
            str: The name of the recorder.
        """
        return RECORDER_MODEL_NAME

    def _get_version(self):
        """
        Gets the version of the recorder.

        Returns:
            str: The version of the recorder.
        """
        return VERSION

    def get_version(self, include_build=False, verbose_info=False) -> str:
        """
        Gets the version of the recorder.

        Args:
            include_build (bool): Whether to include the build number. Defaults to False.
            verbose_info (bool): Whether to include verbose information. Defaults to False.

        Returns:
            str: The version of the recorder.
        """
        with SMP35x.locks[self.address]:
            if verbose_info:
                self.tn.write("0Q")
            else:
                if include_build:
                    self.tn.write("*Q\n")
                else:
                    self.tn.write("1Q\n")

            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def get_bootstrap_version(self):
        """
        Gets the bootstrap version of the recorder.

        Returns:
            str: The bootstrap version of the recorder.
        """
        with SMP35x.locks[self.address]:
            self.tn.write("2Q")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def get_factory_firmware_version(self):
        """
        Gets the factory firmware version of the recorder.

        Returns:
            str: The factory firmware version of the recorder.
        """
        with SMP35x.locks[self.address]:
            self.tn.write("3Q")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def get_updated_firmware_version(self):
        """
        Gets the updated firmware version of the recorder.

        Returns:
            str: The updated firmware version of the recorder.
        """
        with SMP35x.locks[self.address]:
            self.tn.write("4Q")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def get_temperature(self, as_number=False):
        """
        Gets the temperature of the recorder.

        Returns:
            str: The temperature of the recorder.
        """
        with SMP35x.locks[self.address]:
            self.tn.write(f"{self.esc_char}20STAT\n")
            res = TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())
            if as_number:
                return float("".join(i for i in res if i.isdigit() or i in ".,"))
            return res

    def get_part_number(self):
        """
        Gets the part number of the recorder.

        Returns:
            str: The part number of the recorder.
        """
        with SMP35x.locks[self.address]:
            self.tn.write("N")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def get_model_name(self):
        """
        Gets the model name of the recorder.

        Returns:
            str: The model name of the recorder.
        """
        with SMP35x.locks[self.address]:
            self.tn.write("1I")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def get_model_description(self):
        """
        Gets the model description of the recorder.

        Returns:
            str: The model description of the recorder.
        """
        with SMP35x.locks[self.address]:
            self.tn.write("2I")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def get_system_memory_usage(self):
        """
        Gets the system memory usage of the recorder.

        Returns:
            str: The system memory usage of the recorder.
        """
        with SMP35x.locks[self.address]:
            self.tn.write("3I")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def get_number_of_connected_users(self):
        """
        Gets the number of connected users to the recorder.

        Returns:
            str: The number of connected users to the recorder.
        """
        with SMP35x.locks[self.address]:
            self.tn.write("10I")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def get_system_processer_usage(self):
        """
        Gets the system processor usage of the recorder.

        Returns:
            str: The system processor usage of the recorder.
        """
        with SMP35x.locks[self.address]:
            self.tn.write("11I")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def get_system_processor_idle(self):
        """
        Gets the system processor idle of the recorder.

        Returns:
            str: The system processor idle of the recorder.
        """
        with SMP35x.locks[self.address]:
            self.tn.write("12I")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def get_eth0_link_status(self):
        """
        Gets the eth0 link status of the recorder.

        Returns:
            str: The eth0 link status of the recorder.
        """
        with SMP35x.locks[self.address]:
            self.tn.write("13I")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def get_file_transfer_config(self):
        """
        Gets the file transfer configuration of the recorder.

        Returns:
            str: The file transfer configuration of the recorder.
        """
        with SMP35x.locks[self.address]:
            self.tn.write("38I")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def get_active_alarms(self) -> Dict[str, str]:
        """
        Gets the active alarms of the recorder.

        Returns:
            str: The active alarms of the recorder.
        """
        with SMP35x.locks[self.address]:
            self.tn.write("39I")
            res = TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())
            res = {
                x.groupdict()["name"]: x.groupdict()["level"]
                for x in re.finditer(ACTIVE_ALARMS_RE, res)
            }
            return res

    def get_selected_input_status(self, parsed=True) -> str | dict[str, dict]:
        """
        Gets the selected input status of the recorder.

        Returns:
            str: The selected input status of the recorder.
        """
        with SMP35x.locks[self.address]:
            self.tn.write("42I")
            res = TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

        if parsed:

            def parse_channel_output(channel) -> dict:
                ch, sel_input, input_res, frame_rate, _1or0 = channel.split("*")
                return {
                    ch[2]: {
                        "input": sel_input,
                        "input_res": input_res,
                        "frame_rate": frame_rate,
                        "active": bool(
                            int(_1or0)
                        ),  # probably 1 or 0 meaning active or not -> not sure
                    }
                }

            result = {}
            for ch in map(parse_channel_output, res.split(",")):
                result.update(ch)
            return result
        return res

    def _parse_preset_settings_str(self, preset_string) -> dict:
        def_preset_str, sel_preset_str = preset_string.split(",", maxsplit=1)
        def_preset_num, def_preset_name = def_preset_str.split("*")
        sel_preset_num, sel_preset_name = sel_preset_str.split("*")
        return {
            "default_preset_number": def_preset_num,
            "default_preset_name": def_preset_name,
            "selected_preset_number": sel_preset_num,
            "selected_preset_name": sel_preset_name,
        }

    def get_archive_ch_a_encoder_presets(self, parsed=True) -> str | dict[str, str]:
        """
        Sends a command to the Extron SMP device to retrieve the encoder presets
            for channel A of the archive output.
        Returns the response from the device as a string or a dictionary of
            parsed values if `parsed` is True.

        :param parsed: If True, the response will be parsed into a dictionary of key-value pairs.
        :type parsed: bool
        :return: The response from the device as a string or a dictionary of
            parsed values if `parsed` is True.
        :rtype: str | dict[str, str]
        """
        with SMP35x.locks[self.address]:
            self.tn.write("43I")
            res = TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())
            if parsed:
                return self._parse_preset_settings_str(res)
            return res

    def get_ch_b_encoder_presets(self, parsed=True) -> str | dict[str, str]:
        """
        Sends a command to retrieve the channel B encoder presets from the Extron SMP device.

        :param parsed: If True, returns a dictionary of parsed preset settings.
            If False, returns the raw response string.
        :return: A dictionary of parsed preset settings if parsed=True,
            otherwise a raw response string.
        """
        with SMP35x.locks[self.address]:
            self.tn.write("44I")
            res = TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())
            if parsed:
                return self._parse_preset_settings_str(res)
            return res

    def get_confidence_encoder_presets(self, parsed=True) -> str | dict[str, str]:
        """
        Sends a command to retrieve the confidence encoder presets from the Extron SMP device.

        :param parsed: If True, returns a dictionary of parsed preset settings.
            If False, returns the raw response string.
        :return: A dictionary of parsed preset settings if parsed=True,
            otherwise a raw response string.
        """
        with SMP35x.locks[self.address]:
            self.tn.write("45I")
            res = TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())
            if parsed:
                return self._parse_preset_settings_str(res)
            return res

    def get_archive_ch_a_streaming_presets(self, parsed=True) -> str | dict[str, str]:
        """
        Sends a command to the Extron SMP device to get the streaming presets for Archive Channel A.

        Args:
            parsed (bool): If True, returns a dictionary with the selected preset number and name.
                If False, returns a string.

        Returns:
            str | dict[str, str]: The response from the Extron SMP device.
                If parsed is True, returns a dictionary with the selected preset number and name.
                If parsed is False, returns a string.
        """
        with SMP35x.locks[self.address]:
            self.tn.write("46I")
            res = TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())
        if parsed:
            sel_preset_num, sel_preset_name = res.split("*")
            return {
                "selected_preset_number": sel_preset_num,
                "selected_preset_name": sel_preset_name,
            }
        return res

    def get_ch_b_streaming_presets(self, parsed=True) -> str | dict[str, str]:
        """
        Sends a command to retrieve the streaming presets for channel B from the Extron SMP device.

        :param parsed: If True, returns a dictionary with keys "selected_preset_number"
            and "selected_preset_name".
                       If False, returns the raw response string.
        :return: If parsed is True, returns a dictionary with keys "selected_preset_number"
            and "selected_preset_name".
                 If parsed is False, returns the raw response string.
        """
        with SMP35x.locks[self.address]:
            self.tn.write("47I")
            res = TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())
        if parsed:
            sel_preset_num, sel_preset_name = res.split("*")
            return {
                "selected_preset_number": sel_preset_num,
                "selected_preset_name": sel_preset_name,
            }
        return res

    def get_confidence_streaming_presets(self, parsed=True) -> str | dict[str, str]:
        """
        Sends a command to the Extron SMP device to retrieve the currently
            selected confidence streaming preset.
        Returns the response as a string or a dictionary with the selected
            preset number and name if parsed=True.

        :param parsed: Whether to parse the response into a dictionary or
            return it as a string. Default is True.
        :type parsed: bool
        :return: The response as a string or a dictionary with the selected preset number and name.
        :rtype: str | dict[str, str]
        """
        with SMP35x.locks[self.address]:
            self.tn.write("48I")
            res = TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())
        if parsed:
            sel_preset_num, sel_preset_name = res.split("*")
            return {
                "selected_preset_number": sel_preset_num,
                "selected_preset_name": sel_preset_name,
            }
        return res

    def get_layout_presets(self, parsed=True) -> str | dict[str, str]:
        """
        Sends a command to the Extron SMP device to retrieve the current layout presets.

        Args:
            parsed (bool): Whether to parse the response string to a dictionary of preset settings.

        Returns:
            If parsed=True, returns a dictionary of preset settings.
                Otherwise, returns the raw response string.
        """
        with SMP35x.locks[self.address]:
            self.tn.write("49I")
            res = TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())
        if parsed:
            return self._parse_preset_settings_str(res)
        return res

    def trigger_schedule_sync(self) -> bool:
        """
        Triggers a schedule sync on the Extron SMP device.

        Returns:
            bool: True if the schedule sync was successfully triggered, False otherwise.
        """
        with SMP35x.locks[self.address]:
            self.tn.write(f"{self.esc_char}STRGR\n")
            return "TrgrS" == TelnetAdapter._get_response_str(
                self.tn.read_until_non_empty_line()
            )

    def remove_scheduled_events(self) -> bool:
        """
        Sends a command to the Extron SMP device to remove all scheduled events.

        Returns:
            bool: True if the command was successful, False otherwise.
        """
        with SMP35x.locks[self.address]:
            self.tn.write(f"{self.esc_char}XTRGR\n")
            return "TrgrX" == TelnetAdapter._get_response_str(
                self.tn.read_until_non_empty_line()
            )

    def set_unit_name(self, name: str):
        """
        Sets the name of the recorder.

        Args:
            name (str): The name of the recorder.
        """
        with SMP35x.locks[self.address]:
            if ALLOWED_HOSTNAME_RE.match(name):
                self.tn.write(self.esc_char + name + "CN\n")
            else:
                raise ValueError("Invalid name supplied, must be a valid hostname!")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def reset_unit_name(self):
        """
        Resets the unit name of the Extron SMP recorder.

        Returns:
            str: The response from the recorder after resetting the unit name.
        """
        with SMP35x.locks[self.address]:
            self.tn.write(self.esc_char + " CN\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def get_unit_name(self):
        """
        Sends a command to the Extron SMP device to retrieve its unit name.

        Returns:
            str: The unit name of the Extron SMP device.
        """
        with SMP35x.locks[self.address]:
            self.tn.write(self.esc_char + "CN\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def get_telnet_connections(self):
        """
        Sends a command to the Extron SMP device to retrieve a list of
        active Telnet connections, and returns the response.

        Returns:
            str: A string containing the response from the device.
        """
        with SMP35x.locks[self.address]:
            self.tn.write(self.esc_char + "CC\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def set_verbose_mode(self, mode: Union[VerboseMode, int]):
        """
        Sets the verbose mode of the Extron SMP recorder.

        Args:
            mode (Union[VerboseMode, int]): The verbose mode to set. This can be either a
                `VerboseMode` enum value or an integer representing the verbose mode.

        Returns:
            str: The response from the recorder after setting the verbose mode.
        """
        with SMP35x.locks[self.address]:
            mode = self._get_number_from_enum(mode, SMP35x.VerboseMode)
            self.tn.write(self.esc_char + str(mode) + "CV\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def get_verbose_mode(self):
        """
        Sends the 'CV' command to the Extron SMP device to get the current verbose mode setting.

        Returns:
            str: The response from the device, indicating the current verbose mode setting.
        """
        with SMP35x.locks[self.address]:
            self.tn.write(self.esc_char + "CV\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def save_configuration(self, config_type: Union[ConfigurationType, int] = 2):
        """
        Saves the current configuration of the Extron SMP device to non-volatile memory.

        Args:
            config_type (Union[ConfigurationType, int], optional): Type of configuration to save.
            Defaults to 2.

        Returns:
            str: The response from the device after the configuration is saved.
        """
        with SMP35x.locks[self.address]:
            config_type = self._get_number_from_enum(
                config_type, SMP35x.ConfigurationType
            )
            self.tn.write(self.esc_char + f"1*{config_type}XF\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def restore_configuration(self, config_type: Union[ConfigurationType, int] = 2):
        """
        Restores the configuration of the Extron SMP device to the specified configuration type.

        Args:
            config_type (Union[ConfigurationType, int], optional): Configuration type to restore.
            Defaults to 2.

        Returns:
            str: The response from the device.
        """
        with SMP35x.locks[self.address]:
            config_type = self._get_number_from_enum(
                config_type, SMP35x.ConfigurationType
            )
            self.tn.write(self.esc_char + f"0*{config_type}XF\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def reboot(self):
        """
        Reboots the Extron SMP device by sending the '1BOOT' command over Telnet.

        Returns:
            str: The response from the device after sending the '1BOOT' command.
        """
        with SMP35x.locks[self.address]:
            self.tn.write(self.esc_char + "1BOOT\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def restart_network(self):
        """
        Restarts the Extron SMP's network connection by sending the '2BOOT' command over Telnet.

        Returns:
            str: The response from the Extron SMP after sending the '2BOOT' command.
        """
        with SMP35x.locks[self.address]:
            self.tn.write(self.esc_char + "2BOOT\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def reset_flash(self):
        """
        Reset flash memory (excludes recording files).
        :return:
        """
        with SMP35x.locks[self.address]:
            self.tn.write(self.esc_char + "ZFFF\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def system_reset(self):
        """
        Resets device to default and deletes recorded files
        :return:
        """
        with SMP35x.locks[self.address]:
            self.tn.write(self.esc_char + "ZXXX\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def reset_settings_and_delete_all_files(self):
        """
        Reset to default except IP address, delete all user and recorded files
        :return:
        """
        with SMP35x.locks[self.address]:
            self.tn.write(self.esc_char + "ZY\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def absolute_reset(self):
        """
        Same as System Reset, plus returns the IP address and subnet mask to defaults.
        :return:
        """
        self.tn.write(self.esc_char + "ZQQQ\n")
        return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def set_front_panel_lock(self, mode: Union["SMP35x.FrontPanelLockMode", int]):
        """
        Sets the front panel lock mode of the Extron SMP device.

        Args:
            mode (Union["SMP35x.FrontPanelLockMode", int]): The front panel lock mode to set.

        Returns:
            str: The response from the device after setting the front panel lock mode.
        """
        with SMP35x.locks[self.address]:
            mode = self._get_number_from_enum(mode, SMP35x.FrontPanelLockMode)
            self.tn.write(str(mode) + "X\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def get_front_panel_lock(self):
        """
        View executive mode.
        0=Off
        1=complete lockout (no front panel control)
        2=menu lockout
        3=recording controls
        :return:
        """
        with SMP35x.locks[self.address]:
            self.tn.write("X\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

        ### A lot of stuff related to network settings (ports of services, SNMP, IP, DHCP, etc.)
        ### Only some stuff will be implemented here!

    def get_date_time(self):
        """
        Gets the current date and time from the Extron SMP recorder.

        Returns:
            A datetime object representing the current date and time.
        """
        raise NotImplementedError("get_date_time not implemented yet!")

    def get_time_zone(self):
        """
        Gets the time zone of the Extron SMP recorder.

        Returns:
            str: The time zone of the recorder.
        """
        raise NotImplementedError("get_time_zone not implemented yet!")

    def get_dhcp_mode(self):
        """
        Gets the current DHCP mode of the Extron SMP recorder.

        Returns:
            str: The current DHCP mode of the recorder. Possible values are "on", "off", or "auto".
        """
        raise NotImplementedError("get_dhcp_mode not implemented yet!")

    def get_network_settings(self):
        """
        Retrieves the current network settings for the Extron SMP recorder.

        Returns:
            A dictionary containing the current network settings for the recorder.
        """
        raise NotImplementedError("get_network_settings not implemented yet!")

    def get_ip_address(self):
        """
        Returns the IP address of the Extron SMP recorder.
        """
        raise NotImplementedError("get_ip_address not implemented yet!")

    def get_mac_address(self):
        """
        Gets the MAC address of the Extron SMP recorder.

        :return: A string representing the MAC address of the recorder.
        """
        raise NotImplementedError("get_mac_address not implemented yet!")

    def get_subnet_mask(self):
        """
        Gets the subnet mask for the Extron SMP recorder.

        :return: The subnet mask as a string.
        """
        raise NotImplementedError("get_subnet_mask not implemented yet!")

    def get_gateway_ip(self):
        """
        Gets the IP address of the gateway device for the Extron SMP recorder.
        This method is not yet implemented.
        """
        raise NotImplementedError("get_gateway_ip not implemented yet!")

    def get_dns_server_ip(self):
        """
        Returns the IP address of the DNS server configured on the Extron SMP device.

        Raises:
            NotImplementedError: This method has not been implemented yet.
        """
        raise NotImplementedError("get_dns_server_ip not implemented yet!")

    ### RS-232 / serial port related stuff not implemented.

    ### Password and security related stuff not implemented.

    # File related stuff partially implemented

    def view_current_directory(self):
        """
        Sends the 'CJ' command to the Extron SMP device to view the current directory.

        Returns:
            str: The response from the device as a string.
        """
        with SMP35x.locks[self.address]:
            self.tn.write(f"{self.esc_char}CJ\n")
            res = TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())
            return res.split("Dir ", maxsplit=1)[-1]

    def go_to_root_directory(self):
        """
        Sends the command to go to the root directory of the Extron SMP recorder.

        Returns:
            str: The response from the recorder after sending the command to go to
                the root directory.
        """
        with SMP35x.locks[self.address]:
            self.tn.write(f"{self.esc_char}//CJ\n")
            res = TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())
            return res.split("Dir ", maxsplit=1)[-1]

    def up_one_directory(self):
        """
        Sends the command to move up one directory level to the Extron SMP device and
            returns the response.

        Returns:
            str: The response from the Extron SMP device.
        """
        with SMP35x.locks[self.address]:
            self.tn.write(f"{self.esc_char}..CJ\n")
            res = TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())
            return res.split("Dir ", maxsplit=1)[-1]

    def list_files_from_current_directory(
        self, timeout=10
    ) -> List[Dict[str, str | int]]:
        """
        Sends a command to the Extron SMP device to list all files in the current directory.

        Returns:
            A string containing the response from the device, which includes
                a list of all files in the current directory.
        """
        with SMP35x.locks[self.address]:
            self.tn.write(f"{self.esc_char}LF\n")
            res = TelnetAdapter._get_response_str(
                self.tn.read_until(match="Bytes Left", timeout=timeout)
            )

        def parse_line(l):
            l = l.strip()
            match = re.match(FILE_LISTING_RE, l)
            if not match:
                return None
            line_groups = match.groupdict()
            return {
                "file": line_groups["file"],
                "size": int(line_groups["size"]),
                "date": line_groups["date"],
            }

        lines = [
            parse_line(l) if parse_line(l) else None
            for l in res.splitlines()
            if l.strip() != ""
        ]  # remove empty lines

        return [l for l in lines if l is not None]

    def change_directory(self, path: str):
        """
        Changes the current directory on the Extron SMP device to the specified path.

        Args:
            path (str): The path to change to.

        Returns:
            str: Returns the directory path that was changed to.
        """
        if path[-1] != "/":
            path += "/"
        with SMP35x.locks[self.address]:
            self.tn.write(f"{self.esc_char}{path}CJ\n")
            res = TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())
            return res.split("Dir ", maxsplit=1)[-1]

    def erase_current_directory_and_files(self):
        """
        Erases the current directory and all files within it on the Extron SMP recorder.
        This method is intentionally not implemented and will raise a NotImplementedError if called.
        """
        # self.tn.write("/EF\n")
        # return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())
        raise NotImplementedError(
            "erase_current_directory_and_files not implemented on purpose!"
        )

    def erase_current_directory_and_sub_directories(self):
        """
        Erases the current directory and all sub-directories on the Extron SMP device.

        Raises:
            NotImplementedError: This method is not implemented on purpose.
        """
        raise NotImplementedError(
            "erase_current_directory_and_files not implemented on purpose!"
        )

    def set_input(
        self, input_num: Union[InputNumber, int], channel_num: Union[OutputChannel, int]
    ):
        """
        Switches input # (1 to 5) to output channel (1=A [input 1 and 2], 2=B [input 3, 4 and 5])
        :param input_num:
        :param channel_num:
        :return:
        """
        input_num = self._get_number_from_enum(input_num, SMP35x.InputNumber)
        channel_num = self._get_number_from_enum(channel_num, SMP35x.OutputChannel)
        with SMP35x.locks[self.address]:
            self.tn.write(f"{input_num}*{channel_num}!\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def get_input(self, channel_num: Union[OutputChannel, int]) -> int:
        """
        Sends a command to the Extron SMP device to get the current input for the specified channel.

        Args:
            channel_num (Union[OutputChannel, int]): The channel number to get the input for.
            This can be either an integer value or an OutputChannel enum value.

        Returns:
            str: The current input for the specified channel, as a string.

        Raises:
            TelnetError: If there was an error communicating with the Extron SMP device.
        """
        channel_num = self._get_number_from_enum(channel_num, SMP35x.OutputChannel)
        with SMP35x.locks[self.address]:
            self.tn.write(f"{channel_num}!\n")
            return int(
                TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())
            )

    def get_inputs_per_channel(self) -> dict[str, int]:
        """
        Sends a command to the Extron SMP device to retrieve the current input per channel.
        Returns a dictionary with the input number per channel (A+B).
        """
        with SMP35x.locks[self.address]:
            self.tn.write("32I\n")
            res = TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())
            if "*" in res:
                return {x[2]: int(x[3]) for x in res.split("*")}
            return res

    def set_input_format(self, input_num: Union[InputNumber, int], input_format: int):
        """
        Sets the input to the format, where the input_format parameter may be:
        1 = YUVp / HDTV (default)
        2 = YUVi
        3 = Composite
        :param input_num:
        :param input_format:
        :return:
        """
        input_num = self._get_number_from_enum(input_num, SMP35x.InputNumber)
        if input_format not in range(1, 4):
            raise LrcException("input_num must be a value between 1 and 3!")
        with SMP35x.locks[self.address]:
            self.tn.write(f"{input_num}*{input_format}\\\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def get_input_format(self, input_num: Union[InputNumber, int]):
        """
        Get the input format for the specified input number.

        Args:
            input_num (Union[InputNumber, int]): The input number to get the format for.

        Returns:
            str: The input format for the specified input number.
        """
        input_num = self._get_number_from_enum(input_num, SMP35x.InputNumber)
        with SMP35x.locks[self.address]:
            self.tn.write(f"{input_num}\\\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def set_input_name(self, input_num: Union[InputNumber, int], input_name: str):
        """
        Sets the name of the specified input on the Extron SMP device.

        Args:
            input_num (Union[InputNumber, int]): The input number to set the name for.
            input_name (str): The name to set for the input. Must be no longer than
            16 characters and only contain ASCII characters.

        Returns:
            str: The response from the device after setting the input name.
        Raises:
            LrcException: If the input_name is longer than
            16 characters or contains non-ASCII characters.
        """
        input_num = self._get_number_from_enum(input_num, SMP35x.InputNumber)
        if len(input_name) > 16:
            raise LrcException("input_name must be no longer than 16 chars")
        try:
            input_name.encode("ascii")
        except UnicodeEncodeError as exc:
            raise LrcException("input_name must only contain ascii characters") from exc
        with SMP35x.locks[self.address]:
            self.tn.write(f"{self.esc_char}{input_num},{input_name}NI\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def get_input_name(self, input_num: Union[InputNumber, int]) -> str:
        """
        Sends a command to the Extron SMP device to retrieve the name of the input
        corresponding to the given input number. Returns the name of the input as a string.

        Args:
            input_num (Union[InputNumber, int]): The number of the input to retrieve the name for.

        Returns:
            str: The name of the input as a string.
        """
        input_num = self._get_number_from_enum(input_num, SMP35x.InputNumber)
        with SMP35x.locks[self.address]:
            self.tn.write(f"{self.esc_char}{input_num}NI\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def get_input_selection_per_channel(self):
        """
        Sends a command to the Extron SMP device to get the
        input selection per channel and returns the response.

        Returns:
            str: The response from the device.
        """
        with SMP35x.locks[self.address]:
            self.tn.write("32I\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    ### Input configuration part skipped

    def stop_recording(self):
        """
        Sends a command to stop recording on the Extron SMP device and returns the response.

        Returns:
            str: The response from the device.
        """
        with SMP35x.locks[self.address]:
            self.tn.write(f"{self.esc_char}Y0RCDR\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def start_recording(self):
        """
        Sends a command to start recording on the Extron SMP device and returns the response.

        Returns:
            A string containing the response from the device.
        """
        with SMP35x.locks[self.address]:
            self.tn.write(f"{self.esc_char}Y1RCDR\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def pause_recording(self):
        """
        Sends a command to pause recording on the Extron SMP recorder.

        Returns:
            str: The response from the recorder as a string.
        """
        with SMP35x.locks[self.address]:
            self.tn.write(f"{self.esc_char}Y2RCDR\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    @exception_decorator(ConnectionError)
    def get_recording_status(self) -> int:
        """
        Status may be one of:
        0=stop
        1=record
        2=pause
        :return: status
        """
        with SMP35x.locks[self.address]:
            self.tn.write(f"{self.esc_char}YRCDR\n")
            return int(
                TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())
            )

    def is_recording(self) -> bool:
        """
        Returns True if the Extron SMP is currently recording, False otherwise.
        """
        return self.get_recording_status() == 1

    def extent_recording_time(self, extension_time: int):
        """
        Extends a scheduled recording by extension_time minutes
        :param extension_time: must be an int from 0 to 99
        :return:
        """
        if extension_time not in range(0, 100):
            raise LrcException("extension_time must be a value between 0 and 99!")
        with SMP35x.locks[self.address]:
            self.tn.write(f"{self.esc_char}E{extension_time}RCDR\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def add_chapter_marker(self):
        """
        Sends a command to the Extron SMP recorder to add a chapter marker to the current recording.

        Returns:
            str: A response string from the recorder indicating success or failure.
        """
        with SMP35x.locks[self.address]:
            self.tn.write(f"{self.esc_char}BRCDR\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def swap_channel_positions(self):
        """
        Sends a command to the Extron SMP device to swap the positions
            of the current input and output channels.

        Returns:
            str: The response from the device after sending the command.
        """
        with SMP35x.locks[self.address]:
            self.tn.write("%\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def get_recording_status_text(self):
        """
        Sends a command to the Extron SMP device to retrieve the current recording status text.

        Returns:
            A string representing the current recording status text.
        """
        with SMP35x.locks[self.address]:
            self.tn.write("I\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def get_elapsed_recording_time(self):
        """
        Sends a command to the Extron SMP recorder to retrieve the elapsed recording time.

        Returns:
            A string representing the elapsed recording time in the format "HH:MM:SS".
        """
        with SMP35x.locks[self.address]:
            self.tn.write("35I\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def get_remaining_recording_time(self):
        """
        Sends a command to the Extron SMP device to retrieve the remaining recording time.

        Returns:
            str: The remaining recording time in the format "HH:MM:SS".
        """
        with SMP35x.locks[self.address]:
            self.tn.write("36I\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def get_recording_destination(self):
        """
        Sends a command to the Extron SMP device to retrieve the current recording destination.

        Returns:
            str: The recording destination as a string.
        """
        with SMP35x.locks[self.address]:
            self.tn.write("37I\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    ### Metadata part skipped

    def recall_user_preset(
        self,
        channel_number: Union["SMP35x.OutputChannel", int],
        preset_number: Union["SMP35x.UserEncoderLayoutPresetNumber", int],
    ):
        """
        Recalls a user preset on the specified channel.

        Args:
            channel_number (Union[SMP35x.OutputChannel, int]): channel # to recall the preset on.
            preset_number (Union[SMP35x.UserEncoderLayoutPresetNumber, int]): preset # to recall.

        Returns:
            str: The response from the device.
        """
        channel_number = self._get_number_from_enum(
            channel_number, SMP35x.OutputChannel
        )
        preset_number = self._get_number_from_enum(
            preset_number, SMP35x.UserEncoderLayoutPresetNumber
        )
        with SMP35x.locks[self.address]:
            self.tn.write(f"1*{channel_number}*{preset_number}.\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def save_user_preset(
        self,
        channel_number: Union["SMP35x.OutputChannel", int],
        preset_number: Union["SMP35x.UserEncoderLayoutPresetNumber", int],
    ):
        """
        Saves a user preset for the specified channel number and preset number.

        Args:
            channel_number (Union[SMP35x.OutputChannel, int]): The channel number
                to save the preset for.
            preset_number (Union[SMP35x.UserEncoderLayoutPresetNumber, int]): The preset number
                to save the preset to.

        Returns:
            str: The response string from the Telnet server.
        """
        channel_number = self._get_number_from_enum(
            channel_number, SMP35x.OutputChannel
        )
        preset_number = self._get_number_from_enum(
            preset_number, SMP35x.UserEncoderLayoutPresetNumber
        )
        with SMP35x.locks[self.address]:
            self.tn.write(f"1*{channel_number}*{preset_number},\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def set_user_preset_name(
        self,
        preset_number: Union["SMP35x.UserEncoderLayoutPresetNumber", int],
        preset_name: str,
    ):
        """
        Sets the name of a user encoder layout preset on the Extron SMP device.

        Args:
            preset_number (Union[SMP35x.UserEncoderLayoutPresetNumber, int]):
            The number of the preset to set the name for.
            preset_name (str): The name to set for the preset.
            Must be no longer than 16 characters and only contain ASCII characters.

        Returns:
            str: The response from the device after setting the preset name.
        """
        preset_number = self._get_number_from_enum(
            preset_number, SMP35x.UserEncoderLayoutPresetNumber
        )
        if len(preset_name) > 16:
            raise LrcException("preset_name must be no longer than 16 chars")
        try:
            preset_name.encode("ascii")
        except UnicodeEncodeError as exc:
            raise LrcException(
                "preset_name must only contain ascii characters"
            ) from exc
        with SMP35x.locks[self.address]:
            self.tn.write(f"{self.esc_char}1*{preset_number},{preset_name}PNAM\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def get_user_preset_name(
        self, preset_number: Union["SMP35x.UserEncoderLayoutPresetNumber", int]
    ):
        """
        Retrieves the name of a user encoder layout preset from the Extron SMP device.

        Args:
            preset_number (Union[SMP35x.UserEncoderLayoutPresetNumber, int]):
            The number of the preset to retrieve.

        Returns:
            str: The name of the specified user encoder layout preset.
        """
        preset_number = self._get_number_from_enum(
            preset_number, SMP35x.UserEncoderLayoutPresetNumber
        )
        with SMP35x.locks[self.address]:
            self.tn.write(f"{self.esc_char}1*{preset_number}PNAM\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def get_user_presets(self, input_number: Union[InputNumber, int]):
        """
        Retrieves the user presets for the specified input number.

        Args:
            input_number (Union[InputNumber, int]): The input number to retrieve user presets for.

        Returns:
            str: The response string from the device.
        """
        input_number = self._get_number_from_enum(input_number, SMP35x.InputNumber)
        with SMP35x.locks[self.address]:
            self.tn.write(f"52*{input_number}#\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    # Input Presets
    def recall_input_preset(
        self,
        channel_number: Union["SMP35x.OutputChannel", int],
        input_preset_number: int,
    ):
        """
        Recalls an input preset on the specified channel.

        Args:
            channel_number (Union[SMP35x.OutputChannel, int]):
            The channel number to recall the input preset on.
            input_preset_number (int): The input preset number to recall.

        Raises:
            LrcException: If the input preset number is not between 1 and 128.

        Returns:
            str: The response from the device.
        """
        channel_number = self._get_number_from_enum(
            channel_number, SMP35x.OutputChannel
        )
        if input_preset_number not in range(1, 129):
            raise LrcException("preset_number must be a value between 1 and 128!")
        with SMP35x.locks[self.address]:
            self.tn.write(f"2*{channel_number}*{input_preset_number}.\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def save_input_preset(
        self,
        channel_number: Union["SMP35x.OutputChannel", int],
        input_preset_number: int,
    ):
        """
        Saves the current input configuration as a preset on the specified channel.

        Args:
            channel_number (Union[SMP35x.OutputChannel, int]):
            The channel number to save the preset on.
            input_preset_number (int): The preset number to save the input configuration to.

        Raises:
            LrcException: If the input_preset_number is not between 1 and 128.

        Returns:
            str: The response from the device.
        """
        raise NotImplementedError("save_input_preset not implemented yet!")

    def set_input_preset_name(self, input_preset_number: int, preset_name: str):
        """
        Sets the name of an input preset on the Extron SMP recorder.

        Args:
            input_preset_number (int): The number of the input preset to set the name for.
                Must be a value between 1 and 128.
            preset_name (str): The name to set for the input preset. Must be a string of
                ASCII characters no longer than 16 characters.

        Returns:
            str: The response string returned by the Extron SMP recorder after setting
                the input preset name.

        Raises:
            LrcException: If the input_preset_number is not between 1 and 128, or if the
                preset_name is longer than 16 characters or contains non-ASCII characters.
        """
        if input_preset_number not in range(1, 129):
            raise LrcException("preset_number must be a value between 1 and 128!")
        if len(preset_name) > 16:
            raise LrcException("preset_name must be no longer than 16 chars")
        try:
            preset_name.encode("ascii")
        except UnicodeEncodeError as exc:
            raise LrcException(
                "preset_name must only contain ascii characters"
            ) from exc
        with SMP35x.locks[self.address]:
            self.tn.write(f"{self.esc_char}2*{input_preset_number},{preset_name}PNAM\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def get_input_preset_name(self, input_preset_number: int):
        """
        Retrieves the name of the input preset with the given number.

        Args:
            input_preset_number (int): The number of the input preset to retrieve the name of.
                Must be a value between 1 and 128.

        Returns:
            str: The name of the input preset.

        Raises:
            LrcException: If the input_preset_number is not a value between 1 and 128.
        """
        if input_preset_number not in range(1, 129):
            raise LrcException("preset_number must be a value between 1 and 128!")
        with SMP35x.locks[self.address]:
            self.tn.write(f"{self.esc_char}2*{input_preset_number}PNAM\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def delete_input_preset(self, input_preset_number: int):
        """
        Deletes the input preset with the given number.

        Args:
            input_preset_number (int): The number of the input preset to delete.
                Must be a value between 1 and 128.

        Returns:
            str: The response from the device after attempting to delete the input preset.
        """
        if input_preset_number not in range(1, 129):
            raise LrcException("preset_number must be a value between 1 and 128!")
        with SMP35x.locks[self.address]:
            self.tn.write(f"{self.esc_char}X2*{input_preset_number}PRST\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def get_input_presets(self):
        """
        Sends a command to the Extron SMP device to retrieve the available input presets.
        Returns the response from the device as a string.
        """
        self.tn.write("51#\n")
        return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    # Streaming Presets
    def recall_streaming_preset(
        self,
        output_number: int,
        preset_number: Union[UserEncoderLayoutPresetNumber, int],
    ):
        """
        Output_number:
        1 = Channel A
        2 = Channel B
        3 = Confidence Stream
        :param preset_number:
        :param output_number:
        :return:
        """
        if output_number not in range(1, 4):
            raise LrcException("output_number must be a value between 1 and 3!")
        preset_number = self._get_number_from_enum(
            preset_number, SMP35x.UserEncoderLayoutPresetNumber
        )
        with SMP35x.locks[self.address]:
            self.tn.write(f"3*{output_number}*{preset_number}.\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def save_streaming_preset(
        self,
        output_number: int,
        preset_number: Union[UserEncoderLayoutPresetNumber, int],
    ):
        """
        Output_number:
        1 = Channel A
        2 = Channel B
        3 = Confidence Stream
        :param output_number:
        :param preset_number:
        :return:
        """
        if output_number not in range(1, 4):
            raise LrcException("output_number must be a value between 1 and 3!")
        preset_number = self._get_number_from_enum(
            preset_number, SMP35x.UserEncoderLayoutPresetNumber
        )
        with SMP35x.locks[self.address]:
            self.tn.write(f"3*{output_number}*{preset_number},\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def set_streaming_preset_name(
        self, preset_number: Union[UserEncoderLayoutPresetNumber, int], preset_name: str
    ):
        """
        Sets the name of a streaming preset on the Extron SMP device.

        Args:
            preset_number (Union[UserEncoderLayoutPresetNumber, int]):
                The number of the preset to set the name for.
            preset_name (str): The name to set for the preset.
                Must be no longer than 16 characters and contain only ASCII characters.

        Raises:
            LrcException: If the preset_name is longer
            than 16 characters or contains non-ASCII characters.

        Returns:
            str: The response from the Extron SMP device.
        """
        preset_number = self._get_number_from_enum(
            preset_number, SMP35x.UserEncoderLayoutPresetNumber
        )
        if len(preset_name) > 16:
            raise LrcException("preset_name must be no longer than 16 chars")
        try:
            preset_name.encode("ascii")
        except UnicodeEncodeError as exc:
            raise LrcException(
                "preset_name must only contain ascii characters"
            ) from exc
        with SMP35x.locks[self.address]:
            self.tn.write(f"{self.esc_char}3*{preset_number},{preset_name}PNAM\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def get_streaming_preset_name(
        self, preset_number: Union[UserEncoderLayoutPresetNumber, int]
    ):
        """
        Retrieves the name of the streaming preset associated with the given preset number.

        Args:
            preset_number (Union[UserEncoderLayoutPresetNumber, int]): Preset number or enum value.

        Returns:
            str: The name of the streaming preset.
        """
        preset_number = self._get_number_from_enum(
            preset_number, SMP35x.UserEncoderLayoutPresetNumber
        )
        with SMP35x.locks[self.address]:
            self.tn.write(f"{self.esc_char}3*{preset_number}PNAM\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def reset_streaming_preset_to_default(
        self, preset_number: Union[UserEncoderLayoutPresetNumber, int]
    ):
        """
        Resets the streaming preset to its default settings.

        Args:
            preset_number (Union[UserEncoderLayoutPresetNumber, int]): The preset number to reset.

        Returns:
            str: The response from the device.
        """
        preset_number = self._get_number_from_enum(
            preset_number, SMP35x.UserEncoderLayoutPresetNumber
        )
        with SMP35x.locks[self.address]:
            self.tn.write(f"{self.esc_char}X3*{preset_number}PRST\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    # Encoder Presets
    def recall_encoder_preset(
        self,
        output_number: int,
        preset_number: Union[UserEncoderLayoutPresetNumber, int],
    ):
        """
        Output_number:
        1 = Channel A
        2 = Channel B
        3 = Confidence Stream
        :param preset_number:
        :param output_number:
        :return:
        """
        if output_number not in range(1, 4):
            raise LrcException("output_number must be a value between 1 and 3!")
        preset_number = self._get_number_from_enum(
            preset_number, SMP35x.UserEncoderLayoutPresetNumber
        )
        with SMP35x.locks[self.address]:
            self.tn.write(f"4*{output_number}*{preset_number}.\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def save_encoder_preset(
        self,
        output_number: int,
        preset_number: Union[UserEncoderLayoutPresetNumber, int],
    ):
        """
        Output_number:
        1 = Channel A
        2 = Channel B
        3 = Confidence Stream
        :param preset_number:
        :param output_number:
        :return:
        """
        if output_number not in range(1, 4):
            raise LrcException("output_number must be a value between 1 and 3!")
        preset_number = self._get_number_from_enum(
            preset_number, SMP35x.UserEncoderLayoutPresetNumber
        )
        with SMP35x.locks[self.address]:
            self.tn.write(f"4*{output_number}*{preset_number},\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def set_encoder_preset_name(
        self, preset_number: Union[UserEncoderLayoutPresetNumber, int], preset_name: str
    ):
        """
        Sets the name of an encoder preset on the Extron SMP device.

        Args:
            preset_number (Union[UserEncoderLayoutPresetNumber, int]):
                The number of the preset to set the name for.
            preset_name (str): The name to set for the preset.
                Must be no longer than 16 characters and only contain ASCII characters.

        Returns:
            str: The response from the device after setting the preset name.
        Raises:
            LrcException: If the preset_name is longer
            than 16 characters or contains non-ASCII characters.
        """
        preset_number = self._get_number_from_enum(
            preset_number, SMP35x.UserEncoderLayoutPresetNumber
        )
        if len(preset_name) > 16:
            raise LrcException("preset_name must be no longer than 16 chars")
        try:
            preset_name.encode("ascii")
        except UnicodeEncodeError as exc:
            raise LrcException(
                "preset_name must only contain ascii characters"
            ) from exc
        with SMP35x.locks[self.address]:
            self.tn.write(f"{self.esc_char}4*{preset_number},{preset_name}PNAM\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def get_encoder_preset_name(
        self, preset_number: Union[UserEncoderLayoutPresetNumber, int]
    ):
        """
        Sends a command to the Extron SMP device to retrieve the name of the encoder preset
        associated with the given preset number.

        Args:
            preset_number (Union[UserEncoderLayoutPresetNumber, int]): The preset number to
                retrieve the name for. This can be either an integer or a value from the
                UserEncoderLayoutPresetNumber enum.

        Returns:
            str: The name of the encoder preset associated with the given preset number.
        """
        preset_number = self._get_number_from_enum(
            preset_number, SMP35x.UserEncoderLayoutPresetNumber
        )
        with SMP35x.locks[self.address]:
            self.tn.write(f"{self.esc_char}4*{preset_number}PNAM\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def reset_encoder_preset_to_default(
        self, preset_number: Union[UserEncoderLayoutPresetNumber, int]
    ):
        """
        Resets the specified encoder preset to its default settings.

        Args:
            preset_number (Union[UserEncoderLayoutPresetNumber, int]):
                The number of the preset to reset.

        Returns:
            str: The response from the device after sending the reset command.
        """
        preset_number = self._get_number_from_enum(
            preset_number, SMP35x.UserEncoderLayoutPresetNumber
        )
        with SMP35x.locks[self.address]:
            self.tn.write(f"{self.esc_char}X4*{preset_number}PRST\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    # Layout Presets

    def save_layout_preset(
        self, preset_number: Union[UserEncoderLayoutPresetNumber, int]
    ):
        """
        Saves the current layout as a preset with the given number.

        Args:
            preset_number (Union[UserEncoderLayoutPresetNumber, int]):
                The number of the preset to save.
                This can be either an integer or a
                value from the UserEncoderLayoutPresetNumber enum.

        Returns:
            str: The response from the device after sending the save command.
        """
        preset_number = self._get_number_from_enum(
            preset_number, SMP35x.UserEncoderLayoutPresetNumber
        )
        with SMP35x.locks[self.address]:
            self.tn.write(f"7*{preset_number},\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def recall_layout_preset(
        self,
        preset_number: Union[UserEncoderLayoutPresetNumber, int],
        include_input_selections: bool = True,
    ):
        """
        Recalls a layout preset on the Extron SMP device.

        Args:
            preset_number (Union[UserEncoderLayoutPresetNumber, int]):
                The preset number to recall.
            include_input_selections (bool, optional):
                Whether to include input selections in the recall. Defaults to True.

        Returns:
            str: The response from the device.
        """
        preset_number = self._get_number_from_enum(
            preset_number, SMP35x.UserEncoderLayoutPresetNumber
        )
        with SMP35x.locks[self.address]:
            if include_input_selections:
                self.tn.write(f"7*{preset_number}.\n")
            else:
                self.tn.write(f"8*{preset_number}.\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def set_layout_preset_name(
        self, preset_number: Union[UserEncoderLayoutPresetNumber, int], preset_name: str
    ):
        """
        Sets the name of a user encoder layout preset on the Extron SMP device.

        Args:
            preset_number (Union[UserEncoderLayoutPresetNumber, int]):
                The number of the preset to set the name for.
            preset_name (str): The name to set for the preset.
                Must be no longer than 16 characters and only contain ASCII characters.

        Returns:
            str: The response from the device after setting the preset name.
        """
        preset_number = self._get_number_from_enum(
            preset_number, SMP35x.UserEncoderLayoutPresetNumber
        )
        if len(preset_name) > 16:
            raise LrcException("preset_name must be no longer than 16 chars")
        try:
            preset_name.encode("ascii")
        except UnicodeEncodeError as exc:
            raise LrcException(
                "preset_name must only contain ascii characters"
            ) from exc
        with SMP35x.locks[self.address]:
            self.tn.write(f"{self.esc_char}7*{preset_number},{preset_name}PNAM\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def get_layout_preset_name(
        self, preset_number: Union[UserEncoderLayoutPresetNumber, int]
    ):
        """
        Gets the name of the layout preset with the given preset number.

        Args:
            preset_number (Union[UserEncoderLayoutPresetNumber, int]): The preset number
                of the layout preset to get the name of.

        Returns:
            str: The name of the layout preset with the given preset number.
        """
        preset_number = self._get_number_from_enum(
            preset_number, SMP35x.UserEncoderLayoutPresetNumber
        )
        with SMP35x.locks[self.address]:
            self.tn.write(f"{self.esc_char}7*{preset_number}PNAM\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def reset_layout_preset_to_default(
        self, preset_number: Union[UserEncoderLayoutPresetNumber, int]
    ):
        """
        Resets the layout preset to its default value.

        Args:
            preset_number (Union[UserEncoderLayoutPresetNumber, int]):
                The number of the preset to reset.

        Returns:
            str: The response from the device.
        """
        preset_number = self._get_number_from_enum(
            preset_number, SMP35x.UserEncoderLayoutPresetNumber
        )
        with SMP35x.locks[self.address]:
            self.tn.write(f"{self.esc_char}X7*{preset_number}PRST\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    ### Input adjustments skipped

    ### Picture adjustments skipped

    def mute_output(self, output_number: Union[OutputChannel, int]):
        """
        Mutes the specified (video) output channel on the Extron SMP device.

        Args:
            output_number (Union[OutputChannel, int]):
                The output channel to mute. This can be either an
                OutputChannel enum value or an integer representing the channel number.

        Returns:
            str: A response string from the device indicating
            whether the mute command was successful.
        """
        output_number = self._get_number_from_enum(output_number, SMP35x.OutputChannel)
        with SMP35x.locks[self.address]:
            self.tn.write(f"{output_number}*1B\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def unmute_output(self, output_number: Union[OutputChannel, int]):
        """
        Unmute the specified output channel.

        Args:
            output_number (Union[OutputChannel, int]): The output channel to unmute.

        Returns:
            str: The response from the device.
        """
        output_number = self._get_number_from_enum(output_number, SMP35x.OutputChannel)
        with SMP35x.locks[self.address]:
            self.tn.write(f"{output_number}*0B\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def is_muted(self, output_number: Union[OutputChannel, int]) -> bool:
        """
        Returns a boolean indicating whether the specified output channel is currently muted.

        Args:
            output_number (Union[OutputChannel, int]): The output channel to check for muting.

        Returns:
            bool: True if the output channel is muted, False otherwise.
        """
        output_number = self._get_number_from_enum(output_number, SMP35x.OutputChannel)
        with SMP35x.locks[self.address]:
            self.tn.write(f"{output_number}B\n")
            return (
                int(
                    TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())
                )
                > 0
            )

    ### EDID skipped

    ### Encoder settings skipped

    ### some advanced options skipped

    def get_input_hdcp_status(self, input_number: Union[InputNumber, int]):
        """
        returns:
        0 = no sink / source detected
        1 = sink / source detected with HDCP
        2 = sink / source detected without HDCP
        :param input_number: from 1 to 5
        :return:
        """
        input_number = self._get_number_from_enum(input_number, SMP35x.InputNumber)
        with SMP35x.locks[self.address]:
            self.tn.write(f"{self.esc_char}I{input_number}HDCP\n")
            return int(
                TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())
            )

    def is_hdcp_source_detected(self, input_number: Union[InputNumber, int]) -> bool:
        """
        Returns a boolean indicating whether the specified input has an HDCP source connected.

        Args:
            input_number (Union[InputNumber, int]): Input number to check for HDCP source detection.

        Returns:
            bool: True if an HDCP source is detected, False otherwise.
        """
        return int(self.get_input_hdcp_status(input_number)) == 1

    def set_input_authorization_hdcp_on(self, input_number: Union[InputNumber, int]):
        """
        Sets the input authorization HDCP on for the specified input number.

        Args:
            input_number (Union[InputNumber, int]): Input # to set the authorization HDCP on for.

        Returns:
            str: The response string from the TelnetAdapter.

        Raises:
            N/A
        """
        input_number = self._get_number_from_enum(input_number, SMP35x.InputNumber)
        with SMP35x.locks[self.address]:
            self.tn.write(f"{self.esc_char}E{input_number}*1HDCP\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def set_input_authorization_hdcp_off(self, input_number: Union[InputNumber, int]):
        """
        Sets the input authorization for the specified input number to HDCP off.

        Args:
            input_number (Union[InputNumber, int]): The input number to set the authorization for.

        Returns:
            str: The response string from the device.
        """
        input_number = self._get_number_from_enum(input_number, SMP35x.InputNumber)
        with SMP35x.locks[self.address]:
            self.tn.write(f"{self.esc_char}E{input_number}*0HDCP\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def get_input_authorization_hdcp_status(
        self, input_number: Union[InputNumber, int]
    ):
        """
        Gets the HDCP status for the specified input.

        Args:
            input_number (Union[InputNumber, int]): The input number to get the HDCP status for.

        Returns:
            str: The HDCP status of the input.
        """
        input_number = self._get_number_from_enum(input_number, SMP35x.InputNumber)
        with SMP35x.locks[self.address]:
            self.tn.write(f"{self.esc_char}E{input_number}HDCP\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def enable_hdcp_notification(self):
        """
        Enables HDCP notification on the Extron SMP device.

        Returns:
            str: The response from the device.
        """
        with SMP35x.locks[self.address]:
            self.tn.write(f"{self.esc_char}N1HDCP\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def disable_hdcp_notification(self):
        """
        Disables HDCP notification on the Extron SMP device.

        Returns:
            str: The response from the device.
        """
        with SMP35x.locks[self.address]:
            self.tn.write(f"{self.esc_char}N0HDCP\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def get_hdcp_notification_status(self):
        """
        Sends a command to the Extron SMP device to retrieve the current HDCP notification status.

        Returns:
            str: The HDCP notification status response from the device.
        """
        with SMP35x.locks[self.address]:
            self.tn.write(f"{self.esc_char}NHDCP\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    # background image settings

    def set_background_image(self, filename: str):
        """
        Sets the background image of the Extron SMP recorder to the specified file.

        Args:
            filename (str): The filename of the image to set as the background.

        Returns:
            str: The response from the recorder after setting the background image.
        """
        with SMP35x.locks[self.address]:
            self.tn.write(f"{self.esc_char}{filename}RF\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def get_background_image_filename(self):
        """
        Sends a command to the Extron SMP device to retrieve
            the filename of the current background image.

        Returns:
            str: The filename of the current background image.
        """
        with SMP35x.locks[self.address]:
            self.tn.write(f"{self.esc_char}RF\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def mute_background_image(self):
        """
        Mutes the background image of the Extron SMP recorder.

        Returns:
            str: The response from the recorder after muting the background image.
        """
        with SMP35x.locks[self.address]:
            self.tn.write(f"{self.esc_char}0RF\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    # Audio settings
    def mute_audio_channel(self, channel_number: Union["SMP35x.AudioChannels", int]):
        """
        Mutes the specified audio channel.

        Args:
            channel_number (Union[SMP35x.AudioChannels, int]):
                The audio channel to mute. This can be either an integer
                representing the channel number (1-8), or a member of the SMP35x.AudioChannels enum.

        Returns:
            str: The response from the device after muting the channel.
        """
        num = self._get_number_from_enum(channel_number, SMP35x.AudioChannels)
        with SMP35x.locks[self.address]:
            self.tn.write(f"{self.esc_char}M{num}*1AU\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def mute_analog_audio_channel_a(self):
        """
        Mutes both the left and right analog audio channels for input A.

        :return: The response from the device after muting the audio channels.
        :rtype: str
        """
        self.mute_audio_channel(SMP35x.AudioChannels.ANALOG_INPUT_A_LEFT)
        self.mute_audio_channel(SMP35x.AudioChannels.ANALOG_INPUT_A_RIGHT)

    def mute_analog_audio_channel_b(self):
        """
        Mutes both the left and right analog audio channels for input B.

        :return: The response from the device after muting the audio channels.
        :rtype: str
        """
        self.mute_audio_channel(SMP35x.AudioChannels.ANALOG_INPUT_B_LEFT)
        self.mute_audio_channel(SMP35x.AudioChannels.ANALOG_INPUT_B_RIGHT)

    def mute_digital_audio_channel_a(self):
        """
        Mutes both the left and right digital audio channels for input A.

        :return: The response from the device after muting the audio channels.
        :rtype: str
        """
        self.mute_audio_channel(SMP35x.AudioChannels.DIGITAL_INPUT_A_LEFT)
        self.mute_audio_channel(SMP35x.AudioChannels.DIGITAL_INPUT_A_RIGHT)

    def mute_digital_audio_channel_b(self):
        """
        Mutes both the left and right digital audio channels for input B.

        :return: The response from the device after muting the audio channels.
        :rtype: str
        """
        self.mute_audio_channel(SMP35x.AudioChannels.DIGITAL_INPUT_B_LEFT)
        self.mute_audio_channel(SMP35x.AudioChannels.DIGITAL_INPUT_B_RIGHT)

    def mute_output_audio_channels(self):
        """
        Mutes the output audio channels of the Extron SMP device.

        This method calls the `mute_audio_channel` method twice, once for the left output channel
            and once for the right
        output channel.

        :return: None
        """
        self.mute_audio_channel(SMP35x.AudioChannels.OUTPUT_LEFT)
        self.mute_audio_channel(SMP35x.AudioChannels.OUTPUT_RIGHT)

    def mute_all_input_audio_channels(self):
        """
        Mutes all audio channels on the Extron SMP device.

        :return: The response from the device after muting the audio channels.
        :rtype: str
        """
        self.mute_analog_audio_channel_a()
        self.mute_analog_audio_channel_b()
        self.mute_digital_audio_channel_a()
        self.mute_digital_audio_channel_b()

    def unmute_audio_channel(self, channel_number: Union["SMP35x.AudioChannels", int]):
        """
        Unmute the specified audio channel.

        Args:
            channel_number (Union[SMP35x.AudioChannels, int]):
                The audio channel to unmute. This can be either an integer
                representing the channel number, or a member of the SMP35x.AudioChannels enum.

        Returns:
            str: The response from the device after sending the unmute command.
        """
        num = self._get_number_from_enum(channel_number, SMP35x.AudioChannels)
        with SMP35x.locks[self.address]:
            self.tn.write(f"{self.esc_char}M{num}*0AU\n")
            return TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())

    def unmute_analog_audio_channel_a(self):
        """
        Unmutes both the left and right analog audio channels for input A.

        :return: The response from the device after unmuting the audio channels.
        :rtype: str
        """
        self.unmute_audio_channel(SMP35x.AudioChannels.ANALOG_INPUT_A_LEFT)
        self.unmute_audio_channel(SMP35x.AudioChannels.ANALOG_INPUT_A_RIGHT)

    def unmute_analog_audio_channel_b(self):
        """
        Unmutes both the left and right analog audio channels for input B.

        :return: The response from the device after unmuting the audio channels.
        :rtype: str
        """
        self.unmute_audio_channel(SMP35x.AudioChannels.ANALOG_INPUT_B_LEFT)
        self.unmute_audio_channel(SMP35x.AudioChannels.ANALOG_INPUT_B_RIGHT)

    def unmute_digital_audio_channel_a(self):
        """
        Unmutes both the left and right digital audio channels for input A.

        :return: The response from the device after unmuting the audio channels.
        :rtype: str
        """
        self.unmute_audio_channel(SMP35x.AudioChannels.DIGITAL_INPUT_A_LEFT)
        self.unmute_audio_channel(SMP35x.AudioChannels.DIGITAL_INPUT_A_RIGHT)

    def unmute_digital_audio_channel_b(self):
        """
        Unmutes both the left and right digital audio channels for input B.

        :return: The response from the device after unmuting the audio channels.
        :rtype: str
        """
        self.unmute_audio_channel(SMP35x.AudioChannels.DIGITAL_INPUT_B_LEFT)
        self.unmute_audio_channel(SMP35x.AudioChannels.DIGITAL_INPUT_B_RIGHT)

    def unmute_output_audio_channels(self):
        """
        Unmutes the output audio channels of the SMP35x device.
        """
        self.unmute_audio_channel(SMP35x.AudioChannels.OUTPUT_LEFT)
        self.unmute_audio_channel(SMP35x.AudioChannels.OUTPUT_RIGHT)

    def unmute_all_input_audio_channels(self):
        """
        Unmutes all audio channels on the Extron SMP device.

        :return: The response from the device after unmuting the audio channels.
        :rtype: str
        """
        self.unmute_analog_audio_channel_a()
        self.unmute_analog_audio_channel_b()
        self.unmute_digital_audio_channel_a()
        self.unmute_digital_audio_channel_b()

    def is_audio_channel_muted(
        self, channel_number: Union["SMP35x.AudioChannels", int]
    ):
        """
        Returns a boolean indicating whether the specified audio channel is currently muted.

        Args:
            channel_number (Union[SMP35x.AudioChannels, int]): The audio channel number to check.
                This can be either an integer value or a member of the SMP35x.AudioChannels enum.

        Returns:
            bool: True if the audio channel is muted, False otherwise.
        """
        num = self._get_number_from_enum(channel_number, SMP35x.AudioChannels)
        with SMP35x.locks[self.address]:
            self.tn.write(f"{self.esc_char}M{num}AU\n")
            return (
                int(
                    TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())
                )
                > 0
            )

    def is_analog_audio_channel_a_muted(self):
        """
        Returns a boolean indicating whether both
        the left and right analog audio channels for input A are muted.

        :return: A boolean indicating whether both the
        left and right analog audio channels for input A are muted.
        """
        analog_input_a_left = self.is_audio_channel_muted(
            SMP35x.AudioChannels.ANALOG_INPUT_A_LEFT
        )
        analog_input_a_right = self.is_audio_channel_muted(
            SMP35x.AudioChannels.ANALOG_INPUT_A_RIGHT
        )
        return analog_input_a_left and analog_input_a_right

    def is_analog_audio_channel_b_muted(self):
        """
        Returns a boolean indicating whether both the
        left and right channels of analog input B are muted.

        :return: A boolean indicating whether both the
        left and right channels of analog input B are muted.
        :rtype: bool
        """
        analog_input_b_left = self.is_audio_channel_muted(
            SMP35x.AudioChannels.ANALOG_INPUT_B_LEFT
        )
        analog_input_b_right = self.is_audio_channel_muted(
            SMP35x.AudioChannels.ANALOG_INPUT_B_RIGHT
        )
        return analog_input_b_left and analog_input_b_right

    def is_digital_audio_channel_a_muted(self):
        """
        Returns a boolean indicating whether both the
        left and right channels of digital input A are muted.

        :return: A boolean indicating whether both the
        left and right channels of digital input A are muted.
        :rtype: bool
        """
        digital_input_a_left = self.is_audio_channel_muted(
            SMP35x.AudioChannels.DIGITAL_INPUT_A_LEFT
        )
        digital_input_a_right = self.is_audio_channel_muted(
            SMP35x.AudioChannels.DIGITAL_INPUT_A_RIGHT
        )
        return digital_input_a_left and digital_input_a_right

    def is_digital_audio_channel_b_muted(self):
        """
        Returns a boolean indicating whether both the
        left and right channels of digital input B are muted.

        :return: A boolean indicating whether both the
        left and right channels of digital input B are muted.
        :rtype: bool
        """
        digital_input_b_left = self.is_audio_channel_muted(
            SMP35x.AudioChannels.DIGITAL_INPUT_B_LEFT
        )
        digital_input_b_right = self.is_audio_channel_muted(
            SMP35x.AudioChannels.DIGITAL_INPUT_B_RIGHT
        )
        return digital_input_b_left and digital_input_b_right

    def is_audio_output_channel_muted(self):
        """
        Returns a boolean indicating whether both the
        left and right channels of the audio output are muted.

        :return: A boolean indicating whether both the
        left and right channels of the audio output are muted.
        :rtype: bool
        """
        output_left = self.is_audio_channel_muted(SMP35x.AudioChannels.OUTPUT_LEFT)
        output_right = self.is_audio_channel_muted(SMP35x.AudioChannels.OUTPUT_RIGHT)
        return output_left and output_right

    def view_front_panel_audio_level_indicators(self) -> dict:
        """
        Sends a command to the Extron SMP device to view the front panel audio level indicators.
        Values are returned in dB.
        Lowest value is -150 dB, highest value is 0 dB (full bar).
        Bar is empty if value is -60 dB or less.

        Returns:
            dict: dict containing the left and right audio level values.
        """
        with SMP35x.locks[self.address]:
            self.tn.write("34I\n")
            res = TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())
            left, right = res.split("*")
            return {"left": float(int(left) / 10), "right": float(int(right) / 10)}

    def view_audio_input_format(self, audio_input: Union["SMP35x.AudioInput", int]) -> int:
        """
        Sends a command to the Extron SMP device to view the audio input format for the given input.

        Args:
            audio_input (1-5): number of the audio input to view the format for.

        Returns:
            int: 0 = Disable audio, 1 = Analog (default for input 3), 2 = LPCM 2 CH (default)
        """
        with SMP35x.locks[self.address]:
            num = self._get_number_from_enum(audio_input, SMP35x.AudioInput)
            self.tn.write(f"{self.esc_char}I{num}AFMT\n")
            res = TelnetAdapter._get_response_str(self.tn.read_until_non_empty_line())
            return int(res)
