気まぐれCookPad @cookpad_yade　作成者:RandyGen

twitter: https://twitter.com/cookpad_yade

注）このrepositoryにおいてスクレイピングしたレシピの工程はすべて公開するとデータが多くなってしまい、
一部の公開においても権利等の確認を行っていないのでソースコードのみの公開になります。


内容：
cookpadの運営するWebサイトからレシピの工程をスクレイピングして、
nagisaを用いて形態素解析を行うことでレシピの工程を学習させた新たな文章を生成して、
オリジナルのレシピを作成したのちにそのレシピを一時間に一度自動でtwitterでツイートする

src内容：
・crow.py
　cookpadのWebサイトにアクセスしレシピカテゴリごとに1ページずつURLを取得して、
　レシピの工程に該当する部分のスクレイピングを行いページを移動してを繰り返す。
　スクレイピングで得たレシピの工程はWebサイトURLの一部であるidを名前としたcsvとしてrecipe_dataフォルダ内に保存する

・connect.py
　crow.pyで得たrecipe_dataフォルダ内にあるcsvを1つにまとめたall_recipes.csvに結合する

ここでconnect.pyで得たall_resipes.csvの拡張子をtxtに変更しておく

・naginagi.py
　connect.pyで得たcsvの拡張子をtxtに変更したものを読み込み、形態素解析を行う。
　解析結果はparsed_data.txtとして保存する

・bot.py
　naginagi.pyで得たparsed_data.txtを読み込み文章の生成を行う。
　twitterのツイートの文字数制限に合わせて生成する文章量も調節している

・setting.py
　この一連のソースコードの実行がローカルからなのかサーバからかを判定しサーバの場合は.envの情報をloadするよう処理する
　twitterAPIのKEYもここでサーバに渡している

Githubに公開していなかったのを思い出して簡単にどんなものを記述したREADMEとなりました。
もしかしたら説明書きにも不備があるかもしれないのであしからず...(2021/02/14)


　