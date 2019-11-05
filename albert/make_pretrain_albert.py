import argparse
import os
import time


parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file_path", default="/media/sdb2/chc/EHRBERT/data/train.txt")
parser.add_argument("-s", "--split_line", type=int, default=500000)
parser.add_argument("-p", "--split_path", default="./temp_split/")
parser.add_argument("-o", "--output_path")
parser.add_argument("-l", "--max_length", type=int, default=128)
parser.add_argument("-b", "--bert_base_dir", default="/media/sdb2/chc/EHRBERT/chinese_L-12_H-768_A-12")

args = parser.parse_args()

# Split First
os.system(f"mkdir {args.split_path}")
os.system("split -d -l {} {} sp".format(str(args.split_line), args.file_path))
os.system(f"mv ./sp* {args.split_path}")
os.system(f"mkdir {args.output_path}")

# Make pretrain data
for root, dirs, files in os.walk(args.split_path):
    for f in files:
        input_file = os.path.join(root, f)
        opt_basename = f"tf_length_{str(args.max_length)}" + os.path.basename(f).split(".")[0] + ".tfrecord"
        opt_path = os.path.join(args.output_path, opt_basename)
        print(opt_path)
        start_time = time.time()
        os.system(f"python create_pretraining_data.py \
                    --input_file={input_file} \
                    --output_file={opt_path} \
                    --vocab_file={args.bert_base_dir}/vocab.txt \
                    --do_lower_case=False \
                    --max_sequence_length={str(args.max_length)} \
                    --max_predictions_per_seq={str(round(0.15 * args.max_length))} \
                    --random_seed=72 \
                    --dupe_factor=5")
        end_time = time.time()
        print(f"{opt_basename} done. Use time {round(end_time - start_time)}s.")
print("All Done.")
