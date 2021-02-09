from rest_framework import serializers
from .models import *


class lectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ('lectureid','lecturename','courseid','tutoriallink','schoolid','uploaddate','lecturenotes','recordedlecture','lecturedescription')

class classSerializer(serializers.ModelSerializer):
    class Meta:
        model = TblClass
        fields = ('__all__')

class calenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calender
        fields = ('event_id', 'event_name', 'event_details', 'due_date','course_id','class_id')

class_attendance = (
    ('Present','Present'),
    ('Absent','Absent'),
)

class StudentFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calender
        fields = ('feedbackid', 'courseid', 'description', 'submitdate','teacherid','studentid','option','rating')

class attendanceSerializer(serializers.ModelSerializer):
    # mark_attendance = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=class_attendance)
    class Meta:
        model = Attendance
        fields = ('mark_attendance',)
        # widgets = {
        #     'mark_attendance': CheckboxSelectMultiple(attrs={'choices'  : class_attendance}),
        # }

class createquizSerializer(serializers.ModelSerializer):
    class Meta:
        model = createQuiz
        fields = ('quizid', 'quizname', 'quizdate', 'courseid','classid')


class questionSerializer(serializers.ModelSerializer):
    class Meta:
        model = quizQuestionsAndAnswers
        fields = ( '__all__' )
        
class courseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ( '__all__' )
        
class schoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ( '__all__' )
class teacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = schoolTeacher
        fields = ( '__all__' )
        
class assigmentSerializer(serializers.ModelSerializer):
    # classid = serializers.StringRelatedField(many=False)
    # classid = classSerializer()
    # courseid = courseSerializer()
    # schoolid = schoolSerializer()
    # teacherid = teacherSerializer()

    classid = serializers.StringRelatedField(many=False)
    courseid = serializers.StringRelatedField(many=False)
    schoolid = serializers.StringRelatedField(many=False)
    teacherid = serializers.StringRelatedField(many=False)

    class Meta:
        model = Assignment
        # fields = ('assignmentid', 'assignmentname', 'classid', 'courseid','assignment','duedate','schoolid','createddate','teacherid')
        fields = ('__all__')
