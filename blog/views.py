from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Post
from blog.models import Post
from blog.models import Post
from blog.models import Post





def get_profile(httpRequest):
    return HttpResponse('Hello World')


def get_my_page(httpRequest):
    return HttpResponse('24')


def get_posts(request):
    method_post = request.method
    if method_post == 'POST':
        post = Post.objects.create(title='Good Morning',
                                    description='Have a good day')
        return HttpResponse('Put to the our posts')
    elif method_post == 'Post':
        post = Post.objects.post(title='')
        return HttpResponse('Posting')
    elif method_post == 'Get':
        post = Post.objects.get(id(124))
        return HttpResponse('Get to the our posts')
    elif method_post == 'Delete':
        post = Post.objects.delete(title='to the our')
        return HttpResponse('Delete to the our posts')
    elif method_post == 'Put':
        post = Post.objects.put(title='Posts')
        return HttpResponse('Put to the our posts')
