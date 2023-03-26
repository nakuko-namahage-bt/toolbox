# -*- coding: utf-8 -*-
import argparse
import os


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
        args.source: -s, --sourceオプションの引数.
        args.target: -t, --targetオプションの引数.

    """
    parser = argparse.ArgumentParser(description="文字列を比較する.")
    parser.add_argument("-s", "--source", required=True, help="比較元文字列が記載されたファイルを指定.")
    parser.add_argument("-t", "--target", required=True, help="比較先文字列が記載されたファイルを指定.")
    args = parser.parse_args()

    # オプション引数のファイルが存在しない場合
    if not os.path.exists(args.source):
        raise InvalidArguments("{0} does not exist.".format(args.source))
    if not os.path.exists(args.target):
        raise InvalidArguments("{0} does not exist.".format(args.target))

    return args


def get_strings(file_path):
    """指定されたファイルから文字列のリストを取得する.

    Parameters
    ----------
    file_path : str
        対象ファイルパス.

    Returns
    -------
    strings : list
        対象ファイル内の各行の文字列からなるリスト.

    """
    with open(file_path, mode="r", encoding="utf_8") as file:
        line_1st = file.readline()

    # 最初の文字がBOMの場合、文字コードをBOMつきUTF-8とする
    codec = "utf_8_sig" if line_1st[0] == "\ufeff" else "utf_8"

    with open(file_path, mode="r", encoding=codec) as file:
        strings = file.read().splitlines() # 改行文字を含まない

    return strings


def compare_strings(src_strings, tgt_strings):
    """入力文字列リストの比較を行う.

    Parameters
    ----------
    src_strings : list
        比較元文字列のリスト.
    tgt_strings : list
        比較先文字列のリスト.

    Returns
    -------
    results : list
        比較元文字列の内、比較先文字列のリストに含まれない要素からなるリスト.

    """
    results = []
    for src_string in src_strings:
        # 比較元文字列が空白でない場合
        if src_string:
            # 比較先文字列と比較しマッチしなければ比較結果に追加する
            if not (src_string in tgt_strings):
                results.append(src_string)

    return results


def show_result(results):
    """比較結果を出力する.

    Parameters
    ----------
    results : list
        比較結果の文字列からなるリスト.

    Returns
    -------
    None.

    """
    if not results:
        print("All strings matched.")
    # 存在しない文字列があった場合
    else:
        print("The following strings in source file aren't included in target file:")
        for result in results:
            print(result)


if __name__ == "__main__":
    # コマンドライン引数を解析する
    args = parse_args()

    # 対象ファイルから文字列のリストを取得する
    src_strings = get_strings(args.source)
    tgt_strings = get_strings(args.target)

    # 文字列比較を行う
    results = compare_strings(src_strings, tgt_strings)

    # 比較結果を出力する
    show_result(results)
