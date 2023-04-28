from django.urls import path, re_path
from . import views

urlpatterns = [

    re_path(r'^(\w*\/)*$|^$', views.MenuName.as_view())

]