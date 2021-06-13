
def test_request_healthcheck_returns_200(client):
    """Make request to endpoint healthcheck and returns status 200"""
    assert client.get("/api/healthcheck").status_code == 200
