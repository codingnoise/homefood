
class ScheduleMessage:

    def __init__(self, schedule_date, schedule_time, schedule_topic, email):
        self.type = MessageTypes.SCHEDULE
        self.schedule_time = schedule_time
        self.schedule_date = schedule_date
        self.schedule_topic = schedule_topic
        self.email = email

class MessageTypes:
    SCHEDULE = "schedule"