from django import forms

from shopping_list.models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        exclude = ['id',]