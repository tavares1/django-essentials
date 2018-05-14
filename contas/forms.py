from django.forms import ModelForm,DateInput,TextInput,Select,NumberInput,Textarea
from .models import Transacao
#from input_mask.contrib.localflavor.br.widgets import BRDecimalInput

class DateInput(DateInput):
    input_type = 'date'

class TransacaoForm(ModelForm):
    class Meta:
        model = Transacao
        fields = ["descricao","valor","data","categoria","observacoes"]
        widgets = {
 #cl           'valor': BRDecimalInput(attrs={'class':'form-control',}),
            'data' : DateInput(attrs={'class':'form-control'}),
            'descricao': TextInput(attrs= { 'class':'form-control' ,'placeholder':'Descrição da transação'}),
            'categoria': Select(attrs={'class':'form-control'}),
            'observacoes': Textarea(attrs={'class':'form-control'})
        }