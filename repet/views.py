from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Student,Teacher
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
def register_student(request):
    if request.method == 'POST':
        full_name = request.POST.get('phone')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        address = request.POST.get('address')
        parent_name = request.POST.get('parent_name')
        parent_phone = request.POST.get('parent_phone')
        student = Student(
                full_name = full_name,
                phone = phone,
                email = email,
                address = address,#Привязать выбор
                parent_name = parent_name,
                parent_phone = parent_phone)#TODO)
        student.save()
        return JsonResponse({'error':'good'},status=200)
    else:
        return JsonResponse({'error':'Unsuitable request method'},status=404)



def get_developments(request):
    pass
def get_lesson(request):
    pass

