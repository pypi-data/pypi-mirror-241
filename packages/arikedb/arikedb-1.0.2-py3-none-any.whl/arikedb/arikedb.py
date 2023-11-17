import copy
import json
import time
from json.decoder import JSONDecodeError
from queue import Queue, Empty
from threading import Thread
from typing import Optional, List

import socket

START_MSG = "_!1@#2$%3^&4*_"
END_MSG = "*_4&^3%$2#@1!_"
SLEN = len(START_MSG)
ELEN = len(END_MSG)


class ArikedbClientBase:

    def __init__(self, host: str = "localhost", port: int = 6923):
        """RTDB Client constructor"""
        self._host = host
        self._port = port
        self._socket: Optional[socket.socket] = None
        self._recv_th = None
        self._resp_data = Queue()

    def connect(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.connect((self._host, self._port))
        self._socket.setblocking(False)
        self._recv_th = Thread(target=self._read_response_batch, daemon=True)
        self._recv_th.start()

    def exec_command_batch(self, commands: List[dict],
                           timeout: Optional[float] = None) -> List[dict]:
        batch = {"commands": []}
        suid = int(time.time() * 1_000_000)
        uids = [suid + i for i in range(len(commands))]

        for cmd, uid in zip(commands, uids):
            cmd_ = copy.deepcopy(cmd)
            cmd_["uid"] = uid
            batch["commands"].append(cmd_)

        self._send_command_batch(batch)
        responses = []
        t0 = time.time()
        while True:
            try:
                elapsed = time.time() - t0
                to = timeout - elapsed
                if to < 0:
                    to = 0
                resp = self._resp_data.get(timeout=to)
            except Empty:
                break
            if resp["cmd_uid"] in uids:
                responses.append(resp)
                uids.remove(resp["cmd_uid"])
                if not uids:
                    break
            elif resp["cmd_uid"] == -1:
                return [resp]
            else:
                self._resp_data.put(resp)

        assert len(responses) == len(commands)
        return responses

    def exec_command(self, command: dict,
                     timeout: Optional[float] = None) -> dict:
        return self.exec_command_batch([command], timeout)[0]

    def _send_command_batch(self, cmd_batch: dict):
        return self._socket.sendall(
            f"{START_MSG}{json.dumps(cmd_batch)}{END_MSG}".encode()
        )

    def _read_response_batch(self):
        stream = ""
        while True:
            try:
                data = self._socket.recv(2048)
            except socket.error:
                continue
            if len(data) == 0:
                break
            stream += data.decode()
            while START_MSG in stream and END_MSG in stream:
                start = stream.find(START_MSG)
                end = stream.find(END_MSG)
                batch_str = stream[start + SLEN: end]
                try:
                    batch = json.loads(batch_str)
                    for resp in batch["responses"]:
                        self._resp_data.put(resp)
                except (KeyError, TypeError, JSONDecodeError):
                    pass
                stream = stream[end + ELEN:]
