from django.db import models

# Create your models here.

class ShortLink(models.Model):
    slug = models.SlugField(unique=True)  # เช่น 'photoshop2024'
    target_url = models.URLField()        # ลิงก์ปลายทาง (ShrinkMe)
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.slug} -> {self.target_url}"
