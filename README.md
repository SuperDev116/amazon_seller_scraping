# 仕様
MACOSとWindows対応

スクレイピングに加えてWebページのテキストボックへの入力、コンボボックスの選択、Chrome拡張機能からのデータ抽出も含みます。

ジャンルはAmazon物販

エクセル（もしくはスプレッドシート）の商品リスト一覧を一つずつ以下の作業を行います。

・商品をAmazonで検索
・そのページ内で物販元、販売価格、在庫数（拡張機能）、仕入先リスト（拡張機能）、ASINコード等を抽出
・Amazonサイト内でテキストボックスにてASINコードを検索、コンボボックスの値を選択して出た結果を抽出

１．商品名、もしくはASINコードからAmazonのサイトを開く（バックグラウンドのみ切り替えあり）
２．ページからASINコード、価格、販売者、在庫（拡張機能）、画像、他社最安値（拡張機能）など必要な情報を抽出
３．Amazonのセラーページを開いてテキストボックスにASINコードを入力、応答を待って表示されたコンボボックスの値を選択、応答を待って出てきたテキストを抽出

----------------------------------------
keepa

id:postmaster@mh-japan.com
pass:Test123
----------------------------------------
AmazonSellerCentral

メールアドレス：s.jessup.kaieda@gmail.com
パスワード：Test123

商品登録URL
https://sellercentral-japan.amazon.com/product-search?ref=xx_catadd_favb_xx

料金シミュレーター
https://sellercentral-japan.amazon.com/revcal?ref=RC2nonlogin

US Amazon
https://us.amazon.com/
