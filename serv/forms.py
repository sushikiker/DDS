from django import forms
from .models import DDS_record,  category , subcategory

class DDSRecordForm(forms.ModelForm):
    class Meta:
        model = DDS_record
        fields = ['type', 'category', 'subcategory', 'status', 'summ', 'comment']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
       
        

        self.fields['category'].queryset = category.objects.none()
        self.fields['subcategory'].queryset = subcategory.objects.none()


        if 'type' in self.data:
            try:
                type_id = int(self.data.get('type'))
                self.fields['category'].queryset = category.objects.filter(type_id=type_id)
                print(self.data)
            except (ValueError, TypeError):
                pass

        if 'category' in self.data:
            try:
                print(self.data)
                cat_id = int(self.data.get('category'))
                self.fields['subcategory'].queryset = subcategory.objects.filter(category_id=cat_id)
            except (ValueError, TypeError):
                pass
