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

## 参照
[ドキュメント](https://docs.djangoproject.com/ja/4.2/intro/)