import openai
import os
from rich.console import Console
from rich.markdown import Markdown
from grept import config, util
import base64


# calls the openai api to generate a response, with either file or embedded context
def answer(client, messages: list[dict], query: str, tokens: int, context=None, file_messages=[]):
    console = Console()
    system_prompt = {
            "role": "system",
            "content": "You are a helpful assistant with following attributes: \
                        extremely succinct, truthful, dont make stuff up, \
                        answer in the context of the provided files.\n"
        }
    
    if context:
        documents = context["documents"][0]
        context_prompt = f"Query: {query}\n\nContext:\n{''.join(documents)}\n"
        messages.append({"role": "user", "content": context_prompt})
        msgs = [system_prompt, *messages]
    else:
        messages.append({"role": "user", "content": query})
        msgs = [system_prompt, *file_messages, *messages]

    try:
        openai.api_key = os.environ["OPENAI_API_KEY"]
    except KeyError:
        util.error("OPENAI_API_KEY not found in environment")
        return []
    
    try:
        response = client.chat.completions.create(
            model=config.COMPLETIONS_MODEL,
            max_tokens=tokens,
            messages=msgs,
        ).choices[0].message.content
    except Exception as e:
        util.error(f"Error generating response: {str(e)}")
        return []

    messages.append({"role": "assistant", "content": response})
    console.print(Markdown(response))
    return messages


def image_answer(client, image, messages: list[dict], tokens: int, query: str):
    console = Console()
    system_prompt = {
        "role": "system",
        "content": [
            {
                "type": "text",
                "text": "Answer the query about the image you are given. \
                        Each query will have an associated image. Be extremely brief and succinct. \
                        Limit responses to a few sentences unless otherwise asked.\n"
            }
        ]
    }   

    messages.append(
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": f"data:image/jpeg;base64,{image}",
                },
                {
                    "type": "text",
                    "text": query,
                },     
            ]
        }
    )
    msgs = [system_prompt, *messages]

    try:
        openai.api_key = os.environ["OPENAI_API_KEY"]
    except KeyError:
        util.error("OPENAI_API_KEY not found in environment")
        return []
    
    try:
        response = client.chat.completions.create(
            model=config.ChatModels.GPT4_VISION.value,
            max_tokens=tokens,
            messages=msgs,
        ).choices[0].message.content
    except Exception as e:
        util.error(f"Error generating response: {str(e)}")
        return []
    
    messages.append({"role": "assistant", "content": response})
    console.print(Markdown(response))
    return messages

    
    