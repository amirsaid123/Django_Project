"""
URL configuration for root project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from apps import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('say_hello/', views.say_hello),
    path('product/<int:id>', views.show_products),
    path('user/<str:username>', views.show_username),
    # path('product/', views.show_seach),
    path('product/', views.show_prices),
    path('books/<int:id>', views.show_books),
    path('hello_django/', views.hello_django),
    path('django_info/', views.django_info),
    path('products_list/', views.product_list),
    path('products/category/<str:category>', views.show_category),
]
