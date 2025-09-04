from django.contrib import admin

from.models import Priority, Category, Task, Note, SubTask


class SubTaskInline(admin.TabularInline):
   model = SubTask
   extra = 1
   fields = ("title", "status")
   show_change_link = True
class NoteInline(admin.StackedInline):
   model = Note
   extra = 1
   fields = ("content", "created_at")
   readonly_fields = ("created_at",)

@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "deadline", "status", "priority", "category")
    search_fields = ("title", "description", "status")
    list_filter = ("status", "priority", "category")

@admin.register(Note) 
class NoteAdmin(admin.ModelAdmin):
    list_display = ("task", "content","created_at", "updated_at")
    search_fields = ("task", "content") 

@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ("parent_task", "title", "status")
    search_fields = ("parent_task", "title", "status")
    list_filter = ("status",)
