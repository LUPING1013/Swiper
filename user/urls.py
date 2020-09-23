from django.urls import path

from user import apis

app_name='user'

urlpatterns=[
    path('userInfo/', apis.get_userinfo, name='userInfo')
]