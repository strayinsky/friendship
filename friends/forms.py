from django.forms import ModelForm
from django.utils import timezone
from django import forms
from haystack.forms import SearchForm, ModelSearchForm
from haystack.inputs import AutoQuery
from haystack.query import SearchQuerySet
from friends.models import Profile, Activity
from django.forms.models import inlineformset_factory, BaseInlineFormSet


class ActivitiesForm(forms.ModelForm):
    #since i want to override the widget to checkbox, i need to override the entire field
    activities = forms.ModelMultipleChoiceField(queryset=Activity.objects.all(),
                                                widget=forms.CheckboxSelectMultiple(),
                                                required=True)

    class Meta:
        model = Profile
        exclude = ['user', 'likes']
