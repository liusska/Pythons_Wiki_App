from django.shortcuts import render, redirect
from pythons.core.decorators import any_group_required
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .forms import PythonCreateForm
from .models import Python
from pythons.core.mixins import AnyGroupRequiredMixin


class IndexView(ListView):
    template_name = 'index.html'
    model = Python
    context_object_name = 'pythons'
    paginate_by = 5


class PythonCreateView(AnyGroupRequiredMixin, CreateView):
    template_name = 'create.html'
    model = Python
    fields = '__all__'
    success_url = reverse_lazy('index')


# def index(request):
#     pythons = Python.objects.all()
#     return render(request, 'index.html', {'pythons': pythons})


# @login_required(login_url=reverse_lazy('sign in'))
# @any_group_required(groups=['User'])
# def create(request):
#     if request.method == 'GET':
#         form = PythonCreateForm()
#         return render(request, 'create.html', {'form': form})
#     else:
#         form = PythonCreateForm(request.POST, request.FILES)
#         print(form)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#
#         return render(request, 'create.html', {'form': form})
#
