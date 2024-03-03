from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from blog.models import Category, Post

import constants as c


def request_post_data():
    return Post.objects.select_related(
        'author', 'category', 'location'
    ).filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    )


def index(request):
    return render(
        request,
        'blog/index.html',
        {'posts': request_post_data()[:c.NUMBER_OF_POSTS]}
    )


def post_detail(request, post_id):
    return render(
        request,
        'blog/detail.html',
        {'post': get_object_or_404(request_post_data(), pk=post_id)}
    )


def category_posts(request, slug):
    category = get_object_or_404(
        Category.objects.filter(
            is_published=True), slug=slug,
    )
    return render(
        request,
        'blog/category.html',
        {'category': category,
         'posts': request_post_data().filter(category=category)}
    )
