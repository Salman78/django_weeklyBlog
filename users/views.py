from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) #request.POST is a dictionary containing info sent via POST request
        #we want this request.POST dictionary to specifically contain info regarding user form input
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})
