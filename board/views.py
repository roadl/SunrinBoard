from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post, Comment
from .forms import Postform, Commentform, UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login

def free_board(request):
    sort = request.GET.get('sort', '')
    if sort == 'all':
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        return render(request, 'board/free_board.html', {'post':posts})
    elif sort == 'question':
        posts = Post.objects.filter(category = 'QU').order_by('published_date')
        return render(request, 'board/free_board.html', {'post':posts})
    elif sort == 'free':
        posts = Post.objects.filter(category = 'FR').order_by('published_date')
        return render(request, 'board/free_board.html', {'post':posts})
    elif sort == 'tip':
        posts = Post.objects.filter(category = 'TI').order_by('published_date')
        return render(request, 'board/free_board.html', {'post':posts})
    elif sort == 'mypost':
        user = request.user
        posts = Post.objects.filter(author_id=user).order_by('published_date')
        return render(request, 'board/free_board.html', {'post':posts})
    else:
        posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
        return render(request, 'board/free_board.html', {'post':posts})

def post_detail(request,pk):
    posts = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = Commentform(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = posts
            comment.save()
            return redirect('post_detail', pk=posts.pk)
    else:
        form = Commentform()
    return render(request, 'board/post_detail.html', {'post' : posts, 'form' : form})

@login_required
def post_new(request):
    if request.method == "POST":
        form = Postform(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = Postform()
    return render(request, 'board/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = Postform(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = Postform(instance=post)
    return render(request, 'board/post_edit.html', {'form': form})

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('free_board')

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            new_user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, new_user)
            return redirect('free_board')
    else:
        form = UserForm()
    return render(request, 'board/adduser.html', {'form': form})


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)
