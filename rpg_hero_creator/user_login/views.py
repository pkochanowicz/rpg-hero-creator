from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.views.generic.base import View
from django.core.mail import EmailMessage

from .tokens import account_activation_token

from .forms import SignupForm, UserLoginForm
# Create your views here.

class UserLoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            message = "You're already logged in."
            return render(request, 'access_denied.html', {'message': message})
        else:
            form = UserLoginForm()
            return render(request, 'user_login.html', {'form': form})

    def post(self, request):
        form = UserLoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/warhammer/hero-creation/')
            else:
                return render(request, 'user_login.html', {'form': form,
                                                           'message': 'Wrong login or password'})


class UserLogoutView(View):
    @method_decorator(login_required)
    def get(self, request):
        logout(request)
        return redirect('/')


class AddUserView(View):
    def get(self, request):
        form = SignupForm()
        return render(request, 'add_user.html', {'form': form})

    def post(self, request):
        form = SignupForm(request.POST)

        if form.is_valid():
            cleaned_email = form.cleaned_data['email']
            if User.objects.filter(email=cleaned_email).exists():
                return render(request, 'add_user.html', {'form': form,
                                                         'message': 'User with that email already exists.'})
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your RPG Hero Creator account'
            message = render_to_string('acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password']
            # repeated_password = form.cleaned_data['repeat_password']
            # first_name = form.cleaned_data['first_name']
            # last_name = form.cleaned_data['last_name']
            # email = form.cleaned_data['email']
            # if password != repeated_password:
            #     return render(request, 'add_user.html', {'form': form,
            #                                              'message': 'Passwords don\'t match'})

            # User.objects.create_user(username=username, email=email, password=password,
            #                          first_name=first_name, last_name=last_name)
            return render(request, 'add_user.html', {'form': form,
                                                     'message': 'User created. Please confirm your email address to complete the registration'})
        else:
            return render(request, 'add_user.html', {'form': form,
                                                     'message': 'Form is invalid.'})

def activate(request, uidb64, token):
    form = SignupForm()
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)

        # return redirect('home')
        return render(request, 'add_user.html', {'form': form,
                                                 'message': 'Thank you for your email confirmation. Now you can login your account.'})
    else:
        return render(request, 'add_user.html', {'form': form,
                                                 'message': 'Activation link is invalid!'})