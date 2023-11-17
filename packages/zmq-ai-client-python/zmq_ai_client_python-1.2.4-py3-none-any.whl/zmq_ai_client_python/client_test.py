import json
from dataclasses import asdict
import uuid

from zmq_ai_client_python.client import LlamaClient
from zmq_ai_client_python.schema.completion import ChatCompletion
from zmq_ai_client_python.schema.request import Message, ChatCompletionRequest, SessionStateRequest
from zmq_ai_client_python.schema.session_state import SessionStateResponse


def main():
    client = LlamaClient('tcp://localhost:5555')
    user_id = str(uuid.uuid4())
    session_id = str(uuid.uuid4())

    messages = [
        Message(role='user', content='What is the capital of france?'),
        Message(role='assistant', content='The capital of France is Paris'),
        Message(role='user', content='Can you tell me about Flask framework?')

    ]
    stop = ["\n###Human"]
    request = ChatCompletionRequest(
        model='gpt-3.5-turbo',
        messages=messages,
        temperature=0.8,
        n=1,
        stop=stop,
        user=user_id,
        key_values={"session": session_id}
    )

    session_request = SessionStateRequest(
        session_id=session_id,
        user_id=user_id
    )

    json_str = json.dumps(asdict(session_request), indent=4)
    print(json_str)

    session_state_response: SessionStateResponse = client.send_session_state_request(session_request)

    json_str = json.dumps(asdict(session_state_response), indent=4)
    print(json_str)

    json_str = json.dumps(asdict(request), indent=4)
    print(json_str)

    chat_response: ChatCompletion = client.send_chat_completion_request(request)

    json_str = json.dumps(asdict(chat_response), indent=4)
    print(json_str)

    title_generation_list = [Message(
        role="system",
        content="You are a helpful assistant. You generate a descriptive, short and meaningful title for the given "
                "conversation.",
    ),
        Message(
            role="user",
            content=f"Question: {messages[-1].content} Answer: {chat_response.choices[0].message.content}"
        )]

    title_request = ChatCompletionRequest(
        messages=title_generation_list,
        temperature=0.5,
        model="vicuna",
        max_tokens=64,
        stop=stop,
    )

    title_response: ChatCompletion = client.send_title_generation_request(title_request)

    json_str = json.dumps(asdict(title_response), indent=4)
    print(json_str)


if __name__ == "__main__":
    main()
