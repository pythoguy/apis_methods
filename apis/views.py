from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apis.models import *
from apis.serializer import *
# Create your views here.

@api_view(["GET"])
def firstapi(request):
    data=database.objects.all().order_by("-id")
    dataa = dataserlizer(data, many=True)

    return Response({"name" : "sahil",
                     "data" : dataa.data})


@api_view(["POST"])
def save(request):
    abc = dataserlizer(data = request.data)
    if abc.is_valid():
        abc.save()

    return Response({"message" : "Data Saved Successfully"})


@api_view(["PATCH"])
def update(request,id):
    cde = database.objects.get(id = id)
    ghi = dataserlizer(cde, data = request.data, partial = True)

    if ghi.is_valid():
        ghi.save()

    return Response({"message" : "Data Updated Successfully"})


@api_view(["DELETE"])
def delete(request,id):
    cde = database.objects.get(id = id)
    cde.delete()

    return Response({"message" : "Data Deleted Successfully"})