from models import CustomUser
from common.util.log.Logger import  Logger


class CustomUserAuth(object):
    LOGGER = Logger().get_logger()

    def authenticate(self, username=None, password=None):
        if not username or not password:
            pass
        try:
            self.LOGGER.info("Authenticating user for user=%s", username)
            user = CustomUser.objects.get(email=username)
            if user.check_password(password):
                self.LOGGER.info("Successful authnetication for user=%s", username)
                return user
        except CustomUser.DoesNotExist:
            self.LOGGER.exception("No record found during authentication for user=%s", username)
            return None

    def get_user(self, user_id):
        try:
            print "!!!!!!!USERID = %s" % user_id
            user = CustomUser.objects.get(pk=user_id)
            if user.is_active:
                print "User is active!!"
                return user
            return None
        except CustomUser.DoesNotExist:
            self.LOGGER.exception("No record found while trying to get user=%s", user_id)
            return None
