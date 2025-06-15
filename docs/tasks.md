# Development Tasks

This document breaks down the prototype implementation of **mars** into simple tasks.

1. **Gateway API**: Build a FastAPI app that exposes a `/query` endpoint.
2. **Orchestrator**: Create a class that assembles and runs `TaskEnvelope` objects.
3. **Worker Pool**: Define a worker and runner abstraction. Provide an `EchoRunner` for demo.
4. **CLI**: Implement a small `click` CLI with commands to run the gateway and a demo query.
5. **Data Models**: Share `TaskEnvelope` and `ErrorEnvelope` using Pydantic models.
6. **Demo**: Users can run `python -m mars.cli gateway` and send a query with the `demo` command.
