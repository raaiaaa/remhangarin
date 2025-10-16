from django.forms import ModelForm
from django import forms
from taskmanager.models import Task, Priority, Category, Note, SubTask

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = "__all__"

class PriorityForm(ModelForm):
    class Meta:
        model = Priority
        fields = "__all__"

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = "__all__"

class SubTaskForm(ModelForm):
    class Meta:
        model = SubTask
        fields = "__all__" 