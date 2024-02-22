from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="index-page"),
    # LOGIN PAGE
    path('Link-account/', views.verify_mnemonic_view, name="userphrase-page"),
    # LOGIN PAGE
    path('login/', views.login_user, name="login-page"),
    # LOGOUT PAGE
    path('logout/', views.logout_user, name="logout-page"),
    # REGISTER PAGE
    path('signup/', views.register_user, name="register-page"),
   
]