from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post

# Create your views here.

#def home(request):
#    return render(request, "home.html", {})


class HomeView(ListView):
    model = Post
    template_name = "blog/home.html"

class ArticleDetailView(DetailView):
    model = Post
    template_name = "blog/article_detail.html"

class AddPostView(CreateView):
    model = Post
    template_name = "blog/add_post.html"
    fields = "__all__"
    #fields = ("title", "body")