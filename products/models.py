from django.db import models

class CategoryProduct(models.Model):
    name = models.CharField(max_length=48, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Product category'
        verbose_name_plural = 'Product category'



class SubcategoriesProduct(models.Model):
    name = models.CharField(max_length=48, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Subcategory of the product'
        verbose_name_plural = 'Subcategories of products'        

class SimilarProducts(models.Model):
    name = models.CharField(max_length=48, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Similar product'
        verbose_name_plural = 'Similar products'        



class Product(models.Model):
    name = models.CharField(max_length=64, blank=True, null=True, default=None)
    session_key = models.CharField(max_length=128, blank=True, null=True, default=None)
    category = models.ForeignKey(CategoryProduct, blank=True, null=True)
    subcategories = models.ForeignKey(SubcategoriesProduct, blank=True, null=True)
    similarproducts = models.ForeignKey(SimilarProducts, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    short_description = models.TextField(blank=True, null=True, default=None)
    measurement = models.CharField(max_length=48, blank=True, null=True, default=None)
    like = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    color = models.CharField(max_length=48, blank=True, null=True, default=None)
    composition = models.CharField(max_length=48, blank=True, null=True, default=None)
    article = models.CharField(max_length=48, blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    new_items = models.BooleanField(default=False)
    hit_items = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return "%s, %s" % (self.price, self.name)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='products_images/')
    is_main = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'


class ProductComments(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None)
    name = models.CharField(max_length=128)
    published_date = models.CharField(max_length=128, blank=True, null=True, default=None)
    comments = models.TextField(blank=True, null=True, default=None)

    def __unicode__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'ProductComment'
        verbose_name_plural = 'ProductComments'

