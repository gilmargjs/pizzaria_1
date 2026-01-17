from django.contrib import admin
from pizzas.models import Pizza


# Register your models here.
class PizzaAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "ingredients",
        "value",
        "photo",
    )
    search_fields = ("name",)


admin.site.register(Pizza, PizzaAdmin)
