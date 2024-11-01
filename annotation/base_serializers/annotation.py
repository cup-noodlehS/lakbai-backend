from rest_framework import serializers
from annotation.models import Location, AnnotationForm, Annotation, AnnotationImage, Coordinates
from .file import FileSerializer


class CoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinates
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    start_coordinates = CoordinatesSerializer(read_only=True)
    end_coordinates = CoordinatesSerializer(read_only=True)
    start_coordinates_id = serializers.IntegerField(write_only=True)
    end_coordinates_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Location
        fields = '__all__'


class AnnotationFormSerializer(serializers.ModelSerializer):
    created_on = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    updated_on = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    class Meta:
        model = AnnotationForm
        fields = '__all__'


class AnnotationImageSerializer(serializers.ModelSerializer):
    file = FileSerializer(read_only=True)
    file_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = AnnotationImage
        fields = '__all__'


class AnnotationBaseSerializer(serializers.ModelSerializer):
    location = LocationSerializer(read_only=True)
    location_id = serializers.IntegerField(write_only=True)
    created_on = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    updated_on = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    annotator_id = serializers.IntegerField(write_only=True)
    form_template = AnnotationFormSerializer(read_only=True)
    form_template_id = serializers.IntegerField(write_only=True)
    coordinates = CoordinatesSerializer(read_only=True)
    coordinates_id = serializers.IntegerField(write_only=True)
    images = AnnotationImageSerializer(many=True, read_only=True)

    class Meta:
        model = Annotation
        fields = '__all__'


class AnnotationImageSerializer(serializers.ModelSerializer):
    file = FileSerializer(read_only=True)
    file_id = serializers.IntegerField(write_only=True)
    annotation_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = AnnotationImage
        fields = ['id', 'file', 'file_id', 'annotation_id']
