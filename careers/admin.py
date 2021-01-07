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
    pass


admin.site.register(Employer)
admin.site.register(Practice)
admin.site.register(Events)
admin.site.register(RequestForPractice)
admin.site.register(Students)
admin.site.register(Profession)
