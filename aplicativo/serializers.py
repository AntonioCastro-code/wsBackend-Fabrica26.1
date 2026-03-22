from rest_framework import serializers

from .models import User
from .models import UserTasks

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_nickname', 'user_name', 'user_email', 'user_age']

class UserTasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTasks
        fields = ['user_nickname', 'user_task']