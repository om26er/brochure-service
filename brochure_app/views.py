from rest_framework.generics import CreateAPIView

from brochure_app.serializers import QuestionnaireSerializer


class Answer(CreateAPIView):
    serializer_class = QuestionnaireSerializer
