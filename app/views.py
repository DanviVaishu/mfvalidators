from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse

def create_student(request):
    ESFO=StudentForm()
    d={'ESFO':ESFO}
    if request.method=='POST':
        SFDO=StudentForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('data inserted successfully')
        else:
            return  HttpResponse('data is invalid')

    return render(request,'create_student.html',d)
