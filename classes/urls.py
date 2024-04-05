from django.urls import path
from django.views.generic import TemplateView, RedirectView
from .views import *

app_name="classes"

urlpatterns = [
    path('', TemplateView.as_view(template_name="ex1.html", extra_context={'title':'Custom Title'})),
    path('ex2', Ex2View.as_view(), name="ex2"),
    path('rdt', RedirectView.as_view(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"), name="go-to-very"),
    path('ex3/<int:pk>/', PostPreLoadTaskView.as_view(), name="redirect-task"),
    path('ex4/<int:pk>/', SinglePostView.as_view(), name="singlepost"),
]