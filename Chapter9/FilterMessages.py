from pyexpat.errors import messages


def filter_messages(messages):
    filtered_messages = []
    bad_word_count = []

    for message in messages:
        word_list = message.split()
        non_bad_words = []
        counter = 0
        for word in word_list:
            #Checks if word dang is used
            if word == "dang":
                counter+=1
            else:
                non_bad_words.append(word)

        #Add clean message to filtered messages
        filtered_messages.append(" ".join(non_bad_words))

        #Add the bad word count to our list
        bad_word_count.append(counter)


    return filtered_messages, bad_word_count

def main():
    test = ["darn it", "this dang thing won't work", "lets fight one on one"]
    filtered_messages, bad_word_count = filter_messages(test)
    print(filtered_messages)
    print(bad_word_count)

main()




