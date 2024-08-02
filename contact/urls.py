from django.urls import path

from . import views

app_name = "contact"

urlpatterns = [
   path('inbox/',views.inbox,name='inbox'),
   path('new/<int:item_id>/',views.new_conversation,name='new'), 
   path('message/<int:id>/',views.deatil,name='detail')
]
