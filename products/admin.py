from django.contrib import admin

from products.models import Basket, Product, ProductCategory

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'quantity')
    fields = ('name', 'category', 'image',  'description', ('price', 'quantity'), 'stripe_product_price_id')
    list_display_links = ('name', 'category')
    search_fields = ('name',)
    ordering = ('name',)
    list_filter = ('category',)


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0
