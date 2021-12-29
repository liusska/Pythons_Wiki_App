from django.shortcuts import render, redirect
from .forms import PythonCreateForm
from .models import Python
from templates_advanced.core.decorators import any_group_required
from django.contrib.auth import authenticate, login, logout


def sign_in(request):
    user = authenticate(username='liusska', password='123456')
    login(request, user)
    return redirect('index')


def sign_out(request):
    logout(request)
    return redirect('index')


def index(request):
    pythons = Python.objects.all()
    return render(request, 'index.html', {'pythons': pythons})


# @login_required(login_url=reverse_lazy('sign in'))
@any_group_required(groups=['User'])
def create(request):
    if request.method == 'GET':
        form = PythonCreateForm()
        return render(request, 'create.html', {'form': form})
    else:
        form = PythonCreateForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('index')

        return render(request, 'create.html', {'form': form})

