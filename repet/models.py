from django.db import models



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
    qualification = models.CharField(max_length=200,choices=qualifications)#TODOПочеум не Choice Field????
    def __str__(self):
        return self.full_name
