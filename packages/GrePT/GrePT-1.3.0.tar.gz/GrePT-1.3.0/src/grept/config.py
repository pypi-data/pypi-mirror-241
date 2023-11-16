from enum import Enum

class ChatModels(Enum):
    GPT35_16k = "gpt-3.5-turbo-16k"
    GPT35 = "gpt-3.5-turbo"
    GPT4 = "gpt-4"
    GPT4_32K = "gpt-4-32k"
    GPT4_TURBO = "gpt-4-1106-preview"
    GPT4_VISION = "gpt-4-vision-preview"


class EmbeddingModels(Enum):
    ada = "text-embedding-ada-002"


COMPLETIONS_MODEL = ChatModels.GPT4_VISION.value
EMBEDDINGS_MODEL = EmbeddingModels.ada.value

MAX_INPUT_TOKENS = {
    ChatModels.GPT35_16k.value: 16384,
    ChatModels.GPT35.value: 4096,
    ChatModels.GPT4.value: 8192,
    ChatModels.GPT4_32K.value: 32768,
    ChatModels.GPT4_TURBO.value: 128000,
    ChatModels.GPT4_VISION.value: 128000,
}
