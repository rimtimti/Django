import random
from django.http import HttpResponse
import logging

from django.shortcuts import render
from game_app.models import Coin, Article, Author, Comment

logger = logging.getLogger(__name__)

MIN_NUMBER = 0
MAX_NUMBER = 100
CUBE_MIN = 1
CUBE_MAX = 6


# def eagle(request):
#     game_list = ["орел", "решка"]
#     response = random.choice(game_list)
#     coin = Coin(is_eagle=response)
#     coin.save()
#     logger.info(f"Монета выпала стороной: {response}")
#     return HttpResponse(response)


def eagle(request, count: int):
    game_list = ["орел", "решка"]
    result = []
    for _ in range(count):
        response = random.choice(game_list)
        result.append(response)
    context = {"result": result}
    return render(request, "game_app/index.html", context=context)


def show_coins(request, n: int):
    return HttpResponse(f"{Coin.counter(n)}")


def cube(request):
    cube_value = random.randint(CUBE_MIN, CUBE_MAX)
    logger.info(f"Кубик выпал стороной: {cube_value}")
    return HttpResponse(cube_value)


def random_number(request):
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    logger.info(f"Случайное число от {MIN_NUMBER} до {MAX_NUMBER}: {number}")
    return HttpResponse(number)


def get_articles(request, author_id: int):
    author = Author.objects.get(id=author_id)
    articles = Article.objects.filter(author_id=author.id)
    context = {"articles": articles}
    return render(request, "game_app/article.html", context=context)


def detail_article(request, article_id: int):
    article = Article.objects.get(id=article_id)
    comments = Comment.objects.filter(article_id=article_id).order_by("-change_at")
    article.count_views += 1
    article.save()
    context = {"article": article, "comments": comments}
    return render(request, "game_app/detail.html", context=context)
