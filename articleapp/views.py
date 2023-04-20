from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from articleapp.decorators import article_ownership_decorator
from articleapp.forms import ArticleCreationForm
from articleapp.models import Article


# Create your views here.

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleCreationForm
    template_name = 'articleapp/create.html'

    def form_valid(self, form):
        temp_article = form.save(commit=False)
        temp_article.writer = self.request.user
        temp_article.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk':self.object.pk})

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articleapp/detail.html'
    context_object_name = 'targetArticle'

@method_decorator(article_ownership_decorator, 'get')
@method_decorator(article_ownership_decorator, 'post')
class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleCreationForm
    context_object_name = 'targetArticle'
    template_name = 'articleapp/update.html'

    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk':self.object.pk})

@method_decorator(article_ownership_decorator, 'get')
@method_decorator(article_ownership_decorator, 'post')
class ArticleDeleteView(DeleteView):
    model = Article
    context_object_name = 'targetArticle'
    template_name = 'articleapp/delete.html'
    success_url = reverse_lazy('articleapp:list')