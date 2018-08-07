from homefood.constants import InterviewConstants


class ScheduleMessage:

    def __init__(self, schedule_date, schedule_time, schedule_topic, interviewee_email,
                 interview_status=InterviewConstants.INTERVIEW_STATUS_SCHEDULED,
                 interview_duration=InterviewConstants.DEFAULT_INTERVIEW_DURATION_IN_MINS,
                 interviewer_email=InterviewConstants.DEFAULT_INTERVIEWER_EMAIL,
                 interview_metadata = InterviewConstants.DEFAULT_INTERVIEW_METADATA):
        self.type = MessageTypes.SCHEDULE
        self.schedule_date = schedule_date
        self.schedule_time = schedule_time
        self.schedule_topic = schedule_topic
        self.interview_duration = interview_duration
        self.interview_status = interview_status
        self.interviewee_email = interviewee_email
        self.interviewer_email = interviewer_email
        self.interview_metadata = interview_metadata



class MessageTypes:
    SCHEDULE = "schedule"
