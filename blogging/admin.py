"""
blogging admin
"""

from django.contrib import admin

# Register your models here.
# means Post now shows up in django/admin

from blogging.models import Post
from blogging.models import Category

admin.site.register(Post)
admin.site.register(Category)

