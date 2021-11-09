import sys
import os
from django.shortcuts import render
from questions import views

def home(request):
    return render(request, 'index.html')

def newpage(request):
    data = {}
    data['question'] = request.GET['question']
    data['answer'] = request.GET['answer']
    option1 = request.GET['option1']
    option2 = request.GET['option2']
    option3 = request.GET['option3']
    option4 = request.GET['option4']
    data['options'] = [option1, option2, option3, option4]
    if data:
        views.send_firebase(data)
        return render(request, 'newpage.html', {'data':data})
    else:
        return render(request, 'newpage.html', {'data':"DOCUMENT NOT VALID"})