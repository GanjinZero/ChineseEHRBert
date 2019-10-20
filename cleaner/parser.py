import sys, os
import re
import time
import argparse

input_file_path = "data"
output_file_path = "out"
output_mode = "integrate"
log_period = 5000

line_counter = 0
def main():
    global input_file_path
    global output_file_path
    global output_mode
    global log_period
    global line_counter
    parser = argparse.ArgumentParser()
    parser.add_argument("--input",type=str,default=input_file_path,required=False,help="declare input file directory (default: %(default)s)")
    parser.add_argument("--output",type=str,default=output_file_path,required=False,help="declare output file directory (default: %(default)s)")
    parser.add_argument("-s","--seperate",action="store_true",help="check it to make output seperated (write into a single file \"output.txt\" by default)")#seperated
    parser.add_argument("--log",type=int,default=log_period,required=False,help="period of displaying progress (default: %(default)s)")
    args = parser.parse_args()
    if args.seperate == True:
        output_mode = "seperate"
    input_file_path = args.input
    output_file_path = args.output    
    log_period = args.log
    
    time_start = time.time()
    input_exist = os.path.exists(input_file_path)
    if not input_exist:
        print("input directory missing:"+input_file_path+" exit.")
        return
    output_exist = os.path.exists(output_file_path)
    if not output_exist:
        os.makedirs(output_file_path)
    file_path_list = get_file_path_list(input_file_path)
    file_list_handler(file_path_list)
    time_end = time.time()
    print("total valid #lines: ",line_counter)
    print("total time elapsed:",time_end - time_start)

def get_file_path_list(data_dir):
    result = []
    for main_dir, subdir, file_name_list in os.walk(data_dir):
        result = [os.path.join(main_dir,file_name) for file_name in file_name_list]
    return result
  
def clear_file(file_path):
    f = open(file_path,'w')
    f.truncate()
    f.close()
        
def file_list_handler(file_path_list):
    default_output_file_path = os.path.join(output_file_path,"output.txt")
    if output_mode == "integrate":
        clear_file(default_output_file_path)
        for file_path in file_path_list:
            single_file_handler(file_path,default_output_file_path,write_mode='a')
    elif output_mode == "seperate":
        for file_path in file_path_list:
            filename = os.path.split(file_path)[1] #get filename
            tmp_output_file_path = os.path.join(output_file_path,filename)
            single_file_handler(file_path,tmp_output_file_path,write_mode='w')
    
def single_file_handler(input_file_path,output_file_path,write_mode):
    global line_counter
    f_out = open(output_file_path,write_mode)
    for line in open(input_file_path):
        if is_not_empty(line):
            f_out.write(article_processor(line).strip())
            f_out.write('\n\n')
            line_counter += 1
            if line_counter % log_period == 0:
                print("processed valid lines:"+str(line_counter))

    f_out.close()
            
def is_not_empty(line):
    return line.strip() != ""
    
def test_is_not_empty():
    ret = [
        is_not_empty("123"),
        is_not_empty("123  "),
        is_not_empty("  123"),
        is_not_empty("1 2 3"),
        is_not_empty("123\n"),
        is_not_empty("123  \n"),
        is_not_empty("\n"),
        is_not_empty("   \n")
    ]
    print(ret)

"""
processor using original func.
"""
def article_processor(article):
    replaced_list = ['。','！','？','!','?','……']
    sub_dict = {str:str+'\n' for str in replaced_list}
    res = article
    for rep,sub in sub_dict.items():
        res = res.replace(rep,sub)
    return res    
    
"""
processor using reg.(deprecated)
"""
def reg_article_processor(article):
    return re.sub("[。！？!?]|……",reg_new_line,article)
    
def reg_new_line(matched):
    return matched.group(0)+'\n'
    

    
if __name__ == "__main__":
    main()
            
    
