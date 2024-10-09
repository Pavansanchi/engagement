from django.db import models

# Create your models here.

class engagement_post(models.Model):
    tenant_id = models.IntegerField()
    title = models.CharField(max_length=255)
    description = models.TextField()

class engagement_post_content(models.Model):
    post = models.ForeignKey(engagement_post, on_delete=models.CASCADE)
    url = models.URLField(blank=True)

class engagement_post_product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/',blank=True)
    sku = models.CharField(max_length=50)

class engagement_post_product_mapping(models.Model):
    post = models.ForeignKey(engagement_post, on_delete=models.CASCADE)
    product = models.ForeignKey(engagement_post_product, on_delete=models.CASCADE)

class Collection(models.Model):
    name = models.CharField(max_length=255)

class engagement_post_collection(models.Model):
    post = models.ForeignKey(engagement_post, on_delete=models.CASCADE)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    duration_in_seconds = models.IntegerField()
