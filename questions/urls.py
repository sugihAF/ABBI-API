from django.contrib import admin
from django.urls import path

from .views import QuestionViewSet

urlpatterns = [
    path('questions', QuestionViewSet.as_view({
        'get' : 'get_questions',
        'post' : 'input_question'
    }))]