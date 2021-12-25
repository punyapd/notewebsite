from django.contrib import admin
from django.db.models.expressions import Ref
from .models import Course, Subject, Semester, TuModelQuestions, UnitwiseQuestions, RefrencedBooks, MicroSyllabus, News, Customers

# Register your models here.
@admin.register(Course)
class CourseModelAdmin(admin.ModelAdmin):
    list_display = ['faculty']

@admin.register(Semester)
class SemesterModelAdmin(admin.ModelAdmin):
    list_display = ['sem', 'faculty']

@admin.register(Subject)
class SubjectModelAdmin(admin.ModelAdmin):
    list_display = ['faculty', 'sem', 'subject_name']
    
@admin.register(TuModelQuestions)
class TuModelQuestionsModelAdmin(admin.ModelAdmin):
    list_display = ['date', 'model_question', 'subject']

@admin.register(UnitwiseQuestions)
class UnitwiseQuestionsModelAdmin(admin.ModelAdmin):
    list_display = ['unit', 'unit_question', 'subject']


@admin.register(RefrencedBooks)
class RefrencedBooksModelAdmin(admin.ModelAdmin):
    list_display = ['book', 'subject']

@admin.register(MicroSyllabus)
class MicroSyllabusModelAdmin(admin.ModelAdmin):
    list_display = ['syllabus', 'subject']

admin.site.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "add_time")

@admin.register(Customers)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display= ['id', 'fname', 'lname', 'district', 'city', 'number', 'message']