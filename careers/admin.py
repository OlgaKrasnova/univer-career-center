from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import DiplomaThesis, Graduate, Resume, Vacancies, Employer, Practice, Events, RequestForPractice, \
    Students, Profession

admin.site.register(DiplomaThesis)
admin.site.register(Graduate)
admin.site.register(Resume)


@admin.register(Vacancies)
class VacanciesAdmin(ImportExportModelAdmin):
    list_display = ("image", "title", "description", "id_employer")
    list_display_links = ("title",)
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
