from django.contrib import admin

# Register your models here.
from .models import Task, Priority, Note, SubTask, Category

admin.site.register(Note)

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

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "deadline", "priority", "category")
    search_fields = ("title", "description",)
    list_filter = ("status", "priority", "category")
    inlines = [SubTaskInline, NoteInline]

@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "parent_task_name")
    search_fields = ("title",)
    list_filter = ("status",)

    def parent_task_name(self, obj):
        try:
            task = Task.objects.get(id=obj.id)
            return task.title
        except Task.DoesNotExist:
            return None


admin.site.register(Priority)
admin.site.register(Category)

