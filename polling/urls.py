"""
urls
"""
from django.urls import path
from polling.views import list_view, detail_view

urlpatterns = [
    path("", list_view, name="poll_index"),
    # poll_id is passed to detail_vew in views.py
    # "poll_detail" is in list.html in the anchor tag
    path("polls/<int:poll_id>", detail_view, name="poll_detail"),
]
