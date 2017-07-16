from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

from .models import Teacher


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


def register_student(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        try:
            Teacher.objects.get(phone=phone)
        except Teacher.DoesNotExist:
            return JsonResponse({'is_teacher':'False'},status=200)
        else:
            return JsonResponse({'is_teacher':'True'},status=200)
    else:
        return JsonResponse({'error':'paramet doesn\'t exist or it is empty'},status=404)


def get_developments(request):

    pass
def get_lesson(request):
    pass

