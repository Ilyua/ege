from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Teacher
import json

def is_teacher(request):

    if request.GET.get('phone'):
        phone = request.GET.get('phone')
        try:
            Teacher.objects.get(phone=phone)
        except Teacher.DoesNotExist:
            return JsonResponse({'is_teacher':'False'},status=200)
        else:
            return JsonResponse({'is_teacher':'True'},status=200)
    else:
        return JsonResponse({'error':'paramet doesn\'t exist or it is empty'},status=404)

@csrf_exempt
def register_user(request):
    if request.method == 'POST':


        print(request.body)
        phone = request.POST['phone']
        print(phone)
        teacher = Teacher(
                full_name = 'test',
                phone = phone,
                email = '123@mail.com',
                address = 'qwee',#Привязать выбор
                qualification = 'A')#TODO)
        teacher.save()
        return JsonResponse({'error':'good'},status=200)
    else:
        return JsonResponse({'error':'Unsuitable request method'},status=404)



def get_developments(request):
    pass
