from django.shortcuts import render
from django.views.generic.base import View

from .models import Vacancies


class VacanciesView(View):
    def get(self, request):
        vacancies = Vacancies.objects.all()
        return render(request, "vacancy_list.html", {"vacancy_list": vacancies})
