# String Comparator


## NAME
----------------------------------------
`string_comparator.py` : 文字列を比較する。


## SYNOPSIS
----------------------------------------
```sh
$ python string_comparator.py -s source_file -t target_file
```


## DESCRIPTION
----------------------------------------
`source_file`に記述された文字列を`target_file`に記述された文字列と比較する。改行で区切られた文字列を比較単位とする。ただし空行は比較対象としない。`source_file`に記述された文字列の内、`target_file`に存在しない文字列があれば、以下の形式で標準出力へ出力する。
```
The following strings in source file aren't included in target file:
non-existent_string1_in_source_file
non-existent_string2_in_source_file
non-existent_string3_in_source_file
...
```

`source_file`に記述された文字列が全て`target_file`に存在すれば、以下の文字列が標準出力へ出力される。
```
All strings matched.
```


## ARGUMENTS/OPTIONS
----------------------------------------
- `-s, --source source_file`  
    `source_file`に比較元文字列が記載されたファイルを指定する。
- `-t, --target target_file`  
    `target_file`に比較先文字列が記載されたファイルを指定する。


## PARAMETERS
----------------------------------------


## EXAMPLE
----------------------------------------
- source.txt内の文字列がtarget.txtに含まれているかを確認する。
    ```sh
    $ python string_comparator.py -s source.txt -t target.txt
    ```


## DEPENDENCIES
----------------------------------------
- Python 3
