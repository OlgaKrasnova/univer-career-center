from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.utils.safestring import mark_safe
from .models import DiplomaThesis, Graduate, Resume, Vacancies, Employer, Practice, Events, RequestForPractice, \
    Students, Profession

admin.site.register(DiplomaThesis)
admin.site.register(Graduate)
admin.site.register(Resume)


class ResumeInline(admin.TabularInline):
    model = Resume
    extra = 1
    readonly_fields = ("title", "target", "experience", "skills", "id_graduate")
    save_on_top = True

def make_vacancy_not_actual(modeladmin, request, queryset):
    queryset.update(status=False)
make_vacancy_not_actual.short_description = "Вакансия не актуальна"

def make_vacancy_actual(modeladmin, request, queryset):
    queryset.update(status=True)
make_vacancy_actual.short_description = "Вакансия актуальна"

@admin.register(Vacancies)
class VacanciesAdmin(ImportExportModelAdmin):
    list_display = ("get_image", "title", "description", "status", "id_employer")
    actions = [make_vacancy_not_actual, make_vacancy_actual]

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="60" height="50"')

    get_image.short_description = "Изображение"

    list_display_links = ("title",)
    inlines = [ResumeInline]




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


@admin.register(Students)
class StudentsAdmin(ImportExportModelAdmin):
    list_display = ("surname", "name", "patronymic", "year_of_issue", "id_profession")
    list_filter = ("year_of_issue", "id_profession")
    search_fields = ("surname", "name")
    pass


admin.site.register(Profession)
