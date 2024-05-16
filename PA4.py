#Pritam Ban
#COSI 10a Spring 2023
#Programming Assignment 3
#Description:


import random
from tqdm import tqdm

# A constant which stores the length of the randomly generated text to be printed
LENGTH = 10

def main():
    """The main method"""

    words = get_word_list(r'C:\Users\banpr\Desktop\pritam_banPA3\sonnets.txt')
    # create a list of unique words
    unique_words = []
    for word in words:
        if word not in unique_words:
            unique_words.append(word)

    # create a dict where each key is a unique word and each value is an int index
    word_index = {word: index for index, word in enumerate(unique_words)}
    num_words = len(unique_words)

    # Create a 2D array called count[word][next]
    count = [[0] * num_words for i in range(num_words)]

    # iterate through the list of words, tallying up each time a word appears after another one. The result of this
    # function is that the matrix “prob” is filled out with word counts
    count = get_next_word_counts(words, count, word_index)

    # Compute the actual probability for each word. This edits the “prob” matrix so that it is storing actual
    # probabilities rather than just word counts.
    prob = compute_probabilities(count, num_words)

    # Generate text using the computed probabilities
    make_text(unique_words, prob)

def make_text(unique_words, prob) -> str:
  """Given a list of unique words, a dict mapping words to int indexes, and a probability matrix,
  return a string generated using the given probability matrix of a length denoted by the LENGTH constant."""
  for i in range(LENGTH):
    index = random.randint(0,len(unique_words))
    word = unique_words[get_next_word(index, unique_words, prob)]
    if word != None: 
      print(word.upper(), end=" ")
    else:
       break
    i+=1
        
def compute_probabilities(prob, num_words) -> list[list]:
  """Takes in a 2D list called prob and an int length where the size of the 2D list is length x length.
  Computes the probability of any given word showing up after another."""

  for i in tqdm(range(len(prob))):
    for j in range(len(prob[i])):
        prob[i][j] = prob[i][j] / num_words
  return prob

def get_next_word_counts(words, mat, index) -> list[list]:
  """Takes as a parameter a list of words of length n, a 2D list of size n x n,
  and a dictionary where the keys are a word and the values are an int index.
  The matrix should be indexed as mat[current_word][next_word].
  This function tallies up the number of times a word is followed by another word.""" 

  for i in range(len(words) - 1):
    word1 = words[i]
    word2 = words[i + 1]
    word1_index = index[word1]
    word2_index = index[word2]
    mat[word1_index][word2_index] += 1
  return mat

def get_next_word(cur_word, unique_words, dist) -> str:
  """Given a list of unique words and dist, a probability
  distribution, return a word chosen at random based on that distribution"""
  return unique_words.index(random.choices(unique_words, weights=dist[cur_word], k=len(unique_words))[0])

def get_word_list(filename) -> list:
  """Given a string filename, return the contents of the file as a list of words."""
  words = {}
  words = open(filename).read().split()
  return words
  # TODO: Make sure to strip lines by "\n" characters
    
if __name__ == '__main__':
  main()
