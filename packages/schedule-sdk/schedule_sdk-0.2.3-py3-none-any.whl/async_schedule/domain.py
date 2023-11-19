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
    def __init__(self, task_type, context: str,
                 user_id="default",
                 version=0, max_retry_num=5,
                 retry_interval=None, max_running_num=10, priority=0,
                 stage_conf="", stage=""):
        if retry_interval is None:
            retry_interval = [100, 200, 300, 500, 1000]

        self.user_id = user_id
        self.task_id = str(uuid.uuid4())  # 生成task_id
        self.type = task_type
        self.version = version
        self.max_retry_num = max_retry_num
        self.retry_interval = retry_interval
        self.max_running_num = max_running_num
        self.priority = priority
        self.stage_conf = stage_conf
        self.stage = stage
        self.stage_progress = 0
        self.status = TaskStatus.CREATED
        self.retry_index = 0
        self.log = []
        self.context = context

        now = int(time.time())
        self.order_time = now
        self.create_time = now
        self.modify_time = now

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
