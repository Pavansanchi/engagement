from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .models import engagement_post,engagement_post_collection,engagement_post_product,engagement_post_content,engagement_post_product_mapping
from .serializers import EngagementPostSerializer,CollectionSerializer
from django.db.models import Sum
from .forms import formAdd_product

# Create your views here.


def fetch_posts_and_products(request, tenant_id):
    posts = engagement_post.objects.filter(tenant_id=tenant_id)
    data = []

    for post in posts:
        content = engagement_post_content.objects.filter(post=post).first()
        product_mappings = engagement_post_product_mapping.objects.filter(post=post)
        products = [mapping.product for mapping in product_mappings]

        post_data = {
            'title': post.title,
            'description': post.description,
            'content_url': content.url if content else '',
            'products': [{'name': product.name, 'image': product.image.url, 'sku': product.sku} for product in products]
        }
        data.append(post_data)
   
    return render(request,'index.html',{'data':data})
 
def create_new_product(request):
    if request.method == 'POST':
        form = formAdd_product(request.POST, request.FILES)
        if form.is_valid():
           form.save()
    else:
        form = formAdd_product()
    return render(request, 'addproduct.html', {'form': form})


@api_view(['POST'])
def create_new_collection(request):
    data = request.data
    collection_serializer = CollectionSerializer(data={'name': data.get('name')})
    
    if collection_serializer.is_valid():
        collection = collection_serializer.save()
        post_ids = data.get('post_ids', [])
        duration = data.get('duration', 0)

        for post_id in post_ids:
            engagement_post_collection.objects.create(
                post_id=post_id,
                collection=collection,
                duration_in_seconds=duration
            )
        return Response({'message': 'Collection created', 'collection_id': collection.id})
    return Response(collection_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def top_viewed_posts(request, tenant_id):
    top_posts = engagement_post.objects.filter(tenant_id=tenant_id)\
        .annotate(total_duration_in_seconds=Sum('engagement_post_content'))\
        .order_by('-total_duration_in_seconds')[:5]

    serializer = EngagementPostSerializer(top_posts, many=True)
    
    return Response({'top_posts': serializer.data})


@api_view(['GET'])
def top_viewed_products(request, tenant_id):
    top_products = engagement_post_product.objects.filter(id=tenant_id)\
        .annotate(total_duration_in_seconds=Sum('id'))\
        .order_by('-total_duration_in_seconds')[:5]

    # Prepare the response data
    response_data = []
    for product in top_products:
        response_data.append({
            'product_name': product.name,
            'sku': product.sku,
            'image_url': product.image.url if product.image else None,
            'total_duration_in_hours': round(product.total_duration_in_seconds / 3600, 2) if product.total_duration_in_seconds else 0
        })

    return Response({'top_products':response_data})















