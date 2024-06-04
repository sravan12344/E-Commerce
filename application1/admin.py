from django.contrib import admin
from .models import Product, Category


class Padmin(admin.ModelAdmin):
    list_display = [
        "id",
        "image",
        "name",
        "price",
        "description",
        "is_published",
        "created_at",
        "category",
    ]

    list_display_links = ("id", "name")

    list_filter = ("price", "created_at")

    list_editable = ("is_published",)
    search_fields = ("name",)
    ordering = ("price",)


admin.site.register(Product, Padmin)
admin.site.register(Category)
