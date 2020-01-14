from django import forms
import datetime


class CreateNewEmployeeForm(forms.Form):
    employeeCode = forms.CharField(
        widget=forms.TextInput(),   label='Employee Code', required=True, max_length=200)
    firstName = forms.CharField(label='First Name', max_length=120)
    lastName = forms.CharField(label='Last Name', max_length=120)
    birthDate = forms.DateField(label='Birth Date',
                                widget=forms.widgets.DateInput(format="%m/%d/%Y"))
    gender = forms.CharField(label='Gender', max_length=120)
    address = forms.Textarea()
