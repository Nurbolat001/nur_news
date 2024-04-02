# from django.contrib.auth.forms import AuthenticationForm
# from django.shortcuts import render, get_object_or_404
# from .forms import NewUserForm
# from .models import Post
# from django.contrib.auth import authenticate, login, logout
# from django.shortcuts import render, redirect

from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .forms import NewUserForm


def home_page(request):
    posts = Post.objects.all().order_by('-post_date')[:3]
    context = {
        'posts': posts
    }
    return render(request, "./index.html", context)


def all_news_page(request):
    posts = Post.objects.all().order_by('-post_date')
    context = {
        'posts': posts
    }
    return render(request, "./news_all.html", context)


def news_card(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post
    }
    return render(request, "./news_card.html", context)


def logout_view(request):
    logout(request)
    return redirect("home_page")


# регистрация
from django.shortcuts import render, redirect
from .forms import NewUserForm


def register_view(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")  # Перенаправление на страницу входа после успешной регистрации
    else:
        form = NewUserForm()
    context = {
        'form': form
    }
    return render(request, "register.html", context)


#
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home_page")
    else:
        form = AuthenticationForm()

    context = {
        'form': form
    }
    return render(request, "./login.html", context)

#
# # views.py
#
# from django.shortcuts import render, redirect
# from .models import News
# from .forms import AddNewsForm
#
#
# def add_news(request):
#     if request.method == 'POST':
#         form = AddNewsForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect(
#                 'home_page')  # Перенаправляем пользователя на главную страницу после успешного добавления новости
#     else:
#         form = AddNewsForm()
#     return render(request, 'AddNews.html', {'form': form})
#
#
# def home_page(request):
#     news_list = News.objects.all().order_by('-publication_date')[:3]  # Получаем последние 5 новостей
#     return render(request, 'index.html', {'news_list': news_list})


# def edit_news(request, pk):
#     news = get_object_or_404(News, pk=pk)
#     if request.method == "POST":
#         form = NewsForm(request.POST, request.FILES, instance=news)
#         if form.is_valid():
#             form.save()
#             return redirect('all_news_page')
#     else:
#         form = NewsForm(instance=news)
#     return render(request, 'EditNews.html', {'form': form})

def delete_news(request, pk):
    news = get_object_or_404(News, pk=pk)
    news.delete()
    return redirect('home_page')

from django.shortcuts import render, redirect
from .models import News
from .forms import AddNewsForm

def home_page(request):
    news_list = News.objects.all().order_by('-publication_date')
    return render(request, 'index.html', {'news_list': news_list})

def add_news(request):
    if request.method == 'POST':
        form = AddNewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    else:
        form = AddNewsForm()
    return render(request, 'AddNews.html', {'form': form})


from django.shortcuts import render, redirect, get_object_or_404
from .models import News
from .forms import AddNewsForm, UpdateNewsForm  # Импортируем новую форму для обновления

def update_news(request, pk):
    news = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        form = UpdateNewsForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            form.save()
            return redirect('home_page')
    else:
        form = UpdateNewsForm(instance=news)
    return render(request, 'UpdateNews.html', {'form': form})
