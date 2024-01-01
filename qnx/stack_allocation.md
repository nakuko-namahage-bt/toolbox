# Stack Allocation


# 目次
- [スタック割り当て方式](#スタック割り当て方式)
- [スレッドのスタック割り当て詳細](#スレッドのスタック割り当て詳細)
- [nonlazy/lazy stackの設定方法](#nonlazylazy-stackの設定方法)
- [スレッド消費スタック計測方法](#スレッド消費スタック計測方法)
- [参考文献](#参考文献)


## スタック割り当て方式
----------------------------------------
- nonlazy/lazy stackとは、QNXシステムにおけるスレッドのスタック領域への物理メモリ割り当て方式に関する概念である。
- nonlazy stackとは、スレッド起動時にスレッドのスタック領域全体に物理メモリを割り当てること。割り当てられるスタックサイズは[スレッドのスタック割り当て詳細](#スレッドのスタック割り当て詳細)参照。
- lazy stackとは、要求に応じてスレッドのスタック領域に物理メモリを割り当てること。
- デフォルトはlazy stack。


## スレッドのスタック割り当て詳細
----------------------------------------
API等を使用して意図的にスタックサイズを指定しない場合、process managerは以下の規則に従ってスレッドのスタック領域に物理メモリを割り当てる。
|Architecture|Main thread max stack size|Non-main thread max stack size|
|:---|:---|:---|
|x86_64|512KByte|256KByte|
|32-bit ARM|512KByte|128KByte|
|AArch64|512KByte|256KByte|
- lazy stackの場合、スレッドが必要とするスタックの伸長に応じて、最大スタックサイズに到達するまで4KByteずつスタック領域に物理メモリが割り当てられる。
- nonlazy stackの場合、スレッド起動時に最大スタックサイズの物理メモリがスタック領域に割り当てられる。


## nonlazy/lazy stackの設定方法
----------------------------------------
`procnto*`の起動オプションに以下を付与することで、nonlazy stackもしくはlazy stackを設定できる。
- `-n`: nonlazy stack
- `-~n`: lazy stack (default)


## スレッド消費スタック計測方法
----------------------------------------
### `pidin memory`コマンドを使用する方法
`pidin memory`コマンドを実行することで、プロセスの各スレッドにおけるメモリの使用状況を取得できる。`pidin memory`コマンドの実行例を以下に示す。
```
     pid tid name               prio STATE            code  data        stack
       1   1 /procnto-smp-instr   0f RUNNING             0     0    480(480) 
       1   2 /procnto-smp-instr   0f READY               0     0    480(480) 
       1   4 /procnto-smp-instr   1r RECEIVE             0     0  256K(256K) 
       1   5 /procnto-smp-instr  10r CONDVAR             0     0  8192(8192) 
       1   6 /procnto-smp-instr  10r CONDVAR             0     0  8192(8192) 
       1   7 /procnto-smp-instr 255r RECEIVE             0     0  8192(8192) 
       1   8 /procnto-smp-instr 255r RECEIVE             0     0  8192(8192) 
       1   9 /procnto-smp-instr 255r RECEIVE             0     0  8192(8192) 
       1  10 /procnto-smp-instr 255r RECEIVE             0     0  8192(8192) 
       1  11 /procnto-smp-instr  21r RECEIVE             0     0  8192(8192) 
       1  12 /procnto-smp-instr  10r RECEIVE             0     0  8192(8192) 
       1  13 /procnto-smp-instr  10r RUNNING             0     0  8192(8192) 
       1  14 /procnto-smp-instr  10r RECEIVE             0     0  8192(8192) 
       1  15 /procnto-smp-instr  10r RECEIVE             0     0  8192(8192) 
       1  16 /procnto-smp-instr  10r RECEIVE             0     0  8192(8192) 
       1  18 /procnto-smp-instr  10r RECEIVE             0     0  8192(8192) 
       1  19 /procnto-smp-instr  10r RECEIVE             0     0  8192(8192) 
            procnto-smp-instr  @ffff80000002a000             762K  125K
       2   1 proc/boot/slogger2  10r RECEIVE             0  684K   12K(516K)*
            slogger2           @         8048000              64K  8192
            libc.so.5          @       100000000             692K   24K
            libslog2.so.1      @       1002b5000              32K  4096
            slogger2/console.2 @       180000000 (       0)         20K
            /slogger2/random.5 @       180005000 (       0)         20K
            ogger2/devb_eide.7 @       18000a000 (       0)         20K
            2/io_usb_otg.49165 @       18000f000 (       0)         20K
            r2/io_audio.159763 @       180014000 (       0)         20K
       ...
```
- `proc/boot/slogger2`行を例に、スタック使用量の見方を以下に示す。
- `proc/boot/slogger2`行は、`pidin memory`コマンド実行時点でのslogger2プロセスのメインスレッドのメモリ使用状況を示している。
- 8列目(`12K(516K)*`)がスタック使用状況を示している。
    - `12K`はスタック領域に割り当てられている物理メモリが12KByteであることを示してしている。スタック領域に物理メモリは4KByteずつ割り当てられるため、スタック使用量が8KByte以上12KByte以下であると言える。
    - 括弧内の`516K`は、スレッドの最大スタックサイズ512KByte+ガードページ4KByteを示している。
    - アスタリスク(*)は、そのスレッドが終了する際に、スタック領域が自動的には解放されないことを示している。
- nonlazy stackの場合、スレッド起動時に最大スタックサイズの物理メモリがスタック領域に固定的に割り当てられるため、`pidin memory`コマンドでスタック使用量を算出することができない(上記例の場合、`512K(516K)*`と表示される)。

### IDEを使用する方法
IDEと実機を接続し、IDEからプロセスの各スレッドのスタック使用量をモニタリングできる。以下にその方法を示す。
#### プロセス同士の比較
1. 実機とIDEを接続する。
2. `Target Navigator` -> `System Resources` -> `Memory Resources`を選択する。
3. 表に各プロセスのメモリ指標が表示される。
#### 各プロセスのメモリレイアウト表示
1. 実機とIDEを接続する。
2. `Target Navigator` -> `Memory Information`を選択する。
3. `Process Map`バーの赤色の領域を選択すると、スタック領域の分布が表示される。
4. 表の`Stack` -> `thread * allocated`に、各スレッドに割り当てられている物理メモリサイズが表示される。
- nonlazy stackの場合にスタック使用量を算出することができない点については[`pidin memory`コマンドを使用する方法](#pidin-memoryコマンドを使用する方法)を参照。


## 参考文献
----------------------------------------
- [procnto*](https://www.qnx.com/developers/docs/7.1/#com.qnx.doc.neutrino.utilities/topic/p/procnto.html)
- [pthread_attr_setstacklazy()](https://www.qnx.com/developers/docs/7.1/#com.qnx.doc.neutrino.lib_ref/topic/p/pthread_attr_setstacklazy.html)
- [Stack allocation](https://www.qnx.com/developers/docs/7.1/index.html#com.qnx.doc.neutrino.prog/topic/process_stack.html)
- [Calculating virtual memory reserved by a process](https://www.qnx.com/developers/docs/7.1/#com.qnx.doc.neutrino.sys_arch/topic/vm_calculations.html)
- [pidin](https://www.qnx.com/developers/docs/7.1/#com.qnx.doc.neutrino.utilities/topic/p/pidin.html)
- [Monitoring memory consumption at the process level](https://www.qnx.com/developers/docs/7.1/#com.qnx.doc.ide.userguide/topic/monitor_mem_process_sysinfo.html)
