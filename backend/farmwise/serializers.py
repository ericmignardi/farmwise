from rest_framework import serializers
from .models import Farm, Crop, Asset, WealthRecord


class CropSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crop
        fields = "__all__"
        read_only_fields = ["created_at"]


class AssetSerializer(serializers.ModelSerializer):
    asset_type_display = serializers.CharField(
        source="get_asset_type_display", read_only=True
    )

    class Meta:
        model = Asset
        fields = "__all__"
        read_only_fields = ["created_at"]


class WealthRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = WealthRecord
        fields = "__all__"
        read_only_fields = ["created_at"]


class FarmSerializer(serializers.ModelSerializer):
    crops = CropSerializer(many=True, read_only=True)
    assets = AssetSerializer(many=True, read_only=True)
    total_wealth = serializers.SerializerMethodField()

    class Meta:
        model = Farm
        fields = "__all__"
        read_only_fields = ["created_at", "updated_at"]

    def get_total_wealth(self, obj):
        crop_value = sum(crop.current_value for crop in obj.crops.all())
        asset_value = sum(asset.current_value for asset in obj.assets.all())
        return float(crop_value + asset_value)


class FarmListSerializer(serializers.ModelSerializer):
    crop_count = serializers.IntegerField(source="crops.count", read_only=True)
    asset_count = serializers.IntegerField(source="assets.count", read_only=True)

    class Meta:
        model = Farm
        fields = [
            "id",
            "name",
            "location",
            "owner",
            "total_acreage",
            "crop_count",
            "asset_count",
            "created_at",
        ]
        read_only_fields = ["created_at"]
