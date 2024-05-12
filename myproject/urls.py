
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]


# myproject/urls.py
from django.urls import path, include

urlpatterns = [
    path('', include('myapp.urls')),
]
