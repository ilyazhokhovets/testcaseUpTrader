from django.shortcuts import render
from django.views.generic.base import View


class MenuName(View):
    def get(self, request, path):
        return render(request, 'menu/main.html')