from django.urls import path

from . import views

urlpatterns = [
    path('', views.mainPage, name='main'),
    path('patient/<str:pk>/', views.patient, name='patient'),
    path('staff/', views.staff, name='staff'),
    path('login/', views.loginPage, name='login'),
    path('register/', views.registerPatient, name='register'),
    path('logout/', views.logoutUser, name='logout'),


    # path('ajaxResponse', views.ajaxResponse, name='ajaxResponse'),
    path('api/chart/data/<str:pk>', views.ChartData.as_view()),
]