from datetime import date
from django.views.generic import ListView, CreateView ,UpdateView, DeleteView , View
from .models import Todo
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect

class TodoListView(ListView):
    model = Todo


class TodoCreateView(CreateView):
    model = Todo  
    fields = ["title","deadline"]
    success_url = reverse_lazy("todo_list")


class TodoUpdateView(UpdateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")   
    

class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy("todo_list")

class TodoCompleteView(View):
    def get(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.finished_at = date.today()
        todo.save()
        return redirect("todo_list")



