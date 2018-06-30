import ast
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from threading import Thread
from Queue import Queue
import smtplib
import time
from util.Logger import Logger

from constants import Constants
from messages.messages import ScheduleMessage

"""
appointments cache will be of type:
{"YYYY/MM/DD" : ["8:00pm",...]}
"""
class AppointmentsDao:
    appointments = {}

    @staticmethod
    def write_appointments_cache(self, filepath):
        with open(filepath, "w") as f:
            f.write(str(self.appointments))

    @staticmethod
    def get_appointments_cache():
        return AppointmentsDao.appointments

    @staticmethod
    def delete_previous_in_the_past(curr=datetime.today()):
        if not AppointmentsDao.appointments:
            return
        for appointment_date in AppointmentsDao.appointments:
            if datetime.strptime(appointment_date, Constants.DATE_FORMAT) < curr:
                AppointmentsDao.appointments.pop(appointment_date)

    #TODO: Complete
    @staticmethod
    def save_appointment(date, time, topic, email, save_to_db=True):
        # Add to cache
        if date in AppointmentsDao.appointments:
            AppointmentsDao.appointments[date].append(time)
        else:
            AppointmentsDao.appointments[date] = [time]

        # save to db
        if save_to_db:
            pass

    #TODO: Complete
    @staticmethod
    def load_appointments_cache(file_path=None):
        if not file_path:
            # load from db
            pass
        else:
            with open(file_path, "r") as f:
                cache = f.read()
                if not cache:
                    return
                AppointmentsDao.appointments = ast.literal_eval(cache)


class ScheduleManager:
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
    def schedule_appointment(self, date, time, topic, email):
        appointments_cache = AppointmentsDao.get_appointments_cache()
        self.logger.info("Scheduling appointments when cache initially is = %s" % str(appointments_cache))
        if not date or not time:
            self.logger.info("Could not schedule appointment for date=%s, time=%s" % (date, time))
            return False

        AppointmentsDao.save_appointment(date, time, topic, email)
        self.logger.info("Sending email for email=%s date=%s, time=%s" % (email, date, time))
        self._mail_manager.send_email([email], date, time, topic)
        return True


class MailManager:
    FROM_EMAIL = "valleycoachingonline@gmail.com"
    SUBJECT = 'Mock Interview Scheduled'
    BODY = "<html>" \
           "<body>" \
           "<p>Hello there!</p>" \
           "<p>Your %s mock interview has been scheduled for %s at %s and you will soon receive an email with meeting details!</p>" \
           "<p>Thanks,</p>" \
           "<p>Your friends from ValleyCoaching</p>"

    def __init__(self):
        self._gmail_user = "valleycoachingonline@gmail.com"
        self._gmail_password = r"xxxx"
        self._server = None
        self.logger = Logger().get_logger()

    def start_server(self):
        try:
            self.logger.info("Starting email server...")
            self._server = smtplib.SMTP_SSL('smtp.gmail.com')
            self.logger.info("Signing into the email...")
            self._server.login(self._gmail_user, self._gmail_password)
        except Exception as e:
            self.logger.error("Exception occurred on starting SMTP server Exception=%s" % str(e))

    def stop_server(self):
        self.logger.info("Stopping SMTP server")
        self._server.close()

    def get_msg(self, to_email_list, date, time, topic, subject, body, from_email):
        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = from_email
        msg["To"] = to_email_list[0]
        msg_body = MIMEText(body % (topic, date, time), 'html')
        msg.attach(msg_body)
        self.logger.info("Sending message msg=%s" % msg)
        return msg.as_string()

    def send_email(self, to_email_list, date, time, topic, subject=SUBJECT, body=BODY, from_email=FROM_EMAIL, fail_silently=True):
        self.start_server()
        message = self.get_msg(to_email_list, date, time, topic, subject, body, from_email)
        self._server.sendmail(from_email, to_email_list, message)
        self._server.sendmail(from_email, from_email, message)
        self.stop_server()


class ScheduleQueue:
    q = Queue()

class TaskManager:

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
                self._schedule_manager.schedule_appointment(msg.schedule_date, msg.schedule_time, msg.schedule_topic, msg.email)

            time.sleep(2)

    def schedule(self, msg):
        try:
            self.logger.info("Scheduling message %s" % str(msg))
            ScheduleQueue.q.put(msg)
        except Exception as e:
            self.logger.info("Exception occurred during scheduling task. Exception=%s" % str(e))




