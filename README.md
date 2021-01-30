# Fetch Rewards Coding Exercise - Data Engineer
Author: Akanksha Sharma <br/>
Email:   akankshasharma2493@gmail.com <br/>


# Description
This challenge is focused on finding the similarity between two texts. The objective is to write a program that takes as inputs two texts and uses a metric to determine how similar they are. Documents that are exactly the same should get a score of 1, and documents that don’t have any words in common should get a score of 0.

# Constraint
This challenge allowed the use of any language, but it was required to build solution without the use of any relevant text processing libraries like scikit-learn, NLTK, spaCy, numpy. However, Flask is allowed to create web app.

# Deliverable
Created a web app using Flask web framework that allows users to input 2 texts and generates a Cosine Similarity score between 0 and 1.

# Considerations while building solution
Do you count punctuation or only words?
> I included only words and removed all punctuations as I did not want their presence to affect similarity score. Example, "Surprise!" and "Surprised..." should have same impact on similarity score despite difference in punctuation. 

Which words should matter in the similarity comparison?
> The commonly occuring stop words are removed as they misrepresent similarity score by inadvertently increasing it. 

Do you care about the ordering of words?
> For this particular challenge, I did not take the ordering of words into account. This is because the size of given samples is small and I assumed that each new input would also fall in the similar range. The small text size makes it less likely for both the texts to have N-grams(sequence of words) in common. This will lead to distorted "tf-idf" vectors, translating to high dissimilarity between texts despite them having common words. 
    
What metric do you use to assign a numerical value to the similarity?
> I used cosine similarity that takes the angle between the calculated "tf-idf" vectors and computes the cosine of that angle, which refers to the similarity between two texts. This similarity score ranges from 0 to 1, with 0 being the lowest (the least similar) and 1 being the highest (the most similar).

What type of data structures should be used?
> I used the following data structures:
>> "list" in form of nested lists and list comprehension for text processing and for storing stop words 
>> "sets" to calculate document frequency
>> "dictionaries" to store tf-idf values.

# How to execute?
1. Download Zip file by clicking dropdown button of "Code" on the top right of this page.
2. Extract files
3. Run api.py <br/>
a. Open terminal <br/>
b. Type the following commands
```
cd <path/to/the/downloaded_folder>
python api.py
```
4. Click on the link generated on terminal (127.0.0.1:5000). It will open a webpage
5. Enter 2 texts on webpage and click "Compare" button to get Similarity score 

## Library used: 
"Flask" for creating web app

## Environment used:
PyCharm 2020.3.2 
Python 3.7
Flask 1.1.2



