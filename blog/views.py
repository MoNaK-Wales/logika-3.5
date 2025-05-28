from django.shortcuts import render
from blog.models import Post, Author

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', context={'posts': posts})

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'blog/post_detail.html', context={'post': post})

def author_posts(request, author_id):
    author = Author.objects.get(id=author_id)
    posts = author.posts.all()
    return render(request, 'blog/author_post_list.html', context={'posts': posts, 'author': author})