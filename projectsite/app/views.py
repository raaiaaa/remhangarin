from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from app.forms import TaskForm, PriorityForm, CategoryForm, NoteForm, SubTaskForm
from django.urls import reverse_lazy
from app.models import Task, Priority, Category, Note, SubTask

from django.views.generic.edit import CreateView, UpdateView, DeleteView

class HomePageView(ListView):   
    model = Task
    context_object_name = 'home'
    template_name = "home.html"

#tasklist 
class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'task_list.html'
    paginate_by = 10
    ordering = ["-created_at"]

#taskcreate 
class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "task_form.html"
    success_url = reverse_lazy("task-list")

#taskupdate
class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task-list')   

#taskdelete    
class TaskDeleteView(DeleteView):
    model = TaskForm
    template_name = 'task_del.html'
    success_url = reverse_lazy('task-list')

#prioritylist
class PriorityList(ListView):
    model = Priority
    context_object_name = 'priorities'
    template_name = 'priority_list.html'
    paginate_by = 10
    ordering = ["-created_at"]

#prioritycreate
class PriorityCreateView(CreateView):
    model = Priority
    form_class = PriorityForm
    template_name = "priority_form.html"
    success_url = reverse_lazy("priority-list")

#priorityupdate
class PriorityUpdateView(UpdateView):
    model = Priority
    form_class = PriorityForm
    template_name = 'priority_form.html'
    success_url = reverse_lazy('priority-list')

#prioritydelete
class PriorityDeleteView(DeleteView):
    model = Priority
    template_name = 'priority_del.html'
    success_url = reverse_lazy('priority-list')

#categorylist
class CategoryList(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'category_list.html'
    paginate_by = 10
    ordering = ["-created_at"]

#categorycreate
class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "category_form.html"
    success_url = reverse_lazy("category-list")

#categoryupdate
class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('category-list')

#categorydelete
class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category_del.html'
    success_url = reverse_lazy('category-list')

#notelist
class NoteList(ListView):
    model = Note
    context_object_name = 'notes'
    template_name = 'note_list.html'
    paginate_by = 10
    ordering = ["-created_at"]

#notecreate
class NoteCreateView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = "note_form.html"
    success_url = reverse_lazy("note-list")

#noteupdate
class NoteUpdateView(UpdateView):
    model = Note
    form_class = NoteForm
    template_name = 'note_form.html'
    success_url = reverse_lazy('note-list')

#notedelete
class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'note_del.html'
    success_url = reverse_lazy('note-list')

#subtasklist
class SubTaskList(ListView):
    model = SubTask
    context_object_name = 'subtasks'
    template_name = 'subtask_list.html'
    paginate_by = 10
    ordering = ["-created_at"]

#subtaskcreate
class SubTaskCreateView(CreateView):
    model = SubTask
    form_class = SubTaskForm
    template_name = "subtask_form.html"
    success_url = reverse_lazy("subtask-list")

#subtaskupdate
class SubTaskUpdateView(UpdateView):
    model = SubTask
    form_class = SubTaskForm
    template_name = 'subtask_form.html'
    success_url = reverse_lazy('subtask-list')

#subtaskdelete
class SubTaskDeleteView(DeleteView):
    model = SubTask
    template_name = 'subtask_del.html'
    success_url = reverse_lazy('subtask-list')