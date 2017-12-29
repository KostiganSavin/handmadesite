from django.contrib import admin
from .models import ProductModel, ProductPictureModel
# Register your models here.

class PorductAdmin(admin.ModelAdmin):
    pass

class PictureInProduct(admin.StackedInline):
    model = ProductPictureModel


admin.site.register(ProductModel, PorductAdmin)
admin.site.register(ProductPictureModel)