from django.contrib import admin
from pages.models import Category
from pages.models import Document


class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'slug']
    list_display = ['name', 'slug']


class DocumentAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'content', 'category', 'user']
    list_display = ('title', 'slug', 'publish_date', 'update_date')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Document, DocumentAdmin)
