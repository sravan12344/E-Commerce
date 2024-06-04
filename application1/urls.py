from django.urls import path
from . import views

urlpatterns = [
    path("", views.ShowAllProduct, name="show"),
    path("product/<int:pk>", views.productDetail, name="productdetails"),
    path("add/", views.addProduct, name="add"),
    path("update/<int:pk>", views.updateProduct, name="update"),
    path("delete/<int:pk>", views.deleteProduct, name="delete"),
    path("search/", views.searchBar, name="search"),
    path("ck/",views.cke,name="ck"),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('add_to_wishlist/<str:course_name>/', views.add_to_wishlist, name='add_to_wishlist'),
]
