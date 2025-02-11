from django.urls import path
from . import views
from .views import CarFormView

urlpatterns = [
    # path('say_hello/', views.say_hello),
    # path('product/<int:id>', views.show_products),
    # path('user/<str:username>', views.show_username),
    # # path('product/', views.show_seach),
    # path('product/', views.show_prices),
    # path('books/<int:id>', views.show_books),
    # path('hello_django/', views.hello_django),
    # path('django_info/', views.django_info),
    # path('products_list/', views.product_list),
    # path('products/category/<str:category>', views.show_category),
    # path('users_list/', views.users),
    # path('jobs/', views.send_jobs),
    # path('show_products/', views.send_products),
    # path('show_plans/', views.show_plans),
    # path('show_products_list/', views.send_products_list),
    # path('home/', views.home, name='home'),
    # path('home-page/', views.home_page, name='home-page'),
    # path('products/', views.only_products, name='products'),
    # path('product_detail/<int:pk>/', views.to_product, name='product_detail'),
    path('car/', CarFormView.as_view(), name='car'),
]
