from rest_framework import serializers

from brochure_app.models import Questionnaire, Brochure


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


class BrochureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brochure
        fields = (
            'id',
            'name',
            'brochure',
        )


class BrochureValidator(serializers.Serializer):
    name = serializers.CharField(required=True)
