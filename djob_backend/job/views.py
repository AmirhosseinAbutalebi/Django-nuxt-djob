from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, authentication, permissions
from .serializers import JobSerializer, JobDetailSerializer, CategorySerializer
from .models import Job, Category
from .forms import JobForm

# Create your views here.

class NewestJobsView(APIView):
    def get(self, request, format=None):
        jobs = Job.objects.all()[0:4]
        serializer = JobSerializer(jobs, many=True)

        return Response(serializer.data)
    
class JobsDetailView(APIView):
    def get(self, request, pk, format=None):
        job = Job.objects.get(pk=pk)
        serializer = JobDetailSerializer(job)

        return Response(serializer.data)
    
class BrowseJobView(APIView):
    def get(self, request, format=None):
        jobs = Job.objects.all()
        categories = request.GET.get('categories', '')
        query = request.GET.get('query', '')
        if query:
            jobs = jobs.filter(title__icontains=query)
        if categories:
            jobs = jobs.filter(category_id__in=categories.split(','))
        serializer = JobDetailSerializer(jobs, many=True)

        return Response(serializer.data)
    
class CategoriesView(APIView):
    def get(self, request, format=None):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)

        return Response(serializer.data)
    
class MyJobsView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        jobs = Job.objects.filter(created_by=request.user)
        serializer = JobDetailSerializer(jobs, many=True)

        return Response(serializer.data)

class CreateJobView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        form = JobForm(request.data)

        if form.is_valid():
            job = form.save(commit=False)
            job.created_by = request.user
            job.save()

            return Response({'status': 'created'})
        else:
            return Response({'status': 'errors', 'errors': form.errors})
    
    def delete(self, request, pk):
        job = Job.objects.get(pk=pk, created_by=request.user)
        job.delete()
        return Response({'status': 'deleted'})
    
    def put(self, request, pk):
        job = Job.objects.get(pk=pk, created_by=request.user)
        form = JobForm(request.data, instance=job)
        form.save()
        return Response({'status': 'updated'})
