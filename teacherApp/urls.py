
from django.contrib import admin
from django.urls import path
from teacherApp.views import *
from teacherApp import views

from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
      
    # path('forget', views.forget, name = "forget"),
    # path('reset', views.reset, name = "reset"),
    # path('portal', views.portal , name = "portal"),
    # path('', views.home, name = "home"),
    # path('log_in', views.login_page , name = "login_page"),
    # path('log_out', views.logout_page , name = "logout_page"),
    # path('Assignment', views.assignment, name = "assignmnet_page"),

    path('assignment', views.AddAssignment.as_view() , name = "addAssignmnet"),
    path('detail_assignment/<int:pk>/', views.DetailAssignment.as_view(), name = "deleteAssignmnet"),

    # path('uploaded_ass', views.uploadedAssignment, name = "uploadedAssignmnet"),

    # path('submitted_ass', views.submittedAssignment, name = "submittedAssignment"),

    # path('mcqs_quiz', views.mcqs_quiz, name = "mcqs_quiz"),
    # path('theory_quiz', views.theory_quiz, name = "theory_quiz"),

    path('quiz', views.Quiz.as_view(), name = "quiz"),
    path('quiz_detail/<int:pk>/', views.QuizDetail.as_view(), name = "detail_quiz"),

    # path('add_question', views.add_question, name = "add_question"),
    # path('lecture', views.lecture, name = "lecture"),

    path('lecture', views.AddLecture.as_view(), name = "lecture"),
    path('lecture_detail/<int:pk>/', views.LectureDetail.as_view(), name = "lecture_detail"),

    path('feedback', views.Feedback.as_view(), name = "feedback"),
    path('feedback_detail/<int:pk>/', views.FeedbackDetail.as_view(), name = "feedback_detail"),

    # path('discussion', views.discussion, name='discussion'),
    # path('save', views.savemsg, name='savemsg'),

    # path('setting', views.setting, name='setting'),

    path('calender', views.AddCalender.as_view(), name='calender'),
    path('calender_detail/<int:pk>', views.CalenderDetail.as_view(), name='del_cal'),
    
    # path('Attendance', views.attendance, name='attendance'),


    


]

urlpatterns = format_suffix_patterns(urlpatterns)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)