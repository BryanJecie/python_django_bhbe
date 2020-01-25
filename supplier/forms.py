# from django import forms
# import datetime

# from .models import models, Supplier


# def generate_code():
#     count = Supplier.objects.count()
#     return count


# class NewSupplierForm(forms.Form):

# supplier_code = forms.CharField(
#     max_length=20,
#     widget=forms.TextInput(attrs={"readonly": ""}),
#     required=False,
#     initial=generate_code(),
# )
#     supplier_name = forms.CharField(max_length=20, required=False)
#     supplier_email = forms.EmailField(max_length=20)
#     supplier_phone = forms.CharField(max_length=20, required=False)

#     supplier_address = forms.CharField(
#         max_length=20, widget=forms.Textarea, required=False
#     )

#     class Meta:
#         model = Supplier
#         fields = [
#             "supplier_code",
#             "supplier_name",
#             "supplier_email",
#             "supplier_phone",
#             "supplier_address",
#         ]


from django.forms import ModelForm

from .models import Supplier


class SupplierForm(ModelForm):
    class Meta:
        model = Supplier
        fields = [
            "supplier_code",
            "supplier_name",
            "supplier_email",
            "supplier_phone",
            "supplier_address",
        ]

