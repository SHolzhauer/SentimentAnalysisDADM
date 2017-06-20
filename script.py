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
  #print("training")
  #call(["python", "bayes.py", "learn", "positive", "positive.txt", "37500"])
  # Train bayes.py on the negative file.
  #call(["python", "bayes.py", "learn", "negative", "negative.txt", "37500"])
  # Ask for the to be classified text.
  # classify text
  print("classifying")
  call(["python", "bayes.py", "classify", "classify.txt", "positive", "negative"])
  # return classification

main()