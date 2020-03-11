# ChineseEHRBert
A Chinese Electric Health Record Bert Pretrained Model.


[中文版](./README_zh.md)

# cleaner
The cleaner is responsible for cleaning txt files, which is used for training a Chinese bert model. The cleaner split lines in original lines into small lines. Each small line is a complete sentence with a punctuation. This is required for training next sentence prediction task.

## usage
```
cd ./cleaner/
python parser.py [-h] [--input INPUT] [--output OUTPUT] [-s] [--log LOG]
```
- --input: input directory
- --output: output directory
- -s: output is one single file
- --log: log frequency

# train
Pre-train a bert model with cleaned text. We should generate .tfrecord first, and pre-train with google's code. To notice, cleaner file may be too big to load in RAM. Our script splits these files and generate multiple .tfrecord.

## usage
Split file and convert to .tfrecord
```
cd ./train/
python make_pretrain_bert.py [-h] [-f FILE_PATH] [-s SPLIT_LINE]
                             [-p SPLIT_PATH] [-o OUTPUT_PATH] [-l MAX_LENGTH]
                             [-b BERT_BASE_DIR]
```
- -f: cleaned file path
- -s: split line count, default=500000
- -p: splited file save path
- -o: .tfrecord save path
- -l: max length
- -b: bert base dir

One should change parameters for your specific requirement in **pretrain128.sh** and **pretrain512.sh**.
```
sh pretrain128.sh
sh pretrain512.sh
```

# test
Test Chinese medical NLP tasks by BERT in one line! Two NER tasks, one QA task, one RE task and one sentence similarity task.
```
cd ./test/
sh run_test.sh
```
Tasks include [CCKS2019NER](https://www.biendata.com/competition/CCKS2019_1/), [cMedQA2](https://github.com/zhangsheng93/cMedQA2), [Tianchi\_NER](https://tianchi.aliyun.com/dataset/dataDetail?spm=5176.12281978.0.0.75926bacsx0LyL&dataId=22288), [Tianchi\_RE](https://tianchi.aliyun.com/dataset/dataDetail?spm=5176.12281978.0.0.75926bacsx0LyL&dataId=22288), [ncov2019\_sim](https://tianchi.aliyun.com/competition/entrance/231776/introduction).

# Results
Results compared with original BERT and ChineseEHRBert. Results are preparing.

# Citation

# Author
- [Zheng Yuan](https://github.com/GanjinZero)
- Peng Zhao
- Chen Yu
- [Sheng Yu](http://www.stat.tsinghua.edu.cn/teambuilder/faculty/yusheng/)
