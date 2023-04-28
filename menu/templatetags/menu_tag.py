from django import template
from menu.models import *
from django.db.models import Q

register = template.Library()

# @register.simple_tag()
# def show_menu(name):
#     print(name)
#     print(Field.objects.filter(parent__isnull=False, menu__name='Sport').order_by('url')[0].level)
#
#     o = Field.objects.filter( menu__name='Sport').order_by('url')
#     l = [({'level': 0}, o[0])]
#     print(o)
#     for i in range(len(o)-1):
#         l.append((o[i], o[i+1]))
#     print(l)
#     return l


@register.inclusion_tag("menu/menu_draw.html", takes_context=True)
def show_menu(context, menu_name):

    url_path = context.request.path[1:]

    sub_menus = url_path.split('/')
    path = ''
    path_list = []
    for sub_menu in sub_menus:
        path += f'{sub_menu}/'
        path_list.append(path)

    query = Field.objects.filter(Q(menu__name=menu_name)&(Q(parent__url__in=path_list) | Q(parent__isnull=True))).order_by('url')

    neighbour_pairs = [({'level': 0}, query[0])]

    for i in range(len(query)-1):
        neighbour_pairs.append((query[i], query[i+1]))

    return {"menu": neighbour_pairs, "name": query[0].menu.name}


@register.simple_tag()
def binary_range(minn, maxx):
    return range(int(maxx)-int(minn))