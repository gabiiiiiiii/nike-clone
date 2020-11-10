from django.db import models

class Product(models.Model):
    name                = models.CharField(max_length = 100)
    price               = models.DecimalField(max_digits = 10, decimal_places = 2)
    description         = models.CharField(max_length = 100)
    style               = models.CharField(max_length = 100)
    description_title   = models.CharField(max_length = 100)
    description_content = models.CharField(max_length = 1000)
    description_color   = models.CharField(max_length = 100)
    main_image_url      = models.URLField()
    category            = models.ManyToManyField('Category', through = 'ProductCategory')
    item                = models.ManyToManyField('Item', through = 'ProductItem')
    type                = models.ManyToManyField('Type', through = 'ProductType')
    technology          = models.ManyToManyField('Technology', through = 'ProductTechnology')
    color               = models.ManyToManyField('Color', through = 'ProductColor')
    size                = models.ManyToManyField('Size', through = 'ProductSize')

    def __str__(self):
        return self.name

    class Meta:
        db_table = "products"

class SubImageUrl(models.Model):
    url     = models.URLField()
    product = models.ForeignKey('product', on_delete = models.CASCADE)

    def __str__(self):
        return self.url

    class Meta:
        db_table = "sub_image_urls"

class Category(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name
        
    class Meta:
        db_table = "categories"

class ProductCategory(models.Model):
    product  = models.ForeignKey('product', on_delete = models.CASCADE)
    category = models.ForeignKey('category', on_delete = models.CASCADE)

    class Meta:
        db_table = "products_categories"

class Item(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "items"

class ProductItem(models.Model):
    product = models.ForeignKey('product', on_delete = models.CASCADE)
    item    = models.ForeignKey('item', on_delete = models.CASCADE)

    class Meta:
        db_table = "products_items"

class Type(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "types"

class ProductType(models.Model):
    product = models.ForeignKey('product', on_delete = models.CASCADE)
    type    = models.ForeignKey('type', on_delete = models.CASCADE)

    class Meta:
        db_table = "products_types"

class Technology(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "technologies"

class ProductTechnology(models.Model):
    product    = models.ForeignKey('product', on_delete = models.CASCADE)
    technology = models.ForeignKey('technology', on_delete = models.CASCADE)

    class Meta:
        db_table = "products_technologies"

class Color(models.Model):
    name  = models.CharField(max_length = 100)
    value = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "colors"

class ProductColor(models.Model):
    product = models.ForeignKey('product', on_delete = models.CASCADE)
    color   = models.ForeignKey('color', on_delete = models.CASCADE)

    class Meta:
        db_table = "products_colors"

class Size(models.Model):
    size = models.IntegerField()

    def __str__(self):
        return self.size

    class Meta:
        db_table = "sizes"

class ProductSize(models.Model):
    product = models.ForeignKey('product', on_delete = models.CASCADE)
    size    = models.ForeignKey('size', on_delete = models.CASCADE)

    class Meta:
        db_table = "products_sizes"