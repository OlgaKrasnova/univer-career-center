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


@admin.register(Vacancies)
class VacanciesAdmin(ImportExportModelAdmin):
    list_display = ("get_image", "title", "description", "id_employer")

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="60" height="50"')

    get_image.short_description = "Изображение"

    list_display_links = ("title",)
    inlines = [ResumeInline]




admin.site.register(Employer)


@admin.register(Practice)
class PracticeAdmin(ImportExportModelAdmin):
    list_display = ("title", "description", "id_employer")
    pass


admin.site.register(Events)

@admin.register(RequestForPractice)
class RequestAdmin(ImportExportModelAdmin):
    list_display = ("id_practice", "id_student")

@admin.register(Students)
class StudentsAdmin(ImportExportModelAdmin):
    list_display = ("surname", "name", "patronymic", "year_of_issue", "id_profession")
    list_filter = ("year_of_issue", "id_profession")
    search_fields = ("surname", "name")
    pass


admin.site.register(Profession)
