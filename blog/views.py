from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.

"""
Render: put together
"""

def post_list(request):
    """

    :param request: Every thing received by the USER from the URL
    :return:
    """
    """
    posts:  this is a querySet to be passed to model to get the published 
            Posts from db
    html:   Template file
    {}:     Some data to use by the template
    
    django template tags allow us to transfer Python-like things into HTML, 
    so we can build dynamic websites faster.  
    """
    posts = Post.objects.filter(published_date__lte=timezone.now(
    )).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
