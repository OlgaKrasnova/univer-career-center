from rest_framework import serializers

from .models import Vacancies

class VacanciesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancies
        fields = ("title", "description", "image")