from django.contrib import admin
from .models import Category, ChocoPost, Comment
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

class ChocoPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'content')
    list_display_links = ('id', 'content')

admin.site.register(Category, CategoryAdmin)
admin.site.register(ChocoPost, ChocoPostAdmin)
admin.site.register(Comment, CommentAdmin)