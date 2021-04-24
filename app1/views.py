from django.shortcuts import render
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, ProfileUpdateForm
from django.shortcuts import render, redirect

from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import MyUser

def home_view(request):
    return render(request, 'home.html')




class Register(FormView):
    template_name = 'signup.html'
    form_class = SignUpForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Register, self).form_valid(form)

class Login(LoginView):
    template_name = 'login.html'
    form_class = SignUpForm
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')


def profile_view(request):
    context ={'user':request.user}
    return render(request, 'profile.html', context)

def profile_update(request):
    if request.method == 'POST':
        u_form=ProfileUpdateForm(request.POST, instance=request.user)

        if u_form.is_valid():
            u_form.save()
            return redirect('profile')

    else:
        u_form=ProfileUpdateForm(instance=request.user)

    context ={'u_form':u_form}
    return render(request, 'profile_update.html', context)