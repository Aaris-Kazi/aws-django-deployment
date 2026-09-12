from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    dob = serializers.DateField(
        input_formats=["%Y-%m-%d"],
        
    )
    email = serializers.EmailField()
    subject = serializers.CharField(max_length=100)