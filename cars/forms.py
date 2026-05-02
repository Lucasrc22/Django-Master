from django import forms
from cars.models import Car, Brand

class CarModelForm(forms.ModelForm): #Form criado em cima do Model, para facilitar a criação de um formulário com os mesmos campos do Model
    class Meta:
        model = Car
        fields = '__all__'
    def clean_value(self): #Método de validação para o campo 'value', é chamado automaticamente quando o formulário é validado, para verificar se o valor do carro é válido
        value = self.cleaned_data.get('value') #Pega o valor do campo 'value' do formulário
        if value < 20000: #Verifica se o valor é menor que 20000, se for, levanta um erro de validação
            raise forms.ValidationError('O valor do carro não pode ser menor que R$ 20.000,00.') #Se for menor que 20000, levanta um erro de validação
        return value #Retorna o valor, caso seja válido
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year') #Pega o valor do campo 'factory_year' do formulário
        if factory_year < 1970: #Verifica se o ano de fabricação é menor que 1970, se for, levanta um erro de validação
            raise forms.ValidationError('O ano de fabricação do carro não pode ser menor que 1970.') #Se for menor que 1970, levanta um erro de validação
        return factory_year #Retorna o ano de fabricação, caso seja válido
    



#Não precisa de save() porque o ModelForm já tem um método save() que salva os dados do formulário no banco de dados, 
# criando um novo objeto Car. Pois dentro da view já tem metodo save()