from rest_framework import serializers

from .models import Vacancies


class VacanciesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancies
        fields = ("title", "description", "image")


class VacanciesDetailSerializer(serializers.ModelSerializer):
    id_employer = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = Vacancies
        exclude = ("")
