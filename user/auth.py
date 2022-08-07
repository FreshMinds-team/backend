from django.contrib.auth.backends import ModelBackend
from .models import *

class DoctorOrPatientBackend(ModelBackend):

    def authenticate(self, *args, **kwargs):
        return self.downcast_user_type(super().authenticate(*args, **kwargs))
        
    def get_user(self, *args, **kwargs):
        return self.downcast_user_type(super().get_user(*args, **kwargs))

    def downcast_user_type(self, user):
        try:
            kit_user = Doctor.objects.get(pk=user.pk)
            return kit_user
        except:
            pass

        try:
            person_user = Patient.objects.get(pk=user.pk)
            return person_user
        except:
            pass

        return user