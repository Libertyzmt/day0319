from django.shortcuts import render, redirect
from .models import Article
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
def select(request):
    selects = Article.objects.all()
    return render(request, 'post/article_select.html', {'selects': selects})


def post(request, id):
    post = Article.objects.get(id=id)
    return render(request, 'post/article_select2.html', {'post': post})

class ArticleUpdate(UpdateView):
    model = Article
    fields = ('title','body')
    template_name = 'post/article_create.html'
    success_url = reverse_lazy('select')


def removes(request, id):
    remove = Article.objects.get(id=id)
    remove.delete()
    return redirect("select")
