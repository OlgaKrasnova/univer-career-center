from django.shortcuts import render
from django.views.generic.base import View

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import VacanciesListSerializer, VacanciesDetailSerializer
from .models import Vacancies


class VacanciesView(View):
    def get(self, request):
        vacancies = Vacancies.objects.all()
        return render(request, "vacancy_list.html", {"vacancy_list": vacancies})


class VacanciesListAPIView(APIView):
    def get(self, request):
        vacancies = Vacancies.objects.all()
        serializer = VacanciesListSerializer(vacancies, many=True)
        return Response(serializer.data)


class VacanciesDetailView(View):
    def get(self, request, pk):
        vacancy = Vacancies.objects.get(id=pk)
        return render(request, "vacancy_detail.html", {"vacancy": vacancy})


class VacanciesDetailAPIView(APIView):
    def get(self, request, pk):
        vacancy = Vacancies.objects.get(id=pk)
        serializer = VacanciesDetailSerializer(vacancy)
        return Response(serializer.data)
