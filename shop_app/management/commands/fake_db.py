import random
from django.core.management.base import BaseCommand
from shop_app.models import Client, Good, Order


class Command(BaseCommand):
    help = "Generate fake Clients, Goods and Orders."

    def add_arguments(self, parser):
        parser.add_argument("count", type=int, help="Count")

    def handle(self, *args, **kwargs):
        count = kwargs.get("count")
        for i in range(1, count + 1):
            client = Client(
                name=f"name{i}",
                email=f"email{i}@mail.ru",
                phone=random.randint(10_000_000_000, 99_999_999_999),
                address=f"address{i}",
            )
            good = Good(
                name=f"name{i}",
                description=f"description{i}",
                price=random.randint(1, count) * 1_000,
                amount=random.randint(1, count),
            )
            client.save()
            good.save()
            order = Order(client_id=client.id, total_price=0)
            order.save()
        orders = Order.objects.all()
        for order in orders:
            order.goods.set([random.randint(1, count) for _ in range(count)])
            order.total_price = order.total()
            order.save()
