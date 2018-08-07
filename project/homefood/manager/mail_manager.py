from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from common.util.log.Logger import Logger

class MailManager(object):
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
        self._gmail_password = r"Jtlc2012..."
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