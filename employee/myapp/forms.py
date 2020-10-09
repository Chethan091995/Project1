from django import forms
from myapp.models import Employ,Position



class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employ
        fields= "__all__"
        labels = {
            'Fullname' : 'Full Name',
            " emp_code" : "Employee Code",
            "post" : "Position"
        }

    def __init__(self,*args,**kwargs):
        super(EmployeeForm,self).__init__(*args,**kwargs)
        self.fields['post'].empty_label = "Select"