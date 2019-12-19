## Fine Tune Bert NER

### File

Bert模型在chinese_L-12_H-768_A-12

NER数据和代码在fine_tune_bert_ner

### Data

数据来源CCKS 2019任务1，中文医学病例文本的命名实体识别。

实体类别包括：

+ 解剖结构 ANA
+ 疾病和诊断 DIS
+ 药物 DRU
+ 影像检查 IMA
+ 实验室检验 LAB
+ 手术 SUR

### Run

```
bash run_ner.sh
```

### Test

```
python conlleval.py ./output/label_test.txt
```



## Fine Tune Bert RE

To be completed



## Fine Tune Bert QA

To be completed

