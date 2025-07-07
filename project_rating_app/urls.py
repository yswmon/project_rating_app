from django.contrib import admin
from django.urls import path
from projects import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.project_list, name='project_list'),
    path('projects/<int:pk>/', views.project_detail, name='project_detail'),
    path('projects/<int:pk>/vote/', views.submit_vote, name='submit_vote'),
    path('projects/<int:pk>/result/', views.vote_result, name='vote_result'),
    path('', views.role_selection, name='role_selection'),  # 첫 화면
    path('projects/', views.project_list, name='project_list'),  # 리스트 화면
]
