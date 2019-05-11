import requests
import os
import slack


def send_slack(is_test=False):
    client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
    response = client.chat_postMessage(
        channel='GHD8G6RKR',
        text="The ESS Server is Down!" if not is_test else "This is a test message")

def ess_check(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        "OK" if the ESS server is up
        "CRIT" if the server isn't up
    """
    r = requests.get("https://ess.ualberta.ca")

    if "test" in request.args:
        send_slack(is_test=True)
        return "TEST"
    if r.status_code == 200:
        return "OK"
    else:
        send_slack()
        return "CRIT"
