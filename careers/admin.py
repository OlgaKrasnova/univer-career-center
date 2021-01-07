from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import DiplomaThesis, Graduate, Resume, Vacancies, Employer, Practice, Events, RequestForPractice, \
    Students, Profession

admin.site.register(DiplomaThesis)
admin.site.register(Graduate)
admin.site.register(Resume)


class ResumeInline(admin.TabularInline):
    model = Resume
    extra = 1
    readonly_fields = ("title", "target", "experience", "skills", "id_graduate")


@admin.register(Vacancies)
class VacanciesAdmin(ImportExportModelAdmin):
    list_display = ("image", "title", "description", "id_employer")
    list_display_links = ("title",)
    inlines = [ResumeInline]
    pass


admin.site.register(Employer)


@admin.register(Practice)
class PracticeAdmin(ImportExportModelAdmin):
    list_display = ("title", "description", "id_employer")
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
