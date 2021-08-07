from django.contrib import admin
from django.db import models
from .models import Post, Category, Ads

# Register your models here.

class PostAdmin(admin.ModelAdmin):
  list_display = ['__str__', 'slug']
  class Meta:
    model = Post
  prepopulated_fields = {'slug': ['name', 'title']}

class CategoryAdmin(admin.ModelAdmin):
  list_display = ['__str__', 'slug']
  class Meta:
    model = Category
  prepopulated_fields = {'slug': ['title']}

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register( Ads)


