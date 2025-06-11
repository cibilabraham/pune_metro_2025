from django.shortcuts import render, redirect
from django.views.generic import ListView

from django.views import View
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.exceptions import ObjectDoesNotExist

from fracas.models import *
from fracas.logics import get_random_key, sendEmail
from django.urls import reverse
from django.http import HttpResponseRedirect

from django.utils import timezone


# Create your views here
def index(request):
    if request.method == "POST":
        if "failureDataCollection" in request.POST:
            model = FailureData
            field_names = [f.name for f in model._meta.get_fields()]
            data = [[getattr(ins, name) for name in field_names]
                for ins in FailureData.objects.prefetch_related().all()]
            return render(request, "FailureDataCollection.html", {'field_names': field_names, 'data': data})
    return render(request, "index.html")

def failure_data_view(ListView):
    model = FailureData
    return render(ListView, "FailureDataCollection.html")


class IndexView(View):
    """ It was a view for the index view """
    template_name = 'django_sb_admin/login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

    # def post(self, request, *args, **kwargs):
    #     return render(request, self.template_name, {})



class RegistrationView(View):
    """ It was a view for the company registration view """
    template_name = 'django_sb_admin/register.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):

        if request.method == 'POST':
            req = self.request.POST
            first_name = req.get('first_name')
            print(first_name)
            last_name = req.get('last_name')
            print(last_name)
            # x = validateEmail(email)
            # print(x)
            email = req.get('email')
            print(email)
            password = req.get('password')
            conf_pass = req.get('conf_password')
            print(password)
            print(conf_pass)
            message = ''
            if password == conf_pass:
                if not User.objects.filter(username=email):
                    user = User.objects.create(username=email)
                    try:
                        user.set_password(password)
                        user.is_superuser = "True"
                        user.is_staff = "True"
                        user.save()
                        userprofile = UserProfile.objects.create(user=user, first_name=first_name, last_name=last_name)
                        request.session['login'] = 'true'
                        # return redirect('defect status')
                        return HttpResponseRedirect(reverse('admin:index'))
                    except:
                        user.delete()
                        message = 'An error occure while registration'
                else:
                    message = 'A user with this email already exists'
            else:
                message = 'Password and confirm password must be identical'

        return render(request, self.template_name, {"message": message})

class UserLogoutView(View):
    def get(self, request, *args, **kwargs):
        auth.logout(request)
        return redirect('index')

class UserLoginView(View):
    """ It was a view for the comp login view """
    template_name = 'django_sb_admin/login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

    def post(self, request, *args, **kwargs):

        if request.method == 'POST':
            message = ''
            req = self.request.POST
            email = req.get('email')
            password = req.get('password')
            print(email)
            print(password)
            request.session['email'] = email

            auth_user = auth.authenticate(username=email, password=password)

            if auth_user:
                request.session['login'] = 'true'
                # return redirect('defect status')
                auth.login(request, auth_user)
                return HttpResponseRedirect(reverse('admin:index'))
            else:
                message = 'Invalid credentials given'

        return render(request, self.template_name, {"message": message})

class ForgotPasswordView(View):
    template_name = 'django_sb_admin/forgot_password.html'

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            req = request.POST
        print(req.get('email'))
        try:
            message = ''
            # user = User.objects.get(username=req.get('email'))
            user = UserProfile.objects.get(user=User.objects.get(username=req.get('email')))
            url = request.build_absolute_uri()[:-len(request.get_full_path())]
            
            try:
                key = UserResetKey.objects.get(user=user)
            except:
                key = UserResetKey(user=user)

            new_random_key = get_random_key()
            while UserResetKey.objects.filter(key=new_random_key).exists():
                new_random_key = get_random_key()

            key.key = new_random_key
            key.expires_on = timezone.now() + timezone.timedelta(minutes=5)
            key.save()
                
            sender = "mahinmaja5790@gmail.com"
            recipient = req.get('email')
            subject = "Password Reset Email"
            # email_data = {'user':user, 'url':url  + '#/password/reset/confirm/?key=' + key.key}
            # file_name = 'pwd_reset.html'
            # body = "https://fracas-app.com/password_update/?user_name={}".format(recipient)
            body = url + "/password_update/?key=" + key.key
            sendEmail(sender, recipient, subject, body)
        except ObjectDoesNotExist:
            message = 'No user exists'
        return redirect('index')

class PasswordUpdateView(View):
    template_name = 'django_sb_admin/password_reset.html'

    def get(self, request, *args, **kwargs):
        if request.method == "GET":
            req = request.GET
        key = req.get('key')
        key_expire = "false"
        try:
            key = UserResetKey.objects.get(key=key)
        except:
            message = "Invalid key"
        if key.expires_on < timezone.now():
            key_expire = "true"
        return render(request, self.template_name, {'key': key.key, 'key_expire':key_expire})
    
    def post(self, request, *args, **kwargs):

        if request.method == 'POST':
            message = ''
            req = request.POST   
            key = req.get('key')
            key = UserResetKey.objects.get(key=key)
            try:
                key = UserResetKey.objects.get(key=key)
            except:
                message = "Invalid key"

            password = req.get('password')
            conf_password = req.get('conf_password')
            print(password, "passowrd")
            print(conf_password, "confirm password")
            if password == conf_password:
                try:
                    key.user.user.set_password(password)
                    key.user.user.save()
                    key.delete()
                    return redirect('index')
                except:
                    pass
            else:
                message = 'password and confirm password must be identical'
            
        return render(request, self.template_name, {'message': message})