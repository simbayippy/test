from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Post, Comment
from .forms import RegisterForm, LoginForm, PostForm, CommentForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'polls/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'polls/login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('home')

def create_post_page(request):
    return render(request, 'polls/create_post_page.html')

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()  # Set the pub_date field
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'polls/create_post_page.html')

@login_required
def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.user != post.author:
        return redirect('home')
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm(instance=post)
    return render(request, 'edit_post.html', {'form': form})

@login_required
def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.user != post.author:
        return redirect('home')
    post.delete()
    return redirect('home')

@login_required
def create_comment(request, post_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.pub_date = timezone.now()  # Set the pub_date field
            comment.author = request.user
            comment.post = Post.objects.get(id=post_id)
            comment.save()
            return redirect('post', post_id = post_id)  # Redirect to post detail page
    else:
        form = CommentForm()
    return render(request, 'polls/index.html')

@login_required
def delete_comment(request, comment_id):
    comment = Comment.objects.get(id=comment_id)
    if request.user != comment.author:
        return redirect('home')  # Redirect to home or wherever appropriate
    comment.delete()
    return redirect('post', post_id=comment.post.id)  # Redirect to post detail page

def home(request):
    posts = Post.objects.all()
    User = get_user_model()
    users = User.objects.all()
    context = {"postsList": posts,
               "users": users}
    return render(request, 'polls/index.html', context)

def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comment_set.order_by('-pub_date')  # Reverse order by publication date
    return render(request, 'polls/post_detail.html', {'post': post, 'comments': comments})

def users(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    postList = Post.objects.filter(author=user)
    return render(request, "polls/users.html", {"user": user, "postList": postList})

def admin_users_list(request):
    users = User.objects.all()
    return render(request, 'polls/admin_userlist.html', {'users': users})