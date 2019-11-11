# TrainDelay

## 概要

社内Slackに電車の遅延情報を通知します。

## 仕組み

* [電車の運行情報（遅延・運転見合・運休など）を毎朝Slackに通知してみた | Developers.IO](https://dev.classmethod.jp/cloud/aws/notify-slack-train-delay/)
* [Slackで「今の電車の運行情報」を自分だけに教えてくれるSlash commandsを作った | Developers.IO](https://dev.classmethod.jp/cloud/aws/slash-commands-train-delay/)
* [パラメータストアを活用して Lambda で機密情報 (SecureString) を扱う with AWS SAM | Developers.IO](https://dev.classmethod.jp/cloud/aws/secure-string-with-lambda-using-parameter-store/)

## 通知タイミング

毎日、下記時間に通知します。（日本時間）

* AM7時1分から10分毎（AM10時まで18回）
* PM5時1分から10分毎（PM8時まで18回）

情報更新のラグを考慮して、意図的に1分遅れにしています。

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
