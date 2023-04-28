from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name='menu'),
    re_path(r'^(\w*\/)*$', views.MenuName.as_view())

]