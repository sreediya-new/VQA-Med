import re
import pandas as pd
import csv
import matplotlib.image as mpimg
import matplotlib.pyplot as plt


class Utility(object):
    @staticmethod
    def clean(line):
        line = line.lower()
        line = line.replace('?', ' ?')
        line = re.sub(' +',' ', line)
        return line.strip()

    @staticmethod
    def read_dataset(dataset):
        path="/content/dataset/VQAMed2019"+dataset+"/VQAMed2019"+dataset+"-QA.csv"
        #df =pd.read_csv(path, sep='|', header=None, quoting=csv.QUOTE_NONE)
        df =pd.read_csv(path)
        if "Test" in dataset:
           df = df.rename(columns={'0': 'id', '1': 'image_name', '2': 'question', })
        else:
           df = df.rename(columns={'0': 'id', '1': 'image_name', '2': 'question','3': 'answer'})

        print(dataset+" data size=",len(df))
        print("Current columns:", df.columns.tolist())
        images = []
        for i in df["id"]:

            fname = "/content/dataset/VQAMed2019"+dataset+"/VQAMed2019"+dataset+"-images/"+i+".jpg"
            images.append(fname)
        if "Test" in dataset:
            return images, df["question"]
        else:
            return images, df["question"], df["answer"]


    @staticmethod  
    def show_image(id, images, questions, answers):
        fname = images[id]
        img=mpimg.imread(fname, format="jpg")
        print ("Image name :", fname)  
        print ("Question   :", questions[id])
        print ("Answer     :", answers[id] )
        plt.imshow(img)
        plt.show()
