from rest_framework import serializers

from .models import Vacancies, RequestForPractice, Resume

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ("id_graduate", "title", "target", "experience", "skills")

class VacanciesListSerializer(serializers.ModelSerializer):
    resume = ResumeSerializer(many=True)
    class Meta:
        model = Vacancies
        fields = ("title", "description", "image", "resume")


class VacanciesDetailSerializer(serializers.ModelSerializer):
    id_employer = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = Vacancies
        exclude = ("")

class CreateRequestForPracticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestForPractice
        fields = "__all__" 