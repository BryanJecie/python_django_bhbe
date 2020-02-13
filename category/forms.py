from django.forms import ModelForm

from .models import Category, Brand


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ["category_name"]


class BrandForm(ModelForm):
    class Meta:
        model = Brand
        fields = [
            "brand_name",
            "category",
        ]
