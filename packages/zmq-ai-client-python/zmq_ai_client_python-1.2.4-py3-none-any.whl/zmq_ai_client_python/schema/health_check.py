from dataclasses import dataclass


@dataclass
class HealthCheckResponse:
    status: str
    host: str
    worker_count: int
