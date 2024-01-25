from collections.abc import Sequence
from django.urls import reverse_lazy
from django_filters.views import FilterView
from django.views.generic import CreateView, UpdateView, DeleteView

from shopping_list.filters import ItemFilter
from shopping_list.forms import ItemForm
from shopping_list.models import Item

class ItemListView(FilterView):
    model = Item
    template_name = 'shopping_list/item_list.html'
    filterset_class = ItemFilter


class ItemCreateView(CreateView):
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('shopping_list:item_list')

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.save()
        return super().form_valid(form)


class ItemUpdateView(UpdateView):
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('shopping_list:item_list')


class ItemDeleteView(DeleteView):
    model = Item
    success_url = reverse_lazy('shopping_list:item_list')
