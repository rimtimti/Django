import random
from django.core.management.base import BaseCommand
from game_app.models import Author, Article, Comment


class Command(BaseCommand):
    help = "Generate fake authors and posts."

    def add_arguments(self, parser):
        parser.add_argument("count", type=int, help="User ID")

    def handle(self, *args, **kwargs):
        count = kwargs.get("count")

        for i in range(1, count + 1):
            author = Author(
                firstname=f"firstname{i}",
                lastname=f"lastname{i}",
                email=f"email{i}@mail.ru",
                biography=f"biography{i}",
                birthdate=f"{random.randint(1900,2023)}-{random.randint(1,12)}-{random.randint(1,28)}",
            )
            author.save()
            for j in range(1, count + 1):
                article = Article(
                    title=f"Title{j}",
                    description=f"description{j}",
                    author_id=author,
                    category=f"category{i}",
                    is_published=random.randint(0, 1),
                )
                article.save()
                for k in range(1, count + 1):
                    comment = Comment(
                        description=f"article{k}",
                        author=author,
                        article=article,
                        # change_at=f"{random.randint(2023,2024)}-{random.randint(10,11)}-{random.randint(8,10)}",
                    )
                    comment.save()
