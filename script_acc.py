# It can be used on the dataset found at  https://www.kaggle.com/c/word2vec-nlp-tutorial/data, for training and testing purposes
# It can be used on at least 1 other (large) set of reviews from another movie review website , for example rotten tomatoes
# It can be used the classify your own written reviews ( say a set of 10 movie reviews on movies you have recently seen)

# 1) Discovery
#        More than two datasets are imported and combined, more than 500 items each
# 2) Data Preparation
#        Student used advanced features to clean and prepare a variety of datasets with different issues
# 3) Model Planning
#        Student has done some research on classifiers, and can use arguments for using a particular one beyond the mandatory literature
# 4) Model building
#        Student has incorporated some advanced statements into the R-scripts and knows exactly why and how statements are functional
# 5) Communicating results
#        Student has written a elaborate report, understandable for both the expert as the novice, and is capable of comparing the model 
#        and the results with other models and results found in scientific literature


#Importing libraries.
import csv
import os
import subprocess
from subprocess import call

def main():
  print("Importing Data Sets")
  # Import three data sets.
  # Import the required dataset
  posfile = open("positive.txt", "w+")
  negfile = open("negative.txt", "w+")
  print("Reading labeledTrainData in")
  with open("labeledTrainData.tsv") as tsvfile:
    tsvreader = csv.reader(tsvfile, delimiter="\t")
    for line in tsvreader:
      if str(line[1:2]) == "['1']":
        wfile = posfile
      else:
        wfile = negfile
      wfile.write(str(line[2:3]))
  
  # Import the negative IMDB dataset reviews
  print("reading the negative Imdb data")
  negdir = "aclImdb/train/neg"
  for filename in os.listdir(negdir):
    file = negdir + "/" + filename
    rev = open(file, "r")
    negfile.write(rev.read())
    rev.close()
    
  # Import the positive IMDB dataset reviews
  print("reading the posative Imdb data")
  posdir = "aclImdb/train/pos"
  for filename in os.listdir(posdir):
    file = posdir + "/" + filename
    rev = open(file, "r")
    posfile.write(rev.read())
    rev.close()
  
  
  posfile.close()
  negfile.close()
   
  #Dataset = sentiment & review. Review is tekst Sentiment is 0-negativ 1-positive 
  # Train bayes.py on the positive file.
  print("training")
  #call(["python", "bayes.py", "learn", "positive", "positive.txt", "37500"])
  # Train bayes.py on the negative file.
  #call(["python", "bayes.py", "learn", "negative", "negative.txt", "37500"])
  
  # Test the accuracy of the classifier.
  TP = 0
  FP = 0
  TF = 0
  FF = 0
  
  # Import the negative IMDB dataset reviews
  print("testing the negative Imdb data")
  negdir = "aclImdb/test/neg"
  x = 0
  for filename in os.listdir(negdir):
    file = negdir + "/" + filename
    rev = open(file, "r")
    testfile = open("test.txt", "w+")
    testfile.write(rev.read())
    testfile.close()
    process = subprocess.Popen(["python", "bayes.py", "classify", "test.txt", "positive", "negative"], stdout=subprocess.PIPE)
    out, err = process.communicate()
    print(out)
    if(float(out) <- 0.50):
        print("true")
    #classification = call(["python", "bayes.py", "classify", "test.txt", "positive", "negative"])
    #print (classification)
    #try: 
    #  if(float(call(["python", "bayes.py", "classify", "test.txt", "positive", "negative"])) <= 0.5):
    #    TF = TF + 1
    #    print("true")
    #  else:
    #    FF = FF + 1
    #    print("false")
    #except ZeroDivisionError: 
    #    TF = TF + 1
    #    print("error")
    rev.close()
    x = x + 1
    os.remove("test.txt")
    if(x == 50):
        break
    
  # Import the negative IMDB dataset reviews
  x = 0
  print("testing the positive Imdb data")
  negdir = "aclImdb/test/pos"
  for filename in os.listdir(negdir):
    file = negdir + "/" + filename
    rev = open(file, "r")
    testfile = open("test.txt", "w+")
    testfile.write(rev.read())
    testfile.close()
    #classification = call(["python", "bayes.py", "classify", "test.txt", "positive", "negative"])
    mag = subprocess.Popen(["python", "bayes.py", "classify", "test.txt", "positive", "negative"])
    if(float(mag) >= 0.50):
        print("true")
    #try: 
    #  if(float(call(["python", "bayes.py", "classify", "test.txt", "positive", "negative"])) >= 0.50):
    #    print("true")
    #    TP = TP + 1
    #  else:
    #    FP = FP + 1
    #    print("false")
    #except ZeroDivisionError: 
    #    print("error")
    #    FP = FP + 1
    rev.close()
    x = x + 1
    if(x == 50):
        break
  
  print("True Positive: " + str(TP))
  print("False Positive: " + str(FP))
  print("True False: " + str(TF))
  print("False False: " + str(FF))
  
  # Ask for the to be classified text.
  # classify text
  classification = call(["python", "bayes.py", "classify", "classify.txt", "positive", "negative"])
  print(classification)
  # return classification

main()