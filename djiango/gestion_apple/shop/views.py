# shop/views.py
# shop/views.py
from decimal import Decimal
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.db import transaction
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, AddBalanceForm, UserEditForm, PasswordChangeForm
from .models import Profile, Product, Order, OrderItem

def index(request):
    products = Product.objects.all()[:20]
    return render(request, 'shop/index.html', {'products': products})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Registro completado. Ahora puedes iniciar sesión.')
            return redirect('login')
        else:
            messages.error(request, 'Por favor corrige los errores del formulario.')
    else:
        form = UserRegistrationForm()
    return render(request, 'shop/register.html', {'form': form})

def login_view(request):
    # Simple formulario de login manual (podrías usar el genérico de Django)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Bienvenido, {user.username}!')
            next_url = request.GET.get('next') or 'home'
            return redirect(next_url)
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'shop/login.html', {})

def logout_view(request):
    logout(request)
    messages.info(request, 'Has cerrado sesión.')
    return redirect('home')

@login_required
def profile(request):
    profile = request.user.profile
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    add_form = AddBalanceForm(request.POST or None)

    if request.method == 'POST' and add_form.is_valid():
        amount = add_form.cleaned_data['amount']
        profile.balance = profile.balance + amount
        profile.save()
        messages.success(request, f'Se han añadido {amount} € a tu saldo.')
        return redirect('profile')

    return render(request, 'shop/profile.html', {
        'profile': profile,
        'add_form': add_form,
        'orders': orders,
    })


@login_required
def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        uform = UserEditForm(request.POST, instance=user)
        pform = PasswordChangeForm(user, request.POST)  # requiere old_password, new_password1, new_password2
        if 'save_profile' in request.POST:
            if uform.is_valid():
                uform.save()
                messages.success(request, "Perfil actualizado.")
                return redirect('profile')
            else:
                messages.error(request, "Corrige los errores del formulario.")
        elif 'change_password' in request.POST:
            if pform.is_valid():
                user = pform.save()
                update_session_auth_hash(request, user)  # evita que se cierre la sesión
                messages.success(request, "Contraseña cambiada correctamente.")
                return redirect('profile')
            else:
                messages.error(request, "Corrige los errores del cambio de contraseña.")
    else:
        uform = UserEditForm(instance=user)
        pform = PasswordChangeForm(user)

    return render(request, 'shop/edit_profile.html', {
        'uform': uform,
        'pform': pform,
    })

# --- Helpers del carrito (session-based) ---
CART_SESSION_ID = 'cart'

def _get_cart(session):
    """
    Devuelve el dict del carrito desde la session.
    Formato:
    { '<product_id>': { 'quantity': int, 'price': 'Decimal as string' }, ... }
    """
    return session.get(CART_SESSION_ID, {})

def _save_cart(session, cart):
    session[CART_SESSION_ID] = cart
    session.modified = True

def _cart_total_and_count(cart):
    total = Decimal('0.00')
    count = 0
    for pid, item in cart.items():
        total += Decimal(item['price']) * item['quantity']
        count += item['quantity']
    return total, count

# --- Vista: detalle de producto ---
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'shop/product_detail.html', {'product': product})

# --- Añadir al carrito ---
def cart_add(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = _get_cart(request.session)

    # cantidad enviada por POST o por querystring; por defecto 1
    qty = int(request.POST.get('quantity', request.GET.get('quantity', 1)))
    if qty < 1:
        qty = 1

    pid = str(product.id)
    if pid in cart:
        cart[pid]['quantity'] += qty
    else:
        cart[pid] = {
            'quantity': qty,
            # guardamos el precio actual como string para mantener precisión
            'price': str(product.price)
        }
    _save_cart(request.session, cart)
    messages.success(request, f'Has añadido {qty} x {product.name} al carrito.')
    return redirect('cart_detail')

# --- Eliminar item del carrito ---
def cart_remove(request, product_id):
    cart = _get_cart(request.session)
    pid = str(product_id)
    if pid in cart:
        del cart[pid]
        _save_cart(request.session, cart)
        messages.info(request, 'Artículo eliminado del carrito.')
    return redirect('cart_detail')

# --- Ver carrito ---
def cart_detail(request):
    cart = _get_cart(request.session)
    items = []
    for pid, data in cart.items():
        prod = get_object_or_404(Product, id=int(pid))
        items.append({
            'product': prod,
            'quantity': data['quantity'],
            'price': Decimal(data['price']),
            'subtotal': Decimal(data['price']) * data['quantity'],
        })
    total, count = _cart_total_and_count(cart)
    return render(request, 'shop/cart_detail.html', {
        'items': items,
        'total': total,
        'count': count,
    })

# --- Checkout: crear Order y OrderItems ---
@login_required
@transaction.atomic
def checkout(request):
    cart = _get_cart(request.session)
    if not cart:
        messages.error(request, 'Tu carrito está vacío.')
        return redirect('home')

    # Recalcular total y comprobar stock
    items = []
    total = Decimal('0.00')
    for pid, data in cart.items():
        product = get_object_or_404(Product, id=int(pid))
        qty = int(data['quantity'])
        price = Decimal(data['price'])
        if product.stock < qty:
            messages.error(request, f'No hay suficiente stock de {product.name}. Disponible: {product.stock}.')
            return redirect('cart_detail')
        items.append((product, qty, price))
        total += price * qty

    profile = request.user.profile

    if request.method == 'POST':
        # Opción simple: pagar con saldo del perfil si hay suficiente (si no -> error)
        pay_with_balance = request.POST.get('pay_with_balance') == '1'

        if pay_with_balance:
            if profile.balance < total:
                messages.error(request, 'No tienes suficiente saldo para pagar este pedido.')
                return redirect('checkout')
        # Creamos Order y OrderItems
        order = Order.objects.create(user=request.user, total=total, status='P')  # pendiente por defecto
        # crear items y descontar stock
        for product, qty, price in items:
            OrderItem.objects.create(order=order, product=product, quantity=qty, price_at_purchase=price)
            # restar stock
            product.stock = product.stock - qty
            product.save()

        # Si paga con saldo, descontamos
        if pay_with_balance:
            profile.balance = profile.balance - total
            profile.save()
            order.status = 'C'  # marcado como completado si se paga inmediatamente
            order.save()
            messages.success(request, f'Pedido #{order.id} completado y pagado con tu saldo ({total} €).')
        else:
            messages.success(request, f'Pedido #{order.id} creado. Paga en el método elegido (simulado).')

        # vaciar carrito
        request.session.pop(CART_SESSION_ID, None)
        request.session.modified = True

        return redirect('order_detail', order_id=order.id)

    # GET -> mostrar resumen y formulario de pago simple
    total, count = _cart_total_and_count(cart)
    return render(request, 'shop/checkout.html', {
        'items': items,
        'total': total,
        'profile': profile,
    })

# --- Ver detalle de un pedido ---
@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'shop/order_detail.html', {'order': order})
