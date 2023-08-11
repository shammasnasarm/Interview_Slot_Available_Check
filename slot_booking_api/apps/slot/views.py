from django.shortcuts import render

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializers import *

from datetime import datetime

# Create your views here.





class AvailabilityView(generics.ListCreateAPIView):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer


class AvailableSlotView(APIView):
    def get(self, request):

        interviewer_id = request.query_params.get('interviewer_id')
        candidate_id = request.query_params.get('candidate_id')
        available_date = request.query_params.get('available_date', datetime.now().date())

        if (interviewer_id or candidate_id) == None:
            return Response({"Error":"interviewer_id or candidate_id not provided"},status=status.HTTP_400_BAD_REQUEST)

        interviewers = Availability.objects.filter(user_id=interviewer_id, date=available_date, is_interviewer=True)
        candidates = Availability.objects.filter(user_id=candidate_id, date=available_date, is_interviewer=False)

        available_slots = []
        for i in interviewers:
            for c in candidates:
                available_time_start = max(i.start_time,c.start_time)
                available_time_end = min(i.end_time,c.end_time)

                total_hours = int(((available_time_end.hour*60 + available_time_end.minute) - (available_time_start.hour*60 + available_time_start.minute))/60)

                for s in range(total_hours):
                    start = str(available_time_start.hour+s)+":"+str(available_time_start.minute)
                    end = str(available_time_start.hour+s+1)+":"+str(available_time_start.minute)
                    slot = (start,end)
                    if slot not in available_slots:
                        available_slots.append(slot)
        return Response({"Avalible Slots":available_slots},status=status.HTTP_200_OK)