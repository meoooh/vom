# -*- coding: utf-8 -*-

from django import forms
from vom.models import *
from datetime import date, timedelta

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('contents',)
        widgets = {
            'contents': forms.Textarea(
                    attrs={
                        'placeholder': u'답변',
                        'class': u'form-control',
                    }
                )
        }

class JoinForm(forms.ModelForm):
    password2 = forms.CharField(
            widget=forms.PasswordInput(
                attrs={
                    'placeholder': u'비밀번호(확인)',
                    'class': u'form-control',
                    'required': 'true',
                    'maxlength': 128,
                    'autocomplete': "off"
                },
                render_value = True,
            )
    )

    sex = forms.BooleanField(
            widget=forms.CheckboxInput(
                attrs={
                    'placeholder': u'비밀번호(확인)',
                    'class': u'form-control',
                    'required': 'true',
                    'autocomplete': "off"
                },
            )
    )

    class Meta:
        model = VomUser
        fields = ('email', 'name', 'birthday', 'sex', 'password')
        widgets = {
            'email': forms.TextInput(
                    attrs={
                        'placeholder': u'전자우편',
                        'class': u'form-control',
                        'type':u'email',
                        'required': 'true',
                        'autocomplete': "off"
                    }
                ),
            'name': forms.TextInput(
                    attrs={
                        'placeholder': u'이름',
                        'class': u'form-control',
                        'required': 'true',
                        'autocomplete': "off"
                    }
                ),
            'birthday': forms.DateInput(
                    attrs={
                    'placeholder': u'생일',
                    'class': u'form-control',
                    'type': u'date',
                    'required': 'true',
                    'autocomplete': "off"
                    }
                ),
            'password': forms.PasswordInput(
                    attrs={
                        'placeholder': u'비밀번호',
                        'class': u'form-control',
                        'required': 'true',
                        'autocomplete': "off"
                    },
                    render_value = True
                ),
        }

    def clean_sex(self):
        if 'sex' in self.cleaned_data:
            if self.cleaned_data['sex'] not in (0, 1):
                raise forms.ValidationError(u'남자 또는 여자를 선택해주세요.')
            return self.cleaned_data['sex']
        raise forms.ValidationError(u'필수 항목입니다.')

    def clean_password2(self):
        if 'password2' and 'password' in self.cleaned_data:
            if self.cleaned_data['password'] == self.cleaned_data['password2']:
                return self.cleaned_data['password2']
            raise forms.ValidationError(u'비밀번호가 같지 않습니다.')
        raise forms.ValidationError(u'올바른 비밀번호가 아닙니다.')
