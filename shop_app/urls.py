from django.urls import path
from shop_app import views

urlpatterns = [
    path("client/all/", views.get_clients, name="clients"),
    path("good/all/", views.get_goods, name="goods"),
    path("order/all/", views.get_orders, name="orders"),
    path(
        "client/orders/<int:client_id>",
        views.get_orders_by_client_id,
        name="client_orders",
    ),
    path("client/del/<int:client_id>", views.delete_client, name="delete_client"),
    path("good/del/<int:good_id>", views.delete_good, name="delete_good"),
    path("order/del/<int:order_id>", views.delete_order, name="delete_order"),
    path(
        "client/edit_name/<int:client_id>/<str:name>",
        views.edit_client_name,
        name="edit_client_name",
    ),
    path(
        "good/edit_price/<int:good_id>/<int:price>",
        views.edit_good_price,
        name="edit_good_price",
    ),
    path(
        "good/edit_amount/<int:good_id>/<int:amount>",
        views.edit_good_amount,
        name="edit_good_amount",
    ),
    path(
        "order/edit_good_id/<int:order_id>/<int:good_id>/<int:good_id_new>",
        views.edit_good_id_in_order,
        name="edit_good_id_in_order",
    ),
]
