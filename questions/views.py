from django.shortcuts import render
import firebase_admin
from firebase_admin import credentials,firestore, initialize_app
import os
import sys
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

def init():
    cred = credentials.Certificate("./ayo-belajar-bahasa-isyarat-firebase-adminsdk-3nrjb-7e5e12761f.json")
    firebase_admin.initialize_app(cred)

    # env = environ.Env()
    # environ.Env.read_env()
    # firebase_admin.initialize_app({
    #         'project_id': env('PROJECT_ID'),
    #         'client_email': env('CLIENT_EMAIL'),
    #         'private_key': env('PRIVATE_KEY')
    #     })

    db = firestore.client()
    return db

db = init()

def send_firebase(data):
    db.collection(u'questions').add(data)

# Create your views here.
class QuestionViewSet(viewsets.ViewSet):
    def get_questions(self, request):
        docs = db.collection(u'questions').stream()
        questions = []
        for doc in docs:
            if doc.exists:
                questions.append(doc.to_dict())
            else:
                return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(questions)
    def input_question(self, request):
        data = request.data
        if data:
            send_firebase(data)
            return Response(data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
