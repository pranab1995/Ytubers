from django.shortcuts import render, redirect
from . models import Hiretuber

from django.contrib import messages
# Create your views here.

    # first_name = models.CharField(max_length=200)
    # last_name = models.CharField(max_length=200)
    # tuber_id = models.IntegerField()
    # tuber_name = models.CharField(max_length=200)
    # message = models.TextField(blank=True)
    # city = models.CharField(max_length=200)
    # state = models.CharField(max_length=200)
    # phone = models.CharField(max_length=200)
    # user_id = models.IntegerField(blank=True)
    # user_id=models.EmailField(blank=True)



def hiretuber(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        tuber_id = request.POST['tuber_id']
        tuber_name = request.POST['tuber_name']
        message = request.POST['message']
        city = request.POST['city']
        state = request.POST['state']
        phone = request.POST['phone']
        user_id = request.POST['user_id']
        email = request.POST['email']

        hiretuber = Hiretuber(first_name=first_name,last_name=last_name,tuber_id=tuber_id,tuber_name=tuber_name,message=message,city=city,state=state,phone=phone,user_id=user_id,email=email)
        hiretuber.save()
        messages.success(request,'Thanks for reaching out!')
        return redirect('youtubers')