from django.urls import path

from user import views

app_name='user'

urlpatterns=[
    path('userInfo/',views.get_userinfo,name='userInfo')
]