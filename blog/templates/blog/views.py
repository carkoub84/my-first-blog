from pdb import post
from django.shortcuts import render, get_object_or_404

# Create your views here.

def post_detail(request, pk):
    post = get_object_or_404(pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
