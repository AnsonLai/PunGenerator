row = [0] * 39
matrix = []
for i in range(39):
    matrix.append(list(row))

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

sound_groups = {
    # Similar vowels
    "all_vowels": {
        "value": 3,
        "list": ["AA", "AE", "AH", "AO", "AW", "AY", "EH", "ER", "EY", "IH", "IY", "OW", "OY", "UH", "UW"]
    },
    "group_a": {
        "value": 4,
        "list": ["AA", "AH", "AO", "AW", "ER", "OY"]
    },
    "group_b": {
        "value": 4,
        "list": ["AE", "AY"]
    },
    "group_c": {
        "value": 4,
        "list": ["EH", "EY"]
    },
    "group_d": {
        "value": 4,
        "list": ["IH", "IY"]
    },
    "group_e": {
        "value": 4,
        "list": ["UH", "UW", "OW"]
    },
    # Similar consonents
    "all_consonants": {
        "value": 1,
        "list": ["B", "CH", "D", "DH", "F", "G", "HH", "JH", "K", "L", "M", "N", "NG", "P", "R", "S", "SH", "T", "TH", "V", "W", "Y", "Z", "ZH"]
    },
    "group_f": {
        "value": 3,
        "list": ["CH", "G", "JH", "K", "S", "SH", "Z", "ZH"]
    },
    "group_g": {
        "value": 3,
        "list": ["D", "DH", "T", "TH"]
    },
    "group_h": {
        "value": 3,
        "list": ["M", "N"]
    },
    "group_i": {
        "value": 3,
        "list": ["B", "F", "P", "V"]
    },
}

for key in sound_groups:
  for sound1 in sound_groups[key]["list"]:
      for sound2 in sound_groups[key]["list"]:
          matrix[sound_list[sound1]][sound_list[sound2]] = sound_groups[key]["value"]
          matrix[sound_list[sound2]][sound_list[sound1]] = sound_groups[key]["value"]

for i in range(39):
  matrix[i][i] = 5

print(matrix)