from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('list_books')  # Redirect to a page after registration
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('list_books')  # Redirect to a page after login
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')