from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Book


def home(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'books/home.html', context)


class BookListView(ListView):
    model = Book
    template_name = 'books/home.html' 
    context_object_name = 'books'
    ordering = ['-date_published']


class BookDetailView(DetailView):
    model = Book


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'genre']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Book
    fields = ['title', 'genre']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        book = self.get_object()
        if self.request.user == book.author:
            return True
        return False


class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Book
    success_url = '/'

    def test_func(self):
        book = self.get_object()
        if self.request.user == book.author:
            return True
        return False


def about(request):
    return render(request, 'books/about.html', {'title': 'About'})