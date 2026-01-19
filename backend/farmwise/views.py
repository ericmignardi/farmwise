from langchain_core.messages import HumanMessage, SystemMessage
from .services.llm import get_llm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Farm, Crop, Asset, WealthRecord
from .serializers import (
    FarmSerializer,
    FarmListSerializer,
    CropSerializer,
    AssetSerializer,
    WealthRecordSerializer,
)
from .services.rag import get_farm_context_chain

# Create your views here.


@api_view(["GET"])
def farm_list(request):
    farms = Farm.objects.all()
    farmsSerialized = FarmListSerializer(farms, many=True)
    return Response(farmsSerialized.data)


@api_view(["GET"])
def farm_detail(request, pk):
    farm = Farm.objects.get(pk=pk)
    farmSerialized = FarmSerializer(farm)
    return Response(farmSerialized.data)


@api_view(["GET"])
def crop_list(request):
    crops = Crop.objects.all()
    cropsSerialized = CropSerializer(crops, many=True)
    return Response(cropsSerialized.data)


@api_view(["GET"])
def asset_list(request):
    assets = Asset.objects.all()
    assetsSerialized = AssetSerializer(assets, many=True)
    return Response(assetsSerialized.data)


@api_view(["GET"])
def wealth_list(request):
    wealthRecords = WealthRecord.objects.all()
    wealthRecordsSerialized = WealthRecordSerializer(wealthRecords, many=True)
    return Response(wealthRecordsSerialized.data)


@api_view(["POST"])
def chat(request):
    message = request.data.get("message", "")
    chain = get_farm_context_chain()
    response_text = chain.invoke(message)

    return Response({"response": response_text})
