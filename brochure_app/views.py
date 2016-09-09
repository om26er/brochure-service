from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView

from brochure_app.models import Brochure
from brochure_app.serializers import (
    QuestionnaireSerializer,
    BrochureSerializer,
    BrochureValidator
)


class Answer(CreateAPIView):
    serializer_class = QuestionnaireSerializer


class BrochureView(APIView):
    def get(self, request, *args, **kwargs):
        validator = BrochureValidator(data=self.request.data)
        validator.is_valid(raise_exception=True)
        brochure = Brochure.objects.filter(name=self.request.data.get('name'))
        serializer = BrochureSerializer(instance=brochure)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
