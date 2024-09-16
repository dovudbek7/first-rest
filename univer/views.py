from rest_framework import viewsets
from .models import Faculty, Group, Teacher, Student, Subject, Kafedra
from .serializers import FacultySerializer, GroupSerializer, TeacherSerializer, StudentSerializer, SubjectSerializer, KafedraSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
# class FacultyViewSet(viewsets.ModelViewSet):
#     queryset = Faculty.objects.all()
#     serializer_class = FacultySerializer
#
#
# class GroupViewSet(viewsets.ModelViewSet):
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#
#
# class TeacherViewSet(viewsets.ModelViewSet):
#     queryset = Teacher.objects.all()
#     serializer_class = TeacherSerializer
#
#
# class StudentViewSet(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#
# class SubjectViewSet(viewsets.ModelViewSet):
#     queryset = Subject.objects.all()
#     serializer_class = SubjectSerializer
#
#
# class KafedraViewSet(viewsets.ModelViewSet):
#     queryset = Kafedra.objects.all()
#     serializer_class = KafedraSerializer

# generic

# class FacultyListCreateView(generics.ListCreateAPIView):
#     queryset = Faculty.objects.all()
#     serializer_class = FacultySerializer
#
#
# class FacultyDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Faculty.objects.all()
#     serializer_class = FacultySerializer
#
#
# # Group Views
# class GroupListCreateView(generics.ListCreateAPIView):
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#
#
# class GroupDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
#
#
# # Teacher Views
# class TeacherListCreateView(generics.ListCreateAPIView):
#     queryset = Teacher.objects.all()
#     serializer_class = TeacherSerializer
#
#
# class TeacherDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Teacher.objects.all()
#     serializer_class = TeacherSerializer
#
#
# # Student Views
# class StudentListCreateView(generics.ListCreateAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#
# class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer
#
#
# # Subject Views
# class SubjectListCreateView(generics.ListCreateAPIView):
#     queryset = Subject.objects.all()
#     serializer_class = SubjectSerializer
#
#
# class SubjectDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Subject.objects.all()
#     serializer_class = SubjectSerializer
#
#
# # Kafedra Views
# class KafedraListCreateView(generics.ListCreateAPIView):
#     queryset = Kafedra.objects.all()
#     serializer_class = KafedraSerializer
#
#
# class KafedraDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Kafedra.objects.all()
#     serializer_class = KafedraSerializer

# apiviewset

class FacultyList(APIView):
    def get(self, request):
        faculties = Faculty.objects.all()
        serializer = FacultySerializer(faculties, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FacultySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FacultyDetail(APIView):
    def get_object(self, pk):
        try:
            return Faculty.objects.get(pk=pk)
        except Faculty.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        faculty = self.get_object(pk)
        serializer = FacultySerializer(faculty)
        return Response(serializer.data)

    def put(self, request, pk):
        faculty = self.get_object(pk)
        serializer = FacultySerializer(faculty, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        faculty = self.get_object(pk)
        faculty.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Group CRUD API
class GroupList(APIView):
    def get(self, request):
        groups = Group.objects.all()
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GroupDetail(APIView):
    def get_object(self, pk):
        try:
            return Group.objects.get(pk=pk)
        except Group.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        group = self.get_object(pk)
        serializer = GroupSerializer(group)
        return Response(serializer.data)

    def put(self, request, pk):
        group = self.get_object(pk)
        serializer = GroupSerializer(group, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        group = self.get_object(pk)
        group.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Repeat similar CRUD logic for Teacher, Student, Subject, and Kafedra models

# Teacher CRUD API
class TeacherList(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TeacherDetail(APIView):
    def get_object(self, pk):
        try:
            return Teacher.objects.get(pk=pk)
        except Teacher.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        teacher = self.get_object(pk)
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)

    def put(self, request, pk):
        teacher = self.get_object(pk)
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        teacher = self.get_object(pk)
        teacher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Student CRUD API
class StudentList(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentDetail(APIView):
    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Subject CRUD API
class SubjectList(APIView):
    def get(self, request):
        subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SubjectDetail(APIView):
    def get_object(self, pk):
        try:
            return Subject.objects.get(pk=pk)
        except Subject.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        subject = self.get_object(pk)
        serializer = SubjectSerializer(subject)
        return Response(serializer.data)

    def put(self, request, pk):
        subject = self.get_object(pk)
        serializer = SubjectSerializer(subject, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        subject = self.get_object(pk)
        subject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Kafedra CRUD API
class KafedraList(APIView):
    def get(self, request):
        kafedras = Kafedra.objects.all()
        serializer = KafedraSerializer(kafedras, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = KafedraSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class KafedraDetail(APIView):
    def get_object(self, pk):
        try:
            return Kafedra.objects.get(pk=pk)
        except Kafedra.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        kafedra = self.get_object(pk)
        serializer = KafedraSerializer(kafedra)
        return Response(serializer.data)

    def put(self, request, pk):
        kafedra = self.get_object(pk)
        serializer = KafedraSerializer(kafedra, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        kafedra = self.get_object(pk)
        kafedra.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)