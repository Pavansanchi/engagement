from django import forms
from .models import engagement_post_product,engagement_post_content



class formAdd_product(forms.ModelForm):
    class Meta:
        model=engagement_post_product
        fields='__all__'

class formAdd_collection(forms.ModelForm):
    class Meta:
        model=engagement_post_content
        fields='__all__'