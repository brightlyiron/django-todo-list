from django.urls import path, include

app_name = "api_v1"

urlpatterns = [
    path('todo', include('todo.api.urls'))
]
