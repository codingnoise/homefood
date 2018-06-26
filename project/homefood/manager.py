import ast
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from threading import Thread
from Queue import Queue
import smtplib
import time

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
    def get_appointments_cache(self):
        return self.appointments

    @staticmethod
    def delete_previous_in_the_past(self, curr=datetime.today()):
        if not self.appointments:
            return
        for appointment_date in self.appointments:
            if datetime.strptime(appointment_date, Constants.DATE_FORMAT) < curr:
                self.appointments.pop(appointment_date)

    #TODO: Complete
    @staticmethod
    def save_appointment(self, date, time, email, save_to_db=True):
        # Add to cache
        if date in self.appointments:
            self.appointments[date].append(time)
        else:
            self.appointments[date] = [time]

        # save to db
        if save_to_db:
            pass

    #TODO: Complete
    @staticmethod
    def load_appointments_cache(self, file_path=None):
        if not file_path:
            # load from db
            pass
        else:
            with open(file_path, "r") as f:
                cache = f.read()
                if not cache:
                    return
                self.appointments = ast.literal_eval(cache)

class SchedulerManager:

    """
    Weekdays: 8:00pm, 9:00pm, 10:00pm, 11:00 pm
    Weekends: 8:00pm, 9:00pm, 10:00pm, 11:00 pm, 11:30pm, 12:00pm, 12:30pm

    date format = "YYYY-MM-DD"
    appointments will have ex: {"YYYY/MM/DD" : ["8:00pm",...]}
    """

    def __init__(self):
        self._weekday_times = ["8:00pm", "9:00pm", "10:00pm", "11:00pm"]
        self._weekend_times = ["8:00pm", "9:00pm", "10:00pm", "11:00pm", "11:45pm", "12:30pm"]
        self._mail_manager = MailManager()

    # date should be in PST
    def get_availability(self, date):
        if not date:
            return []
        dt = datetime.strptime(date, Constants.DATE_FORMAT)
        if dt < datetime.now() or dt == datetime.today():
            return []
        times = self._weekend_times if dt.weekday() == 4 or dt.weekday() == 5 else self._weekday_times
        appointments_cache = AppointmentsDao.get_appointments_cache()
        if date in appointments_cache:
            return list(set(times) - set(appointments_cache))
        return times

    # assuming date is in "YYYY-MM-DD" format and time is in "8:00pm" format
    # Todo: What if more than one person schedules at the same time
    # Todo: Write schedule to a file/db
    # on success - returns true, else false
    # @asyncio.coroutine
    def schedule_appointment(self, date, time, email):
        appointments_cache = AppointmentsDao.get_appointments_cache()
        print "Begin Appointments = " + str(appointments_cache)
        if not date or not time:
            print "not date or time"
            return False

        AppointmentsDao.save_appointment(date, time, email)
        # if date in AppointmentsCache.appointments:
        #     AppointmentsCache.appointments[date].append(time)
        # else:
        #     AppointmentsCache.appointments[date] = [time]

        print "Preparing to send email..."
        self._mail_manager.sendMail([email])
        return True


class MailManager:
    FROM_EMAIL = "valleycoachingonline@gmail.com"
    SUBJECT = 'Mock Interview Scheduled'
    BODY = "<html>" \
           "<body>" \
           "<p>Hello there!</p>" \
           "<p>Your mock interview has been scheduled for %s at %s and you will soon receive an email with meeting details!</p>" \
           "<p>Thanks,</p>" \
           "<p>Your friends from ValleyCoaching</p>"

    def __init__(self):
        self._gmail_user = "valleycoachingonline@gmail.com"
        self._gmail_password = r"xxx"
        self._server = None

    def start_server(self):
        try:
            print "Starting server..."
            self._server = smtplib.SMTP_SSL('smtp.gmail.com')
            print "logging in..."
            self._server.login(self._gmail_user, self._gmail_password)
        except Exception as e:
            print "Exception occurred on starting SMTP server " + str(e)

    def stop_server(self):
        print "Stopping gmail server..."
        self._server.close()

    def get_msg(self, to_email_list, subject, body, from_email):
        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = from_email
        msg["To"] = to_email_list[0]
        msg_body = MIMEText(body, 'html')
        msg.attach(msg_body)
        return msg.as_string()

    # @asyncio.coroutine
    def sendMail(self, to_email_list, subject=SUBJECT, body=BODY, from_email=FROM_EMAIL, fail_silently=True):
        self.start_server()
        message = self.get_msg(to_email_list, subject, body, from_email)
        self._server.sendmail(from_email, to_email_list, message)
        self.stop_server()


class ScheduleQueue:
    q = Queue()

class TaskManager:

    def __init__(self):
        self._schedule_manager = SchedulerManager()
        self._is_running = False

    def is_running(self):
        return self._is_running

    def run(self):
        self._is_running = True
        taskThread = Thread(target=self.check_for_messages)
        try:
            taskThread.start()
        except Exception as e:
            print "Something went wrong during running Task Manager... exception=" + str(e)

    def check_for_messages(self):
        while True:
            if not ScheduleQueue.q.empty():
                print "Starting to schedule..."
                msg = ScheduleQueue.q.get()
                self._schedule_manager.schedule_appointment(msg.schedule_date, msg.schedule_time, msg.email)

            time.sleep(2)

    def schedule(self, msg):
        try:
            print "scheduled!!!!!"
            ScheduleQueue.q.put(msg)
            print "after scheduling q.empty()-->" + str(ScheduleQueue.q.empty())
        except Exception as e:
            print "Something went wrong during scheduling task " + str(msg) + " exception=" + str(e)




