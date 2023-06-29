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

## 参照
[ドキュメント](https://docs.djangoproject.com/ja/4.2/intro/)