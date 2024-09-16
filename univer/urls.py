from django.urls import include, path
from rest_framework.routers import DefaultRouter
# from .views import FacultyViewSet, GroupViewSet, TeacherViewSet, StudentViewSet, SubjectViewSet, KafedraViewSet

# router = DefaultRouter()
# router.register(r'faculties', FacultyViewSet)
# router.register(r'groups', GroupViewSet)
# router.register(r'teachers', TeacherViewSet)
# router.register(r'students', StudentViewSet)
# router.register(r'subjects', SubjectViewSet)
# router.register(r'kafedras', KafedraViewSet)

# from .views import (
#     FacultyListCreateView, FacultyDetailView,
#     GroupListCreateView, GroupDetailView,
#     TeacherListCreateView, TeacherDetailView,
#     StudentListCreateView, StudentDetailView,
#     SubjectListCreateView, SubjectDetailView,
#     KafedraListCreateView, KafedraDetailView
# )

from .views import (
    FacultyList, FacultyDetail,
    GroupList, GroupDetail,
    TeacherList, TeacherDetail,
    StudentList, StudentDetail,
    SubjectList, SubjectDetail,
    KafedraList, KafedraDetail
)
# urlpatterns = [
#     # path('', include(router.urls)),
#     path('faculties/', FacultyListCreateView.as_view(), name='faculty-list'),
#     path('faculties/<int:pk>/', FacultyDetailView.as_view(), name='faculty-detail'),
#
#     # Group URLs
#     path('groups/', GroupListCreateView.as_view(), name='group-list'),
#     path('groups/<int:pk>/', GroupDetailView.as_view(), name='group-detail'),
#
#     # Teacher URLs
#     path('teachers/', TeacherListCreateView.as_view(), name='teacher-list'),
#     path('teachers/<int:pk>/', TeacherDetailView.as_view(), name='teacher-detail'),
#
#     # Student URLs
#     path('students/', StudentListCreateView.as_view(), name='student-list'),
#     path('students/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
#
#     # Subject URLs
#     path('subjects/', SubjectListCreateView.as_view(), name='subject-list'),
#     path('subjects/<int:pk>/', SubjectDetailView.as_view(), name='subject-detail'),
#
#     # Kafedra URLs
#     path('kafedras/', KafedraListCreateView.as_view(), name='kafedra-list'),
#     path('kafedras/<int:pk>/', KafedraDetailView.as_view(), name='kafedra-detail'),
# ]

urlpatterns = [
    path('faculties/', FacultyList.as_view(), name='faculty-list'),
    path('faculties/<int:pk>/', FacultyDetail.as_view(), name='faculty-detail'),
    path('groups/', GroupList.as_view(), name='group-list'),
    path('groups/<int:pk>/', GroupDetail.as_view(), name='group-detail'),
    path('teachers/', TeacherList.as_view(), name='teacher-list'),
    path('teachers/<int:pk>/', TeacherDetail.as_view(), name='teacher-detail'),
    path('students/', StudentList.as_view(), name='student-list'),
    path('students/<int:pk>/', StudentDetail.as_view(), name='student-detail'),
    path('subjects/', SubjectList.as_view(), name='subject-list'),
    path('subjects/<int:pk>/', SubjectDetail.as_view(), name='subject-detail'),
    path('kafedras/', KafedraList.as_view(), name='kafedra-list'),
    path('kafedras/<int:pk>/', KafedraDetail.as_view(), name='kafedra-detail'),
]
