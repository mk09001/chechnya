from django.db import models
from courses.models import Course

class Cart(models.Model):
    """Корзина покупок"""
    session_key = models.CharField(max_length=40, unique=True, verbose_name="Ключ сессии")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    
    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"
    
    def __str__(self):
        return f"Корзина {self.session_key}"
    
    def get_total_price(self):
        return sum(item.get_total_price() for item in self.items.all())
    
    def get_total_items(self):
        return sum(item.quantity for item in self.items.all())

class CartItem(models.Model):
    """Элемент корзины"""
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items', verbose_name="Корзина")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")
    added_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")
    
    class Meta:
        verbose_name = "Элемент корзины"
        verbose_name_plural = "Элементы корзины"
        unique_together = ['cart', 'course']
    
    def __str__(self):
        return f"{self.course.title} в корзине {self.cart.session_key}"
    
    def get_total_price(self):
        return self.course.price * self.quantity
