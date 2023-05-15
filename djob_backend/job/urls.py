from django.urls import path
from .views import NewestJobsView, JobsDetailView, CategoriesView, BrowseJobView, MyJobsView, CreateJobView


urlpatterns = [
    path('categories/', CategoriesView.as_view()),
    path('my/', MyJobsView.as_view()),
    path('create/', CreateJobView.as_view()),
    path('<int:pk>/', JobsDetailView.as_view()),
    path('<int:pk>/delete/', CreateJobView.as_view()),
    path('<int:pk>/edit/', CreateJobView.as_view()),
    path('newest/', NewestJobsView.as_view()),
    path('', BrowseJobView.as_view()),
]
 