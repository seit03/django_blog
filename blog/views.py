from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
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
    elif method_post == 'GET':
        post_all = Post.objects.all()
        return HttpResponse('post_all')
    elif method_post == 'DELETE':
        post = Post.objects.get(id=7)
        post.delete()
        return HttpResponse('Delete this post')
    elif method_post == 'PUT':
        post = Post.objects.get(id=7)
        post.title = 'Put to the our posts'
        post.description = 'Put to the our post'
        post.save()
        return HttpResponse('Post was changed')


# def get_all_posts(request):
#     context = {
#         'post': Post.objects.all()
#     }
#     return render(request, 'posts_list.html', context)


class PostView(ListView):
    model = Post
    template_name = 'posts/posts_list.html'

    def get_queryset(self):
        return Post.objects.all()
