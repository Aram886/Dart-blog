from typing import Tuple

from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class PostAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}
    form = PostAdminForm
    save_on_top = True
    empty_value_display = 'None'
    save_as = True
    list_display = ('id', 'title', 'slug', 'category',  'author',
                    'created_at', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ("category", 'tags')
    readonly_fields = ('views', 'created_at', 'get_photo')
    fields = ('title', 'slug', 'category', 'tags', 'author',
              'content', 'photo', 'get_photo', 'views', 'created_at')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="65">')

    get_photo.short_description = "Image"


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.site_header = 'Blog'
admin.site.site_title = 'Blog'
