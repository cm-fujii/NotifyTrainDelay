import os
import json
import boto3
import requests

from common_lambda import get_notify_delays, get_message

ssm = boto3.client('ssm')


def lambda_handler(event, context) -> None:

    notify_delays = get_notify_delays()

    if not notify_delays:
        # 遅延が無ければ通知しない
        return

    # Slack用のメッセージを作成して投げる
    (title, detail) = get_message(notify_delays)
    post_slack(title, detail)

    return


def post_slack(title, detail) -> None:
    """SlackにPostする

    Args:
        title: メッセージのタイトル
        detail: メッセージの詳細（遅延情報）

    Returns:

    """
    # https://api.slack.com/incoming-webhooks
    # https://api.slack.com/docs/message-formatting
    # https://api.slack.com/docs/messages/builder
    payload = {
        'attachments': [
            {
                'color': '#36a64f',
                'pretext': title,
                'text': detail
            }
        ]
    }

    # http://requests-docs-ja.readthedocs.io/en/latest/user/quickstart/
    try:
        response = requests.post(get_notify_url(), data=json.dumps(payload))
    except requests.exceptions.RequestException as e:
        print(e)
    else:
        print(response.status_code)


def get_notify_url() -> str:
    # https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ssm.html#SSM.Client.get_parameter
    response = ssm.get_parameter(
        Name='NotifyTrainDelayToSlack-WebhookURL',
        WithDecryption=True
    )
    return response['Parameter']['Value']
