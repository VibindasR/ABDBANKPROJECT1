from django import forms

from banking.models import Branch
from credentials.models import Material
from loan.models import Loan


class DateInput(forms.DateInput):
    input_type = 'date'

class RadioSelect(forms.RadioSelect):
    input_type = 'radio'

class CheckboxSelectMultiple(forms.CheckboxSelectMultiple):
    input_type = 'checkbox'



class LoanCreationForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ('first_name','last_name','email','gender','DOB','age','adress','phoneNum','district','branch','materials','account','loan_type')

        materials = forms.ModelMultipleChoiceField(
            queryset=Material.objects.all(),
        )
        widgets ={
            'DOB': DateInput(),
            'gender': RadioSelect(),
            'materials': CheckboxSelectMultiple()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['branch'].queryset = Branch.objects.none()

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['branch'].queryset = Branch.objects.filter(district_id=district_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['branch'].queryset = self.instance.district.branch_set.order_by('name')
