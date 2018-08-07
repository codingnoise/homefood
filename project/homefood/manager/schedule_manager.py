
from datetime import datetime
from common.util.log.Logger import Logger

from homefood.manager.mail_manager import MailManager
from homefood.dao.appointments_dao import AppointmentsDao
from homefood.constants import Constants


class ScheduleManager(object):
    def __init__(self):
        self._weekday_times = ["8:00pm", "9:00pm", "10:00pm", "11:00pm"]
        self._weekend_times = ["8:00pm", "9:00pm", "10:00pm", "11:00pm", "11:45pm", "12:30pm"]
        self._mail_manager = MailManager()
        self.logger = Logger().get_logger()

    def get_availability(self, date):
        if not date:
            self.logger.info("The date supplied is empty, date=%s" % date)
            return []

        dt = datetime.strptime(date, Constants.DATE_FORMAT)
        if dt < datetime.now() or dt == datetime.today():
            self.logger.info("The date supplied is current, date=%s" % date)
            return []

        times = self._weekend_times if dt.weekday() == 4 or dt.weekday() == 5 else self._weekday_times
        appointments_cache = AppointmentsDao.get_appointments_cache()
        if date in appointments_cache:
            return list(set(times) - set(appointments_cache[date]))
        return times

    # assuming date is in "YYYY-MM-DD" format and time is in "8:00pm" format
    # Todo: What if more than one person schedules at the same time
    # Todo: Write schedule to a file/db
    # on success - returns true, else false
    def schedule_appointment(self, schedule_message):
        appointments_cache = AppointmentsDao.get_appointments_cache()
        self.logger.info("Scheduling appointments when cache initially is = %s" % str(appointments_cache))
        time = schedule_message.schedule_time
        date = schedule_message.schedule_date
        topic = schedule_message.schedule_topic
        interviewee_email = schedule_message.interviewee_email
        if not schedule_message.schedule_date or not schedule_message.schedule_time:
            self.logger.info("Could not schedule appointment for date=%s, time=%s"
                             % (schedule_message.schedule_date, schedule_message.schedule_time))
            return False

        AppointmentsDao.save_appointment(schedule_message)
        AppointmentsDao.get_scheduled_interviews(user_email="penchant09@gmail.com")
        self.logger.info("Sending email for email=%s date=%s, time=%s" % (interviewee_email, date, time))
        self._mail_manager.send_email([interviewee_email], date, time, topic)
        return True