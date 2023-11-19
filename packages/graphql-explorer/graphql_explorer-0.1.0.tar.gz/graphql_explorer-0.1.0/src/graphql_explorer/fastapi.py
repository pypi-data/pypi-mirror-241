from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from .templates import APOLLO_SANDBOX_HTML, GRAPHIQL_HTML


router = APIRouter(tags=["GraphQL Router"])

@router.get("/explorer/apollo", name="Apollo Sandbox")
@router.get("/", name="Apollo Sandbox")
async def apollo_sandbox() -> HTMLResponse:
    """Endpoint for ping-pong healthcheck"""
    return HTMLResponse(
        content=APOLLO_SANDBOX_HTML
    )


@router.get("/explorer/graphiql", name="Apollo Sandbox")
async def graphiql() -> HTMLResponse:
    """Endpoint for ping-pong healthcheck"""
    return HTMLResponse(
        content=GRAPHIQL_HTML
    )