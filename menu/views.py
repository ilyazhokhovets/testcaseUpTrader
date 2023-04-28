from django.shortcuts import render
from django.views.generic.base import View
from .models import *
from django.db.models import Q
# Create your views here.

def home(request):

    return render(request, 'menu/main.html')


class MenuName(View):
    def get(self, request, path):
        return render(request, 'menu/main.html')