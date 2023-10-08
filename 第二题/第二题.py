import random

total_chars = random.randint(500, 600)
def create_line():

    key = random.randint(0, 100)  # 概率

    if key <= 10:
        lens = random.randint(1, 2)
    elif key >= 10 and key <= 80:
        lens = random.randint(3, 9)
    else:
        lens = random.randint(10, 20)
    line = ""
    i = 0
    while i <= lens:
        word = create_word()
        if word:
            if not i:  # 首个单词  i != 0
                word = word.capitalize()
            line += word
            i += 1
    if line[-2] == ',':
        line = line[:-2]
        line += '. '
    else:
        line = line[:-1]
        line += '. '
    return line


def create_word():
    global total_chars
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
            if key >= 34:  # 是否有逗号 34%概率
                total_chars -= lens  #
                return word + " "
            else:
                return word + ', '
    return None


def create_title():
    yuan = ["a", "e", "i", "o", "u"]
    title = ''
    lens = random.randint(1, 5)
    for i in range(lens):
        title += chr(random.randint(97, 122))
    for y in yuan:
        if y in title:
            return title.upper()
    else:
        return create_title()


def create_para():
    para = ''


    global total_chars
    while total_chars > 0:
        key = random.randint(0, 100)
        if key <= 30:
            para += create_line() + '\n' + "    "
        else:
            para += create_line()
    return para



if __name__ == "__main__":
    key = random.randint(500, 600)
    title = create_title()
    para = create_para()
    print(para)
    file = open("1.txt", "w")
    file.write(title + "\n" + para)

    file.flush()
    file.close()
    file = open("2.txt", "w")
    file.write(title + "\n" + para)

    file.flush()
    file.close()

