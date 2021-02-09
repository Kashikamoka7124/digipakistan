from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = UserModel
        fields = ('__all__')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('__all__')

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseModel
        fields = ('__all__')

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleModel
        fields = ('__all__')

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = ('__all__')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventModel
        fields = ('__all__')

class CallobrationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallobrationsModel
        fields = ('__all__')

class OnlineTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = OnlineTestModel
        fields = ('__all__')

class QueriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = QueriesModel
        fields = ('__all__')