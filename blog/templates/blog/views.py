from datetime import timezone
from pdb import post
from django.shortcuts import render, get_object_or_404
from django.template import RequestPOST
from forms import PostForm
from django.shortcuts import redirect
form = PostForm(RequestPOST.POST)


# Create your views here.

def post_detail(request, pk):
    post = get_object_or_404(pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})