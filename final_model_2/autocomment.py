import csv
import pandas as pd
import tensorflow as tf
from transformers import TFGPT2LMHeadModel, GPT2Tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = TFGPT2LMHeadModel.from_pretrained("gpt2", pad_token_id=tokenizer.eos_token_id)

input_ids = tokenizer.encode("Exciting partnership with GODSFLAME The Taiwanese Market-leading Game studio. Its 20m users are now ready to enter", return_tensors='tf')

output_list=[]
for i in range(100):
    sample_output = model.generate(input_ids,do_sample=True,max_length=50,top_p=0.92,top_k=0)
    output_list.append(tokenizer.decode(sample_output[0], skip_special_tokens=True))
    print("Output:\n" + 100 * '-')
    print(tokenizer.decode(sample_output[0], skip_special_tokens=True))
# print(output_list)
df=pd.DataFrame(list(zip(output_list)),
              columns=['outputs'])
df.to_csv("/content/drive/MyDrive/Ayush_Gupta/auto_comments/sample.csv")