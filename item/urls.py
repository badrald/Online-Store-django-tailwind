from django.urls import path
from . import views

app_name= 'item'

urlpatterns=[
    path('',views.browse,name='browse'),
    path("<int:id>/",views.detail,name='detail'),
    path("newItem/",views.new_item,name='new_item'),
     path("delete/<int:id>/",views.delete,name='delete'),
     path("edit/<int:id>/",views.edit,name='edit')
]