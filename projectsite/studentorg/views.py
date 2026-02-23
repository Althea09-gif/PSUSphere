from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from studentorg.models import Organization, OrgMember, Student, College, Program
from studentorg.forms import OrganizationForm, MemberForm, StudentForm, CollegeForm, ProgramForm
from django.urls import reverse_lazy 

class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = "home.html"

class OrganizationList(ListView): 
    model = Organization
    context_object_name = 'organization' 
    template_name = 'org_list.html' 
    paginate_by = 5 

class OrganizationCreateView(CreateView): 
    model = Organization
    form_class = OrganizationForm 
    template_name = 'org_form.html' 
    success_url = reverse_lazy('organization-list')


class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('organization-list')

class OrganizationDeleteView(DeleteView):
    model = Organization 
    template_name = 'org_del.html'
    success_url = reverse_lazy('organization-list') 

class MembersListView(ListView):
   model = OrgMember
   context_object_name = 'member'
   template_name = 'member_list.html'
   paginate_by = 5

class MembersCreateView(CreateView):
  model = OrgMember
  form_class = MemberForm
  template_name = 'member_form.html'
  success_url = reverse_lazy('member-list')

class MembersUpdateView(UpdateView):
   model = OrgMember
   form_class = MemberForm
   template_name = 'member_form.html'
   success_url = reverse_lazy('member-list')

class MembersDeleteView(DeleteView):
  model = OrgMember
  template_name = 'member_del.html'
  success_url = reverse_lazy('member-list')

class StudentListView(ListView):
   model = Student
   context_object_name = 'student'
   template_name = 'student_list.html'
   paginate_by = 5


class StudentCreateView(CreateView):
  model = Student
  form_class = StudentForm
  template_name = 'student_form.html'
  success_url = reverse_lazy('student-list')

class StudentUpdateView(UpdateView):
   model = Student
   form_class = StudentForm
   template_name = 'student_form.html'
   success_url = reverse_lazy('student-list')

class StudentDeleteView(DeleteView):
  model = Student
  template_name = 'student_del.html'
  success_url = reverse_lazy('student-list')

class CollegeListView(ListView):
   model = College
   context_object_name = 'college'
   template_name = 'college_list.html'
   paginate_by = 5

class CollegeCreateView(CreateView):
  model = College
  form_class = CollegeForm
  template_name = 'college_form.html'
  success_url = reverse_lazy('college-list')

class CollegeUpdateView(UpdateView):
   model = College
   form_class = CollegeForm
   template_name = 'college_form.html'


class CollegeDeleteView(DeleteView):
  model = College
  template_name = 'college_del.html'
  success_url = reverse_lazy('college-list')


class ProgramListView(ListView):
   model = Program
   context_object_name = 'program'
   template_name = 'program_list.html'
   paginate_by = 5



