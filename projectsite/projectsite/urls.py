"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from studentorg import views

urlpatterns = [
    path("admin/", admin.site.urls),

    # Home
    path("", views.HomePageView.as_view(), name="home"),

    # Organization
    path("organization_list", views.OrganizationList.as_view(), name="organization-list"),
    path("organization_list/add", views.OrganizationCreateView.as_view(), name="organization-add"),
    path("organization_list/<pk>", views.OrganizationUpdateView.as_view(), name="organization-update"),
    path("organization_list/<pk>/delete", views.OrganizationDeleteView.as_view(), name="organization-delete"),

    # OrgMember (Member)
    path("member_list", views.MembersListView.as_view(), name="member-list"),
    path("member_list/add", views.MembersCreateView.as_view(), name="member-add"),
    path("member_list/<pk>", views.MembersUpdateView.as_view(), name="member-update"),
    path("member_list/<pk>/delete", views.MembersDeleteView.as_view(), name="member-delete"),

    # Student
    path("student_list", views.StudentListView.as_view(), name="student-list"),
    path("student_list/add", views.StudentCreateView.as_view(), name="student-add"),
    path("student_list/<pk>", views.StudentUpdateView.as_view(), name="student-update"),
    path("student_list/<pk>/delete", views.StudentDeleteView.as_view(), name="student-delete"),

    # College
    path("college_list", views.CollegeListView.as_view(), name="college-list"),
    path("college_list/add", views.CollegeCreateView.as_view(), name="college-add"),
    path("college_list/<pk>", views.CollegeUpdateView.as_view(), name="college-update"),
    path("college_list/<pk>/delete", views.CollegeDeleteView.as_view(), name="college-delete"),

    # Program
    path("program_list", views.ProgramListView.as_view(), name="program-list"),
    path("program_list/add", views.ProgramCreateView.as_view(), name="program-add"),
    path("program_list/<pk>", views.ProgramUpdateView.as_view(), name="program-update"),
    path("program_list/<pk>/delete", views.ProgramDeleteView.as_view(), name="program-delete"),
]