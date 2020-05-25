def pangram_checker(s):

    c = [0]*26


    for i in s.lower():

        if i != " ":
            c[ord(i) - ord("a")] += 1

    for i in range(26):
        if c[i] == 0 :
            return False

    return True


sentence = "The quick brown fox jumps over the little lazy dog"

if (pangram_checker(sentence)):
    print (sentence)
    print("is a pangram")
else:
    print(sentence)
    print("is not a pangram")


sentence = "The quick brown fox jumps over the little lazy"

if (pangram_checker(sentence)):
    print (sentence)
    print("is a pangram")
else:
    print(sentence)
    print("is not a pangram")
