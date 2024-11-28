from accounts import serializers
from faces.models import Face


class FaceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Face
        fields = '__all__'
