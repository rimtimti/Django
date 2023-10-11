from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.CharField(max_length=100)
    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.email} {self.phone} {self.address} {self.create_at}"


class Good(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="imagzes_goods/")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    amount = models.IntegerField()
    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.description} {self.price} {self.amount} {self.create_at}"


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    goods = models.ManyToManyField(Good)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    create_at = models.DateField(auto_now_add=True)

    def total(self):
        goods = self.goods.all()
        return sum([good.price * good.amount for good in goods])

    def get_goods(self):
        return [good.__str__() for good in self.goods.all()]

    def __str__(self):
        return f"{self.client} {self.get_goods} {self.total_price} {self.create_at}"
