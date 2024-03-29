from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.models import User
from .forms import LoginForm, RegistrationForm
from .models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


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
    return render(request,"./news_card.html", context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_page')
        else:
            # Обработка ошибки входа
            pass
    return render(request, 'login.html')

def register_view(request):
    # Реализация регистрации пользователя
    return render(request, 'register.html')

def logout_view(request):
    logout(request)
    return redirect('home_page')


from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def register(request):
    if request.method == 'POST':
        # Получаем данные из формы
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['pass']
        re_password = request.POST['re_pass']

        # Проверяем, что пароли совпадают
        if password != re_password:
            # Если пароли не совпадают, можно сделать какое-то действие,
            # например, отобразить сообщение об ошибке
            return render(request, 'register.html', {'error': 'Passwords do not match'})

        # Создаем нового пользователя
        user = User.objects.create_user(username, email, password)
        user.save()

        # Логиним пользователя сразу после регистрации
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # Перенаправляем пользователя на другую страницу, например, на главную
            return redirect('home_page')
        else:
            # Если не удалось залогинить пользователя, можно сделать какое-то действие,
            # например, отобразить сообщение об ошибке
            return render(request, 'register.html', {'error': 'Failed to log in'})

    # Если запрос не POST, просто отображаем страницу регистрации
    return render(request, 'register.html')

from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_page')
        else:
            # Обработка ошибки входа
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home_page')  # Перенаправление на главную страницу после успешной регистрации
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})



