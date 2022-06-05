# def file_read():
#     content_array = []
#     with open(fname) as f:
#         # Content_list is the list that contains the read lines.
#         for line in f:
#             # if line !='\n':
#             #     print(line)
#             strippedLine = line.strip()
#             content_array.append(strippedLine)
#         print(content_array)
#         print(len(content_array))

content_array = []
with open('l1_test1_questions.txt') as f:
    for index, line in enumerate(f):
#        print("Line {}: {}".format(index, line.strip()))
        sline = line.strip()
        content_array.append(sline)

#print(content_array)

quesNum = 1
score = 0

while quesNum < 90:
    print("\n\nScore: " + str(score))
    print("\nQuestion: " + content_array[7*quesNum])
    print("(1) "+ content_array[7*quesNum+1])
    print("(2) " + content_array[7*quesNum + 2])
    print("(3) " + content_array[7*quesNum + 3])
    print("(4) " + content_array[7*quesNum + 4])
#    print(int(content_array[7*quesNum+5]))
    ans = input("What is your answer? ")

    if (ans==content_array[7*quesNum+5]):
        print("Your Answer is correct!\n")
        score = score+1
    else:
        print("Sorry, that's the wrong answer! Correct answer is "+content_array[7*quesNum+5])
        print("\n")

    quesNum += 1





#file_read('l1_test1_questions.txt')



