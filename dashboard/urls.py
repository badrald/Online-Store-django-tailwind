from django.urls import path
from . import views
app_name = 'dash'
urlpatterns = [
    path("",views.index,name='index')
]