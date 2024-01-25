from django.urls import path
from shopping_list.apps import ShoppingListConfig
from shopping_list.views import ItemCreateView, ItemListView, ItemUpdateView, ItemDeleteView


app_name = ShoppingListConfig.name

urlpatterns = [
    path('', ItemListView.as_view(), name='item_list'),
    path('item_create/', ItemCreateView.as_view(), name='item_create'),
    path('item_update/<int:pk>/', ItemUpdateView.as_view(), name='item_update'),
    path('item_delete/<int:pk>/', ItemDeleteView.as_view(), name='item_delete'),
]