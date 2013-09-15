from itertools import chain
from django.dispatch import receiver
from django.forms import ModelForm
from django.utils import timezone
from django import forms
from django.utils.encoding import force_unicode
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
from haystack.forms import SearchForm, ModelSearchForm
from haystack.inputs import AutoQuery
from haystack.query import SearchQuerySet
from friends.models import Profile, Activity
from django.forms.models import inlineformset_factory, BaseInlineFormSet


#custom widget so Activities checkboxes can be organized by group
class ActivitiesByCategory(forms.CheckboxSelectMultiple):
    def render(self, name, value, attrs=None, choices=()):
        if value is None: value = []
        has_id = attrs and 'id' in attrs
        final_attrs = self.build_attrs(attrs, name=name)

        #the div that stores the main output
        output = [u'<div>']

        # Normalize to strings
        str_values = set([force_unicode(v) for v in value])

        categories = Activity.objects.values('group').distinct()
        for category in categories:
            groupname = category['group']
            output.append(u'<h3>%s</h3>' % groupname)
            #div storing choices under each category
            output.append(u'<div>')
            del self.choices
            self.choices = []
            activities = Activity.objects.filter(group=groupname)
            for activity in activities:
                self.choices.append((activity.id, activity.name))
            for i, (option_value, option_label) in enumerate(chain(self.choices, choices)):
                if has_id:
                    final_attrs = dict(final_attrs, id='%s_%s' % (attrs['id'], i))
                    label_for = u' for="%s"' % final_attrs['id']
                else:
                    label_for = ''
                cb = forms.CheckboxInput(final_attrs, check_test=lambda value: value in str_values)
                option_value = force_unicode(option_value)
                rendered_cb = cb.render(name, option_value)
                option_label = conditional_escape(force_unicode(option_label))
                output.append(
                    u'<div class="checkbox"><label%s>%s %s</label></div>' % (label_for, rendered_cb, option_label))
            output.append(u'</div>')
        output.append(u'</div>')
        return mark_safe(u'\n'.join(output))


class ActivitiesForm(forms.ModelForm):
    #since i want to override the widget to checkbox, i need to override the entire field
    activities = forms.ModelMultipleChoiceField(queryset=Activity.objects.all(),
                                                widget=ActivitiesByCategory,
                                                required=True)

    class Meta:
        model = Profile
        exclude = ['user', 'likes']


