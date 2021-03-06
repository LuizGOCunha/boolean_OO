from django import forms


class BooleanForm (forms.Form):
    techchoices1 =(
        ("python", "Python"),
        ("react", "React"),
        ("react native","React Native"),
        ("","None")
    )
    techchoices2 =(
        ("python", "Python"),
        ("react", "React"),
        ("react native","React Native"),
        ("","None")
    )
    jobchoices = (
        ("developer", "Developer"),
        ("techlead", "Tech Lead"),
        ("devops", "Dev Ops")
    )
    languagechoices = (
        ("english", "English"),
        ("portuguese","Portuguese"),
        ("spanish", "Spanish")
    )
    levelchoices = (
        ("3","High"),
        ("2","Medium"),
        ("1","Low"),
    )
    tech1 = forms.ChoiceField(choices=techchoices1)
    tech2 = forms.ChoiceField(choices=techchoices2)
    job = forms.ChoiceField(choices=jobchoices)
    language = forms.ChoiceField(choices=languagechoices)
    level = forms.ChoiceField(choices=levelchoices)