# Warning #
This project has been moved to [github](https://github.com/shell909090/python-segment).

# 简介 #
python-segment是一个纯python实现的分词库，他的目标是提供一个可用的，完善的分词系统和训练环境，包括一个可用的词典。更进一步的说明，请看[INSTALL](INSTALL.md)文档和[README](README.md)文档。同时，系统中附带了一个简单的分类库，具体可以看[clsUsage](clsUsage.md)文档。

# 原理 #
python-segment的词典是带词频无词性词典，程序基于剪枝和词频概率工作，不考虑词性，不考虑马尔可夫链。词典含两部分内容，单字词频和词组词频。两者的统计和使用是分离的。词典一般有两种形态，marshal格式和txt格式。

# 性能说明 #
在一台虚拟机上测试的结果，载入词典后消耗内存（带python）大约60m，分词效率大约100k字/秒。注意，默认情况下，程序使用yield返回分词结果，这不会消耗太多内存。但是如果需要保留分词得到的每个词语碎片，将耗费大量内存。根据测试，一个10M的文本文件（大约500W字）需要120m以上的内存来保持词语碎片。

# 词典生成 #
按照如下方式，使用[dbmgr](dbmgrUsage.md)生成frq.db文件。
```
gunzip dict.tar.gz
./ps_dbmgr create dict.txt
```
你可以看到生成了frq.db，这是词典的默认文件名。注意，词典文件的格式和具体的版本有关，换用版本后最好重新生成词典。

# 命令行使用 #
假定有一个文本文件，test.txt，里面内容是中文平文本，编码任意。
```
./ps_cutter cutshow test.txt
```
[cutter](cutterUsage.md)会自动推测编码。

# 代码使用 #
假如当前有一个frq.db词库。
```
import segment
cut = segment.get_cutter('frq.db')
print list(cut.parse(u'工信处女干事每月经过下属科室都要亲口交代24口交换机等技术性器件的安装工作'))
```
注意，仅仅使用parse是不会进行分词的，因为parse返回的是一个生成器。