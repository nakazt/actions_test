# GitHub Actions と GitHub Pages のテスト

このリポジトリは、GitHub Actions と GitHub Pages の機能をテストするためのものです。

## CI/CD パイプライン

このプロジェクトでは、`.github/workflows/main.yml` ファイルで定義された CI/CD パイプラインを使用しています。

主な特徴：
- Python 3.10 環境でのテスト実行
- 依存関係のキャッシュ
- `main` ブランチへのプッシュ時に自動デプロイ

## デプロイ先

GitHub Pages: https://nakazt.github.io/actions_test/

`main` ブランチにプッシュされた変更は、自動的にこのURLにデプロイされます。