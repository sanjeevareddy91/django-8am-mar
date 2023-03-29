from django.forms import ModelForm,Form,CharField,ImageField,IntegerField
from .models import Team_Name
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

# from django import forms

class TeamModelForm(ModelForm):
    class Meta:
        model = Team_Name
        fields = "__all__"
        # fields = ('team_name','nick_name')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('team_name', css_class='form-group col-md-6 mb-0'),
                Column('nick_name', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('captain_name', css_class='form-group col-md-6 mb-0'),
                Column('started_year', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('team_logo', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Register')
        )

class TeamNormalForm(Form):
    team_name = CharField(max_length=30)
    nick_name = CharField(max_length=5)
    team_logo = ImageField(required=False)
    captain_name = CharField(max_length=30)
    started_year = IntegerField()

