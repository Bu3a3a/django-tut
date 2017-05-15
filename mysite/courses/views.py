from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from .models import CourseSession, UserCourseSession


class CourseSessionListView(generic.ListView):
    model = CourseSession
    template_name = 'courses/course-session_list.html'


class CourseSessionDetailView(generic.ListView):
    model = CourseSession
    template_name = 'courses/course-session_detail.html'


class UserCourseSessionListView(LoginRequiredMixin, generic.ListView):
    model = UserCourseSession
    template_name = 'courses/user-course-session_list.html'


class UserCourseSessionDetailView(LoginRequiredMixin, generic.ListView):
    model = UserCourseSession
    template_name = 'courses/user-course-session_detail.html'


class UserCourseSessionCreateView(LoginRequiredMixin, generic.CreateView):
    model = UserCourseSession
    template_name = 'courses/user-course-session_create.html'
    success_url = reverse_lazy('courses:list_user_course_session')
    fields = ['student', 'course_session']

