# -*- coding: utf-8 -*-
"""
NAME:
    tool.py - 各種機能の実行.
SYNOPSIS:
    $ python tool.py
DESCRIPTION:
    指定した各オプションに応じて各種機能を実行する.
OPTIONS:
    -w, --web WEB
        WEBに指定したjsonファイルに記載されているWebページを既定のブラウザで開く.
    -p, --path PATH
        PATHに指定したjsonファイルに記載されているファイル/ディレクトリを開く.
EXAMPLE:
    $ python tool.py
"""
import argparse
import os
import json
import webbrowser
import subprocess


class InvalidArguments(Exception):
    """引数エラーで使用する例外クラス.

    """
    pass


def parse_args():
    """コマンドライン引数を解析する.

    Parameters
    ----------
    None.

    Returns
    -------
    args : argparse.Namespace
        コマンドライン引数をメンバとするオブジェクト.
        args.web: -w, --webオプションの引数.

    """
    parser = argparse.ArgumentParser(description="各種機能を実行する.")
    parser.add_argument("-w", "--web", nargs=1, required=False, help="開くWebページを記述したjsonファイルを指定.")
    parser.add_argument("-p", "--path", nargs=1, required=False, help="開くファイル/ディレクトリを記述したjsonファイルを指定.")
    args = parser.parse_args()

    # オプション引数のファイルが存在しない場合
    if args.web is not None:
        if not os.path.exists(args.web[0]):
            raise InvalidArguments("{0} does not exist.".format(args.web[0]))
    if args.path is not None:
        if not os.path.exists(args.path[0]):
            raise InvalidArguments("{0} does not exist.".format(args.web[0]))

    return args


def open_webpage(file):
    """指定したWebページを既定のブラウザで開く.

    Parameters
    ----------
    file : str
        開くべきWebページを記載したjsonファイル.
        例: {"title":"TITLE","urls":{"URL_NAME":"https://XXXX"}}

    Returns
    -------
    None.

    """
    with open(file) as f:
        contents = json.load(f)
    # jsonの"urls"属性の各要素の値に指定したURLを開く
    for url in contents["urls"].values():
        webbrowser.open(url, new=0, autoraise=True)


def open_path(file):
    """指定したファイル/ディレクトリを開く.

    Parameters
    ----------
    file : str
        開くべきファイル/ディレクトリを記載したjsonファイル.
        例: {"title":"TITLE","paths":{"PATH_NAME":"C:\XXXX"}}

    Returns
    -------
    None.

    """
    with open(file) as f:
        contents = json.load(f)
    # jsonの"paths"属性の各要素の値に指定したファイル/ディレクトリを開く
    for path in contents["paths"].values():
        # NOTE: セキュリティの観点からshell=True引数は使用しない
        subprocess.Popen(["explorer", path])


if __name__ == "__main__":
    # コマンドライン引数を解析する
    args = parse_args()

    # -w, --webオプションを処理する
    if args.web is not None:
        open_webpage(args.web[0])

     # -p, --pathオプションを処理する
    if args.path is not None:
        open_path(args.path[0])
