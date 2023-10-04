from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)


def index(request):
    html = (
        "<h1>Привет! Это мой первый сайт на Django!</h1>"
        "<p>Стартовая страница, пока в процессе написания....</p>"
    )
    logger.info(f"Показана информация: {html}")
    return HttpResponse(html)


def about(request):
    html = "<h1>Обо мне</h1>" "<p>Меня зовут Иван. Я начинающий Python-программист.</p>"
    logger.info(f"Показана информация: {html}")
    return HttpResponse(html)
