# zubora-crawler

* イメージのビルド
  * `make build`
* 対象サイトを追加する
  * `make build SPIDER_NAME=saruwaka DOMAIN=saruwakakun.com/life/recipe`
* 特定のspiderを実行する
  * `make run SPIDER_NAME=saruwaka`
* scrapyで特定のURLを試行錯誤
  * `make shell URL=https://saruwakakun.com/life/recipe`

