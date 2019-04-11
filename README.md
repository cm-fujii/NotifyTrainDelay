# TrainDelay

## 概要

社内Slackに電車の遅延情報を通知します。

## 仕組み

* [電車の運行情報（遅延・運転見合・運休など）を毎朝Slackに通知してみた | Developers.IO](https://dev.classmethod.jp/cloud/aws/notify-slack-train-delay/)
* [Slackで「今の電車の運行情報」を自分だけに教えてくれるSlash commandsを作った | Developers.IO](https://dev.classmethod.jp/cloud/aws/slash-commands-train-delay/)

## 通知タイミング

* 毎日
  * AM 8:01
  * AM 8:11
  * AM 8:21
  * AM 8:31
  * AM 8:41
  * AM 8:51

## 通知対象の路線

* [hello_world/target.json](https://github.com/cm-fujii/NotifyTrainDelay/blob/master/hello_world/target.json)

## Slash commands

Slackの任意のチャンネルで下記コマンドを実行します。引数は無しです。

```text
/train
```

## 通知対象の追加

下記どちらかでお願いします。

* 社内Slackチャンネルで依頼
* プルリク
