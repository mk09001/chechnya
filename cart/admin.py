from django.contrib import admin
from .models import Cart, CartItem

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 0
    readonly_fields = ['added_at']

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['session_key', 'get_total_price', 'get_total_items', 'created_at']
    readonly_fields = ['created_at', 'updated_at']
    inlines = [CartItemInline]
    
    def get_total_price(self, obj):
        return obj.get_total_price()
    get_total_price.short_description = 'Общая стоимость'
    
    def get_total_items(self, obj):
        return obj.get_total_items()
    get_total_items.short_description = 'Количество товаров'

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['cart', 'course', 'quantity', 'get_total_price', 'added_at']
    list_filter = ['added_at']
    readonly_fields = ['added_at']
    
    def get_total_price(self, obj):
        return obj.get_total_price()
    get_total_price.short_description = 'Общая стоимость'
