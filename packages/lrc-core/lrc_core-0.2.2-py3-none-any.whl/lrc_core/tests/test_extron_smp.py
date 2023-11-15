# pylint: disable=missing-function-docstring, redefined-outer-name
"""_summary_

Returns:
    _type_: _description_
"""
from loguru import logger
import pytest
from lrc_core.config import SMP_IP, SMP_PW

from lrc_core.recorder_adapters.extron_smp import SMP35x


@pytest.fixture  # test fixture decorator
def smp():
    """
    Returns an instance of the SMP35x class with the specified IP address and password.
    If auto_login is True, the function will attempt to log in to the device automatically.
    """
    logger.debug(f"Creating SMP35x instance with IP: {SMP_IP}, PW: ****")
    return SMP35x(SMP_IP, SMP_PW, auto_login=True)


def test_view_audio_input_format(smp: SMP35x):
    res = smp.view_audio_input_format(1)
    logger.debug(res)
    assert isinstance(res, dict)


def test_get_inputs_per_channel(smp: SMP35x):
    res = smp.get_inputs_per_channel()
    logger.debug(res)
    assert isinstance(res, dict)


def test_change_directory(smp: SMP35x):
    target_dir = "backgrounds"
    res = smp.change_directory(target_dir)
    assert isinstance(res, str)
    assert target_dir in res


def test_view_current_directory(smp: SMP35x):
    target_dir = "certs"
    smp.change_directory(target_dir)
    res = smp.view_current_directory()
    assert target_dir in res
    assert isinstance(res, str)


def test_up_one_directory(smp: SMP35x):
    smp.change_directory("certs")
    res = smp.up_one_directory()
    assert isinstance(res, str)
    assert res == "/"


def test_list_files_from_current_directory(smp: SMP35x):
    smp.change_directory("certs")
    res = smp.list_files_from_current_directory()
    assert isinstance(res, list)
    assert len(res) > 0


def test_go_to_root_directory(smp: SMP35x):
    res = smp.go_to_root_directory()
    assert isinstance(res, str)
    assert res == "/"


def test_view_front_panel_audio_level_indicators(smp: SMP35x):
    res = smp.view_front_panel_audio_level_indicators()
    assert isinstance(res, dict)


def test_get_active_alarms(smp: SMP35x):
    res = smp.get_active_alarms()
    assert isinstance(res, dict)


def test_trigger_schedule_sync(smp: SMP35x):
    res = smp.trigger_schedule_sync()
    assert isinstance(res, bool)


def test_get_layout_presets(smp: SMP35x):
    res = smp.get_layout_presets()
    assert isinstance(res, dict)
    assert len(res) > 0


def test_get_bootstrap_version(smp: SMP35x):
    res = smp.get_bootstrap_version()
    assert isinstance(res, str)
    assert len(res) > 0


def test_get_part_number(smp: SMP35x):
    res = smp.get_part_number()
    assert isinstance(res, str)
    assert len(res) > 0


def test_get_model_name(smp: SMP35x):
    res = smp.get_model_name()
    assert isinstance(res, str)
    assert len(res) > 0


def test_get_model_description(smp: SMP35x):
    res = smp.get_model_description()
    assert isinstance(res, str)
    assert len(res) > 0


def test_get_system_memory_usage(smp: SMP35x):
    res = smp.get_system_memory_usage()
    assert isinstance(res, str)
    assert len(res) > 0


def test_get_confidence_encoder_presets(smp: SMP35x):
    res = smp.get_confidence_encoder_presets(parsed=True)
    assert isinstance(res, dict)
    assert len(res) > 0


def test_get_archive_ch_a_encoder_presets(smp: SMP35x):
    res = smp.get_archive_ch_a_encoder_presets()
    assert isinstance(res, dict)


def test_get_ch_b_encoder_presets(smp: SMP35x):
    res = smp.get_ch_b_encoder_presets()
    assert isinstance(res, dict)


def test_get_selected_input_status(smp: SMP35x):
    res = smp.get_selected_input_status(parsed=True)
    assert isinstance(res, dict)


def test_get_temperature(smp: SMP35x):
    res = smp.get_temperature(as_number=True)
    assert isinstance(res, float)


def test_get_recording_status(smp: SMP35x):
    res = smp.get_recording_status()
    assert res in [0, 1, 2]
    assert smp.is_recording() == (res == 1)


def test_get_version(smp: SMP35x):
    res = smp.get_version()
    assert isinstance(res, str)


def test_audio_channel_mute(smp: SMP35x):
    res = smp.is_audio_channel_muted(SMP35x.AudioChannels.ANALOG_INPUT_A_LEFT)
    assert isinstance(res, bool)
    if res:
        smp.unmute_audio_channel(SMP35x.AudioChannels.ANALOG_INPUT_A_LEFT)
        assert smp.is_analog_audio_channel_a_muted() is False
    else:
        smp.mute_audio_channel(SMP35x.AudioChannels.ANALOG_INPUT_A_LEFT)
        assert smp.is_analog_audio_channel_a_muted() is True


def test_video_muted(smp: SMP35x):
    res = smp.is_muted(2)
    assert isinstance(res, bool)
    if res is True:
        smp.unmute_output(2)
        assert smp.is_muted(2) is False
        smp.mute_output(2)
    else:
        smp.mute_output(2)
        assert smp.is_muted(2) is True
        smp.unmute_output(2)
    assert res == smp.is_muted(2)


def test_all_audio_channel_mute(smp: SMP35x):
    smp.mute_all_input_audio_channels()
    assert smp.is_audio_channel_muted


def test_get_encoder_preset_name(smp: SMP35x):
    res = smp.get_encoder_preset_name(1)
    assert isinstance(res, str)


def test_get_user_presets(smp: SMP35x):
    res = smp.get_user_presets(1)
    assert len(res) == 16


def test_get_stream_presets(smp: SMP35x):
    res = smp.get_streaming_preset_name(1)
    assert isinstance(res, str)


def test_get_input_preset_name(smp: SMP35x):
    res = smp.get_input_preset_name(1)
    assert isinstance(res, str)


def test_get_input_presets(smp: SMP35x):
    res = smp.get_input_presets()
    assert len(res) == 128


def test_get_recording_status_text(smp: SMP35x):
    res = smp.get_recording_status_text()
    assert isinstance(res, str)


def test_hdcp_state(smp: SMP35x):
    res = smp.is_hdcp_source_detected(SMP35x.InputNumber.INPUT_1)
    assert isinstance(res, bool)


def _():
    print(smp.get_version(verbose_info=False))
    print(smp.get_file_transfer_config())
    print(smp.save_configuration())
    print(smp.restore_configuration())

    print(smp.get_file_transfer_config())

    # print(smp.get_unit_name())
    # print(smp.set_unit_name("mzsmp"))
    # print(smp.get_unit_name())
    # print(smp.reset_unit_name())

    print(smp.set_front_panel_lock(0))
    print(smp.get_front_panel_lock())

    print(smp.get_input_name(1))
    print(smp.get_input_selection_per_channel())
    print("Preset Name: " + smp.get_user_preset_name(2))
    print(smp.get_layout_preset_name(2))
    print(smp.recall_encoder_preset(3, 1))
