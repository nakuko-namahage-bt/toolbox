# C project


## NAME
----------------------------------------
- `sample_app` : サンプルCアプリケーション
- `libsample.so` : サンプルC共有ライブラリ


## SYNOPSIS
----------------------------------------
```sh
$ sample_app [-o operation] num1 num2
```


## DESCRIPTION
----------------------------------------
2項演算 (加減乗除) を行う。


## ARGUMENTS/OPTIONS
----------------------------------------
- num1  
    演算対象の整数1つ目 (int)
- num2  
    演算対象の整数2つ目 (int)
- `-o operation`  
    実行する演算を指定する。operationには以下の数を指定する。
    - 0 : 可算 (num1 + num2)
    - 1 : 減算 (num1 - num2)
    - 2 : 乗算 (num1 * num2)
    - 3 : 除算 (num1 / num2)  
    上記以外の数を指定した場合はエラー終了する。


## PARAMETERS
----------------------------------------


## EXAMPLE
----------------------------------------
1. sample_libをビルドする。
    ```sh
    $ cd [sample_lib_top_directory]
    $ make
    ```
2. sample_appをビルドする。
    ```sh
    $ cd [sample_app_top_directory]
    $ make
    ```
3. ライブラリ検索パス (LD_LIBRARY_PATH) の設定。
    ```sh
    $ source setlibpath.sh
    ```
4. `1 + 2`を実行する。
    ```sh
    $ ./sample_app -o 0 1 2
    1 + 2 = 3
    ```


## DEPENDENCIES
----------------------------------------
- sample_appはlibsample.soに依存。
