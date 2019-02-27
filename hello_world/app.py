import os
import json
import requests


# ここを任意に変更してください。
CHECK_LIST = [
    {
        'name': '中央･総武各駅停車',
        'company': 'JR東日本',
        'website': 'https://traininfo.jreast.co.jp/train_info/kanto.aspx'
    },
    {
        'name': '山手線',
        'company': 'JR東日本',
        'website': 'https://traininfo.jreast.co.jp/train_info/kanto.aspx'
    },
    {
        'name': '湘南新宿ライン',
        'company': 'JR東日本',
        'website': 'https://traininfo.jreast.co.jp/train_info/kanto.aspx'
    },
    {
        'name': '東海道線',
        'company': 'JR東日本',
        'website': 'https://traininfo.jreast.co.jp/train_info/kanto.aspx'
    },
    {
        'name': '横須賀線',
        'company': 'JR東日本',
        'website': 'https://traininfo.jreast.co.jp/train_info/kanto.aspx'
    },
    {
        'name': '横浜線',
        'company': 'JR東日本',
        'website': 'https://traininfo.jreast.co.jp/train_info/kanto.aspx'
    },
    {
        'name': '相模線',
        'company': 'JR東日本',
        'website': 'https://traininfo.jreast.co.jp/train_info/kanto.aspx'
    },
    {
        'name': '南武線',
        'company': 'JR東日本',
        'website': 'https://traininfo.jreast.co.jp/train_info/kanto.aspx'
    },
    {
        'name': '中央線快速電車',
        'company': 'JR東日本',
        'website': 'https://traininfo.jreast.co.jp/train_info/kanto.aspx'
    },
    {
        'name': '中央･総武各駅停車',
        'company': 'JR東日本',
        'website': 'https://traininfo.jreast.co.jp/train_info/kanto.aspx'
    },
    {
        'name': '総武快速線',
        'company': 'JR東日本',
        'website': 'https://traininfo.jreast.co.jp/train_info/kanto.aspx'
    },
    {
        'name': '中央本線',
        'company': 'JR東日本',
        'website': 'https://traininfo.jreast.co.jp/train_info/kanto.aspx'
    },
    {
        'name': '総武本線',
        'company': 'JR東日本',
        'website': 'https://traininfo.jreast.co.jp/train_info/kanto.aspx'
    },
    {
        'name': '青梅線',
        'company': 'JR東日本',
        'website': 'https://traininfo.jreast.co.jp/train_info/kanto.aspx'
    },
    {
        'name': '五日市線',
        'company': 'JR東日本',
        'website': 'https://traininfo.jreast.co.jp/train_info/kanto.aspx'
    },
    {
        'name': '宇都宮線',
        'company': 'JR東日本',
        'website': 'https://traininfo.jreast.co.jp/train_info/kanto.aspx'
    },
    {
        'name': '高崎線',
        'company': 'JR東日本',
        'website': 'https://traininfo.jreast.co.jp/train_info/kanto.aspx'
    },
    {
        'name': '八高線',
        'company': 'JR東日本',
        'website': 'https://traininfo.jreast.co.jp/train_info/kanto.aspx'
    },
    {
        'name': '常磐線快速電車',
        'company': 'JR東日本',
        'website': 'https://traininfo.jreast.co.jp/train_info/kanto.aspx'
    },
    {
        'name': '常磐線各駅停車',
        'company': 'JR東日本',
        'website': 'https://traininfo.jreast.co.jp/train_info/kanto.aspx'
    },
    {
        'name': '京葉線',
        'company': 'JR東日本',
        'website': 'https://traininfo.jreast.co.jp/train_info/kanto.aspx'
    },
    {
        'name': '武蔵野線',
        'company': 'JR東日本',
        'website': 'https://traininfo.jreast.co.jp/train_info/kanto.aspx'
    },
    {
        'name': '京浜東北線',
        'company': 'JR東日本',
        'website': 'https://traininfo.jreast.co.jp/train_info/kanto.aspx'
    },
    {
        'name': '銀座線',
        'company': '東京メトロ',
        'website': 'https://www.tokyometro.jp/unkou/history/ginza.html'
    },
    {
        'name': '丸ノ内線',
        'company': '東京メトロ',
        'website': 'https://www.tokyometro.jp/unkou/history/marunouchi.html'
    },
    {
        'name': '日比谷線',
        'company': '東京メトロ',
        'website': 'https://www.tokyometro.jp/unkou/history/hibiya.html'
    },
    {
        'name': '東西線',
        'company': '東京メトロ',
        'website': 'https://www.tokyometro.jp/unkou/history/touzai.html'
    },
    {
        'name': '千代田線',
        'company': '東京メトロ',
        'website': 'https://www.tokyometro.jp/unkou/history/chiyoda.html'
    },
    {
        'name': '有楽町線',
        'company': '東京メトロ',
        'website': 'https://www.tokyometro.jp/unkou/history/yurakucho.html'
    },
    {
        'name': '半蔵門線',
        'company': '東京メトロ',
        'website': 'https://www.tokyometro.jp/unkou/history/hanzoumon.html'
    },
    {
        'name': '南北線',
        'company': '東京メトロ',
        'website': 'https://www.tokyometro.jp/unkou/history/nanboku.html'
    },
    {
        'name': '副都心線',
        'company': '東京メトロ',
        'website': 'https://www.tokyometro.jp/unkou/history/fukutoshin.html'
    },
    {
        'name': '京成線',
        'company': '京成電鉄',
        'website': 'http://www.keisei.co.jp/info/index.htm'
    },
    {
        'name': '京王電鉄線',
        'company': '京王電鉄',
        'website': 'https://www.keio.co.jp/unkou/unkou_pc.html'
    },
    {
        'name': '浅草線',
        'company': '都営地下鉄',
        'website': 'https://www.kotsu.metro.tokyo.jp/subway/schedule/asakusa.html'
    },
    {
        'name': '三田線',
        'company': '都営地下鉄',
        'website': 'https://www.kotsu.metro.tokyo.jp/subway/schedule/'
    },
    {
        'name': '新宿線',
        'company': '都営地下鉄',
        'website': 'https://www.kotsu.metro.tokyo.jp/subway/schedule/'
    },
    {
        'name': '大江戸線',
        'company': '都営地下鉄',
        'website': 'https://www.kotsu.metro.tokyo.jp/subway/schedule/'
    },
    {
        'name': '小田急線',
        'company': '小田急電鉄',
        'website': 'https://www.odakyu.jp/cgi-bin/user/emg/emergency_bbs.pl'
    },
    {
        'name': 'りんかい線',
        'company': 'りんかい線',
        'website': 'https://service.twr.co.jp/service_info/information.html'
    },
    {
        'name': '京急線',
        'company': '京浜急行電鉄',
        'website': 'https://unkou.keikyu.co.jp/?from=top'
    },
    {
        'name': '東急線',
        'company': '東京急行電鉄',
        'website': 'https://unkou.keikyu.co.jp/?from=top'
    },
    {
        'name': '相鉄線',
        'company': '相模鉄道',
        'website': 'https://www.sotetsu.co.jp/train/move/'
    },
    {
        'name': '押上線',
        'company': '京成電鉄',
        'website': 'http://www.keisei.co.jp/info/index.htm'
    },
    {
        'name': '北総線',
        'company': '京成電鉄',
        'website': 'http://www.keisei.co.jp/info/index.htm'
    },
    {
        'name': '京成本線',
        'company': '京成電鉄',
        'website': 'http://www.keisei.co.jp/info/index.htm'
    },
    {
        'name': 'つくばエクスプレス線',
        'company': 'つくばエクスプレス',
        'website': 'http://www.mir.co.jp/info/'
    },
]

JSON_ADDR = 'https://rti-giken.jp/fhc/api/train_tetsudo/delay.json'

SLACK_WEBHOOK_URL = os.environ['SLACK_WEBHOOK_URL']


def lambda_handler(event, context):

    notify_delays = get_notify_delays()

    if not notify_delays:
        post_slack("電車の遅延はありません。", "")
        return

    # Slack用のメッセージを作成して投げる
    (title, detail) = get_message(notify_delays)
    post_slack(title, detail)

    return


def get_notify_delays():

    current_delays = get_current_delays()

    notify_delays = []

    for delay_item in current_delays:
        for check_item in CHECK_LIST:
            if delay_item['name'] == check_item['name'] and delay_item['company'] == check_item['company']:
                notify_delays.append(check_item)

    return notify_delays


def get_current_delays():
    try:
        res = requests.get(JSON_ADDR)
    except requests.RequestException as e:
        print(e)
        raise e

    if res.status_code == 200:
        return json.loads(res.text)
    return []


def get_message(delays):
    title = "電車の遅延があります。"

    details = []

    for item in delays:
        company = item['company']
        name = item['name']
        website = item['website']
        details.append(f'・{company}： {name}： <{website}|こちら>')

    return title, '\n'.join(details)


def post_slack(title, detail):
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
        response = requests.post(SLACK_WEBHOOK_URL, data=json.dumps(payload))
    except requests.exceptions.RequestException as e:
        print(e)
    else:
        print(response.status_code)
