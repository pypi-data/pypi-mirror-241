from hugchat import hugchat
from hugchat.login import Login

class MyChatBot:
    def require_login(self):
        self.login_email = input("Enter your huggingface.co email: ")
        self.login_password = input("Enter your huggingface.co password: ")

    def __init__(self):
        # Call require_login before initializing other attributes
        self.require_login()

        # Log in to huggingface and grant authorization to huggingchat
        self.sign = Login(self.login_email, self.login_password)
        self.cookies = self.sign.login()

    def chat(self, user_input):
        # Create a ChatBot
        chatbot = hugchat.ChatBot(cookies=self.cookies.get_dict())  # or cookie_path="usercookies/<email>.json"
        response = chatbot.chat(user_input)
        return response

    def create_conversation(self):
        # Create a new conversation
        id = chatbot.new_conversation()
        chatbot.change_conversation(id)

    def get_conversation_list(self):
        # Get conversation list
        conversation_list = chatbot.get_conversation_list()

    def switch_model(self, model_index):
        # Switch model (default: meta-llama/Llama-2-70b-chat-hf.)
        chatbot.switch_llm(model_index)
