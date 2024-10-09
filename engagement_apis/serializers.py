from rest_framework import serializers

from .models import engagement_post,engagement_post_content,engagement_post_product,engagement_post_collection,engagement_post_product_mapping,Collection


class EngagementPostContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = engagement_post_content
        fields = ['url']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = engagement_post_product
        fields = ['name', 'image', 'sku']


class EngagementPostSerializer(serializers.ModelSerializer):
    content_url = serializers.SerializerMethodField()
    products = serializers.SerializerMethodField()

    class Meta:
        model = engagement_post
        fields = ['id', 'tenant_id', 'title', 'description', 'content_url', 'products']

    def get_content_url(self, obj):
        content = engagement_post_content.objects.filter(post=obj).first()
        return content.url if content else None

    def get_products(self, obj):
        product_mappings = engagement_post_product_mapping.objects.filter(post=obj)
        return ProductSerializer([mapping.product for mapping in product_mappings], many=True).data


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'name']


class EngagementPostCollectionSerializer(serializers.ModelSerializer):
    post = EngagementPostSerializer()
    collection = CollectionSerializer()

    class Meta:
        model = engagement_post_collection
        fields = ['post', 'collection', 'duration_in_seconds']
