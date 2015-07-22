from django.contrib import admin
from pages.models import Category, Document, Tag


class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'slug']
    list_display = ['name', 'slug']


class TagAdmin(admin.ModelAdmin):
    fields = ['name', 'slug']
    list_display = ['name', 'slug']


class DocumentAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'content', 'category', 'tags', 'user']
    list_display = ('title', 'slug', 'publish_date', 'update_date')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Document, DocumentAdmin)
