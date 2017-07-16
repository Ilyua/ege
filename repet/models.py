from django.db import models
from wiki.models.article import Article


class Pupil(models.Model):
    full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)#TODO
    email = models.EmailField()
    address = models.CharField(max_length=200)#Привязать выбор
    parent_name = models.CharField(max_length=200)
    parent_phone = models.CharField(max_length=200)#TODO
    def __str__(self):
        return self.full_name


class Teacher(models.Model):
    qualifications  =  (('A','Category A'),('B','Category B'),('C','Category C'))
    full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)#TODO
    email = models.EmailField()
    address = models.CharField(max_length=200)#Привязать выбор
    qualification = models.CharField(max_length=1,choices=qualifications)#TODO
    def __str__(self):
        return self.full_name


class Lesson(models.Model):
    theory = models.OneToOneField(
        Article,
        on_delete=models.CASCADE)
    #models.TextField(max_length=200)
    test = theory = models.OneToOneField(
        Article,
        on_delete=models.CASCADE)
    tip = models.TextField(max_length=200)
    number = models.CharField(max_length=200)
    result_type = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    true_answer = models.CharField(max_length=200)
    #TODO
    def __str__(self):
        return self.number

