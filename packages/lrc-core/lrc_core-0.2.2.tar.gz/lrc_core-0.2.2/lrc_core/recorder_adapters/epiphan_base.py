#  Copyright (c) 2019. Tobias Kurze
"""
This is the recorder adapter implementation for Epiphan Recorders. 
The following Epiphan recorder models are supported:
 - LectureRecorder X2
 - LectureRecorder
 - VGADVI Recorder
 - DVI Broadcaster DL
 - DVIRecorderDL
"""
import shutil
import time
from datetime import datetime
from pprint import pprint

import requests
from requests.auth import HTTPBasicAuth

from lrc_core.exception import LrcException, exception_decorator
from lrc_core.recorder_adapters import RecorderAdapter

# HOST = "localhost"

RECORDER_MODEL_NAME = (
    "Epiphan Recorder Adapter "
    "(for: LectureRecorder X2, LectureRecorder, VGADVI Recorder, "
    "DVI Broadcaster DL and DVIRecorderDL)"
)

class Epiphan(RecorderAdapter):
    def __init__(
        self,
        address: str,
        user: str,
        password: str,
        firmware_version: str = "",
        **_kwargs
    ):
        if not address.startswith("http"):
            address = "http://" + address
        super().__init__(address, user, password)
        self.firmware_version = firmware_version
        self.session = requests.Session()
        self.session.auth = HTTPBasicAuth(self.user, self.password)

    @classmethod
    def get_recorder_params(cls) -> dict:
        return {"_requires_user": True, "_requires_password": True}

    def _get_name(self):
        return RECORDER_MODEL_NAME

    def _get_version(self):
        pass

    @exception_decorator(ConnectionError)
    def get_recording_status(self) -> dict:
        res = self.session.get(self.address + "/admin/ajax/recorder_status.cgi")
        if res.ok:
            return res.json()
        raise LrcException(res.text, res.status_code)

    @exception_decorator(ConnectionError)
    def get_sysinfo(self) -> dict:
        res = self.session.get(self.address + "/ajax/sysinfo.cgi")
        if res.ok:
            return res.json()
        raise LrcException(res.text, res.status_code)

    def is_recording(self) -> bool:
        state = self.get_recording_status().get("state", None)
        return state == "up"

    def get_recording_time(self):
        """
        Returns recording time in seconds. Also returns 0 if not recording.
        :return:
        """
        return self.get_recording_status().get("seconds", None)

    def start_recording(self):
        res = self.session.get(self.address + "/admin/ajax/start_recorder.cgi")
        if not res.ok:
            raise LrcException(res.text, res.status_code)
        time.sleep(
            2
        )  # just a little bit of waiting time -> it takes a bit for the Epiphan to update its state

    def stop_recording(self):
        res = self.session.get(self.address + "/admin/ajax/stop_recorder.cgi")
        if not res.ok:
            raise LrcException(res.text, res.status_code)
        time.sleep(
            4
        )  # just a little bit of waiting time -> it takes a bit for the Epiphan to update its state

    def get_ip_address(self):
        try:
            return (
                self.get_sysinfo()
                .get("system")
                .get("network")
                .get("interfaces")[0]
                .get("ipaddr", None)
            )
        except Exception as err:
            raise LrcException(str(err))

    def get_disk_space(self):
        try:
            data = self.get_sysinfo().get("system").get("data")
            return {
                "available": data.get("available", None),
                "free": data.get("free", None),
                "total": data.get("total", None),
                "used": data.get("total", 0) - data.get("available", 0),
            }
        except Exception as err:
            raise LrcException(str(err))

    def get_video_inputs(self) -> list:
        ret = []
        try:
            video = self.get_sysinfo().get("inputs").get("video")
            for v in video:
                ret.append(
                    {
                        "id": v.get("id", None),
                        "name": v.get("name", None),
                        "resolution": v.get("resolution", None),
                    }
                )
            return ret
        except Exception as err:
            raise LrcException(str(err))

    def get_hardware_revision(self):
        try:
            return self.get_sysinfo().get("system").get("firmware")
        except Exception as err:
            raise LrcException(str(err))

    def get_system_time(self):
        try:
            time_stamp = self.get_sysinfo().get("time")
            return {
                "unix_time_stamp": time_stamp,
                "date_time_utc": datetime.utcfromtimestamp(time_stamp).strftime(
                    "%Y-%m-%dT%H:%M:%SZ"
                ),
            }
        except Exception as err:
            raise LrcException(str(err))

    def get_screenshot(self):
        ret = self.session.get(
            self.address
            + "/admin/grab_frame.cgi?size=256x192&device=DAV93133.vga&_t=1573471990578",
            stream=True,
        )

        print(ret)
        pprint(ret.headers)
        with open("out.jpg", "wb") as out_file:
            shutil.copyfileobj(ret.raw, out_file)
        del ret
