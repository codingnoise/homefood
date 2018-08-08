import ast
from datetime import datetime

from django.db import connection

from homefood.constants import Constants, InterviewConstants
from homefood.models import Appointments

from users.models import CustomUser

from common.util.log.Logger import Logger

class AppointmentsDao(object):
    """
    appointments cache will be of type:
    {"YYYY/MM/DD" : ["8:00pm",...]}
    """
    appointments = {}
    LOGGER = Logger().get_logger()

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
    def save_appointment(schedule_msg, save_to_db=True):
        # Add to cache
        date, time, topic, email = schedule_msg.schedule_date, schedule_msg.schedule_time, \
                                   schedule_msg.schedule_topic, schedule_msg.interviewee_email
        if date in AppointmentsDao.appointments:
            AppointmentsDao.appointments[date].append(time)
        else:
            AppointmentsDao.appointments[date] = [time]

        interviewee_user = CustomUser.objects.get(email=email)
        if not interviewee_user:
            raise Exception("Invalid interviewee user provided while saving appointment")

        # save to db
        if save_to_db:
            AppointmentsDao.LOGGER.info("Saving appointment to database, "
                                        "appointment_date=%s and appointment_time=%s" % (date, time))
            appointment = Appointments(interview_date=schedule_msg.schedule_date,
                                       interview_time=schedule_msg.schedule_time,
                                       interview_topic=schedule_msg.schedule_topic,
                                       interview_duration=schedule_msg.interview_duration,
                                       interviewee_email=interviewee_user,
                                       interviewer_email= schedule_msg.interviewer_email,
                                       interview_status=schedule_msg.interview_status,
                                       interview_metadata=schedule_msg.interview_metadata)
            print "interviewee=" +str(appointment.interviewee_email)
            appointment.save()


    @staticmethod
    def get_scheduled_interviews(user_email, status=InterviewConstants.INTERVIEW_STATUS_SCHEDULED):
        interviews = Appointments.objects.filter(interview_status=status, interviewee_email__email=user_email)
        response = [{
                        "interview_date": interview.interview_date,
                        "interview_topic": interview.interview_topic
                    }
                    for interview in interviews]
        print "interviews: "
        print str(interviews)
        return response

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



