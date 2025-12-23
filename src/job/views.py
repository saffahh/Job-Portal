from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from job.services.services import (
    get_all_jobs,
    get_job_by_id,
    create_job,
    update_job,
    delete_job
)


class JobListCreateView(APIView):
    def get(self, request):
        jobs = get_all_jobs()
        return Response(jobs, status=status.HTTP_200_OK)
    def post(self, request):
        data, errors = create_job(request.data, request.user)
        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(data, status=status.HTTP_201_CREATED)


class JobDetailView(APIView):

    def get(self, request, pk):
        job = get_job_by_id(pk)
        if not job:
            return Response(
                {'error': 'Job not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        return Response(job, status=status.HTTP_200_OK)

    def put(self, request, pk):
        data, errors = update_job(pk, request.data)
        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        success = delete_job(pk)
        if not success:
            return Response(
                {'error': 'Job not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        return Response(status=status.HTTP_204_NO_CONTENT)
