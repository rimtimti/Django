import datetime
from django.http import HttpResponse
from django.shortcuts import render
from shop_app.models import Client, Good, Order
from .forms import GoodForm

import logging

logger = logging.getLogger(__name__)


def get_clients(request):
    clients = Client.objects.all()
    context = {"clients": clients}
    return render(request, "shop_app/clients.html", context=context)


def get_client_goods(request, client_id: int, days: int):
    repiod = datetime.date.today() - datetime.timedelta(days=days)
    client = Client.objects.get(id=client_id)
    orders = Order.objects.filter(client_id=client_id, create_at__gte=repiod)
    context = {"count_days": days, "client": client, "orders": orders}
    return render(request, "shop_app/client_goods.html", context=context)


def get_goods(request):
    goods = Good.objects.all()
    context = "<br>".join(str(g) + "<br>" for g in goods)
    return HttpResponse(context)


def get_orders(request):
    orders = Order.objects.all()
    context = "<br>".join(str(order) + "<br>" for order in orders)
    return HttpResponse(context)


def get_orders_by_client_id(request, client_id: int):
    orders = Order.objects.filter(client_id=client_id)
    if orders:
        context = "<br>".join(str(order) + "<br>" for order in orders)
    else:
        context = f"У клиента с id: {client_id} нет заказов"
    return HttpResponse(context)


def delete_client(request, client_id: int):
    client = Client.objects.filter(pk=client_id)
    if client:
        client.delete()
        return HttpResponse(f"Клиент {client_id} удален")
    else:
        return HttpResponse(f"Клиент {client_id} не найден")


def delete_good(request, good_id: int):
    good = Good.objects.filter(pk=good_id)
    if good:
        good.delete()
        return HttpResponse(f"Товар {good_id} удален")
    else:
        return HttpResponse(f"Товар {good_id} не найден")


def delete_order(request, order_id: int):
    order = Order.objects.filter(pk=order_id)
    if order:
        order.delete()
        return HttpResponse(f"Заказ {order_id} удален")
    else:
        return HttpResponse(f"Заказ {order_id} не найден")


def edit_client_name(request, client_id: int, name: str):
    client = Client.objects.filter(pk=client_id).first()
    if client:
        client.name = name
        client.save()
        return HttpResponse(f"Имя клиента {client_id} изменено")
    else:
        return HttpResponse(f"Клиент {client_id} не найден")


def edit_good_price(request, good_id: int, price: int):
    good = Good.objects.filter(pk=good_id).first()
    if good:
        good.price = price
        good.save()
        return HttpResponse(f"Цена товара {good_id} изменена на {price}")
    else:
        return HttpResponse(f"Товар {good_id} не найден")


def edit_good_amount(request, good_id: int, amount: int):
    good = Good.objects.filter(pk=good_id).first()
    if good:
        good.amount = amount
        good.save()
        return HttpResponse(f"Количество товара {good_id} изменено на {amount}")
    else:
        return HttpResponse(f"Товар {good_id} не найден")


def edit_good_id_in_order(request, order_id: int, good_id: int, good_id_new: int):
    order = Order.objects.filter(pk=order_id).first()
    if order:
        goods = order.goods.all()
        for good in goods:
            if good.id == good_id:
                good.id = good_id_new
                order.goods.set(goods)
                order.save()
                return HttpResponse(
                    f"Товар {good_id} в заказе {order_id} изменен на {good_id_new}"
                )
            else:
                return HttpResponse(f"Товар {good_id} в заказе {order_id} не найден")
    else:
        return HttpResponse(f"Заказ {order_id} не найден")


def add_good(request):
    if request.method == "POST":
        form = GoodForm(request.POST, request.FILES)
        if form.is_valid():
            good = Good.objects.create(**form.cleaned_data)
            logger.info(f"В базу данных введен товар: {good.__str__()}")
            good.save()
            return HttpResponse(f"Товар сохранен: {good.__str__()}")
    else:
        form = GoodForm()
    return render(request, "shop_app/good_form.html", {"form": form})
