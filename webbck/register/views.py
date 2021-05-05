from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
# Create your views here.

def register(request):
    permission_classes = (IsAuthenticated,)
    
    return HttpResponse('inside register')