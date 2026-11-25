# Lab 01: Governed AI Banking Assistant

This companion repository demonstrates how to enforce enterprise identity governance and deterministic policy boundaries in front of an AI assistant backend.

## Architecture Stack
* **Keycloak 24+**: OpenID Connect Identity Provider managing realms, user attributes, groups, and application client roles.
* **Open Policy Agent (OPA)**: Deterministic policy engine rejecting destructive database operations and enforcing transaction approval thresholds.
* **FastAPI Service**: Backend validating RS256 JWT tokens and checking OPA authorization before executing AI tool actions.
* **PostgreSQL**: Production database holding banking invoice records.

## Quick Start

1. Start all infrastructure containers:
```bash
docker-compose up -d
```

2. Access the Keycloak Admin Console:
* URL: `http://localhost:8080`
* User: `admin`
* Password: `AdminSuperSecretPassword123!`

3. Verify OPA policies:
* OPA endpoint: `http://localhost:8181/v1/data/bank/ai/governance`
