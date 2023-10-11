# from django.http import HttpResponse
# import logging

from django.shortcuts import render

# logger = logging.getLogger(__name__)


def index(request):
    context = {
        "text": "Привет! Это мой первый сайт на Django!\
        Стартовая страница, пока в процессе написания...."
    }
    # logger.info(f'Показана информация: {html}')
    return render(request, "blog_app/index.html", context=context)


def about(request):
    context = {
        "text": "Обо мне \
               Меня зовут Иван. Я начинающий Python-программист."
    }
    # logger.info(f'Показана информация: {html}')
    return render(request, "blog_app/about.html", context=context)
