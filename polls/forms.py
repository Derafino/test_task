from django import forms


class UploadFileForm(forms.Form):
    csv_file = forms.FileField(label='CSV file')
    xml_file = forms.FileField(label='XML file')
