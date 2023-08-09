def search4vowels():
    """Выводит гласные, найденные во введенном слове."""
    vowels = set('aeiou')
    word = input("Введите слово в котором надо найти глассные: ")
    found = vowels.intersection(set(word))
    for vowel in found:
        print(vowel)