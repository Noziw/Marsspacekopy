from rest_framework.views import  APIView
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializer import *
from .models import *
from rest_framework.response import Response
import random
import datetime
# Create your views here.



class RegisterView (APIView):
    def post(self, request):
        serializer = Registersrl(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class Teacher(APIView):
    def post(self, request):
        serializer = TeachersSRL(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class Group(APIView):
    def post(self, request):
        serializer = GroupSRL(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class Student(APIView):
    def post(self, request):
        serializer = StudentSRL(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        

class LginView(APIView):
    def post(self, request):
        name = request.data.get('name')
        password = request.data.get('password')
        user = User.object.filter(name = name, password = password).first()
        if user:
            return Response('Login success')
        else:
            return Response('Not found such kind of user')
        
class StudentRegisterView(APIView):
    def post(self, request):
        serializer = StudentSRL(data=request.data)
        if serializer.is_valid():
            student = serializer.save()
            student.space_id = random.randint(1000,9999)
            student.save()
            return Response(dict(student))
        else:
            return Response(serializer.errors)
        
    
class CreatGroupView(APIView):
    def post( self, request):
        serializer = GroupSRL(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializer.errors)
        

class DavomatView(APIView):
    def post( self, request):
        serializer = DavomatSRL(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializer.errors)
        

class GiveCoinView(APIView):
    def post(self,request):
        student = request.data.get('student')
        coin = request.data.get('coins')
        if student:
            serializer = CoinSRL(data=request.data)
            if serializers.is_valid():
                student.coin += coin
                student.save()
                serializer.save()
                return Response('Good')
            else:
                return Response(serializer.errors)
        else:
            return Response('bunday student yoq')
        

class HomeworkViewTeacher(APIView):
    def pos(self, request, id):
        teacher = Group.object.filter(teacher = id).first()
        if teacher:
            serializers = HomeworkSRL(data = request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data)
            else:
                return Response(serializers.errors)
        else:
            return Response('Uyga vazifani yuklash ustozlarga berilgan!')
        

class GetHomework(APIView):
    def get(self,request):
        homework = Homework.object.all()
        if homework:
            serializers = HomeworkSRL(homework, many = True)
            return Response(serializers.data)
        else:
            return Response('Hozircha uyga vazifa topilmadi')
        
# uy ishini turadigon mudati
class GetStudentHomework(APIView):
    def grt(self, request, id):
        ser = []
        student = Group.object.filter(student = id).first()
        if student:
            today = datetime.datetime.today
            homework = Homework.objects.filter(group = student.group)
            for i in homework:
                if i.date + 7 <= today:
                    ser.append(i)
                else:
                    continue
                serializers= HomeworkSRL(ser, many = True)
                return Response(serializers.data)
            else:
                return Response('student xato')
            
# bor uyga vazifaga fayl yuklashi
class UploaduHomeworkStudent(APIView):
    def patch(self, request, id):
        homework = Homework.objects.filter(id = id).first()
        if homework:
            serializers = HomeworkSRL(instance=homework, data = request.data, partial = True)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data)
            else:
                return Response(serializers.errors)
        else:
            return Response("uyga vazifa topilmadi")


class HacktonView(generics.CreateAPIView):
    serializers_class = HackatonSRL
    queryset = Hackaton.objects.all()
    permission_classes = [AllowAny]


class HacktonGetView(generics.ListAPIView):
    serializers_class = HackatonSRL
    queryset = Hackaton.objects.all()
    permission_classes = [AllowAny]


class HacktonUpView(generics.RetrieveUpdateDestroyAPIView):
    serializers_class = HackatonSRL
    queryset = Hackaton.objects.all()
    permission_classes = [AllowAny]
    lookup_field = 'id'