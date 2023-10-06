import random


def create_line():
    first_character = chr(random.randint(65, 90))
    key = random.randint(0, 100)

    if key <= 10:
        lens = random.randint(1, 2)
    elif key >= 10 and key <= 80:
        lens = random.randint(3, 9)
    else:
        lens = random.randint(10, 20)
    line = ""
    for i in range(lens):
        word = create_word()
        if word:
            if not i:  # 首个单词  i != 0
                word = word.capitalize()
            line += word
    if line[-2] == ',':
        pass
    else:
        line = line[:-1]
        line += '.\n'
    return line




def create_word():
    yuan = ["a", "e", "i", "o", "u"]
    key = random.randint(0, 100)
    if key <= 10:
        lens = random.randint(1, 2)
    elif key >= 10 and key <= 80:
        lens = random.randint(3, 9)
    else:
        lens = random.randint(10, 20)
    word = ""
    for i in range(lens):
        word += chr(random.randint(97, 122))
        for y in yuan:
            if y in word:
                if key >= 30:  # 是否有逗号
                    return word + " "
                else:
                    return word + ', '
    return None


if __name__ == "__main__":
    key = random.randint(500, 600)
    print(create_line())

