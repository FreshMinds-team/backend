from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import *


class CustomPatientCreationForm(UserCreationForm):

    class Meta:
        model = Patient
        fields = "__all__"


class CustomPatientChangeForm(UserChangeForm):

    class Meta:
        model = Patient
        fields = "__all__"


class CustomDoctorCreationForm(UserCreationForm):

    class Meta:
        model = Doctor
        fields = "__all__"


class CustomDoctorChangeForm(UserChangeForm):

    class Meta:
        model = Doctor
        fields = "__all__"