from django.shortcuts import render,redirect
from . models import register

from django.contrib.auth import login, authenticate #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this


def demo(request):
    return render(request,'index.html')
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return render(request, 'login.html')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="/login.html", context={"login_form": form})
def register(request):
    if request.method == 'POST':
        name = request.POST.get('name', )
        psw = request.POST.get('psw', )
        cpsw = request.POST.get('cpsw', )
        m = register(name=name, psw=psw, cpsw=cpsw)
        m.save()
        return redirect('/')
    return render(request,'register.html')
