from django.urls import path
from .views import *


urlpatterns = [
    path('give/coin/', GiveCoinView.as_view()),
    path('RegisterView/', RegisterView.as_view()),
    path('Teacher/', Teacher.as_view()),
    path('Group/', Group.as_view()),
    path('Student/', Student.as_view()),
    path('LginView/', LginView.as_view()),
    path('StudentRegisterView/', StudentRegisterView.as_view()),
    path('CreatGroupView/', CreatGroupView.as_view()),
    path('davomatView/', DavomatView.as_view()),
    path('HomeworkViewTeacher/<int:id>/', HomeworkViewTeacher.as_view()),
    path('GetHomework/', GetHomework.as_view()),
    path('GetStudentHomework/<int:id>/', GetStudentHomework.as_view()),
    path('UploaduHomeworkStudent/<int:id>/', UploaduHomeworkStudent.as_view()),
    path('hacktonView/',HacktonView.as_view()),
    path('hacktonGetView/', HacktonGetView.as_view()),
    path('HacktonUpView/', HacktonUpView.as_view()),
]


