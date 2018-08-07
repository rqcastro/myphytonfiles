def word_distribution(s):

    word_list = s.lower().split()

    #remove last punctuation char (if any) from each word
    count = 0
    for each_word in word_list:
        if not each_word[len(each_word)-1].isalpha():
            word_list[count] = each_word[:len(each_word)-1]
        count = count + 1

    #print(word_list)

    wordcount = dict()
    count = 0
    for element in word_list:
        if element in wordcount:
            wordcount[element] = wordcount[element] + 1
        else:
            wordcount.setdefault(element, 1)

    return wordcount

print(word_distribution("Hello. How are you? Please say hello if you don’t love me!"))
print(word_distribution("That's when I saw Jane (John's sister)!"))