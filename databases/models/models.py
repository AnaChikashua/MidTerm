from django.db import models


class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=200)
    other_date = models.CharField(max_length=200)

    class Meta:
        db_table = 'Product'


class ApparelSize(models.Model):
    size_id = models.IntegerField(primary_key=True)
    size_code = models.IntegerField(null=True)
    sort_order = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'ApparelSize'


class ProductColors(models.Model):
    color_id = models.IntegerField(primary_key=True)
    product = models.ManyToManyField(Product, related_name='productToProductColors')

    class Meta:
        db_table = 'ProductColors'


class Color(models.Model):
    color_id = models.IntegerField(primary_key=True)
    color_code = models.CharField(max_length=100)
    color_name = models.CharField(max_length=100)
    product_color = models.ForeignKey(ProductColors, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Color'


class ProductCategories(models.Model):
    category_id = models.IntegerField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        db_table = 'ProductCategories'


class Categories(models.Model):
    category_id = models.IntegerField(primary_key=True)
    parent_category_id = models.OneToOneField(ProductCategories, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'Categories'
