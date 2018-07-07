from django.views.generic import View, ListView
from django.shortcuts import render
from django.template import RequestContext
from forms import CustomUserCreationForm, AuthForm
from models import CustomUserManager, CustomUser
from user_backend import CustomUserAuth
from django.contrib.auth import login


class RegisterView(View):
    user_home_template = "users/home.html"
    signup_template = "users/register.html"

    def post(self, request):
        try:
            create_user_form = CustomUserCreationForm(request.POST)
            if create_user_form.is_valid():
                user = create_user_form.cleaned_data
                print "USER NAME= " + user.get("name") + " EMAIL=" + user.get("email") + " PASS=" + user.get("password1")
                user_email = user.get("email")
                user_password = user.get("password1")
                user_name = user.get("name")
                # TODO: Validate password using auth
                # Create user
                CustomUser.objects.create_user(user_email, user_name, user_password)
                print "Success!"
            else:
                user = create_user_form
                print "invalid" + str(user.errors)
            return render(request, self.user_home_template)
        except Exception as e:
            print "Error " + str(e)
            return render(request, self.signup_template)


class AuthView(View):
    user_home_template = "homefood/schedule.html"
    signup_template = "users/register.html"

    def post(self, request):
        try:
            print "Here!"
            auth_form = AuthForm(request.POST)
            if auth_form.is_valid():
                user_data = auth_form.cleaned_data
                print "data = " + str(user_data)
                user_email = user_data.get("email")
                user_password = user_data.get("password")
                print "pass: " + str(user_password)
                auth = CustomUserAuth()
                user = auth.authenticate(user_email, user_password)
                print "auth=" + str(user.is_authenticated())
                # TODO: Login with user name and details
                if not user:
                    print "failure!"
                    return render(request, self.signup_template, RequestContext(request))
                if user.is_active:
                    print "active"
                    request.session.set_expiry(86400)
                    login(request, user)
                print "Success!"
            else:
                print "invalid" + str(auth_form.errors)
            return render(request, self.user_home_template)
        except Exception as e:
            print "Error " + str(e)
            return render(request, self.signup_template)

class SignupView(ListView):
    template_name = "users/register.html"

    def get_queryset(self):
        return ""

class HomeView(ListView):
    template_name = "users/home.html"

    def get_queryset(self):
        return ""
