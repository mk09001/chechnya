from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from courses.models import Course
from .models import Cart, CartItem

def get_or_create_cart(request):
    """Получить или создать корзину для сессии"""
    if not request.session.session_key:
        request.session.create()
    
    cart, created = Cart.objects.get_or_create(session_key=request.session.session_key)
    return cart

def cart_detail(request):
    """Детальная страница корзины"""
    cart = get_or_create_cart(request)
    return render(request, 'cart/cart_detail.html', {'cart': cart})

def add_to_cart(request, course_id):
    """Добавить курс в корзину"""
    if request.method == 'POST':
        course = get_object_or_404(Course, id=course_id, is_active=True)
        cart = get_or_create_cart(request)
        
        cart_item, created = CartItem.objects.get_or_create(
            cart=cart,
            course=course,
            defaults={'quantity': 1}
        )
        
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        
        messages.success(request, f'Курс "{course.title}" добавлен в корзину')
        
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': True,
                'message': f'Курс "{course.title}" добавлен в корзину',
                'cart_count': cart.get_total_items()
            })
        
        return redirect('cart:cart_detail')
    
    return redirect('courses:course_list')

def remove_from_cart(request, item_id):
    """Удалить курс из корзины"""
    if request.method == 'POST':
        cart_item = get_object_or_404(CartItem, id=item_id, cart__session_key=request.session.session_key)
        course_title = cart_item.course.title
        cart_item.delete()
        
        messages.success(request, f'Курс "{course_title}" удален из корзины')
        
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': True,
                'message': f'Курс "{course_title}" удален из корзины'
            })
    
    return redirect('cart:cart_detail')

def update_cart_quantity(request, item_id):
    """Обновить количество курса в корзине"""
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        cart_item = get_object_or_404(CartItem, id=item_id, cart__session_key=request.session.session_key)
        
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()
        
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': True,
                'total_price': cart_item.cart.get_total_price(),
                'item_total': cart_item.get_total_price()
            })
    
    return redirect('cart:cart_detail')
