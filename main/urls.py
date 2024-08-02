from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import LogInForm
urlpatterns = [
     path('',views.Index,name='index'),
     path('Contect/',views.Contect,name='contect'),
     path('signup/',views.SignUp,name="signup"),
     path('login/',auth_views.LoginView.as_view(template_name='Main/login.html',authentication_form=LogInForm),name='login')
]