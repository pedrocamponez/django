from typing import Any

from django.shortcuts import render
from django.http import HttpRequest, Http404
from blog.data import posts

def blog(request):
    
    print('blog')

    context = {
        'text': 'Olá blog',
        'posts': posts,
    }

    return render(
        request, 
        'blog/index.html',
        context
    )

def post(request: HttpRequest, post_id: int):
    found_post: dict[str:Any] = None

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break

    if found_post is None:
        raise Http404('Post não existe')
    
    print('post', post_id)

    context = {
        'title': found_post['title'] + ' - ',
        'post': found_post,
        'id': post_id
    }

    return render(
        request, 
        'blog/post.html',
        context
    )


def exemplo(request):
    
    print('exemplo')

    context = {
        'text': 'Olá exemplo',
        'title': 'Página de Exemplo do Blog '
    }

    return render(
        request, 
        'blog/exemplo.html',
        context
    )
