from django.shortcuts import render
from django.views.generic import TemplateView


# https://uguide.ru/tablica-osnovnykh-tegov-html-s-primerami

# Create your views here.

def index(request):
    text = 1
    name = 'tom'
    list = ['aa', 'bb', 'cc']
    list_int = [1.5364545, 5.39856, 6.32489754789]
    len_list = len(list)
    context = {
        'text': text,
        'name': name,  # передается в шаблон как переменная name
        'list': list,
        'list_int': list_int,
        'len_list': len_list
    }
    return render(request, 'index.html', context)






# def index(request):
#     title = 'мой сайт'
#     text = 'какой-то текст'
#     context = {
#         'title': title,
#         'text': text
#     }
#     return render(request, 'index.html', context)


# class index2(TemplateView):
#     template_name = 'index2.html'
