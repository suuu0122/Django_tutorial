# Django_tutorial

## [プロジェクトの作成](https://docs.djangoproject.com/ja/4.2/intro/tutorial01/#creating-a-project)
* プロジェクトを作成するには以下のコマンドを実行する.
	```zsh
	django-admin startproject [project_name]
	```
	* 上記コマンドを実行すると、`project_name`ディレクトリが作成される.
* 作成されるディレクトリ構造
	```zsh
	project_name/
		manage.py
		project_name/
			__init__.py
			settings.py
			urls.py
			asgi.py
			wsgi.py
	```
	* `project_name/`（ルートディレクトリ）
		* プロジェクトのコンテナ.
	* `manage.py`
		* プロジェクトに対する様々な操作を行うためのコマンドラインユーティリティ.
	* `project_name/project_name/`
		* プロジェクトの実際のPythonパッケージ.
		* importの際に使用する名前（`import project_name.urls`）.
	* `project_name/project_name/__init__.py`
		* ディレクトリがPythonパッケージであることをPythonに知らせるためのからのファイル.
	* `project_name/project_name/settings.py`
		* プロジェクトの設定ファイル.
		* [Djangoの設定](https://docs.djangoproject.com/ja/4.2/topics/settings/)
	* `project_name/project_name/urls.py`
		* プロジェクトのURL宣言.
		* Djangoサイトにおける「目次」に相当する.
		* [URLディスパッチャ](https://docs.djangoproject.com/ja/4.2/topics/http/urls/)
	* `project_name/project_name/asgi.py`
		* プロジェクトを提供するASGI互換Webサーバのエントリポイント.
		* [How to deploy with ASGI](https://docs.djangoproject.com/ja/4.2/howto/deployment/asgi/)
	* `project_name/project_name/wsgi.py`
		* プロジェクトをサーブするためのWSGI互換Webサーバとのエントリーポイント.
		* [WSGIとともにデプロイするには](https://docs.djangoproject.com/ja/4.2/howto/deployment/wsgi/)
<br />

## [開発用サーバ](https://docs.djangoproject.com/ja/4.2/intro/tutorial01/#the-development-server)
* Django開発サーバを起動するには、`manege.py`が直下にあるディレクトリに移動し、下記のコマンドを実行する.
	```zsh
	python manage.py runserver
	```
* Django開発サーバは、Pythonだけで書かれた軽量なWebサーバであり、開発を迅速に行い、運用に適した状態になるまで`Apache`のような運用サーバの設定をいじらずに済むようにするためのものである.
* Django開発サーバが正しく起動している場合、ブラウザで[ http://127.0.0.1:8000/](http://127.0.0.1:8000/)にアクセスできる.
* ポート番号の変更
	* デフォルトでは内部IPのポート8000で起動する.
	* 変更したい場合は下記のコマンドのように引数として、ポート番号を引数として渡す.
	```zsh
	python manage.py runserver [ポート番号]
	```
* `runserver`の自動リロード
	* 開発サーバーは必要に応じてリクエストごとにPythonコードを自動的にリロードする.
	* コード変更の効果を得るためにサーバーを再起動する必要はない.
	* ファイルの追加のようないくつかの行動は再起動をトリガーせず、このような場合はサーバーを再起動する必要がある.
<br />

## [アプリケーションの作成](https://docs.djangoproject.com/ja/4.2/intro/tutorial01/#creating-the-polls-app)
* プロジェクトとアプリケーションの違い
	* アプリケーションは、ブログシステム、公的記録のデータベース、小規模な投票アプリなど、何かを行うWebアプリケーションである.
	* プロジェクトは、特定のウェブサイトの構成とアプリケーションのコレクションである.
	* プロジェクトは複数のアプリケーションを含めることができ、アプリケーションは複数のプロジェクトに存在することができる.
* アプリケーションの作成
	* アプリケーションを作成するには、`manege.py`が直下にあるディレクトリに移動し、下記のコマンドを実行する.
		```zsh
		python manage.py starapp [app_name]
		```
	* 作成されるディレクトリ構造
		```zsh
		app_name/
			__init__.py
			admin.py
			apps.py
			migrations/
				__init__.py
			models.py
			tests.py
			views.py
		```
<br />

## [Databaseの設定](https://docs.djangoproject.com/ja/4.2/intro/tutorial02/#database-setup)
* デフォルトの設定では、`SQLite`を使用する.
* `SQLite`以外のデータベースを使用した場合、適切な[データベースのバインディング](https://docs.djangoproject.com/ja/4.2/topics/install/#database-installation)をインストールして、設定ファイル（`project_name/project_name/settings.py`）の`DATABASES`の`default`項目内の以下のキーをデータベースの接続設定に合うように変更する.
	* `ENGINE`
		* `django.db.backends.sqlite3`、`django.db.backends.postgresql`、`django.db.backends.mysql`、`django.db.backends.oracle`のいずれかにする.
		* [他のデータベース](https://docs.djangoproject.com/ja/4.2/ref/databases/#third-party-notes)も利用可能である.
	* `NAME`
		* データベースの`NAME`である.
		* `SQLite`を使用している場合、データベースはコンピュータ上のファイルになる. デフォルト値の`BASE_DIR / 'db.sqlite3'`は、プロジェクトディレクトリにファイルを保存する.
	* [`SQLite`以外を使用する場合は、`USER`や`PASSWORD`、`HOST`などの追加設定を加える必要がある.](https://docs.djangoproject.com/ja/4.2/ref/settings/#std-setting-DATABASES)
* `TIME_ZONE`
	* `project_name/project_name/settings.py`を編集する際、`TIME_ZONE`に[自分のタイムゾーン](https://kuma-server.com/timezone_settings/#toc3)も設定する.
* `INSTALLED_APPS`
	* Djangoインスタンスの中で有効化されているすべてのDjangoアプリケーションの名前を保持している.
	* アプリケーションは、複数のプロジェクトによって使用されることもできるし、他の開発者が自身のプロジェクトで使用するためにパッケージして配布することもできる.
	* デフォルト
		* [django.contrib.admin](https://docs.djangoproject.com/ja/4.2/ref/contrib/admin/#module-django.contrib.admin)
			* 管理（admin）サイト.
		* [django.contrib.auth](https://docs.djangoproject.com/ja/4.2/topics/auth/#user-authentication-in-django)
			* 認証システム.
		* [django.contrib.contenttypes](https://docs.djangoproject.com/ja/4.2/ref/contrib/contenttypes/#module-django.contrib.contenttypes)
			* コンテンツタイプフレームワーク
		* [django.contrib.sessions](https://docs.djangoproject.com/ja/4.2/topics/http/sessions/#module-django.contrib.sessions)
			* セッションフレームワーク
		* [django.contrib.messages](https://docs.djangoproject.com/ja/4.2/ref/contrib/messages/#module-django.contrib.messages)
			* メッセージフレームワーク
		* [django.contrib.staticfiles](https://docs.djangoproject.com/ja/4.2/ref/contrib/staticfiles/#module-django.contrib.staticfiles)
			* 静的ファイルの管理フレームワーク
* テーブルの作成
	* データベースにテーブルを作成するには、以下のコマンドを実行する.
		```zsh
		python manage.py migrate
		```
	* `migrate`コマンドは、`INSTALLED_APPS`の設定を参照するとともに、`project_name/project_name/settings.py`ファイルのデータベース設定に従って必要なすべてのデータベースのテーブルを作成する.
<br />

## [モデルの作成](https://docs.djangoproject.com/ja/4.2/intro/tutorial02/#creating-models)
* モデルは、データベースのレイアウトと、それに付随するメタデータである.
* 設計思想
	* モデルは、手持ちのデータに対する唯一無二の決定的なソースである.
	* モデルには、格納したいデータのフィールドと、そのデータの挙動を記述する.
	* Djangoのモデルの目的は、ただ一つの場所でデータモデルを定義し、そこから自動的にデータを取り出すことにある. クラスとして定義する.
	* これらはマイグレーションを含み、Ruby on Railsと異なり、マイグレーションは完全にデータモデルのファイルから生成される.
	* マイグレーションは、本質的には単なる履歴である.
	* Djangoは、データベーススキーマをアップデートしながら履歴を進んでいき、現在のモデルに合致させることができる.
* モデルは、`project_name/app_name/models.py`にクラスとして定義する. クラスは、[`django.db.models.Model`](https://docs.djangoproject.com/ja/4.2/ref/models/instances/#django.db.models.Model)のサブクラスとして定義する. 各モデルには複数のクラス変数があり、個々のクラス変数はモデルのデータベースフィールドを表現する. 
* 各フィールドは、[`Field`](https://docs.djangoproject.com/ja/4.2/ref/models/fields/#django.db.models.Field)クラスのインスタンスとして表現されています。例えば、[`CharField`](https://docs.djangoproject.com/ja/4.2/ref/models/fields/#django.db.models.CharField)は文字のフィールドで、[`DateTimeField`](https://docs.djangoproject.com/ja/4.2/ref/models/fields/#django.db.models.DateTimeField)は日時フィールドである. こうしたクラスは、各フィールドにどのようなデータ型を記憶させるかをDjangoに伝える.
* `Field`クラスの中には、必須の引数を持つものがある. 例えば、`CharField`には`max_length`を指定する必要がある. この引数はデータベーススキーマで使われる他、バリデーションでも使われる.
* リレーションシップは、[`ForeignKey`](https://docs.djangoproject.com/ja/4.2/ref/models/fields/#django.db.models.ForeignKey)を使用して定義する. Djangoは、多対一、多対多、そして一対一のような一般的なデータベースリレーションシップすべてをサポートする.
<br />

## [モデルの有効化](https://docs.djangoproject.com/ja/4.2/intro/tutorial02/#activating-models)
* アプリケーションをプロジェクトに含めるには、構成クラスの参照を`INSTALLED_APPS`設定に追加する必要がある. `project_name/project_name/settings.py`の`INSTALLED_APPS`に、`project_name/app_name/apps.py`で定義されているクラスを追加する.
	```python
	INSTALLED_APPS = [
    	"<app_name>.apps.<app_name>Config",
    	"django.contrib.admin",
    	"django.contrib.auth",
    	"django.contrib.contenttypes",
    	"django.contrib.sessions",
    	"django.contrib.messages",
    	"django.contrib.staticfiles",
	]
	```
* `makemigrations`を実行することで、Djangoにモデルに変更があったことを伝え、その変更をマイグレーションの形で保存することができる. モデルの作成や変更を行なった時には以下のコマンドを実行する.
	```zsh
	python manage.py makemigrations [app_name]
	```
* マイグレーションは、Djangoがモデルやデータベーススキーマの変更を保存する方法である. マイグレーションは、ディスク上のただのファイルである. 望むならば、新しいモデルのためのマイグレーションをファイル`polls/migrations/0001_initial.py`から読むこともできる. Django がマイグレーションのファイルを作成するたびにそれを毎回読む必要はないが、Djangoが行う変更を手動で微調整したいというときのために、マイグレーションは設計されてる.
* Djangoには、マイグレーションを自分の代わりに実行し、自動でデータベーススキーマを管理するためのコマンドがある. これは、`migrate`呼ばれるコマンドである.
* マイグレーションがどんなSQLを実行するのか見たい場合は、`sqlmigrate`コマンドを使用する. このコマンドは、マイグレーションの名前を引数にとってSQLを返す.
	```zsh
	python manage.py sqlmigrate [app_name] 0001
	```
* モデルの変更を実施するための3ステップガイド
	* `project_name/app_name/models.py`の中のモデルを変更する.
	* これらの変更のためのマイグレーションを作成するために、`python manage.py makemigrations`を実行する.
	* データベースにこれらの変更を適用するために、`python manage.py migrate`を実行する.
* マイグレーションの作成と適用のコマンドが分割されている理由は、マイグレーションをバージョン管理システムにコミットし、アプリケーションとともに配布するためである. これによって、自分の開発が容易になるだけでなく、他の開発者や本番環境にとって使いやすいものになる.
<br />

## [Django Admin](https://docs.djangoproject.com/ja/4.2/intro/tutorial02/#introducing-the-django-admin)
* 設計思想
	* Djangoは、コンテンツ追加、変更そして削除のための管理サイトの生成を完全に自動化している.
	* サイト管理者は、新たな話題やイベント、 スポーツのスコアなどの入力にシステムを使い、コンテンツは公開用サイト上で表示される. Djangoは、サイト管理者向けの一元化されたコンテンツ編集インタフェースを提供している.
	* `admin`は、サイトの訪問者ではなく、サイト管理者に使用されることを意図している.
* 管理ユーザーの作成
	* `admin`サイトにログインできるユーザを作成するには下記コマンドを実行する.
		```zsh
		python manage.py createsuperuser
		```
		* `Username`、`Email address`、`Password`を入力する.
* `admin`サイト
	* `python manage.py runserver`で開発サーバを起動して`/admin`に接続し、管理ユーザの作成で設定した`Username`と`Password`を使用することで、`admin`サイトにアクセスすることができる.
	* `groups`、`user`などが編集可能で、これらは[`django.contrib.auth`](https://docs.djangoproject.com/ja/4.2/topics/auth/#module-django.contrib.auth)によって提供されている.
	* `admin`サイトでアプリケーションのモデルを編集可能にするためには、`project_name/app_name/admin.py`に下記のようなコードを記述する.
		```python
		from django.contrib import admin

		from .models import <model_class_name>


		admin.site.register(<model_class_name>)
		```
<br />

## [ビュー](https://docs.djangoproject.com/ja/4.2/intro/tutorial03/#overview)
* ビューとは、Djangoのアプリケーションにおいて特定の機能を提供するWebページの「型（type）」であり、各々テンプレートを持っている.
* ブログアプリケーションでの例
	* ホームページ. 最新エントリーをいくつか表示.
	* エントリー詳細ページ. 1エントリーへのパーマリンクページ. パーマリンクとは、ウェブサイトの各ページに対して個別に与えられているURLのこと.
	* 年ごとのアーカイブページ. 指定された年のエントリーの月をすべて表示.
	* 月ごとのアーカイブページ. 指定された月のエントリーの日をすべて表示.
	* 日ごとのアーカイブページ. 指定された日のすべてのエントリーを表示.
	* コメント投稿、エントリーに対するコメントの投稿を受け付け.
* Djangoでは、ウェブページとコンテンツはビューによって提供される. 各ビューは、Python関数（クラスベースビューの場合はメソッド）として実装される. Djangoは、ビューをリクエストされたURL（ドメイン以降の部分）から決定する.
* Djangoは、URLからビューを取得するために`URLconf`と呼ばれているものを使用する. `URLconf`は、URLパターンをビューにマッピングする.
* `<>`の使用
	* 例えば、`detail(request=<HttpRequest object>, question_id=34)`のような関数を考える. `question_id=34`の部分は、`project_name/app_name/urls.py`で指定するURLパターン中の`path()`で指定する`<int:question_id>`から来る.
	* `<>`を使用すると、URLの一部がキャプチャされ、キーワード引数としてビュー関数に送信する. `<int:question_id>`を考えると、`:question_id`は一致するパターンを識別するために使用される名前を定義し、`int`部分はURLパスのこの部分に一致するパターンを決定するコンバータである. `:`はコンバータとパターン名を区切る.
<br />

## テンプレート
* テンプレートを使用することで、Pythonからデザインを分離する.
* デフォルトの設定ファイルでは、`DjangoTemplates`バックエンドが設定されており、その`APP_DIRS`のオプションが`True`になっている.規約により、`DjangoTemplates`は`INSTALLED_APPS`のそれぞれの`templates`サブディレクトリを検索する.
* したがって、そのアプリに関するテンプレートは、`project_name/app_name/templates/app_name/xxx.html`に記述する必要がある.
* テンプレートの名前空間
	* `app_name`というサブディレクトリを作成せず、`project_name/app_name/templates/xxx.html`と直接`templates`ディレクトリの中にテンプレートを作成するのは良くない.
	* Djangoは、名前がマッチした最初のテンプレートを使用するので、もし異なるアプリケーションの中に同じ名前のテンプレートがあった場合、Djangoはそれらを区別することができない.
	* 上記を防ぐための一番簡単な方法は、テンプレートに **名前空間** を与えることである. そのため、アプリケーションと同じ名前を付けたサブディレクトリの中にテンプレートを置くのが良い.
<br />

## [レンダリング](https://docs.djangoproject.com/ja/4.2/intro/tutorial03/#a-shortcut-render)
* テンプレートをロードしてコンテキストを値に入れ、テンプレートをレンダリングした結果を`HttpResponse`オブジェクトで返すという方法は非常によく使用されるので、Djangoはショートカットとして[`render()`](https://docs.djangoproject.com/ja/4.2/topics/http/shortcuts/#django.shortcuts.render)を提供している.
* `render()`は、第1引数としてrequestオブジェクト、第2引数としてテンプレート名、第3引数（任意）として辞書を受け取る. `render()`は、テンプレートを指定のコンテキストでレンダリングし、その`HttpResponse`オブジェクトを返す.
* すべてのビューを`render()`で書き換えることで、`loader`や`HttpResponse`を`import`する必要はなくなる.
<br />

## [404エラーの検出](https://docs.djangoproject.com/ja/4.2/intro/tutorial03/#raising-a-404-error)
* `get()`を実行してオブジェクトが存在しない場合には、`Http404`を返すという方法は非常によく使用されるので、Djangoはショートカットとして[`get_object_or_404()`](https://docs.djangoproject.com/ja/4.2/topics/http/shortcuts/#django.shortcuts.get_object_or_404)を提供している.
* `get_object_or_404()`は、第1引数としてDjangoモデル、任意の数のキーワード引数を受け取り、モデルのマネージャの[`get()`](https://docs.djangoproject.com/ja/4.2/ref/models/querysets/#get)に渡す. オブジェクトが存在しない場合は、`Http404`を発生させる.
	```python
	# get_object_or_404()を使用しない場合
	from django.http import Http404
	try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

	# get_object_or_404()を使用
	from django.shortcuts import get_object_or_404
	question = get_object_or_404(Question, pk=question_id)
	```
* [`get_list_or_404()`](https://docs.djangoproject.com/ja/4.2/topics/http/shortcuts/#django.shortcuts.get_list_or_404)という関数もある. この関数は`get_object_or_404()`と同じように動くが、`get()`ではなく、[`filter()`](https://docs.djangoproject.com/ja/4.2/ref/models/querysets/#django.db.models.query.QuerySet.filter)を使用する. リストが空の場合は`Http404`を返す.
<br />

## [テンプレート内URLのハードコーディングを避ける](https://docs.djangoproject.com/ja/4.2/intro/tutorial03/#removing-hardcoded-urls-in-templates)
* テンプレート内でURLをハードコーディングしていると、URLの変更が困難になるので、テンプレートタグの`{% url %}`を使用する.
* `{% url %}`は、`project_name/app_name/urls.py`に指定されたURLの定義を検索する. URLを変更する場合は、テンプレート内で`{% url %}`を使用しハードコーディングを避けていれば、`project_name/app_name/urls.py`を変更するだけで良い.
<br />

## [URLの名前空間](https://docs.djangoproject.com/ja/4.2/intro/tutorial03/#namespacing-url-names)
* Djangoプロジェクトが複数のアプリケーションを含む場合、これらの間の同URL名を区別するには、`URLconf`に名前空間を追加すればよい.
* `prject_name/app_name/urls.py`に`app_name`を追加する.
	```python
	from django.urls import path
	
	from . import views


	app_name = "polls" # この1行を追加
	urlpatterns = [
    	path("", views.index, name="index"),
    	path("<int:question_id>/", views.detail, name="detail"),
    	path("<int:question_id>/results/", views.results, name="results"),
    	path("<int:question_id>/vote/", views.vote, name="vote"),
	]
	```
* 上記に合わせてテンプレート内のURLも変更する.
	* 変更前
		```html
		<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
		```
	* 変更後
		```html
		<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
		```
<br />

## [フォーム](https://docs.djangoproject.com/ja/4.2/intro/tutorial04/#write-a-minimal-form)
* サーバ側のデータを更新するフォームを作成する場合は、`method="post"`（`method="get"`ではなく）を使用する.
* 自サイト内をURLに指定したPOSTフォームにはすべて、[`{% csrf_token %}`](https://docs.djangoproject.com/ja/4.2/ref/templates/builtins/#std-templatetag-csrf_token)テンプレートタグを使用する. このテンプレートタグを使用することで、CSRFを防止することができる.
* [CSRF（クロスサイトリクエストフォージェリ）](https://www.trendmicro.com/ja_jp/security-intelligence/research-reports/threat-solution/csrf.html)
	* 概要
		* 掲示板や問い合わせフォームなどを処理するWebアプリケーションが、本来拒否すべき他サイトからのリクエストを受信し処理してしまう.
	* 攻撃手法
		* 攻撃者は攻撃用Webページを準備し、ユーザがアクセスするように誘導する.
		* ユーザが攻撃用Webページにアクセスすると、攻撃用Webページ内にあらかじめ用意されていた不正なリクエストが攻撃対象サーバに送られる.
		* 攻撃サーバ上のWebアプリケーションは不正なリクエストを処理し、ユーザが意図していない処理が行われる.
	* 対策
		* Webアプリケーションをサイト外からのリクエストを受信、処理しないようにシステムを構築する.
		* 攻撃者に推測されにくい任意の情報（セッションID、ページトークン、ランダムな数字など）を照合する処理を実装する.
	* [XSS（クロスサイトスクリプティング）との違い](https://solution.fielding.co.jp/service/security/measures/column/column-9/#:~:text=%EF%BC%88CSRF%EF%BC%89%E3%81%A7%E3%81%99%E3%80%82-,%E3%82%AF%E3%83%AD%E3%82%B9%E3%82%B5%E3%82%A4%E3%83%88%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%97%E3%83%86%E3%82%A3%E3%83%B3%E3%82%B0%EF%BC%88XSS%EF%BC%89%E3%81%AF%E3%80%81%E5%85%A5%E5%8A%9B%E3%83%95%E3%82%A9%E3%83%BC%E3%83%A0%E3%82%84%E6%8E%B2%E7%A4%BA%E6%9D%BF,URL%E3%82%92%E3%82%AF%E3%83%AA%E3%83%83%E3%82%AF%E3%81%95%E3%81%9B%E3%81%BE%E3%81%99%E3%80%82)
		* XSSは、入力フォームや掲示板など動的ページの脆弱性を悪用した攻撃である.
		* CSRFは、ユーザのリクエストを偽装する攻撃である. つまり、ユーザを攻撃用サイトに誘導し、攻撃用URLをクリックさせる. すると不正なリクエストが攻撃対象のサーバに送られ、攻撃用サイト（罠サイト）に誘導されたユーザには直接的な被害はないが、攻撃がユーザからのリクエストとして実行されるので、攻撃者として認識されることになる.

	![CSRF_img](/img/csrf.png)
* [`request.POST`](https://docs.djangoproject.com/ja/4.2/ref/request-response/#django.http.HttpRequest.POST)
	* リクエストにフォームデータが含まれている場合、指定されたすべての HTTP POST パラメータを含む辞書のようなオブジェクト.
	* キーを指定すると、送信したデータにアクセスできる.
	* `request.POST`の値は常に文字列である.
	* 指定したキーがなければ、`KeyEroor`を返す.
* [`HttpResponseRedirect](https://docs.djangoproject.com/ja/4.2/ref/request-response/#django.http.HttpResponseRedirect)
	* `HttpResponseRedirect`は1つの引数（リダイレクト先のURL）をとる.
	* POSTデータが成功した後は常に`HttpResponseRedirect`を返す必要がある. これはDjango固有のものではなく、Web開発におけるベストプラクティスである.
* [`reverse()`](https://docs.djangoproject.com/ja/4.2/ref/urlresolvers/#django.urls.reverse)
	* `reverse()`を使用することで、ビュー関数中でのURLのハードコーディングを防ぐことができる.
	* 引数として、制御を渡したいビューの名前と、そのビューに与えるURLパターンの位置引数を与える.
<br />

## [汎用ビュー](https://docs.djangoproject.com/ja/4.2/intro/tutorial04/#use-generic-views-less-code-is-better)
* URLを介して渡されたパラメータに従ってデータベースからデータを取り出し、テンプレートをロードして、レンダリングしたテンプレートを返すことは、Web開発において極めてよく存在するケースなので、Djangoでは汎用ビュー（generic view）というショートカットを提供している.
* 汎用ビューとは、よくあるパターンを抽象化して、Pythonコードすら書かずにアプリケーションを書き上げられる状態にしたものである.
* 各汎用ビューは、自身がどのモデルに対して動作するのかを知っておく必要があるので、`model`属性を指定する.
* コンテキスト変数の名前をデフォルトの名前から任意の名前に変更するには、`context_object_name`属性を与えて名前を指定する.
* [ListView](https://docs.djangoproject.com/ja/4.2/ref/class-based-views/generic-display/#django.views.generic.list.ListView)
	* オブジェクトのリストを表示する概念を抽象化したもの.
	* デフォルトでは、`ListView`汎用ビューは`project_name/app name/<model_name>_list.html`という名前のテンプレートを使用する.
	* `template_name`属性を指定すると、自動生成されたデフォルトのテンプレート名ではなく、指定したテンプレート名を使うように Djangoに伝えることができる.
* [DetailView](https://docs.djangoproject.com/ja/4.2/ref/class-based-views/generic-display/#django.views.generic.detail.DetailView)
	* あるタイプのオブジェクトの詳細ページを表示する概念を抽象化したもの.
	* `pk`（primary key）という名前でURLからプライマリキーをキャプチャして渡すことになっているので、`project_name/app_name/urls.py`の`urlpatterns`には`<int:pk>`を`path()`に指定してやる必要がある.
	* デフォルトでは、`DetailView`汎用ビューは`/project_name/app_name/<model_name>_detail.html`という名前のテンプレートを使用する.
	* `template_name`属性を指定すると、自動生成されたデフォルトのテンプレート名ではなく、指定したテンプレート名を使うように Djangoに伝えることができる.
* [汎用ビューのドキュメント](https://docs.djangoproject.com/ja/4.2/topics/class-based-views/)
<br />

## 参照
[ドキュメント](https://docs.djangoproject.com/ja/4.2/intro/)