from django import forms


class BooleanForm (forms.Form):
    techchoices =(
        ("python", "Python"),
        ("react", "React"),
    )
    jobchoices = (
        ("developer", "Developer"),
        ("techlead", "Tech Lead"),
        ("devops", "Dev Ops")
    )
    languagechoices = (
        ("portuguese","Portuguese"),
        ("english", "English"),
        ("spanish", "Spanish")
    )
    levelchoices = (
        ("high","High"),
        ("mid","Medium"),
        ("low","Low"),
    )
    tech = forms.ChoiceField(choices=techchoices)
    job = forms.ChoiceField(choices=jobchoices)
    language = forms.ChoiceField(choices=languagechoices)
    level = forms.ChoiceField(choices=levelchoices)