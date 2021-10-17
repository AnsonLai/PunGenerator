import csv

# Word class

class Entry:
  def __init__(self, line):
    self.line = line
    self.word = list(filter(None, line.split('  ')))[0]
    self.pron = list(filter(None, line.split('  ')))[1].replace("0", "").replace("1", "").replace("2", "").split()



# Supporting Functions
def compare_sound(sound1, sound2):
  sound_list = {
    "AA": 0,
    "AE": 1,
    "AH": 2,
    "AO": 3,
    "AW": 4,
    "AY": 5,
    "B": 6,
    "CH": 7,
    "D": 8,
    "DH": 9,
    "EH": 10,
    "ER": 11,
    "EY": 12,
    "F": 13,
    "G": 14,
    "HH": 15,
    "IH": 16,
    "IY": 17,
    "JH": 18,
    "K": 19,
    "L": 20,
    "M": 21,
    "N": 22,
    "NG": 23,
    "OW": 24,
    "OY": 25,
    "P": 26,
    "R": 27,
    "S": 28,
    "SH": 29,
    "T": 30,
    "TH": 31,
    "UH": 32,
    "UW": 33,
    "V": 34,
    "W": 35,
    "Y": 36,
    "Z": 37,
    "ZH": 38
  }
  sound_matrix =[
    [5, 3, 4, 4, 4, 3, 0, 0, 0, 0, 3, 4, 3, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 3, 4, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0],
    [3, 5, 3, 3, 3, 4, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0],
    [4, 3, 5, 4, 4, 3, 0, 0, 0, 0, 3, 4, 3, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 3, 4, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0],
    [4, 3, 4, 5, 4, 3, 0, 0, 0, 0, 3, 4, 3, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 3, 4, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0],
    [4, 3, 4, 4, 5, 3, 0, 0, 0, 0, 3, 4, 3, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 3, 4, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0],
    [3, 4, 3, 3, 3, 5, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 5, 1, 1, 1, 0, 0, 0, 3, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 3, 1, 1, 1, 1, 1, 0, 0, 3, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 5, 1, 1, 0, 0, 0, 1, 2, 1, 0, 0, 3, 2, 1, 1, 1, 1, 0, 0, 1, 1, 2, 3, 1, 1, 0, 0, 1, 1, 1, 2, 3],
    [0, 0, 0, 0, 0, 0, 1, 1, 5, 4, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 3, 3, 0, 0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 4, 5, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 3, 3, 0, 0, 1, 1, 1, 1, 1],
    [3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 5, 3, 4, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0],
    [4, 3, 4, 4, 4, 3, 0, 0, 0, 0, 3, 5, 3, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 3, 4, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0],
    [3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 4, 3, 5, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 3, 1, 1, 1, 0, 0, 0, 5, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 3, 1, 1, 1, 1, 1, 0, 0, 3, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 0, 0, 1, 5, 1, 0, 0, 2, 2, 1, 1, 1, 1, 0, 0, 1, 1, 2, 2, 1, 1, 0, 0, 1, 1, 1, 2, 2],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 5, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1],
    [3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 5, 4, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0],
    [3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 4, 5, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 3, 1, 1, 0, 0, 0, 1, 2, 1, 0, 0, 5, 2, 1, 1, 1, 1, 0, 0, 1, 1, 2, 3, 1, 1, 0, 0, 1, 1, 1, 2, 3],
    [0, 0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 0, 0, 1, 2, 1, 0, 0, 2, 5, 1, 1, 1, 1, 0, 0, 1, 1, 2, 2, 1, 1, 0, 0, 1, 1, 1, 2, 2],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 5, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 5, 3, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 3, 5, 4, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 4, 5, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1],
    [3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 5, 3, 0, 0, 0, 0, 0, 0, 4, 4, 0, 0, 0, 0, 0],
    [4, 3, 4, 4, 4, 3, 0, 0, 0, 0, 3, 4, 3, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 3, 5, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 3, 1, 1, 1, 0, 0, 0, 3, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 5, 1, 1, 1, 1, 1, 0, 0, 3, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 5, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 0, 0, 1, 2, 1, 0, 0, 2, 2, 1, 1, 1, 1, 0, 0, 1, 1, 5, 4, 1, 1, 0, 0, 1, 1, 1, 3, 3],
    [0, 0, 0, 0, 0, 0, 1, 3, 1, 1, 0, 0, 0, 1, 2, 1, 0, 0, 3, 2, 1, 1, 1, 1, 0, 0, 1, 1, 4, 5, 1, 1, 0, 0, 1, 1, 1, 3, 3],
    [0, 0, 0, 0, 0, 0, 1, 1, 3, 3, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 5, 4, 0, 0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 3, 3, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 4, 5, 0, 0, 1, 1, 1, 1, 1],
    [3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 4, 3, 0, 0, 0, 0, 0, 0, 5, 4, 0, 0, 0, 0, 0],
    [3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 4, 3, 0, 0, 0, 0, 0, 0, 4, 5, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 3, 1, 1, 1, 0, 0, 0, 3, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 3, 1, 1, 1, 1, 1, 0, 0, 5, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 5, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 5, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 2, 1, 1, 0, 0, 0, 1, 2, 1, 0, 0, 2, 2, 1, 1, 1, 1, 0, 0, 1, 1, 3, 3, 1, 1, 0, 0, 1, 1, 1, 5, 4],
    [0, 0, 0, 0, 0, 0, 1, 3, 1, 1, 0, 0, 0, 1, 2, 1, 0, 0, 3, 2, 1, 1, 1, 1, 0, 0, 1, 1, 3, 3, 1, 1, 0, 0, 1, 1, 1, 4, 5],
  ]
  return sound_matrix[sound_list[sound1]][sound_list[sound2]]

def find_word(word):
  output = None
  f1 = open("cmudict-0.7b.txt", "r")
  for line1 in f1:
    entry1 = Entry(line1)
    word1 = entry1.word
    pron1 = entry1.pron
    if word1 == word.upper():
      output = entry1
  return output

def compare_pron(pron1, pron2):
  max_score = 0
  # ['K', 'AA', 'R', 'M', 'AH', 'N']
  # ['K', 'AA', 'R', 'M', 'OW', 'N', 'AA']
  if len(pron1) > len(pron2):
    s_pron = pron2
    l_pron = pron1
  else:
    s_pron = pron1
    l_pron = pron2
  
  for i in range(len(l_pron) - len(s_pron) + 1):
    score = 0
    for x in range(len(s_pron)):
      sound1 = s_pron[x]
      sound2 = l_pron[x+i]
      score = score + compare_sound(sound1, sound2)
    if score > max_score:
      max_score = score
  return max_score

def find_similar_words(word):
  results = []

  # Create an entry for the word first, by finding it in the dictionary, source pron
  entry2 = find_word(word)
  word2 = entry2.word
  pron2 = entry2.pron

  # Compare with each line
  f1 = open("cmudict-0.7b.txt", "r")
  progress = 0
  for line1 in f1:
    if progress%5000 == 0:
      print("Similar word search: " + str(round(progress/134373*100, 2)) + "%")
    progress += 1
    entry1 = Entry(line1)
    word1 = entry1.word
    pron1 = entry1.pron
    score = compare_pron(pron1, pron2)
    results.append((word1, score))
  
  results = sorted(results, key=lambda x: x[1], reverse=True)
  results = results[0:350]

  print(results)

  return results

def find_quotes(results):
  word_list = []
  quote_list = []
  for result in results:
    word_list.append(result[0])

  progress = 0
  with open('quotes_dataset.csv', newline='', encoding="utf-8") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
      if progress%5000 == 0:
        print("Quote search: " + str(round(progress/499715*100, 2)) + "%")
      progress += 1

      for word in word_list:
        if word in row[0].upper():
          print("Word: " + word + ", Quote: " + row[0])
          quote_list.append((word, row[0]))
          break

  return quote_list

def find_idioms(results):
  word_list = []
  idiom_list = []
  for result in results:
    word_list.append(result[0])


  f1 = open("idioms.txt", "r", encoding="utf-8")
  progress = 0
  for line1 in f1:
    if progress%300 == 0:
      print("Idioms search: " + str(round(progress/1545*100, 2)) + "%")
    progress += 1
    for word in word_list:
      if word in line1:
        print("Word: " + word + ", Idiom: " + line1)
        idiom_list.append((word, line1))
        break

  return idiom_list

def find_puns(word):
  results = find_similar_words(word)
  print(results)
  find_idioms(results)
  find_quotes(results)


word = "sushi"
find_puns(word)
  


