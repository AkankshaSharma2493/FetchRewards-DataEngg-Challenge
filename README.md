# Fetch Rewards Coding Exercise - Data Engineer
Author: Akanksha Sharma <br/>
Email:  akankshasharma2493@gmail.com <br/>
Link to My Resume

# Description
This challenge is focused on finding the similarity between two texts. The objective is to write a program that takes as inputs two texts and uses a metric to determine how similar they are. Documents that are exactly the same should get a score of 1, and documents that don’t have any words in common should get a score of 0.

# Deliverable
Created a web app using Flask web framework that allows users to input 2 texts and generates a Cosine Similarity score between 0 and 1.

# Considerations while building solution
>Do you count punctuation or only words?
>> I included only words and removed all punctuations as I did not want their presence to affect similarity score. Example, "Surprise!" and "Surprised..." should >>have same impact on similarity score despite difference in punctuation. 

> Which words should matter in the similarity comparison?
>> The commonly occuring stop words are removed as they misrepresent similarity score by inadvertently increasing it. 

> Do you care about the ordering of words?
>> For this particular challenge, I did not take into account the ordering of words as 

> What metric do you use to assign a numerical value to the similarity?


> What type of data structures should be used?

# Metric
Cosine similarity takes the angle between two non-zero vectors and calculates the cosine of that angle, and this value is known as the similarity between the two vectors. This similarity score ranges from 0 to 1, with 0 being the lowest (the least similar) and 1 being the highest (the most similar).
