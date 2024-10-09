from django.contrib import admin
from .models import engagement_post,engagement_post_content,engagement_post_product_mapping,engagement_post_collection,engagement_post_product,Collection
# Register your models here.
admin.site.register(engagement_post)
admin.site.register(engagement_post_product)
admin.site.register(engagement_post_content)
admin.site.register(engagement_post_collection)
admin.site.register(engagement_post_product_mapping)
admin.site.register(Collection)