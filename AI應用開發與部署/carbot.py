import json

from flask import Flask, request, abort
import requests

from linebot.v3 import (
    WebhookHandler
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    MessagingApiBlob,
    ReplyMessageRequest,
    TextMessage
)
from linebot.v3.webhooks import (
    MessageEvent,
    ImageMessageContent
)

with open('carbot.json', encoding='utf-8') as f:
    conf = json.load(f)


app = Flask(__name__)

configuration = Configuration(access_token=conf.get('CHANNEL_ACCESS_TOKEN'))
handler = WebhookHandler(conf.get('CHANNEL_SECRET'))


def recognize_plate(
    image: bytes,
    model='gemini-3.5-flash-lite',
    user_id=None
):
    url = conf.get('CAR_API', 'http://127.0.0.1:8080/plate')
    files = {'image': ('test.jpg', image, 'image/jpeg')}
    data = {'model': model, 'user_id': user_id}
    r = requests.post(url, files=files, data=data)
    if r.status_code == 200:
        r_json = r.json()
        show = []
        if 'model' in r_json:
            show.append(f'model: {r_json['model']}')
        if 'user_id' in r_json:
            show.append(f'user_id: {r_json['user_id']}')
        if 'plate' in r_json:
            show.append(f'plate: {r_json['plate']}')
        return '\n'.join(show)

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        app.logger.info("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=ImageMessageContent)
def handle_message(event):
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        line_bot_api_blob = MessagingApiBlob(api_client)
        image = line_bot_api_blob.get_message_content(event.message.id)
        plate = recognize_plate(
            image,
            conf.get('MODEL', 'gemini-3.5-flash-lite'),
            user_id=event.source.user_id
        )

        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[TextMessage(text=plate or 'error')]
            )
        )

if __name__ == "__main__":
    app.run()