# pylint: disable=missing-function-docstring, redefined-outer-name
"""_summary_

Returns:
    _type_: _description_
"""
import pytest
from lrc_core.config import EPIPHAN_URL, EPIPHAN_USER, EPIPHAN_PW
from lrc_core.recorder_adapters.epiphan_base import Epiphan


@pytest.fixture  # test fixture decorator
def epiphan():
    """
    Returns an instance of the SMP35x class with the specified IP address and password.
    If auto_login is True, the function will attempt to log in to the device automatically.
    """
    return Epiphan(EPIPHAN_URL, EPIPHAN_USER, EPIPHAN_PW)

@pytest.mark.skip(reason="no way of currently testing this")
def test_get_recording_status(epiphan: Epiphan):
    res = epiphan.get_recording_status()
    assert isinstance(res, dict)


def _(epiphan):
    if epiphan.is_recording():
        epiphan.stop_recording()
    else:
        epiphan.start_recording()

    print(epiphan.get_ip_address())
    print(epiphan.get_disk_space())
    print(epiphan.get_video_inputs())
    print(epiphan.get_hardware_revision())
    print(epiphan.get_system_time())

    epiphan.get_screenshot()
