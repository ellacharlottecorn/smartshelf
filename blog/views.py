from django.shortcuts import render
from django.utils import timezone
from .models import Paint
from .forms import PostForm
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect

# Create your views here.
def post_list(request):
     paints = Paint.objects.order_by('entered_date')
     return render(request, 'blog/post_list.html', {'paints': paints})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.project_end_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_detail(request, pk):
    paint = get_object_or_404(Paint, pk=pk)
    return render(request, 'blog/post_detail.html', {'paint': paint})
