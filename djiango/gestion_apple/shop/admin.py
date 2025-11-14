# shop/admin.py
from decimal import Decimal
from django.contrib import admin, messages
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.db import transaction

from .models import Product, Profile, Order, OrderItem

# Personalización del Admin site (encabezados)
admin.site.site_header = "Gestión Tienda Apple"
admin.site.site_title = "Admin - Tienda Apple"
admin.site.index_title = "Panel de control - Tienda Apple"

# Inline: Profile dentro del User
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name = 'Perfil'
    verbose_name_plural = 'Perfiles'
    fk_name = 'user'
    readonly_fields = ('balance',)  # si quieres que admin no edite balance, quítalo

# Desregistrar User si ya estaba registrado (evita AlreadyRegistered)
try:
    admin.site.unregister(User)
except admin.sites.NotRegistered:
    pass

# Custom UserAdmin que muestra el Profile
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_balance')
    list_select_related = ('profile',)

    def get_balance(self, instance):
        try:
            return instance.profile.balance
        except Profile.DoesNotExist:
            return "—"
    get_balance.short_description = 'Saldo (€)'

# Registrar nuestro UserAdmin
admin.site.register(User, UserAdmin)

# Product admin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    readonly_fields = ('created_at',)
    list_editable = ('price', 'stock')
    ordering = ('-created_at',)

# OrderItem inline para Order
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ('product', 'quantity', 'price_at_purchase')
    can_delete = False

# Order admin con acciones y protecciones
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status', 'created_at', 'total')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username', 'id')
    inlines = [OrderItemInline]
    actions = ['mark_as_completed', 'mark_as_cancelled', 'refund_order']

    @transaction.atomic
    def mark_as_completed(self, request, queryset):
        updated = 0
        for order in queryset.select_for_update():
            if order.status == 'C':
                continue
            order.status = 'C'
            order.save()
            updated += 1
        self.message_user(request, f'{updated} pedido(s) marcado(s) como Completado.')
    mark_as_completed.short_description = 'Marcar como completado'

    @transaction.atomic
    def mark_as_cancelled(self, request, queryset):
        updated = 0
        for order in queryset.select_for_update():
            if order.status == 'X':
                continue
            if order.status == 'C':
                prof = getattr(order.user, 'profile', None)
                if prof:
                    prof.balance = prof.balance + order.total
                    prof.save()
            for item in order.items.all():
                prod = item.product
                prod.stock = prod.stock + item.quantity
                prod.save()
            order.status = 'X'
            order.save()
            updated += 1
        self.message_user(request, f'{updated} pedido(s) marcado(s) como Cancelado y stock/saldo restaurado.')
    mark_as_cancelled.short_description = 'Marcar como cancelado (restaura stock / devuelve saldo si aplica)'

    @transaction.atomic
    def refund_order(self, request, queryset):
        refunded = 0
        for order in queryset.select_for_update():
            if order.status == 'X':
                continue
            prof = getattr(order.user, 'profile', None)
            if prof:
                prof.balance = prof.balance + order.total
                prof.save()
                refunded += 1
        self.message_user(request, f'{refunded} pedido(s) reembolsado(s) (saldo añadido).')
    refund_order.short_description = 'Reembolsar pedido(s) al saldo del usuario'
