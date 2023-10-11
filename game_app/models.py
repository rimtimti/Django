from collections import Counter
from django.db import models

# Create your models here.


class Coin(models.Model):
    is_eagle = models.CharField(max_length=50)
    create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Сторона: {self.is_eagle}, время: {self.create}"

    @staticmethod
    def counter(n: int) -> dict:
        """
        Возвращает ключ:кол-во значений для n последних бросков монеты
        """
        coins = Coin.objects.order_by("-create")[:n]
        return dict(Counter(coin.is_eagle for coin in coins))


class Author(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.CharField(max_length=300)
    birthdate = models.DateField()

    def fullname(self):
        return f"{self.firstname} {self.lastname}"


class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    create_at = models.DateField(auto_now_add=True)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    count_views = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)


class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    description = models.CharField(max_length=300)
    create_at = models.DateField(auto_now_add=True)
    change_at = models.DateField(auto_now_add=True)
