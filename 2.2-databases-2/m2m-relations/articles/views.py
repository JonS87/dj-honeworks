from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    object_list = Article.objects.all()
    template = 'articles/news.html'
    context = {'object_list': object_list}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/3.1/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    #ordering = '-pub lished_at'

    return render(request, template, context)
