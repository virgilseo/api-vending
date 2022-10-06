from django.urls import path, include
from . views import *

urlpatterns = [
    path('products', ProductListView.as_view()),
    path('products/<int:id>', ProductDetailView.as_view()),
    path('products/buy', ProductBuyView.as_view()),
]
 