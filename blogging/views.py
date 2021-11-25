from django.shortcuts import render
from django.http.response import HttpResponse, Http404
from django.template import loader
from blogging.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.


def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args: \n"
        # outdated notation, insert variables into a string
        body += "\n".join(["\t%s" % a for a in args])
    if kwargs:
        body += "Kwargs: \n"
        body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])

    return HttpResponse(body, content_type="text/plain")


class PostListView(ListView):
    queryset = Post.objects.exclude(published_date__exact=None).order_by(
        "-published_date"
    )
    template_name = "list.html"


class PostDetailView(DetailView):
    # do i need this?
    # queryset = Post.objects.exclude(published_date__exact=None)
    model = Post
    template_name = "blogging/detail.html"
