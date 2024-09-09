def count_vowels(sentence):
    count = 0
    for letter in sentence:
        if letter in "aeiou":
            count +=1
    return count






print(count_vowels("this is about school"))