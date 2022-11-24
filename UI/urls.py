from django.urls import path
from UI import views

urlpatterns = [
    path('', views.index),
    path('admission/', views.admission),
    path('admin/', views.admin),
    path('admin/admission_details/', views.admission_details),
    path('admin/food/', views.food_body),
    path('admin/grieveance/', views.grieveance_body),
    path('admin/student_details/', views.student_details_body),
    path('admin/rooms/', views.accomodation_body),
    path('student/', views.student),
    path('student/food/',views.student_food),
    path('student/grieveance/',views.student_grieveance),
    path('student/remarks/',views.student_remarks)
]