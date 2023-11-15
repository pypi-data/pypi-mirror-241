import httpx

def http_client(*, base_url: str, token: str) -> httpx.Client:
    """A pre-configured httpx Client.

    Args:
        base_url: base URL of the server
        token: access token for the remote service.
    """
    headers = {"Authorization": f"Bearer {token}", "User-Agent": USER_AGENT}
    return httpx.Client(headers=headers, base_url=base_url, timeout=10.0)