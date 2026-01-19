from django.db import models


class Farm(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=300)
    owner = models.CharField(max_length=150)
    total_acreage = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.owner})"

    class Meta:
        ordering = ["-created_at"]


class Crop(models.Model):
    name = models.CharField(max_length=100)
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name="crops")
    planted_date = models.DateField()
    harvest_date = models.DateField(null=True, blank=True)
    expected_yield = models.DecimalField(
        max_digits=10, decimal_places=2, help_text="Expected yield in bushels"
    )
    current_value = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.farm.name}"

    class Meta:
        ordering = ["-planted_date"]


class Asset(models.Model):
    ASSET_TYPES = [
        ("equipment", "Equipment"),
        ("land", "Land"),
        ("livestock", "Livestock"),
        ("building", "Building"),
        ("vehicle", "Vehicle"),
        ("other", "Other"),
    ]

    name = models.CharField(max_length=200)
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE, related_name="assets")
    asset_type = models.CharField(max_length=20, choices=ASSET_TYPES)
    purchase_date = models.DateField(null=True, blank=True)
    purchase_price = models.DecimalField(max_digits=12, decimal_places=2)
    current_value = models.DecimalField(max_digits=12, decimal_places=2)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.get_asset_type_display()})"

    class Meta:
        ordering = ["-current_value"]


class WealthRecord(models.Model):
    farm = models.ForeignKey(
        Farm, on_delete=models.CASCADE, related_name="wealth_records"
    )
    date = models.DateField()
    total_crop_value = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    total_asset_value = models.DecimalField(max_digits=14, decimal_places=2, default=0)
    total_value = models.DecimalField(max_digits=14, decimal_places=2)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.farm.name} - {self.date} - ${self.total_value}"

    class Meta:
        ordering = ["-date"]
        unique_together = ["farm", "date"]
