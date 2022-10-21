from django import forms
from .models import ContactForm


class DisplayContactForm(forms.ModelForm):

    class Meta:
        model = ContactForm
        fields = [
            'name',
            'email',
            'phone',
            'product',
            'message',
        ]
        labels = {
            "product": "If your query relates to a product:"
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'add-product-form'
