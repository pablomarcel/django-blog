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
    model = Post
    template_name = 'list.html'


# def list_view(request):
#     published = Post.objects.exclude(published_date__exact=None)
#     posts = published.order_by('-published_date')
#     context = {'posts': posts}
#     # changed to blogging/list.html and passed,
#     # then updated settings.py and added blogging/templates/blogging in TEMPLATES DIRS
#     return render(request, 'list.html', context)


class PostDetailView(DetailView):
    model = Post
    template_name = 'blogging/detail.html'


# def detail_view(request, post_id):
#     published = Post.objects.exclude(published_date__exact=None)
#     try:
#         post = published.get(pk=post_id)
#     except Post.DoesNotExist:
#         raise Http404
#     context = {'post': post}
#     return render(request, 'blogging/detail.html', context)
