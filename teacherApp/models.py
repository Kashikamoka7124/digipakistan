# Create your models here.
from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model


class School(models.Model):
    schoolid = models.IntegerField(primary_key=True)
    schoolname = models.CharField(max_length=50)
    schoolimage = models.ImageField(default='default.jpg')
    schoolcontactno = models.IntegerField()
    schooladdress = models.CharField(max_length=500)
    createddate = models.DateTimeField()
    schoolemail = models.EmailField()
    password = models.CharField(max_length=13)

    def __str__(self):
        return self.schoolname


class RoleName(models.Model):
    roleid = models.IntegerField(primary_key=True)
    rolename = models.CharField(max_length=50)

    def __str__(self):
        return self.rolename


class TblClass(models.Model):
    classid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    schoolid = models.IntegerField()

    def __str__(self):
        return self.name


class Course(models.Model):
    courseid = models.IntegerField(primary_key=True)
    coursedescription = models.CharField(max_length=500)
    coursename = models.CharField(max_length=50)
    userid = models.IntegerField()
    code = models.CharField(max_length=50)
    videolink = models.FileField(default='default_link')
    roleid = models.ForeignKey(RoleName, on_delete=models.CASCADE)
    createddate = models.DateTimeField()
    imagelink = models.URLField(default='default_link')
    duration = models.DateTimeField()
    longdes = models.TextField()
    coursetype = models.CharField(max_length=50)
    classid = models.ForeignKey(TblClass, on_delete=models.CASCADE)
    assignto = models.CharField(max_length=200)
    status = models.BinaryField()

    def __str__(self):
        return self.coursename

class Student(models.Model):
    studentid = models.IntegerField(primary_key=True)
    regno = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    contactno = models.CharField(max_length=13)
    registrationdate = models.DateTimeField()
    address = models.CharField(max_length=200)
    classid = models.ForeignKey(TblClass, on_delete=models.CASCADE)
    schoolid = models.ForeignKey(School, on_delete=models.CASCADE)
    password = models.CharField(max_length=13)
    imagepath = models.ImageField(max_length=100, default='default.jpg')
    sectionid = models.IntegerField()

    def __str__(self):
        return self.name


class Lecture(models.Model):
    lectureid = models.IntegerField(primary_key=True)
    lecturename = models.CharField(max_length=150)
    courseid = models.ForeignKey(Course, on_delete=models.CASCADE)
    tutoriallink = models.CharField(max_length=100, default='No tutorial for this lecture.')
    schoolid = models.ForeignKey(School, on_delete=models.CASCADE)
    uploaddate = models.DateTimeField()
    lecturenotes = models.FileField(max_length=100, default='no notes',upload_to='media')
    recordedlecture= models.FileField(max_length=100, default='no video', upload_to='media')
    lecturedescription = models.TextField(max_length=500)

    def __str__(self):
        return self.lecturename


class schoolTeacher(models.Model):
    teacherid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    contact = models.IntegerField()
    classid = models.ForeignKey(TblClass, on_delete=models.CASCADE)
    schoolid = models.ForeignKey(School, on_delete=models.CASCADE)
    passowrd = models.CharField(max_length=13)
    image = models.ImageField(default='default.jpg')
    regno = models.CharField(max_length=20)
    joiningdate = models.DateTimeField()

    def __str__(self):
        return self.name


class Assignment(models.Model):
    assignmentid = models.IntegerField(primary_key=True)
    assignmentname = models.CharField(max_length=50)
    classid = models.ForeignKey(TblClass, related_name='classname' ,on_delete=models.CASCADE)
    courseid = models.ForeignKey(Course, related_name='course', on_delete=models.CASCADE)
    assignment = models.FileField(max_length=100, default='no assignmnet yet',upload_to='media')
    duedate = models.DateTimeField()
    schoolid = models.ForeignKey(School, related_name='school', on_delete=models.CASCADE)
    createddate = models.DateTimeField()
    teacherid = models.ForeignKey(schoolTeacher, related_name='teacher', on_delete=models.CASCADE, default= 0)

    def __str__(self):
        return self.assignmentname

class createQuiz(models.Model):
    quizid = models.IntegerField(default=0)
    quizname = models.CharField(max_length=100)
    quizdate = models.DateTimeField(default = '0000-00-00')
    courseid = models.ForeignKey(Course, on_delete=models.CASCADE)
    classid = models.ForeignKey(TblClass, on_delete=models.CASCADE)

    def __str__ (self):
        return (self.quizname)

class quizQuestionsAndAnswers(models.Model):
    questionid=models.CharField(max_length=20 , default=0)
    quizid=models.ForeignKey(createQuiz, on_delete=models.CASCADE)
    courseid = models.ForeignKey(Course, on_delete=models.CASCADE, default=0)
    question = models.CharField(max_length = 500)
    option1 = models.CharField(max_length = 20)
    option2 = models.CharField(max_length = 20)
    option3 = models.CharField(max_length = 20)
    option4 = models.CharField(max_length = 20)
    answer = models.CharField(max_length = 20)
    
    def __str__ (self):
        return (self.questionid)

class SubmitAssignment(models.Model):
    uploadid = models.IntegerField()
    assignmentid = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    schoolid = models.ForeignKey(School, on_delete=models.CASCADE)
    studentid = models.ForeignKey(Student, on_delete=models.CASCADE)
    courseid = models.ForeignKey(Course, on_delete=models.CASCADE)
    assignmnet_file = models.FileField(max_length=100, default='no file',upload_to='media')
    submitdate = models.DateTimeField()


class StudentFeedBack(models.Model):
    feedbackid = models.AutoField(primary_key=True)
    courseid = models.ForeignKey(Course, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    submitdate = models.DateTimeField(auto_now_add=True)
    teacherid = models.ForeignKey(schoolTeacher, on_delete=models.CASCADE)
    studentid = models.ForeignKey(Student,on_delete=models.CASCADE)
    option = [('Good','Good'),('Average','Average'),('Bad','Bad')]
    rating = models.CharField(max_length=100, choices=option, default='none')

class Discussion(models.Model):
    Message_id = models.AutoField(primary_key=True)
    classname = models.CharField(max_length=200)
    author = models.CharField(max_length=200 , default='no name')
    content = models.TextField( null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return "{}".format(self.pk)

class Calender(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=200 , default='NULL')
    event_details = models.CharField(max_length=200 , default='NULL')
    due_date = models.DateField()
    class_id = models.ForeignKey(TblClass, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    def __str__ (self):
        return (self.event_name)

class_attendance = (
    ('Present','Present'),
    ('Absent','Absent'),
)

class Attendance(models.Model):
    classid = models.ForeignKey(TblClass, on_delete=models.CASCADE)
    courseid = models.ForeignKey(Course, on_delete=models.CASCADE)
    student_name = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    mark_attendance = models.CharField(max_length=50, choices=class_attendance)








