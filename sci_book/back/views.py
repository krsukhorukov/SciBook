from django.http import HttpResponse, JsonResponse
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.template import RequestContext

from .forms import UserForm

class Main(TemplateView):
    template_name = 'base/main_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

class Login(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def form_valid(self, form):
        """Redirect to the main page on successful login."""
        self.user = form.get_user()
        login(self.request, self.user)
        return redirect('main')

class RegisterUserView(FormView):
    template_name = 'base/registration.html'
    form_class = UserForm

    def form_valid(self, form):
        if self.request.method == 'POST':
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(self.request, user)
            return redirect(reverse('main'))
        return super().form_invalid(form)

#class ProfileView(LoginRequiredMixin, View):
#    template_name = 'base/profile.html'

#    def get(self, request, *args, **kwargs):
#        user = request.user
#        return render(request, self.template_name, {'user': user})