from django.urls import path
from . import views  # Import views from the current app

urlpatterns = [
    path('reg', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    # ... other customer-related URL patterns (if any) ...
]
