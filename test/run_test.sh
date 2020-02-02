#!/usr/bin/env bash

# ccks2019 ner
  python ./ccks2019_ner/BERT_NER.py  \
    --data_dir=./ccks2019_ner/data/  \
    --bert_config_file=./bert_model/bert_config.json  \
    --task_name="NER"  \
    --vocab_file=./bert_model/vocab.txt  \
    --output_dir=./ccks2019_ner/output/  \
    --middle_output=./ccks2019_ner/middle_data/  \
    --init_checkpoint=./bert_model/bert_model.ckpt  \
    --do_lower_case=True  \
    --max_seq_length=512  \
    --do_train=True  \
    --do_eval=False  \
    --do_predict=True  \
    --train_batch_size=6  \
    --eval_batch_size=6  \
    --predict_batch_size=6  \
    --learning_rate=5e-5  \
    --num_train_epochs=3.0  \
    --warmup_proportion=0.1  \
    --save_checkpoints_steps=10000  \
    --iterations_per_loop=10000  \
    --crf=False  \
    --doc_stride=128
    
  python ./ccks2019_ner/conlleval.py \
    ./ccks2019_ner/output/label_test.txt \
    ./ccks2019_ner/output/

# tianchi ner
  python ./tianchi_ner/BERT_NER.py  \
    --data_dir=./tianchi_ner/data/  \
    --bert_config_file=./bert_model/bert_config.json  \
    --task_name="NER"  \
    --vocab_file=./bert_model/vocab.txt  \
    --output_dir=./tianchi_ner/output/  \
    --middle_output=./tianchi_ner/middle_data/  \
    --init_checkpoint=./bert_model/bert_model.ckpt  \
    --do_lower_case=True  \
    --max_seq_length=512  \
    --do_train=True  \
    --do_eval=False  \
    --do_predict=True  \
    --train_batch_size=6  \
    --eval_batch_size=6  \
    --predict_batch_size=6  \
    --learning_rate=5e-5  \
    --num_train_epochs=3.0  \
    --warmup_proportion=0.1  \
    --save_checkpoints_steps=10000  \
    --iterations_per_loop=10000  \
    --crf=False  \
    --doc_stride=128

  python ./tianchi_ner/conlleval.py \
    ./tianchi_ner/output/label_test.txt \
    ./tianchi_ner/output/

# tianchi re
  python ./tianchi_re/BERT_RE.py  \
    --data_dir=./tianchi_re/data/  \
    --bert_config_file=./bert_model/bert_config.json  \
    --task_name="RE"  \
    --vocab_file=./bert_model/vocab.txt  \
    --output_dir=./tianchi_re/output/  \
    --middle_output=./tianchi_re/middle_data/  \
    --init_checkpoint=./bert_model/bert_model.ckpt  \
    --do_lower_case=True  \
    --max_seq_length=512  \
    --do_train=True  \
    --do_eval=False  \
    --do_predict=True  \
    --train_batch_size=6  \
    --eval_batch_size=6  \
    --predict_batch_size=6  \
    --learning_rate=2e-5  \
    --num_train_epochs=3.0  \
    --warmup_proportion=0.1  \
    --save_checkpoints_steps=70000  \
    --iterations_per_loop=70000

# cmedqa2 qa
  python ./cmedqa2_qa/BERT_QA.py  \
    --data_dir=./cmedqa2_qa/data/  \
    --bert_config_file=./bert_model/bert_config.json  \
    --task_name="QA"  \
    --vocab_file=./bert_model/vocab.txt  \
    --output_dir=./cmedqa2_qa/output/  \
    --middle_output=./cmedqa2_qa/middle_data/  \
    --init_checkpoint=./bert_model/bert_model.ckpt  \
    --do_lower_case=True  \
    --max_seq_length=512  \
    --do_train=True  \
    --do_eval=False  \
    --do_predict=True  \
    --train_batch_size=6  \
    --eval_batch_size=6  \
    --predict_batch_size=6  \
    --learning_rate=2e-5  \
    --num_train_epochs=3.0  \
    --warmup_proportion=0.1  \
    --save_checkpoints_steps=200000  \
    --iterations_per_loop=200000

# concat test results
  touch test_result.txt
  echo -e '===== CCKS2019 NER =====' >> test_result.txt
  cat ./ccks2019_ner/output/test_result.txt >> test_result.txt
  echo -e '\n\n===== TianChi NER =====' >> test_result.txt
  cat ./tianchi_ner/output/test_result.txt >> test_result.txt
  echo -e '\n\n===== TianChi RE =====' >> test_result.txt
  cat ./tianchi_re/output/test_result.txt >> test_result.txt
  echo -e '\n\n===== cMedQA2 QA =====' >> test_result.txt
  cat ./cmedqa2/output/test_result.txt >> test_result.txt
