from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from blog.models import Category, Post

def index(request):
    post_list = Post.objects.filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=timezone.now()
    )[:5]
    return render(request, 'blog/index.html', {'post_list': post_list})

def post_detail(request, post_id):
    post = get_object_or_404(
        Post,
        is_published=True,
        category__is_published=True,
        pk=post_id,
        pub_date__lte=timezone.now()
    )
    return render(request, 'blog/detail.html', {'post': post})

def category_posts(request, slug):
    category = get_object_or_404(
        Category.objects.filter(is_published=True),
        slug=slug,
    )
    post_list = Post.objects.filter(
        category=category,
        pub_date__lte=timezone.now(),
        is_published=True
    )
    return render(request, 'blog/category.html',
                  {'category': category, 'post_list': post_list}
    )
