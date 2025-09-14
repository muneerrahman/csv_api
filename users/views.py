from django.shortcuts import render
import csv
import io
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer


class UploadCSVView(APIView):
    def post(self, request, *args, **kwargs):
        file = request.FILES.get("file")

        # checking if the files csv or not
        if not file:
            return Response({"error": "No file uploaded"}, status=status.HTTP_400_BAD_REQUEST)

        if not file.name.endswith(".csv"):
            return Response({"error": "Only CSV files are allowed"}, status=status.HTTP_400_BAD_REQUEST)

        #read the file as bites and convert to string
        data_set = file.read().decode("UTF-8")
        io_string = io.StringIO(data_set)
        reader = csv.DictReader(io_string)

        saved_count = 0
        rejected_count = 0
        errors = []

        # looping the files and finding values
        for i, row in enumerate(reader, start=1):
            serializer = UserSerializer(data=row)
            if serializer.is_valid():
                try:
                    serializer.save()
                    saved_count += 1
                except Exception as e:
                    rejected_count += 1
                    errors.append({"row": i, "error": str(e)})
            else:
                rejected_count += 1
                errors.append({"row": i, "error": serializer.errors})

        return Response(
            {
                "saved_records": saved_count,
                "rejected_records": rejected_count,
                "errors": errors,
            },
            status=status.HTTP_200_OK,
        )

