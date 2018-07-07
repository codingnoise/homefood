from models import CustomUser


class CustomUserAuth(object):

    def authenticate(self, username=None, password=None):
        if not username or not password:
            pass
        try:
            user = CustomUser.objects.get(email=username)
            print "user: " + str(user)
            if user.check_password(password):
                print "checking pass"
                return user
        except CustomUser.DoesNotExist:
            print "does not exist"
            return None

    def get_user(self, user_id):
        try:
            user = CustomUser.objects.get(pk=user_id)
            if user.is_active:
                return user
            return None
        except CustomUser.DoesNotExist:
            return None
