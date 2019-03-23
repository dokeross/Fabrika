from django.contrib import admin

from .models import *


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0

class ProductCommentsInline(admin.TabularInline):
    model = ProductComments
    extra = 0

class CategoryAdmin (admin.ModelAdmin):
    list_display = [field.name for field in CategoryProduct._meta.fields]

    class Meta:
        model = CategoryProduct

admin.site.register(CategoryProduct, CategoryAdmin)

class ProductCommentsAdmin (admin.ModelAdmin):
    # list_display = ["name", "email"]
    list_display = [field.name for field in ProductComments._meta.fields]
    list_filter = ['name',]
    search_fields = ['name', 'email']

    # exclude = ["email"]
	# inlines = [FieldMappingInline]
	# fields = []
    # #exclude = ["type"]
	# #list_filter = ('report_data',)
	# search_fields = ['category', 'subCategory', 'suggestKeyword']

    class Meta:
        model = ProductComments

admin.site.register(ProductComments, ProductCommentsAdmin)

class SubcategoriesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SubcategoriesProduct._meta.fields]

    class Meta:
        model = SubcategoriesProduct

admin.site.register(SubcategoriesProduct, SubcategoriesAdmin)

class SimilarProductsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SimilarProducts._meta.fields]

    class Meta:
        model = SimilarProducts

admin.site.register(SimilarProducts, SimilarProductsAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    inlines = [ProductImageInline]

    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)


class ProductImageAdmin (admin.ModelAdmin):
    list_display = [field.name for field in ProductImage._meta.fields]

    class Meta:
        model = ProductImage

admin.site.register(ProductImage, ProductImageAdmin)
