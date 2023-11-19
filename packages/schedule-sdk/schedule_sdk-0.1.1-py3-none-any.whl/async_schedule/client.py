from abc import ABC, abstractmethod
from dataclasses import dataclass

import requests

from async_schedule.domain import Task


@dataclass
class UpdateTaskReq:
    def __init__(self, filedMasks: [str], task: Task):
        # 注意filedMasks中的字段名必须与Task中的字段名一致，且为大写开头的驼峰命名
        self.filedMasks = filedMasks
        self.taskData = task.__dict__


class TaskRpcInterface(ABC):
    @abstractmethod
    def submit_task(self, task: Task):
        pass

    @abstractmethod
    def get_task(self, task_id: str) -> Task:
        pass

    @abstractmethod
    def update_task(self, task_id: str, req: UpdateTaskReq):
        pass


class TaskRpcClient(TaskRpcInterface):
    def __init__(self, host):
        self.host = host

    def submit_task(self, task: Task):
        url = "/task/create"
        response = self._json_post(url, task)
        self._handle_error(response)
        return

    # def hold_tasks(self, req):
    #     url = "/task/hold"
    #     response = self._json_post(url, req)
    #     self._handle_error(response)
    #     return response['data']

    def get_task(self, task_id: str) -> Task:
        url = f"/task/query/{task_id}"
        response = self._json_get(url)
        self._handle_error(response)
        return Task(**response['data']['taskData'])

    def update_task(self, task_id: str, req: UpdateTaskReq):
        url = "/task/update/" + task_id
        response = self._json_post(url, req)
        self._handle_error(response)

    def _json_post(self, url, data=None):
        if data:
            data = data.__dict__
        headers = {'Content-Type': 'application/json'}
        response = requests.post(f"{self.host}{url}", json=data, headers=headers)
        return response.json()

    def _json_get(self, url, data=None):
        if data:
            data = data.__dict__
        headers = {'Content-Type': 'application/json'}
        response = requests.get(f"{self.host}/{url}", json=data, headers=headers)
        return response.json()

    @staticmethod
    def _handle_error(response):
        if response.get('code') == 0 or response.get('code') == 200:
            return
        raise RuntimeError(f"RPC internal error: {response.get('msg')}")
