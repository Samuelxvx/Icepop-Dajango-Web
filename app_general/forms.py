from django import forms
from app_icepops.models import Icepop
from .models import Subscription

class IcepopMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.title

class SubscriptionForm(forms.Form):
    name = forms.CharField(max_length=60, required=True, label="Name") 
    email = forms.CharField(max_length=60, required=True, label="Email") 
    icepop_set = IcepopMultipleChoiceField(
        queryset=Icepop.objects.order_by('-is_premium'),
        required = True,
        label = 'menu',
        widget = forms.CheckboxSelectMultiple
    )
    accepted = forms.BooleanField(required=True, label='water that is water tooo much water')
        
class SubscriptionModelForm(forms.ModelForm):
    icepop_set = IcepopMultipleChoiceField(
        queryset=Icepop.objects.order_by('-is_premium'),
        required = True,
        label = 'menu',
        widget = forms.CheckboxSelectMultiple
    )
    accepted = forms.BooleanField(required=True, label='water that is water tooo much water')

    class Meta:
        model = Subscription
        fields = ['name' , 'email', 'icepop_set','accepted']
        labels = {
            'name': 'Name',
            'email': 'Email',
            'icepop_set': 'Menu'
        }