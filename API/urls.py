from django.urls import path
from API import views

urlpatterns = [
    path('check/',views.check),
    path('logout/',views.logout),
    path('newApplications/',views.newApplications),
    path('newStudent/',views.insertStudent),
    path('getStudentDetails/',views.getStudentDetails),
    path('setApprove/',views.setApprove),
    path('getRoomsDetails/',views.getRoomsDetails),
    path('getAvailableRooms/',views.getAvailableRooms),
    path('addMenuItem/',views.addMenuItem),
    path('fetchFoodItems/',views.fetchFoodItems),
    path('addDailyItem/',views.addDailyItem),
    path('FetchDailyItem/',views.FetchDailyItem),
    path('setGrieveanceViewed/',views.setGrieveanceViewed),
    path('fetchGrieveance/',views.fetchGrieveance),
    path('newGrieveance/',views.newGrieveance),
]