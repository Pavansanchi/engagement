from django.urls import path
from . import views

urlpatterns = [
    path('fetch_posts_and_products/<int:tenant_id>/', views.fetch_posts_and_products),
    path('create_new_product/', views.create_new_product),
    path('create_new_collection/', views.create_new_collection),
    path('top_viewed_posts/<int:tenant_id>/', views.top_viewed_posts),
    path('top_viewed_products/<int:tenant_id>/', views.top_viewed_products),
]