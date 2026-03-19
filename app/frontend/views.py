from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

def auth_view(request):
    return render(request, 'frontend/auth.html')

def login_view(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('email')
        password = request.POST.get('password')

        # Try login with username first
        user = authenticate(request, username=username_or_email, password=password)

        # If not found, try finding by email
        if user is None:
            try:
                found_user = User.objects.get(email=username_or_email)
                user = authenticate(request, username=found_user.username, password=password)
            except User.DoesNotExist:
                pass

        if user is not None:
            login(request, user)
            return redirect('/dashboard/')
        else:
            messages.error(request, 'Invalid username/email or password!')
            return render(request, 'frontend/auth.html')
    return render(request, 'frontend/auth.html')

def register_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = request.POST.get('username')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken!')
            return render(request, 'frontend/auth.html')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        login(request, user)
        return redirect('/dashboard/')
    return render(request, 'frontend/auth.html')

def forgot_password_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            messages.success(request, 'Password reset instructions sent to your email!')
        except User.DoesNotExist:
            messages.error(request, 'No account found with that email!')
        return render(request, 'frontend/auth.html')
    return render(request, 'frontend/forgot_password.html')

def dashboard_view(request):
    if not request.user.is_authenticated:
        return redirect('/')
    return render(request, 'frontend/dashboard.html')