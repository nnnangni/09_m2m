from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth import get_user_model

from .forms import UserCustomCreationForm
# Create your views here.

def user_list(request):
    User = get_user_model()
    users = User.objects.all()
    return render(request, 'accounts/user_list.html', {'users':users})
    
def user_page(request, id):
    User = get_user_model()
    user_info = User.objects.get(id=id)
    return render(request, 'accounts/user_page.html', {'user_info':user_info})
    
@require_http_methods(["GET", "POST"])
def signup(request):
    if request.user.is_authenticated:
        return redirect('movies:list')
    if request.method == 'POST':
        user_form = UserCustomCreationForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            auth_login(request, user)
            return redirect('movies:list')
    else:
        user_form = UserCustomCreationForm()
    context = {'form': user_form}
    return render(request, 'accounts/forms.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('movies:list')
    if request.method == 'POST':
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
            return redirect('movies:list')
    else:
        login_form = AuthenticationForm()
    context = {'form': login_form}
    return render(request, 'accounts/forms.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('movies:list')
    
@login_required
def follow(request, id):
    User = get_user_model()
    me = request.user
    you = User.objects.get(id=id)
    
    if me != you:
        if you in me.from_user.all():
            me.from_user.remove(you)
        else:
            me.from_user.add(you)
    return redirect('accounts:user_page', id)

def followers(request, id):
    User = get_user_model()
    user = User.objects.get(id=id)
    follows = user.to_user.all()
    return render(request, 'accounts/follow.html',{'follows':follows,'user':user})
    
def followings(request, id):
    User = get_user_model()
    user = User.objects.get(id=id)
    follows = user.from_user.all()
    return render(request, 'accounts/follow.html',{'follows':follows,'user':user})