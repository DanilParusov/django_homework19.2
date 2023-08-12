from django import forms

from catalog.models import Product, Version

class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'price', 'category')



    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        stop_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        if cleaned_data in stop_list:
            raise forms.ValidationError('Запрещенный продукт')


class VersionForm(forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'


