from django.shortcuts import render
from django.views.generic import TemplateView,DetailView,ListView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .models import Book,BookInstance

# Create your views here.

class IndexView(TemplateView):
    template_name = 'catalog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["num_of_books"] = Book.objects.all().count()
        context["num_of_book_instance"] = BookInstance.objects.all().count()
        context["num_of_book_instance_avail"]= BookInstance.objects.filter(status='a').count()
        return context
    

class ProfileView(LoginRequiredMixin,ListView):
    template_name = 'catalog/profile.html'
    context_object_name = 'borrowed_books'

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user)
     


class BookDetailView(DetailView):
    model = Book


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'catalog/signup.html'
    success_url = reverse_lazy('login')


class BookFormView(LoginRequiredMixin,CreateView):
    model = Book
    fields = '__all__'