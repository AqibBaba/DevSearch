from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    path("",views.getRoutes,name='getRoutes'),
    path("projects/",views.getProjects,name='getProjects'),
    path("projects/<str:pk>/",views.getProject,name='getProject'),
    path("projects/<str:pk>/vote/",views.projectVote,name='projectVote'),

    path("remove-tag/",views.removeTag)
]
