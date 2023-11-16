from termcolor import cprint
from grept.util import _generate_file_messages, _init_chroma, error
from grept.completions import answer, image_answer
from openai import OpenAI
import base64
import sys


class Chat:
    def __init__(self, messages, tokens, query):
        self.messages = messages
        self.tokens = tokens
        self.init_query = query
        self.client = OpenAI()
    
    def load(self):
        raise NotImplementedError
    
    def refresh(self):
        raise NotImplementedError
    
    def get_answer(self, query):
        raise NotImplementedError
    
    def interact(self):
        print("'exit' or 'quit' to exit, 'clear' to clear chat history")
        while True:
            try:
                query = input("> ")
                if query.lower() in ["exit", "quit"]:
                    break
                if query.lower() == "clear":
                    self.messages = []
                    cprint("Chat history cleared", "green")
                    continue
                if query.lower() == "refresh":
                    self.refresh()
                    continue
                if query == "":
                    continue
                self.messages = self.get_answer(query)
            except KeyboardInterrupt:
                print()
                return
            

class EmbeddingChat(Chat):
    def __init__(self, messages, tokens, query, embedding):
        super().__init__(messages, tokens, query)
        self.embedding = embedding
        self.collection = _init_chroma(self.embedding)

    def get_context(self, query):
        context = self.collection.query(
            query_texts = [query],
            n_results = 3
        )
        return context
    
    def get_answer(self, query):
        context = self.get_context(query)
        return answer(
            self.client,
            self.messages, 
            query, 
            self.tokens, 
            context=context,
        )
    
    def refresh(self):
        cprint("To recompute embeddings call 'grept-embed' from the command line.", "yellow")

class CompletionChat(Chat):
    def __init__(self, messages, tokens, query, file_set):
        super().__init__(messages, tokens, query)
        self.file_set = file_set
        self.file_messages = _generate_file_messages(self.file_set)

    def load(self):
        self.file_messages = _generate_file_messages(self.file_set)

    def get_answer(self, query):
        return answer(
            self.client,
            self.messages, 
            query, 
            self.tokens, 
            file_messages=self.file_messages,
        )
    
    def refresh(self):
        self.messages = []
        self.load()


class ImageChat(Chat):
    def __init__(self, messages, tokens, query, image_path):
        super().__init__(messages, tokens, query)
        self.image_path = image_path
        self.encoded_image = self.base64_encode()

    
    def base64_encode(self):
        try:
            with open(self.image_path, "rb") as f:
                return base64.b64encode(f.read()).decode("utf-8")
        except:
            error("Could not read image file")
            sys.exit(1)

    def get_answer(self, query):
        return image_answer(
            self.client,
            self.encoded_image,
            self.messages,
            self.tokens,
            query,
        )
    
    def refresh(self):
        self.messages = []

    
    
