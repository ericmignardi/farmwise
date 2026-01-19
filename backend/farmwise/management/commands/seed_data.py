from django.core.management.base import BaseCommand
from farmwise.models import Farm, Crop, Asset, WealthRecord
from datetime import date, timedelta
from decimal import Decimal


class Command(BaseCommand):
    help = "Seed database with sample farm data"

    def handle(self, *args, **kwargs):
        # Clear existing data
        Farm.objects.all().delete()

        # Create Farms
        farm1 = Farm.objects.create(
            name="Green Valley Farm",
            location="Saskatchewan, Canada",
            owner="John Anderson",
            total_acreage=Decimal("2500.00"),
        )

        farm2 = Farm.objects.create(
            name="Prairie Gold Farms",
            location="Manitoba, Canada",
            owner="Sarah Mitchell",
            total_acreage=Decimal("1800.00"),
        )

        farm3 = Farm.objects.create(
            name="Northern Harvest Co",
            location="Alberta, Canada",
            owner="Michael Chen",
            total_acreage=Decimal("3200.00"),
        )

        # Create Crops
        today = date.today()
        crops_data = [
            (
                farm1,
                "Winter Wheat",
                today - timedelta(days=180),
                today + timedelta(days=30),
                Decimal("85.5"),
                Decimal("425000.00"),
            ),
            (
                farm1,
                "Canola",
                today - timedelta(days=120),
                today + timedelta(days=60),
                Decimal("42.0"),
                Decimal("315000.00"),
            ),
            (
                farm2,
                "Barley",
                today - timedelta(days=150),
                today + timedelta(days=45),
                Decimal("68.0"),
                Decimal("204000.00"),
            ),
            (
                farm2,
                "Soybeans",
                today - timedelta(days=100),
                today + timedelta(days=75),
                Decimal("35.0"),
                Decimal("280000.00"),
            ),
            (
                farm3,
                "Durum Wheat",
                today - timedelta(days=160),
                today + timedelta(days=40),
                Decimal("72.0"),
                Decimal("540000.00"),
            ),
            (
                farm3,
                "Lentils",
                today - timedelta(days=90),
                today + timedelta(days=90),
                Decimal("25.0"),
                Decimal("187500.00"),
            ),
        ]

        for farm, name, planted, harvest, yield_val, value in crops_data:
            Crop.objects.create(
                farm=farm,
                name=name,
                planted_date=planted,
                harvest_date=harvest,
                expected_yield=yield_val,
                current_value=value,
                notes=f"{name} crop for {farm.name}",
            )

        # Create Assets
        assets_data = [
            (
                farm1,
                "John Deere S780 Combine",
                "equipment",
                Decimal("450000.00"),
                Decimal("380000.00"),
            ),
            (
                farm1,
                "North Quarter Section",
                "land",
                Decimal("1200000.00"),
                Decimal("1450000.00"),
            ),
            (
                farm1,
                "Grain Storage Bins",
                "building",
                Decimal("85000.00"),
                Decimal("78000.00"),
            ),
            (
                farm2,
                "Case IH Magnum 380",
                "equipment",
                Decimal("320000.00"),
                Decimal("275000.00"),
            ),
            (
                farm2,
                "Cattle Herd (150 head)",
                "livestock",
                Decimal("225000.00"),
                Decimal("262500.00"),
            ),
            (
                farm2,
                "Equipment Shed",
                "building",
                Decimal("120000.00"),
                Decimal("115000.00"),
            ),
            (
                farm3,
                "New Holland CR10.90",
                "equipment",
                Decimal("520000.00"),
                Decimal("445000.00"),
            ),
            (
                farm3,
                "South Field (640 acres)",
                "land",
                Decimal("1600000.00"),
                Decimal("1920000.00"),
            ),
            (
                farm3,
                "Pickup Truck Fleet",
                "vehicle",
                Decimal("180000.00"),
                Decimal("145000.00"),
            ),
        ]

        for farm, name, asset_type, purchase, current in assets_data:
            Asset.objects.create(
                farm=farm,
                name=name,
                asset_type=asset_type,
                purchase_date=today - timedelta(days=365 * 2),
                purchase_price=purchase,
                current_value=current,
                description=f"{name} for {farm.name}",
            )

        # Create Wealth Records
        for farm in [farm1, farm2, farm3]:
            total_crop = sum(c.current_value for c in farm.crops.all())
            total_asset = sum(a.current_value for a in farm.assets.all())
            WealthRecord.objects.create(
                farm=farm,
                date=today,
                total_crop_value=total_crop,
                total_asset_value=total_asset,
                total_value=total_crop + total_asset,
                notes=f"Current valuation for {farm.name}",
            )

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully created:\n"
                f"  - 3 Farms\n"
                f"  - {Crop.objects.count()} Crops\n"
                f"  - {Asset.objects.count()} Assets\n"
                f"  - {WealthRecord.objects.count()} Wealth Records"
            )
        )
