from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        label="Nome",
        min_length=3,
        max_length=100,
    )

    email = forms.EmailField(
        label="E-mail",
    )

    subject = forms.CharField(
        label="Assunto",
        min_length=5,
        max_length=150,
    )

    message = forms.CharField(
        label="Mensagem",
        min_length=10,
        max_length=1000,
        widget=forms.Textarea
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        base_classes = (
            "w-full p-2 border border-gray-200 rounded-lg placeholder:text-gray-300 text-blue-800 font-medium "
            "focus:ring-2 focus:ring-cyan-500 "
            "focus:outline-none transition duration-200"
        )

        error_classes = " border-red-500 focus:ring-red-500 "

        placeholders = {
            "name": "Seu nome",
            "email": "Seu e-mail",
            "subject": "Assunto da mensagem",
            "message": "Digite sua mensagem"
        }

        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                "class": base_classes,
                "placeholder": placeholders.get(field_name, "")
            })

            # Se houver erro, aplica estilo vermelho
            if self.errors.get(field_name):
                field.widget.attrs["class"] += error_classes