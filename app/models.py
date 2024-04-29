from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length = 20)
    lastname = models.CharField(max_length = 20)
    phone = models.CharField(max_length = 20, unique = True)
    password = models.CharField(max_length = 20)




class Teacher(User):
    def str(self):
        return f"{self.name} {self.lastname}"


LESSON_TIMES = (
    ("1-vaqt", "09:00-10:00"),
    ("2-vaqt", "10:10-11:10"),
    ("3-vaqt", "11:20-12:30"),
    ("4-vaqt", "14:00-15:00"),
    ("5-vaqt", "15:10-16:20"),
    ("6-vaqt", "16:30-17:30"),
    ("7-vaqt", "17:40-18:40"),
)

DAYS = (
    ('Odd', "Toq"),
    ("Even", "Juft")
)

class Student(User):
    space_id = models.CharField(max_length=6, unique=True)
    avatar = models.ImageField(upload_to="media/avatars")
    coin = models.IntegerField(default=0)

    def str(self):
        return self.space_id

    def __str__(self) -> str:
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=10, unique=True)
    time = models.CharField(max_length=50, choices=LESSON_TIMES)
    day = models.CharField(max_length=10, choices=DAYS)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def str(self):
        return self.name
    
class Davomat(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    is_have = models.BooleanField()
    kun = models.IntegerField()

    def str(self):
        return self.student.name
    
    def self_save(self):
        if self.is_have == True:
            self.kun += 1 
            return self.kun
        
class Coins(models.Model): #coin berish uchun
    TWO = 2
    THREE = 3
    FIVE = 5
    TEN = 10

    COIN_CHOICES = (
        (TWO, '2'),
        (THREE, '3'),
        (FIVE, '5'),
        (TEN, '10'),
    )
    coins = models.IntegerField(choices = COIN_CHOICES)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.student.name
    
    
    
class Homework(models.Model):
    file = models.FileField(upload_to='homework/')
    text = models.TextField()
    date = models.DateField(auto_now=True)
    coins = models.IntegerField(default=10)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.group.name
    

class Hackaton(models.Model):
    text = models.TextField()
    day = models.DateField()
    file = models.FileField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    coins = models.IntegerField()


    def __str__(self) -> str:
        return self.date 



    





    



