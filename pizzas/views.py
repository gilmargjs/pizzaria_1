from django.shortcuts import render

# Create your views here.
from pizzas.models import Pizza
from pizzas.forms import PizzaModelForm
from django.views import View
from django.views.generic import ListView, CreateView


class PizzasView(ListView):
    model = Pizza
    template_name = "pizzas.html"
    context_object_name = "pizzas"

    def get_queryset(self):
        pizzas = super().get_queryset().order_by("name")

        return pizzas


class NewPizzas(CreateView):
    model = Pizza
    form_class = PizzaModelForm
    template_name = "new_pizzas.html"
    success_url = "/pizzas/"
