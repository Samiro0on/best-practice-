
def str_compression(inputstr):
    counter = 1
    output = ""
    for i in range(len(inputstr)-1):
        if inputstr[i] == inputstr[i+1]:
            counter += 1
        else:
            if counter > 1:
                output += inputstr[i] + str(counter)
                counter = 1
            else:
                output += inputstr[i]

    output += inputstr[i+1] + str(counter)

    return output

inputstr = 'kaabcaabbbccdddarrb'

print(str_compression(inputstr))

