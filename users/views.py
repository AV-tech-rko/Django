from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm,ProfileUpdateForm,UserUpdateForm

def register(request):
    if request.method == 'POST':
        form  = UserRegisterForm(request.POST) 
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username} ! Login now')
            return redirect('login')
    else:
        form = UserRegisterForm()        
    
    context = {
        "form" : form
    }

    return render(request,'users/register.html',context)

@login_required
def profile(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.FILES,request.POST,instance=request.user.profile)
        u_form = UserUpdateForm(request.POST,instance=request.user)

        if p_form.is_valid() and u_form.is_valid():
            p_form.save()
            u_form.save()
            messages.success(request,f'Your profile is updated')
            return redirect('profile')
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)
        u_form = UserUpdateForm(instance=request.user)    

    context = {
        "p_form" : p_form,
        "u_form" : u_form
    }
    return render(request,'users/profile.html',context)