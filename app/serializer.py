from rest_framework import serializers
from .models import *

class Registersrl(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class TeachersSRL(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class StudentSRL(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['name', 'lastname', 'phone', 'password']


class GroupSRL(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class DavomatSRL(serializers.ModelSerializer):
    class Meta:
        model = Davomat
        fields = '__all__'


class CoinSRL(serializers.ModelSerializer):
    class Meta:
        model = Coins
        fields = '__all__'



class HomeworkSRL(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = '__all__'


class HackatonSRL(serializers.ModelSerializer):
    class Meta:
        model = Hackaton
        fields = '__all__'