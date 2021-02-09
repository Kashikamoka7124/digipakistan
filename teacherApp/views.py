# from django.shortcuts import render, HttpResponse,redirect
# from teacherApp.models import *
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.forms.formsets import formset_factory
from django.utils.timezone import datetime
# from .form import *

# ***************** API ****************
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import *
from django.http import Http404
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,viewsets


# Create your views here.
username = ''

# def home(request):
#     return render(request,'home.html')

# def portal(request):
#     return render(request,'portal.html')
'''
def discussion(request):
    queryset1 = TblClass.objects.all()
    context = { 
            "object_list1" : queryset1 
        }
    if (request.method == "POST"):
        data = JSONParser.parse(request)
        classname = data('classname')
        queryset = Discussion.objects.filter(classname=classname)
        context = { 
            "object_list" : queryset,
            "object_list2" : classname,
        }
        return JsonResponse(data, context, status = 201)
    return JsonResponse(request, context, status = 201)

def savemsg(request):  
    queryset1 = TblClass.objects.all()
    context = { 
            "object_list1" : queryset1 
        }  
    if (request.method == "POST"):
        author = username
        data = JSONParser.parse(request)
        classname = data('classname')
        content = data('msg')
        if(author != ''):
            Discussion(classname= classname , author = author ,content = content).save() 
            queryset = Discussion.objects.filter(classname=classname)
            context = { 
                "object_list" : queryset,
                "object_list2" : classname,
            }
            return JsonResponse(data, context,status = 201)
        else:
            return JsonResponse(data, context, status = 400)
    return JsonResponse(request, context, status = 201)
'''    

class AddAssignment(APIView):
    def get(self,request):
        assignment = Assignment.objects.all()
        serializer = assigmentSerializer(assignment, many = True)
        return Response(serializer.data,status = status.HTTP_200_OK)

    def post(self,request,format = None):
        data = JSONParser().parse(self.request)
        serializer = assigmentSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.data,status = status.HTTP_400_BAD_REQUEST)

# class AddAssignment(viewsets.ModelViewSet):
#     queryset = Assignment.objects.all()
#     serializer_class = assigmentSerializer

class DetailAssignment(APIView):
    def get_object(self, pk):
        try:
            return Assignment.objects.get(assignmentid=pk)
        except Assignment.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        data = self.get_object(pk)
        serilizer = assigmentSerializer(data)
        return Response(serilizer.data)

    def delete(self, request, pk, format=None):
        assignement = self.get_object(pk)
        assignement.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class Quiz(APIView):
    def get(self,request):
        quiz = createQuiz.objects.all()
        serializer = createquizSerializer(quiz, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        data = JSONParser().parse(request)
        serializer = createquizSerializer(data.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            serializer = createquizSerializer()
            return Response(serializer.errors,status = status.HTTP_406_NOT_ACCEPTABLE)

class QuizDetail(APIView):
    def get_object(self,pk):
        try:
            return createQuiz.objects.filter(quizid=pk)
        except:
            raise Http404

    def get(self,request,pk):
        data = self.get_object(pk)
        serializer = createquizSerializer(data)
        return Response(serializer.data)

    def put(self,request,pk):
        data = self.get_object(pk)
        serializer = createquizSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        data = self.get_object(pk)
        data.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

'''
def add_question(request):
    if request.method == "POST":
        data = JSONParser().parse(request)
        serializer = questionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status = 201)
    else:
        form = questionSerializer()
    return JsonResponse(request,status = 404)
    '''
class AddLecture(APIView):
    def get(self,request,format=None):
        data = Lecture.objects.all()
        serializer = lectureSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request,format=None):
        data = JSONParser().parse(request)
        serializer = lectureSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status =status.HTTP_201_CREATED)
        else:
            serializer = lectureSerializer()
            return Response(serializer.errors,status =status.HTTP_400_BAD_REQUEST)   

class LectureDetail(APIView):
    def get_object(self,pk):
        try:
            return Lecture.objects.filter(lectureid=pk)
        except:
            raise Http404

    def get(self,request,pk,format=None):
        data = self.get_object(pk)
        serializer = lectureSerializer(data)
        return Response(serializer.data)

    def put(self,request,pk,format=None):
        data = self.get_object(pk)
        serializer = lectureSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk,format=None):
        data = self.get_object(pk)
        data.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class Feedback(APIView):
    def get(self,request):
        data = StudentFeedBack.objects.all()
        serializer = StudentFeedbackSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):
        data = JSONParser().parse(request)
        serializer = StudentFeedbackSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status =status.HTTP_201_CREATED)
        else:
            serializer = StudentFeedbackSerializer()
            return Response(serializer.errors,status =status.HTTP_400_BAD_REQUEST)   

class FeedbackDetail(APIView):
    def get_object(self,pk):
        try:
            return StudentFeedBack.objects.filter(id=pk)
        except:
            raise Http404

    def get(self,request,pk):
        data = self.get_object(pk)
        serializer = StudentFeedbackSerializer(data)
        return Response(serializer.data)

    def delete(self,request,pk):
        data = self.get_object(pk)
        data.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

#############################################################
class AddCalender(APIView):
    def get(self,request,format=None):
        data = Calender.objects.all()
        serializer = calenderSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request,format=None):
        data = JSONParser().parse(request)
        serializer = calenderSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status =status.HTTP_201_CREATED)
        else:
            serializer = calenderSerializer()
            return Response(serializer.errors,status =status.HTTP_400_BAD_REQUEST)   
class CalenderDetail(APIView):
    def get_object(self,pk,class_id,course_id):
        try:
            return Calender.objects.filter(calenderid=pk).filter(classid=class_id).filter(courseid=course_id)
        except:
            raise Http404

    def get(self,request,pk,format=None):
        data = self.get_object(pk,request.classid,request.courseid)
        serializer = calenderSerializer(data)
        return Response(serializer.data)

    def put(self,request,pk,format=None):
        data = self.get_object(pk)
        serializer = calenderSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk,format=None):
        data = self.get_object(pk)
        data.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

'''
def attendance(request):
    # AttendanceFormset = formset_factory(AttendanceForm)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        if 'studentname' in request.POST:
            classid = request.POST.get("classid")
            courseid = request.POST.get("courseid")
            queryset = Student.objects.filter(classid__classid = classid )
            # AttendanceFormset = formset_factory(AttendanceForm)
            # formset = AttendanceFormset()
            serializer = attendanceSerializer()
            context = { 
                "object_list" : queryset,
                # "formset" : formset,
                "form" : serializer,
                "courseid" : courseid,
                "classid" : classid,
                }
            return JsonResponse(request,context, status = 201)     
        
        elif 'attendance' in request.POST:
            classid = request.POST.get("classid")
            courseid = request.POST.get("courseid")
            # students = Student.objects.filter(classid__classid=classid)
            student = request.POST.get("student")
            print(student)
            data = JSONParser().parse(request)
            serializer = attendanceSerializer(data=data)
            if serializer.is_valid():
                print(student)
                serializer.save()
                Attendance(classid = TblClass.objects.get(classid=classid) , courseid = Course.objects.get(courseid=courseid) , student_name= student ).save()
                return JsonResponse(serializer.data ,status = 201)
            else:
                return JsonResponse(serializer.data,status = 400)
    else:
        return JsonResponse(request,status = 404)
    return JsonResponse(request,status = 404)
'''
#################################################


'''
***************************************************************************
|               Documentation
***************************************************************************

1)Attendance:  Attendance will taken when Student will active in class by
his/her personal student account

2) Login/Registration/forgot/logout: For Login and Registration we will
use Django built-in model and create its relation with role model and then redirect it to dashboard
corresponding his/her role

'''