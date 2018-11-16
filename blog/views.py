from django.shortcuts import render

# Create your views here.

"""
Render: put together
"""

def post_list(request):
    return render(request, 'blog/post_list.html', {})
