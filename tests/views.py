from rest_framework_json_api.views import ModelViewSet
from tests.models import BasicModel
from tests.serializers import BasicModelSerializer
import json
from io import BytesIO

class BasicModelViewSet(ModelViewSet):
    serializer_class = BasicModelSerializer
    queryset = BasicModel.objects.all()
