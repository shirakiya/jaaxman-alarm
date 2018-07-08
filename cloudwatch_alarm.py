import json
import os

import slackweb

incomming_url = os.environ['SLACK_INCOMMING_URL']
slack = slackweb.Slack(url=incomming_url)


def _send_slack(title, body):
    attachments = [{
        'title': title,
        'pretext': 'CloudWatch Alarm Notification',
        'text': body,
    }]

    slack.notify(username='jaaxman-alarm-handler',
                 attachments=attachments)


def lambda_handler(event, context):
    sns_event = event['Records'][0]['Sns']
    message_json = sns_event['Message']
    message = json.loads(message_json)

    alarm_name = message['AlarmName']
    new_state_reason = message['NewStateReason']

    _send_slack(alarm_name, new_state_reason)
