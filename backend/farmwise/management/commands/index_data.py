from django.core.management.base import BaseCommand
from farmwise.models import Farm, Crop, Asset
from farmwise.services.rag import get_vectorstore
from langchain_core.documents import Document


class Command(BaseCommand):
    help = "Index farm data into ChromaDB"

    def handle(self, *args, **kwargs):
        docs = []

        # Index Farms
        for farm in Farm.objects.all():
            content = f"FARM: {farm.name}\nOwner: {farm.owner}\nLocation: {farm.location}\nAcres: {farm.total_acreage}"
            docs.append(
                Document(
                    page_content=content, metadata={"source": "farm", "id": farm.id}
                )
            )

        # Index Crops
        for crop in Crop.objects.all():
            content = f"CROP: {crop.name}\nFarm: {crop.farm.name}\nPlanted: {crop.planted_date}\nYield: {crop.expected_yield}"
            docs.append(
                Document(
                    page_content=content, metadata={"source": "crop", "id": crop.id}
                )
            )

        # Index Assets
        for asset in Asset.objects.all():
            content = f"ASSET: {asset.name} ({asset.get_asset_type_display()})\nFarm: {asset.farm.name}\nValue: ${asset.current_value}"
            docs.append(
                Document(
                    page_content=content, metadata={"source": "asset", "id": asset.id}
                )
            )
        if docs:
            vectorstore = get_vectorstore()
            vectorstore.add_documents(docs)
            self.stdout.write(
                self.style.SUCCESS(f"Successfully indexed {len(docs)} documents")
            )
        else:
            self.stdout.write(self.style.WARNING("No data found to index"))
