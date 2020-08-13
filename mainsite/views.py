from django.conf import settings
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string

from .models import Post
from .forms import PostForm


def home(request):
    posts = Post.objects.filter(active=True, featured=True)[0:3]
    context = {'posts': posts}
    return render(request, 'mainsite/index.html', context)


def posts(request):
    posts = Post.objects.filter(active=True)
    context = {'posts': posts}
    return render(request, 'mainsite/posts.html', context)


def post(request, pk):
    post = Post.objects.get(id=pk)
    context = {'post': post}
    return render(request, 'mainsite/post.html', context)


def profile(request):
    return render(request, 'mainsite/profile.html')


# CRUD VIEWS
@login_required(login_url="home")
def create_post(request):
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('posts')

    context = {'form': form}
    return render(request, 'mainsite/post_form.html', context)


@login_required(login_url="home")
def update_post(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
        return redirect('posts')

    context = {'form': form}
    return render(request, 'mainsite/post_form.html', context)


@login_required(login_url="home")
def delete_post(request, pk):
    post = Post.objects.get(id=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('posts')
    context = {'item': post}
    return render(request, 'mainsite/delete.html', context)


def send_email(request):

    if request.method == 'POST':
        template = render_to_string('mainsite/email_template.html', {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'message': request.POST['message'],

        })

        email = EmailMessage(
            request.POST['subject'],
            template,
            settings.EMAIL_HOST_USER,
            ['zokirovrustam202@gmail.com']
        )
        email.fail_silently = False
        email.send()

    return render(request, 'mainsite/email_sent.html')
