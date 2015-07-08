from django.contrib import admin
from pages.models import Document


class DocumentAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'content', 'user']
    list_display = ('title', 'slug', 'publish_date', 'update_date')

admin.site.register(Document, DocumentAdmin)
