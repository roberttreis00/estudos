from django import forms
from django.core.mail.message import EmailMessage


class Contato(forms.Form):
    nome = forms.CharField(label='Nome', max_length=50)
    email_remetente = forms.EmailField(label='E-mail Remetente')
    email_destinatario = forms.EmailField(label='E-mail Destinatário')
    assunto = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_email(self):
        nome = self.cleaned_data['nome']
        email_remetente = self.cleaned_data['email_remetente']
        email_destinatario = self.cleaned_data['email_destinatario']
        assunto = self.cleaned_data['assunto']

        mail = EmailMessage(
            subject=f'{nome} Enviou um Email pelo sistema DJANGO TWO',
            body=assunto,
            from_email=email_remetente,
            to=[email_destinatario, ],
            headers={'Reply-To': email_remetente}
        )
        mail.send()
