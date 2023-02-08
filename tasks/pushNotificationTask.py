from tasks.baseTask import *
from tools.pushNotificationHandler import PushNotificationHelperV2


class PushNotificationTask(BaseTask):
    def __init__(self):
        super().__init__()
        self.notification_helper = PushNotificationHelperV2()

    async def task(self):
        while self.is_running:
            try:
                await self.notification_helper.send_push_notification()
            finally:
                await asyncio.sleep(0.5)
