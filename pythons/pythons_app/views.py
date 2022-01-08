from django.shortcuts import render, redirect
from pythons.core.decorators import any_group_required
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView

from .forms import PythonCreateForm
from .models import Python


# def index(request):
#     pythons = Python.objects.all()
#     return render(request, 'index.html', {'pythons': pythons})


class IndexView(ListView):
    template_name = 'index.html'
    model = Python
    context_object_name = 'pythons'


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

