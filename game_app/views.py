import random
from django.http import HttpResponse
import logging

from django.shortcuts import render
from game_app.models import Coin, Article, Author, Comment
from .forms import GamesForm, AddAuthorForm

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


def cube(request, count: int):
    result = []
    for _ in range(count):
        response = random.randint(CUBE_MIN, CUBE_MAX)
        result.append(response)
    context = {"result": result}
    return render(request, "game_app/index.html", context=context)


def random_number(request, count: int):
    result = []
    for _ in range(count):
        response = random.randint(MIN_NUMBER, MAX_NUMBER)
        result.append(response)
    context = {"result": result}
    return render(request, "game_app/index.html", context=context)


def get_articles(request, author_id: int):
    author = Author.objects.get(id=author_id)
    articles = Article.objects.filter(author_id=author.id)
    context = {"title": f"Автор: {author.fullname()}", "articles": articles}
    return render(request, "game_app/article.html", context=context)


def detail_article(request, article_id: int):
    article = Article.objects.get(id=article_id)
    comments = Comment.objects.filter(article_id=article_id).order_by("-change_at")
    article.count_views += 1
    article.save()
    context = {"article": article, "comments": comments}
    return render(request, "game_app/detail.html", context=context)


def choice_game(request):
    if request.method == "POST":
        form = GamesForm(request.POST)
        if form.is_valid():
            game = form.cleaned_data["game"]
            count = form.cleaned_data["count"]
            match game:
                case "c":
                    return eagle(request, count)
                case "d":
                    return cube(request, count)
                case "r":
                    return random_number(request, count)
    else:
        form = GamesForm()

    context = {"form": form}
    return render(request, "game_app/games.html", context=context)


def add_author(request):
    if request.method == "POST":
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            # firstname = form.cleaned_data["firstname"]
            # lastname = form.cleaned_data["lastname"]
            # email = form.cleaned_data["email"]
            # biography = form.cleaned_data["biography"]
            # birthdate = form.cleaned_data["birthdate"]
            author = Author.objects.create(**form.cleaned_data)
            #     firstname=firstname,
            #     lastname=lastname,
            #     email=email,
            #     biography=biography,
            #     birthdate=birthdate,
            # )
            author.save()
            return get_articles(request, author.pk)
    else:
        form = AddAuthorForm()

    context = {"form": form}
    return render(request, "game_app/add_author.html", context=context)
