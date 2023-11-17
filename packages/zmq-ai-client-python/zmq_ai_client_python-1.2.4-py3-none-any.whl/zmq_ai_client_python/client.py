from dataclasses import asdict
from dacite import from_dict


import msgpack
import zmq

from zmq_ai_client_python.schema.completion import (
    ChatCompletion)
from zmq_ai_client_python.schema.health_check import HealthCheckResponse
from zmq_ai_client_python.schema.request import (
    ChatCompletionRequest,
    RequestType,
    SessionStateRequest)
from zmq_ai_client_python.schema.session_state import SessionStateResponse


class LlamaClient:
    """
    LlamaClient is a client class to communicate with a server using ZeroMQ and MessagePack, with a timeout feature.
    """

    def __init__(self, host: str, timeout: int = 360000):
        """
        Initializes the LlamaClient with the given host and an optional timeout.

        :param host: The server host to connect to.
        :param timeout: The receive timeout in milliseconds. Default is 360000ms (6 minutes).
        """
        self.host = host
        self.timeout = timeout
        self.context = zmq.Context()
        self._create_socket()

    def _create_socket(self):
        """ Helper function to create a new socket with the current timeout setting. """
        if hasattr(self, 'socket'):
            self.socket.close()
        self.socket = self.context.socket(zmq.REQ)
        self.socket.setsockopt(zmq.RCVTIMEO, self.timeout)
        self.socket.connect(self.host)

    def _send_request(self, request_type: RequestType, request) -> dict:
        """
        Sends a request to the server and receives a response with a timeout.

        :param request_type: The type of the request.
        :param request: The request object to be sent.
        :return: The unpacked response or raises a timeout exception.
        """
        packed_request = bytes([request_type.value]) + msgpack.packb(asdict(request))
        self.socket.send(packed_request)
        try:
            response = self.socket.recv()
            return msgpack.unpackb(response, raw=False)
        except zmq.Again:
            self._create_socket()
            raise TimeoutError(f"Request timed out after {self.timeout} milliseconds")

    def send_chat_completion_request(self, request: ChatCompletionRequest) -> ChatCompletion:
        """
        Sends a ChatCompletionRequest to the server and receives a ChatCompletion.

        :param request: ChatCompletionRequest.
        :return: ChatCompletion.
        """
        res_dict = self._send_request(RequestType.CHAT_COMPLETION_REQUEST, request)
        chat_completion = from_dict(ChatCompletion, res_dict)
        return chat_completion

    def send_session_state_request(self, request: SessionStateRequest) -> SessionStateResponse:
        """
        Sends a SessionStateRequest to the server and receives a SessionStateResponse.

        :param request: SessionStateRequest.
        :return: SessionStateResponse.
        """
        res_dict = self._send_request(RequestType.SESSION_STATE_REQUEST, request)
        session_state_response = from_dict(SessionStateResponse, res_dict)
        return session_state_response

    def send_title_generation_request(self, request: ChatCompletionRequest) -> ChatCompletion:
        """
        Sends a ChatCompletionRequest to the server and receives a ChatCompletion.
        :param request: ChatCompletionRequest.
        :return: ChatCompletion.
        """
        res_dict = self._send_request(RequestType.TITLE_GENERATION_REQUEST, request)
        chat_completion = from_dict(ChatCompletion, res_dict)
        return chat_completion

    def send_healthcheck_request(self) -> HealthCheckResponse:
        """
        Sends a byte header to the llama server and receives a HealthCheckResponse.
        :return: HealthCheckResponse.
        """
        self.socket.send(bytes([RequestType.HEALTH_CHECK_REQUEST.value]))
        try:
            response = self.socket.recv()
        except zmq.Again:
            self._create_socket()
            raise TimeoutError(f"Request timed out after {self.timeout} milliseconds")
        res_dict = msgpack.unpackb(response, raw=False)
        health_check_response = from_dict(HealthCheckResponse, res_dict)
        return health_check_response
