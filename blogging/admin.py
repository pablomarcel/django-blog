"""
blogging admin
"""

from django.contrib import admin

# Register your models here.
# means Post now shows up in django/admin

from blogging.models import Post
from blogging.models import Category


class RefInline(admin.TabularInline):
    """
    inline
    """

    model = Category.posts.through


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    post admin
    """

    inlines = [
        RefInline,
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    category admin
    """

    fields = ("name", "description")
    exclude = ("posts",)
