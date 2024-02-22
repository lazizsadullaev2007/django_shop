from django.contrib import admin
from .models import Category, Subcategory, Product, ProductImage


class SubcategoryInline(admin.TabularInline):
    model = Subcategory
    extra = 1
    prepopulated_fields = {'slug': ('name',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    inlines = [SubcategoryInline, ]


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price', 'quantity', 'condition', 'category', 'subcategory')
    list_display_links = ('pk', 'name')
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductImageInline,]
    list_editable = ['category', 'subcategory', 'condition']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
