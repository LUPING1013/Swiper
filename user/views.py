from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
def get_userinfo(request):
    phonenum = request.GET.get('phonenum')
    nickname = request.GET.get('nickname')
    gender = request.GET.get('gender')
    birthday = request.GET.get('birthday')
    avatar = request.GET.get('avatar')
    location = request.GET.get('location')
    data = {
        'phonenum': phonenum,
        'nickname': nickname,
        'gender': gender,
        'birthday': birthday,
        'avatar': avatar,
        'locations': location
    }
    return JsonResponse(data=data)

def send_code(request):
    phonenum=request.GET.get('phonenum')
    sms(phonenum)
    return JsonResponse(data=data)
