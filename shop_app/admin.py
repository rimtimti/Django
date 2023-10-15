from django.contrib import admin

# Register your models here.

from shop_app.models import Client, Good, Order


@admin.action(description="Сбросить количество товара до ноля")
def reset_amount(modeladmin, request, queryset):
    queryset.update(amount=0)


@admin.action(description="Сбросить цену товара до ноля")
def reset_price(modeladmin, request, queryset):
    queryset.update(price=0)


class ClientAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone", "create_at"]
    ordering = ["name"]
    list_filter = ["create_at"]
    search_fields = ["name"]
    search_help_text = "Поиск по имени (name)"


class GoodAdmin(admin.ModelAdmin):
    actions = [reset_amount, reset_price]


class OrderAdmin(admin.ModelAdmin):
    """Список товаров в заказе"""

    list_display = ["client", "total_price"]

    fieldsets = [
        (
            "Клиент",
            {
                "description": "Клиент",
                "fields": ["client"],
            },
        ),
        (
            "Товар",
            {
                "description": "Товары",
                "fields": ["goods"],
            },
        ),
        (
            "Цена",
            {
                "fields": ["total_price"],
            },
        ),
    ]


# Register your models here.
admin.site.register(Client, ClientAdmin)
admin.site.register(Good, GoodAdmin)
admin.site.register(Order, OrderAdmin)
