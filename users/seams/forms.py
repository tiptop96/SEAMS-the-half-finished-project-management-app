from seams.models import Project, Event
from django import forms

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'info', 'saleDocLink','salePointsCreated','researchDone','internalMeetingCreated']


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'eventtype', 'datetime', 'description']
        widgets = {
          'description': forms.Textarea(),
        }

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['datetime'].widget.attrs['class'] = 'datepicker'

