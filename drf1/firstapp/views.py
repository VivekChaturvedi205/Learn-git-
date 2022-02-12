from django.shortcuts import render
from firstapp.models import student
from .serializers import Studentserializer
from django.http import HttpResponse, JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

#GET -- Serialization use in GET

def student_list(request):
    stud = student.objects.all()
    serializer = Studentserializer(stud, many=True)
    return JsonResponse(serializer.data, safe=False)

def student_get(request,id):
    stud = student.objects.get(pk=id)
    serializer = Studentserializer(stud)
    return JsonResponse(serializer.data)

#POST -- Deserialization use in POST, PUT , DELETE
@csrf_exempt
def student_create(request):
    if request.method=='POST':
        json_data=request.body
        print(json_data)
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer=Studentserializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'Data Created'}
            return JsonResponse(res)
 