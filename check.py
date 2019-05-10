import requests

def ess_check(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        "OK" if the ESS server is up
        "CRIT" if the server isn't up
    """
    r = requests.get("https://ess.ualberta.ca")
    if r.status_code == 200:
        return "OK"
    else:
        return "CRIT"