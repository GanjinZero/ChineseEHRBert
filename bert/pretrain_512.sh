export BERT_BASE_DIR=/media/sdb2/chc/EHRBert/chinese_L-12_H-768_A-12

python run_pretraining.py \
  --input_file=./train/*.tfrecord \
  --output_dir=./train/pretraining_512/ \
  --do_train=True \
  --do_eval=True \
  --bert_config_file=$BERT_BASE_DIR/bert_config.json \
  --init_checkpoint=$BERT_BASE_DIR/bert_model.ckpt \
  --train_batch_size=6 \
  --max_seq_length=512 \
  --max_predictions_per_seq=20 \
  --num_train_steps=20000 \
  --num_warmup_steps=10000 \
  --save_checkpoints_step=20000 \
  --learning_rate=2e-5
