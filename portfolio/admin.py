from django.contrib import admin
from portfolio.models import *

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display = ["title", "image_links"]
    fields = ['title','description']

class ImageAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    list_display = "__unicode__ title category created".split()
    list_filter  = ["category"]
    fields = ['image', 'title','description', 'category', 'tags']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Image, ImageAdmin)
