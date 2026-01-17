from django import forms
from pizzas.models import Pizza


class PizzaModelForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = "__all__"
