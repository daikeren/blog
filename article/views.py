from django.shortcuts import render
from django.http import HttpResponse

import datetime

from django import forms
from article.models import Article
from django.http import HttpResponseRedirect


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', ]


def home(request):
    str = "Hello World!"
    return HttpResponse(str)


def now(request):
    return HttpResponse(datetime.datetime.now())


def detail(request, pk):
    article = Article.objects.get(pk=int(pk))
    return render(request, "detail.html", {'article': article})


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            new_article = form.save()
            return HttpResponseRedirect('/article/' + str(new_article.pk))

    form = ArticleForm()
    return render(request, 'create_article.html', {'form': form})
