from django.urls import path
from apis import views


urlpatterns = [
    path("get", views.firstapi),
    path("post", views.save),
    path("patch/<int:id>", views.update),
    path("delete/<int:id>", views.delete)
]
