from django.contrib import admin
from .models import ApparelSize, Color, Categories, ProductCategories, ProductColors, Product

# Register your models here.
admin.site.register(ApparelSize)
admin.site.register(Color)
admin.site.register(Categories)
admin.site.register(Product)
admin.site.register(ProductCategories)
admin.site.register(ProductColors)
