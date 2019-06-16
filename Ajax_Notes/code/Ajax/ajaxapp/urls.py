from django.urls import path
from ajaxapp import views

app_name='ajax'

urlpatterns=[
    path('regist/',views.regist,name='regist'),
    path('checkname/',views.checkname,name='checkname'),

]
