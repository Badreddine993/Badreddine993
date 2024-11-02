from rest_framework import serializers
from .models import ChatMessage

class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = ['id', 'user_message', 'bot_response', 'timestamp']

# lets installr rest_framework using pip: pip install djangorestframework