# ChineseEHRBert
中文电子病历Bert预训练模型


[English Version](./README.md)

# cleaner
cleaner可以将文件清理为预训练bert需要的格式。将原文件按标点符号切割为行。

## 用法
```
cd ./cleaner/
python parser.py [-h] [--input INPUT] [--output OUTPUT] [-s] [--log LOG]
```
- --input: 输入文件夹
- --output: 输出文件夹
- -s: 输出是否是单个文件
- --log: log频率

# train
进行预训练之前需要先生成tfrecord文件。因为需要训练的文本可能很大，脚本会先进行切分。

## 用法
切分和生成tfrecord
```
cd ./train/
python make_pretrain_bert.py [-h] [-f FILE_PATH] [-s SPLIT_LINE]
                             [-p SPLIT_PATH] [-o OUTPUT_PATH] [-l MAX_LENGTH]
                             [-b BERT_BASE_DIR]
```
- -f: 清理完的输入文件夹
- -s: 分割行数, 默认=500000
- -p: 分割文件保存位置
- -o: .tfrecord文件保存位置
- -l: 句子最长字数
- -b: bert文件夹（需要从google下载）

**pretrain128.sh**和**pretrain512.sh**的参数需要根据需要自行修改。
```
sh pretrain128.sh
sh pretrain512.sh
```

# test
一行测试中文NLP任务!两个NER任务，一个RE任务，一个QA任务，一个句子相似性判断任务。具体说明见**./test/readme.md**。
```
cd ./test/
sh run_test.sh
```
包含了如下任务[CCKS2019NER](https://www.biendata.com/competition/CCKS2019_1/), [cMedQA2](https://github.com/zhangsheng93/cMedQA2), [Tianchi\_NER](https://tianchi.aliyun.com/dataset/dataDetail?spm=5176.12281978.0.0.75926bacsx0LyL&dataId=22288), [Tianchi\_RE](https://tianchi.aliyun.com/dataset/dataDetail?spm=5176.12281978.0.0.75926bacsx0LyL&dataId=22288), [ncov2019_sim](https://tianchi.aliyun.com/competition/entrance/231776/introduction)。

# Results
结果包括用Google训练的中文Bert和用ChineseEhrBert分别fine-tune之后的结果。结果正在准备中。

# Citation

# Author
- [袁正](https://github.com/GanjinZero)
- [赵芃](https://github.com/zp9763)
- 俞辰
- [俞声](http://www.stat.tsinghua.edu.cn/teambuilder/faculty/yusheng/)
