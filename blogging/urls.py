from django.conf.urls import url

from django.urls import path

from blogging.views import stub_view

# from blogging.views import list_view

from blogging.views import detail_view

from blogging.views import PostListView

# urlpatterns = [path('', stub_view, name="blog_index"),
#                path('posts/<int:post_id>/', stub_view, name="blog_detail"),
#                ]

urlpatterns = [path('', PostListView.as_view(), name="blog_index"),
               path('posts/<int:post_id>/', detail_view, name="blog_detail"),

               ]

