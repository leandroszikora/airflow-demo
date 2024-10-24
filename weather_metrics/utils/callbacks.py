from gc import callbacks
from typing import Callable, Dict, Any

from airflow.providers.slack.hooks.slack import SlackHook


def send_slack_notification(channel: str, message: str) -> Callable[[Dict[str, Any]], None]:
    """
    Callback used to send a message to Slack channel.

    :param channel: Slack channel name
    :param message: Message to send
    """

    def callback(context: Dict[str, Any]) -> None:
        hook = SlackHook(
            slack_conn_id="slack_demo"
        )

        body = {
            "channel": channel,
            "username": "Airflow",
            "text": message,
            "icon_url": "https://raw.githubusercontent.com/apache/airflow/2.5.0/airflow/www/static/pin_100.png"
        }

        hook.call("chat.postMessage", json=body)

    return callback