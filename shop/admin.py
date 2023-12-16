from django.contrib import admin
from .models import Course, Category

admin.site.site_header = "Courses Admin"
admin.site.site_title = "My Courses"
admin.site.index_title = "Welcom to the courses admin area"


class CourseAdmin(admin.ModelAdmin):
    # с помощью этого атрибута можно указать какие поля будут отображаться в веб интерфейсе администратора для определенной модели
    list_display = ('title', 'price', 'category')


class CoursesInline(admin.TabularInline):
    model = Course
    exclude = ['created_at']
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    fieldsets = [
        (None, {'fields': ['title']}),
        ('Dates', {
            'fields': ['created_at'],
            'classes': ['collapse']
        })
    ]
    inlines = [CoursesInline]


admin.site.register(Category, CategoryAdmin)
# добавим название класса вторым аргументом
admin.site.register(Course, CourseAdmin)
