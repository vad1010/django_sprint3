from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from blog.models import Category, Post

import constants as c


def index(request):
    return render(
        request,
        'blog/index.html',
        {'posts': Post.objects.filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now())[:c.NUMBER_OF_POSTS]}
    )


def post_detail(request, post_id):
    return render(
        request,
        'blog/detail.html',
        {'post': get_object_or_404(
        Post,
        is_published=True,
        category__is_published=True,
        pk=post_id,
        pub_date__lte=timezone.now())}
    )


def category_posts(request, slug):
    category = get_object_or_404(
        Category.objects.filter(is_published=True),
        slug=slug,
    )
    return render(
        request,
        'blog/category.html',
        {'category': category, 'post_list': Post.objects.filter(
        category=category,
        pub_date__lte=timezone.now(),
        is_published=True)}
    )

