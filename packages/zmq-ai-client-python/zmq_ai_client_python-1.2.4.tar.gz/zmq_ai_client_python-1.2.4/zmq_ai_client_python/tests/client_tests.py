import json
import uuid
from dataclasses import asdict

import pytest

from zmq_ai_client_python.client import LlamaClient
from zmq_ai_client_python.schema.completion import ChatCompletion
from zmq_ai_client_python.schema.health_check import HealthCheckResponse
from zmq_ai_client_python.schema.request import Message, ChatCompletionRequest, SessionStateRequest
from zmq_ai_client_python.schema.session_state import SessionStateResponse


@pytest.fixture
def setup_client():
    host = "tcp://localhost:5555"
    timeout = 15000
    client = LlamaClient(host=host, timeout=timeout)
    return client


@pytest.fixture
def setup_chat_completion_request() -> ChatCompletionRequest:
    session_id = str(uuid.uuid4())
    user_id = str(uuid.uuid4())
    messages = [
        Message(role='system', content='You are a helpful assistant'),
        Message(role='user', content="What is the capital of Turkey?")
    ]
    stop = ["\n ###Human:"]
    return ChatCompletionRequest(
        model='vicuna7b-1.5',
        messages=messages,
        temperature=0.8,
        n=256,
        stop=stop,
        user=user_id,
        key_values={"session": session_id}
    )


@pytest.fixture
def setup_session_state_request() -> SessionStateRequest:
    session_id = str(uuid.uuid4())
    user_id = str(uuid.uuid4())
    return SessionStateRequest(
        session_id=session_id,
        user_id=user_id,
        has_detail=False
    )


@pytest.fixture
def setup_title_generation_request() -> ChatCompletionRequest:
    messages = [
        Message(
            role="system",
            content="You are a helpful assistant. You generate a descriptive, short and meaningful title for the given "
                    "conversation.",
        ),
        Message(
            role="user",
            content=f"Question: What is the capital of France? Answer: The capital of France is Paris"
        )
    ]
    stop = ["\n ###Human:"]
    return ChatCompletionRequest(
        model='vicuna7b-1.5',
        messages=messages,
        temperature=0.8,
        n=256,
        stop=stop,
    )


def print_json(data):
    json_str = json.dumps(asdict(data), indent=4)
    print(json_str)


def test_session_state_request(setup_client, setup_session_state_request):
    try:
        response: SessionStateResponse = setup_client.send_session_state_request(setup_session_state_request)
        assert response.key_values.get("status") == "success"
        print_json(response)
    except TimeoutError as e:
        pytest.fail(str(e))


def test_health_check_request(setup_client):
    try:
        response: HealthCheckResponse = setup_client.send_healthcheck_request()
        assert response is not None, "No health check response received"
        print_json(response)
    except TimeoutError as e:
        pytest.fail(str(e))


def test_chat_completion_request(setup_client, setup_chat_completion_request):
    try:
        response: ChatCompletion = setup_client.send_chat_completion_request(setup_chat_completion_request)
        assert (response.key_values.get("status") == "success")
        print_json(response)
    except TimeoutError as e:
        pytest.fail(str(e))


def test_title_generation_request(setup_client, setup_title_generation_request):
    try:
        response: ChatCompletion = setup_client.send_title_generation_request(setup_title_generation_request)
        assert (response.key_values.get("status") == "success")
        print_json(response)
    except TimeoutError as e:
        pytest.fail(str(e))


if __name__ == "__main__":
    pytest.main()
