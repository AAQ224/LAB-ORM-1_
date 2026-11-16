from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm


def home(request):
    posts = Post.objects.filter(
        is_published=True
    ).order_by("-published_at", "-pk")

    featured_post = posts.first()
    recent_posts = posts[1:]

    return render(request, "blog/home.html", {
        "featured_post": featured_post,
        "posts": recent_posts,
        "total_posts": posts.count(),
    })


def post_detail(request, pk):
    post = get_object_or_404(
        Post,
        pk=pk,
        is_published=True
    )

    return render(request, "blog/post_detail.html", {
        "post": post
    })


def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save()
            return redirect("post_detail", pk=post.pk)
    else:
        form = PostForm()

    return render(request, "blog/add_post.html", {
        "form": form
    })