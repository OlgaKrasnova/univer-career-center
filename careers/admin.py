from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import DiplomaThesis, Graduate, Resume, Vacancies, Employer, Practice, Events, RequestForPractice, \
    Students, Profession

admin.site.register(DiplomaThesis)
admin.site.register(Graduate)
admin.site.register(Resume)

def make_vacancy_not_actual(modeladmin, request, queryset):
    queryset.update(status=False)
make_vacancy_not_actual.short_description = "Вакансия не актуальна"

def make_vacancy_actual(modeladmin, request, queryset):
    queryset.update(status=True)
make_vacancy_actual.short_description = "Вакансия актуальна"

@admin.register(Vacancies)
class VacanciesAdmin(ImportExportModelAdmin):
    list_display = ("image", "title", "description", "status", "id_employer")
    actions = [make_vacancy_not_actual, make_vacancy_actual]
    pass


admin.site.register(Employer)

def make_practice_not_actual(modeladmin, request, queryset):
    queryset.update(status=False)
make_practice_not_actual.short_description = "Практика не актуальна"

def make_practice_actual(modeladmin, request, queryset):
    queryset.update(status=True)
make_practice_actual.short_description = "Практика актуальна"

@admin.register(Practice)
class PracticeAdmin(ImportExportModelAdmin):
    list_display = ("title", "description", "status", "id_employer")
    actions = [make_practice_not_actual, make_practice_actual]
    pass

admin.site.register(Events)
admin.site.register(RequestForPractice)
admin.site.register(Students)
admin.site.register(Profession)
