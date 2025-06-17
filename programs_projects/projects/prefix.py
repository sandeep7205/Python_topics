# find the longest prefix of the words list
 
# array = ['flow', 'flower', 'flown']
# array = ["flower", "flow", "flight"]
array = ["interview", "intermediate", "internal", "internet"]


f_word = array[0]
print(f"first index value is [{f_word}] \n\n")
array.pop(0)
# new_word = ''
for index, arr in enumerate(array):
    print(f"\n-----index - {index} and arr - {arr}-----\n")
    while f_word:
        print(f"f_word - {f_word}")
        if f_word == '':
            break
        else:
            if f_word in arr:
                f_word = f_word
                break
            else:
                f_word = f_word[:-1]

print(f"\n\n prefix word ->>>>\t [{f_word}]")