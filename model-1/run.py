import pandas as pd
from main import main
import random
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--no_of_comment", "-nc", help="no of comment", required= True)
parser.add_argument("--text_file", "-f", help="text_file", required= True)

# Read arguments from the command line
args = parser.parse_args()

class run:
    def __init__(self):
        self.df=pd.read_csv("DB/comment_1.csv")
    def processing(self, text_file):
        list_p=main("DB/1.txt")
        m=[]
        l=[]
        for i in list_p:
            k=i[:-3].strip()
            k=k.replace("’ S", "’s").replace("’ s", "’s").replace("’ t", "’t")
            m.append(k)
        i=0
        while i < len(m):
            k=m[i]
            for w in k.split(" "):
                if len(w)==1 and w.isalpha():
                    if w != "a" :
                        if w != "i": 
                            l.append(i)
                            break
          
            i += 1
        m = [i for j, i in enumerate(m) if j not in l]
        return m
    def result(self, text_file,nc):
        results = []
        test_list=["normal_text","paraphase_formal","paraphase_causal","paraphase_passive","paraphase_active"]
        m=self.processing(text_file)
        nc=int(nc)
        for i in range(nc):
            if(i%2==0):
                s=m[random.randint(0, len(m))]
            else:
                rt = random.choice(test_list)
                s=self.df[rt][random.randint(0, len(self.df))]
            print(i+1,":  ",s)
            results.append(s)
        pd.DataFrame({'Question':results}).to_csv('results.csv')
        return results
       
#"""
mm=run()
mm.result(args.text_file,args.no_of_comment)
#"""