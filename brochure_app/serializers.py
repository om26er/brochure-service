from rest_framework import serializers

from brochure_app.models import Questionnaire


class QuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionnaire
        fields = (
            'name',
            'email',
            'answer1',
            'answer2',
            'answer3',
            'comments',
        )
