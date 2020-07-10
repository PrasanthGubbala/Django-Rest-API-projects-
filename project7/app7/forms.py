import re
from django import forms
from app7.models import Course,Faculty,Student

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

    def clean_fee(self):
        fee = self.cleaned_data['fee']
        if fee>=3000:
            return fee
        else:
            return forms.ValidationError('Fee Must Be Grater Than 3000 Rupees')
    def clean_name(self):
        name = self.cleaned_data['name']
        res = re.findall(r'^[A-Z a-z]*$',name)
        if res:
            return res
        else:
            raise forms.ValidationError('Invalid Name-It Will Accept Only A-Z and a-z Alphabets Only')

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class FacultyForm(forms.ModelForm):
    class Meta:
        model = Faculty
        fields = '__all__'
