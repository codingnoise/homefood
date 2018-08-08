from django.views.generic import View, ListView
from django.shortcuts import render, reverse, redirect
from django.template import RequestContext
from forms import CustomUserCreationForm, AuthForm
from models import CustomUserManager, CustomUser
from user_backend import CustomUserAuth
from django.contrib.auth import login

from common.util.log.Logger import Logger


class RegisterView(View):
    LOGGER = Logger().get_logger()
    signup_template = "users/register.html"

    def post(self, request):
        try:
            create_user_form = CustomUserCreationForm(request.POST)
            if create_user_form.is_valid():
                user = create_user_form.cleaned_data
                self.LOGGER.info("Registered user email=%s name=%s" %(user.get("email"), user.get("name")))
                user_email = user.get("email")
                user_password = user.get("password1")
                user_name = user.get("name")
                # TODO: Validate password using auth
                # Create user
                CustomUser.objects.create_user(user_email, user_name, user_password)
                self.LOGGER.info("Successful sign up for user email=%s name=%s" % (user_email, user_name))
            else:
                user = create_user_form.cleaned_data
                self.LOGGER.error("Create user form is invalid for form=%s" % str(user))
            return redirect(reverse("homefood:schedule"))
        except Exception as e:
            self.LOGGER.exception("Error during sign up for user name=%s" % str(e))
            return render(request, self.signup_template)


class AuthView(View):
    LOGGER = Logger().get_logger()
    signup_template = "users/register.html"

    def post(self, request):
        try:
            auth_form = AuthForm(request.POST)
            if auth_form.is_valid():
                user_data = auth_form.cleaned_data
                self.LOGGER.info("Authenticating user details=%s" % (str(user_data)))
                user_email = user_data.get("email")
                user_password = user_data.get("password")
                auth = CustomUserAuth()
                user = auth.authenticate(user_email, user_password)
                self.LOGGER.info("Is Authenticated=%s user details=%s" % (str(user.is_authenticated()), str(user_data)))
                # TODO: Login with user name and details
                if not user:
                    self.LOGGER.error("User doesn't exist for user details=%s" % (str(user_data)))
                    return render(request, self.signup_template, RequestContext(request))
                if user.is_active:
                    request.session.set_expiry(2592000)
                    login(request, user)
                self.LOGGER.info("Successfully authenticated user=%s" % (str(user_email)))
            else:
                self.LOGGER.error("AuthForm is not valid for details=%s" % (auth_form.cleaned_data))
            return redirect(reverse("homefood:schedule"))
        except Exception as e:
            self.LOGGER.exception("Error during authentication for user name=%s" % str(e))
            return redirect(reverse("users:signup"))


class SignupView(ListView):
    template_name = "users/register.html"

    def get_queryset(self):
        return ""


class HomeView(ListView):
    template_name = "users/home.html"

    def get_queryset(self):
        return ""
