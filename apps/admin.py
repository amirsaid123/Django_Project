from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Job, Product, Category, Plan, OnlyProduct, Images


# Register your models here.

@admin.register(Job)
class JobAdmin(ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(ModelAdmin):
    pass

@admin.register(Plan)
class PlanAdmin(ModelAdmin):
    pass

@admin.register(OnlyProduct)
class OnlyProductAdmin(ModelAdmin):
    pass
@admin.register(Images)
class ImagesAdmin(ModelAdmin):
    pass