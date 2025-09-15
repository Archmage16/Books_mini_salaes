from rest_framework import serializers
from .models import Employer

class EmpSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = ['FIO', 'salary']
    pass