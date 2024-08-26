# GitHub Actions と GitHub Pages のテスト

このリポジトリは、GitHub Actions と GitHub Pages の機能をテストするためのものです。

## CI/CD パイプライン

このプロジェクトでは、`.github/workflows/main.yml` ファイルで定義された CI/CD パイプラインを使用しています。

主な特徴：
- Python 3.10 環境でのテスト実行
- `main` ブランチへのプッシュ時に自動デプロイ
- `test` ブランチでのテスト実行

## プロジェクト構造

- `docs/index.html`: メインのHTMLファイル
- `docs/styles.css`: CSSスタイルシート
- `hello.py`: サンプルPythonスクリプト
- `test_hello.py`: テストファイル

## スタイリング

このプロジェクトでは、HTMLとCSSを分離しています：
- `index.html`ファイルにはHTMLマークアップのみが含まれています。
- すべてのスタイリングは`styles.css`ファイルに記述されています。

この分離により、コードの管理が容易になり、再利用性が向上します。

## Pythonスクリプト

`hello.py`には、"Hello, world!"を指定回数出力する関数が含まれています。このスクリプトは、CI/CDパイプラインでテストされます。

## テスト

`test_hello.py`ファイルには、`hello.py`の機能をテストするためのPytestテストが含まれています。CIプロセスの一部としてこれらのテストが実行されます。

## デプロイ先

GitHub Pages: https://nakazt.github.io/actions_test/

`main` ブランチにプッシュされた変更は、自動的にこのURLにデプロイされます。