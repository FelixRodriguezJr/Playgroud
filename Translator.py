def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation


# print(translate(input("Enter a phrase: ")))

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "o":
            if letter.isupper():
                translation = translation + "Owo"
            else:
                translation = translation + "owo"
        elif letter.lower() in "u":
            if letter.isupper():
                translation = translation + "Uwu"
            else:
                translation = translation + "uwu"
        elif letter.lower() in "w":
            if letter.isupper():
                translation = translation + "Uwu"
            else:
                translation = translation + "uwu"
        elif letter.lower() in "r":
            if letter.isupper():
                translation = translation + "W"
            else:
                translation = translation + "w"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter text: ")))
