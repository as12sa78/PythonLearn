vowels = set('aeiou') # Взять множество глассных.
word = input("Введите слово в котором надо найти глассные: ")  # ..и слово
found = vowels.intersection(set(word))
for vowel in found:
    print(vowel)