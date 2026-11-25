import os
import requests
from fastapi import FastAPI, Depends, HTTPException, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
from jwt import PyJWKClient
from pydantic import BaseModel

app = FastAPI(title="Governed AI Banking Assistant")
security = HTTPBearer()

KEYCLOAK_ISSUER = os.getenv("KEYCLOAK_ISSUER", "http://localhost:8080/realms/bank-realm")
JWKS_URL = f"{KEYCLOAK_ISSUER}/protocol/openid-connect/certs"
OPA_URL = os.getenv("OPA_URL", "http://localhost:8181/v1/data/bank/ai/governance")

jwks_client = PyJWKClient(JWKS_URL)

class AIExecutionRequest(BaseModel):
    action: str
    amount: float = 0.0
    sql_statement_type: str = "SELECT"
    payload: dict = {}

def verify_jwt(credentials: HTTPAuthorizationCredentials = Security(security)) -> dict:
    token = credentials.credentials
    try:
        signing_key = jwks_client.get_signing_key_from_jwt(token)
        return jwt.decode(
            token,
            signing_key.key,
            algorithms=["RS256"],
            audience="account",
            options={"verify_exp": True}
        )
    except Exception as e:
        raise HTTPException(status_code=401, detail=f"Invalid Keycloak token: {str(e)}")

def evaluate_opa_policy(user_claims: dict, request: AIExecutionRequest) -> dict:
    client_roles = (
        user_claims.get("resource_access", {})
        .get("ai-banking-assistant", {})
        .get("roles", [])
    )
    opa_input = {
        "input": {
            "user": {
                "username": user_claims.get("preferred_username"),
                "email": user_claims.get("email"),
                "client_roles": client_roles
            },
            "action": request.action,
            "amount": request.amount,
            "sql_statement_type": request.sql_statement_type
        }
    }
    response = requests.post(OPA_URL, json=opa_input, timeout=3.0)
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Policy engine unavailable")
    return response.json().get("result", {})

@app.post("/api/v1/ai/execute-tool")
async def execute_tool(request: AIExecutionRequest, user_claims: dict = Depends(verify_jwt)):
    decision = evaluate_opa_policy(user_claims, request)
    if decision.get("deny"):
        raise HTTPException(status_code=403, detail="Policy blocks destructive SQL operations.")
    if decision.get("require_human_approval"):
        return {"status": "SUSPENDED", "message": "Transaction requires human sign-off."}
    if not decision.get("is_authorized"):
        raise HTTPException(status_code=403, detail="Insufficient client roles.")
    return {"status": "SUCCESS", "action": request.action}
