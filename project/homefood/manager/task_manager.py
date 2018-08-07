from threading import Thread
from Queue import Queue
import time
from common.util.log.Logger import Logger

from homefood.manager.schedule_manager import ScheduleManager


class ScheduleQueue(object):
    q = Queue()


class TaskManager(object):

    def __init__(self):
        self._schedule_manager = ScheduleManager()
        self._is_running = False
        self.logger = Logger().get_logger()

    def is_running(self):
        return self._is_running

    def run(self):
        self._is_running = True
        taskThread = Thread(target=self.check_for_messages)
        try:
            self.logger.info("Starting a task thread for checking for messages from queue")
            taskThread.start()
        except Exception as e:
            self.logger.info("Exception occurred during starting task thread. Exception=%s" % str(e))

    def check_for_messages(self):
        while True:
            if not ScheduleQueue.q.empty():
                msg = ScheduleQueue.q.get()
                self.logger.info("Queue has message %s" % str(msg))
                self._schedule_manager.schedule_appointment(msg)

            time.sleep(2)

    def schedule(self, msg):
        try:
            self.logger.info("Scheduling message %s" % str(msg))
            ScheduleQueue.q.put(msg)
        except Exception as e:
            self.logger.info("Exception occurred during scheduling task. Exception=%s" % str(e))
