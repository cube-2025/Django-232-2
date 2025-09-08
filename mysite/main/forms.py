
from django import forms

# class UserForm(forms.Form):
#     char_field = forms.CharField(
#         label = 'Текстовое поле',
#         max_length=100,
#         required=True,
#         help_text='Введите текст (макс 100)'
#     )
#     integer_field = forms.IntegerField(
#         label='Целое число',
#         min_value=0,
#         max_value=100,
#         required=True,
#         help_text='Введите число от 0 до 100'
#     )
#     float_field = forms.FloatField(
#         label='Вещественное число',
#         min_value=0.0,
#         max_value=100.0,
#         required=True,
#         help_text='Введите число от 0 до 100'
#     )
#     boolean_field = forms.BooleanField(
#         label='Флажок',
#         required=True,
#         help_text='Отметьте'
#     )
#     data_field = forms.DateField(
#         label='Дата',
#         input_formats=['%d-%m-%Y'],
#         required=True,
#         help_text='Введи дату'
#     )
#     email_field = forms.EmailField(
#         label='email',
#         max_length =254,
#         help_text='введите почту'
#     )
#     file_field = forms.FileField(
#         label='Файл',
#         required=False,
#         help_text='Выберите файл для загрузки'
#     )
#     image_field = forms.ImageField(
#         label='Фото',
#         required=False,
#         help_text='Выберите фото для загрузки'
#     )
#     CHOICES = [
#         ('option1', 'Вар 1'),
#         ('option2', 'Вар 2'),
#         ('option3', 'Вар 3')
#     ]
#     choice_field = forms.ChoiceField(
#         label='Выбор вариантов',
#         choices=CHOICES,
#         required=True,
#         help_text='Выберите один вариант'
#     )
#     multiple_choice_field = forms.MultipleChoiceField(
#         label='Множественный выбор',
#         choices=CHOICES,
#         required=False,
#         help_text='Выберите несколько вариантов'
#     )
#     radio_select_field = forms.ChoiceField(
#         label='radio',
#         choices=CHOICES,
#         widget=forms.RadioSelect,
#         required=True,
#         help_text='Радиокнопки'
#     )

class UserForm(forms.Form):
    name = forms.CharField(
        label= 'Имя клиента',
        widget = forms.TextInput(attrs={"class":"myfield"})
    )
    age = forms.IntegerField(
        label = "Возраст клиента",
        widget=forms.NumberInput(attrs={"class":"myfield"}))







