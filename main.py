# main.py
from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.security import OAuth2AuthorizationCodeBearer
from msal import ConfidentialClientApplication
import config

app = FastAPI()

# MSAL Client setup
msal_client = ConfidentialClientApplication(
    client_id=config.CLIENT_ID,
    client_credential=config.CLIENT_SECRET,
    authority=config.AUTHORITY
)

# OAuth2 Authorization flow
oauth2_scheme = OAuth2AuthorizationCodeBearer(
    authorizationUrl=f"{config.AUTHORITY}/oauth2/v2.0/authorize",
    tokenUrl=f"{config.AUTHORITY}/oauth2/v2.0/token"
)

# Redirect to Microsoft login
@app.get("/auth/login")
def login():
    auth_url = msal_client.get_authorization_request_url(
        scopes=config.SCOPE,
        redirect_uri=config.REDIRECT_URI
    )
    return RedirectResponse(auth_url)

# Redirect URI endpoint (callback)
@app.get("/auth/redirect")
async def auth_redirect(code: str):
    # Get token after successful login
    token_response = msal_client.acquire_token_by_authorization_code(
        code=code,
        scopes=config.SCOPE,
        redirect_uri=config.REDIRECT_URI
    )
    if "error" in token_response:
        raise HTTPException(status_code=400, detail=token_response["error_description"])

    # Store user information
    id_token = token_response.get("id_token_claims")
    return JSONResponse(content={"access_token": token_response["access_token"], "id_token": id_token})

# Protected route example
@app.get("/protected")
async def protected_route(token: str = Depends(oauth2_scheme)):
    # Token validation
    auth_result = msal_client.acquire_token_silent(config.SCOPE, account=None)
    if not auth_result:
        raise HTTPException(status_code=401, detail="Authentication failed")
    return {"message": "You are accessing a protected route"}


@app.get("/auth/logout")
def logout():
    logout_url = f"{config.AUTHORITY}/oauth2/v2.0/logout"
    post_logout_redirect_uri = config.POST_LOGOUT_REDIRECT_URI
    redirect_url = f"{logout_url}?post_logout_redirect_uri={post_logout_redirect_uri}"
    return RedirectResponse(redirect_url)