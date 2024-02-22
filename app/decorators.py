from django.contrib.auth.decorators import user_passes_test
from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def check_user(user):
    return not user.is_authenticated


user_logout_required = user_passes_test(check_user, '/', None)

def auth_user_should_not_access(viewfunc):
    return user_logout_required(viewfunc)





def not_logged_in_required(function):
    """
    Decorator that restricts access to the decorated view only to unauthenticated users.

    Args:
        function: The view function to be decorated.

    Returns:
        The decorated function.
    """
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index-page')  # Redirect to your desired URL
        else:
            return function(request, *args, **kwargs)
    return wrapper



