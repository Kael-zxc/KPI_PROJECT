from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),  # ← Health-check будет по /api/health/
    # path('api/metrics/', include('metrics.urls')),  ← остальной API
]
