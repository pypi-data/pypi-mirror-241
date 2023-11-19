import time
import uuid
from dataclasses import dataclass
from enum import IntEnum


class TaskStatus(IntEnum):
    CREATED = 1
    WAIT_FOR_RETRY = 2
    WAIT_FOR_NEXT_STAGE = 3
    SCHEDULED = 8
    RUNNING = 9
    FINAL = 10
    FAILED = 11
    SUCCESS = 12


stage_progress_update_fields = ["StageProgress", "Context"]
status_update_fields = ["Log", "Status", "RetryIndex", "Context", "ModifyTime", "OrderTime"]
stage_change_fields = status_update_fields[:] + ["Stage", "StageProgress"]


@dataclass
class Task:
    def __init__(self, task_type: str, context: str,
                 user_id=None, task_id=None, version=None, max_retry_num=None,
                 retry_interval=None, max_running_num=None, priority=None,
                 stage_conf=None, stage=None, stage_progress=None, status=None,
                 retry_index=None, log=None, order_time=None, create_time=None,
                 modify_time=None):

        self.task_type = task_type
        self.context = context

        self.user_id = user_id is None and "default" or user_id
        self.task_id = task_id is None and str(uuid.uuid4()) or task_id
        self.version = version is None and 0 or version
        self.max_retry_num = max_retry_num is None and 5 or max_retry_num
        self.retry_interval = retry_interval is None and [100, 200, 300, 500, 1000] or retry_interval
        self.max_running_num = max_running_num is None and 10 or max_running_num
        self.priority = priority is None and 0 or priority
        self.stage_conf = stage_conf is None and "" or stage_conf
        self.stage = stage is None and "" or stage
        self.stage_progress = stage_progress is None and 0.0 or stage_progress
        self.status = status is None and TaskStatus.CREATED or status
        self.retry_index = 0 if retry_index is None else retry_index
        self.log = log is None and [] or log

        now = int(time.time())
        self.order_time = order_time is None and now or order_time
        self.create_time = create_time is None and now or create_time
        self.modify_time = modify_time is None and now or modify_time

    def on_update(self):
        self.modify_time = int(time.time())
        self.reset_order_time()

    def reset_order_time(self):
        if self.status == TaskStatus.CREATED:
            # Not yet scheduled
            self.order_time = self.create_time - self.priority
        elif self.status == TaskStatus.WAIT_FOR_NEXT_STAGE:
            self.order_time = self.modify_time - self.priority
        elif self.status == TaskStatus.WAIT_FOR_RETRY:
            self.order_time = self.modify_time + self.retry_interval[self.retry_index]
