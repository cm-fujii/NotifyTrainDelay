# TrainDelay

## 概要

社内Slackに電車の遅延情報を通知します。

## 仕組み

* [電車の運行情報（遅延・運転見合・運休など）を毎朝Slackに通知してみた | Developers.IO](https://dev.classmethod.jp/cloud/aws/notify-slack-train-delay/)

## 通知タイミング

* 毎日 AM8時

## 通知対象の路線

Lambdaのコードを確認してください。

* hello_world/app.py

## 通知対象の追加

下記どちらかでお願いします。

* 社内Slackチャンネルで依頼
* プルリク
