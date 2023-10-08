filename = input("please input filename:")
with open(filename) as file:
    file_lines = file.readlines()
    print(f'Title:{file_lines[0]}\n')
    Word_Freq = {key: 0 for key in range(1, 21)}
    word_count = 0
    sent_count = 0
    para_count = 0
    eva_appear = 0
    for para in file_lines[1:]:
        para_count += 1  # 数段落
        lines = para.split('.')
        for line in lines:
            if line:  # 确认有
                sent_count += 1
                words = line.split()
                for word in words:
                    if word:
                        word_count += 1
                        if word == "eva" or word == "EVA":
                            eva_appear += 1
                        #  检测单词长度
                        lens = len(word)
                        Word_Freq[lens] += 1
    print(f"Word Count: {word_count}\n")
    print(f"Sent Count: {sent_count}\n")
    print(f"Para Count: {para_count}\n")
    print(f"EVA Count: {eva_appear}\n")
    print('Word Freq:\n')
    for key in Word_Freq:
        print(f"{key}.", Word_Freq[key])



