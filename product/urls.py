from django.urls import path
from .views      import ProductlistView, DetailView

urlpatterns = [
    path('', ProductlistView.as_view()),
    path('<int:product_id>', DetailView.as_view()),
]