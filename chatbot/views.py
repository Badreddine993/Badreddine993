from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ChatMessage
from .serializers import ChatMessageSerializer
from .utils import query_model  # Import the query_model function

class ChatbotView(APIView):
    def post(self, request, *args, **kwargs):
        # Get the user message from the request
        user_message = request.data.get("message")
        
        # Get bot response from the AI model using the user_message
        bot_response = self.get_bot_response(user_message)

        # Save the conversation to the database
        chat_message = ChatMessage.objects.create(user_message=user_message, bot_response=bot_response)
        chat_message.save()

        # Serialize the chat message
        serializer = ChatMessageSerializer(chat_message)

        # Return the chatbot response
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_bot_response(self, user_message):
        # Use the query_model function to get the response from the AI model
        try:
            response = query_model(prompt=user_message)
            return response
        except Exception as e:
            return "Sorry, there was an error with the chatbot. Please try again later."
