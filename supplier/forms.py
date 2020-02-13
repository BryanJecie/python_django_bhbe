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
