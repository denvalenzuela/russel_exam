# Using python, write a program that will rank from highest to lowest the number of times a
# keyword is used in a given paragraph, and sort alphabetically if keyword has occurred
# the same number of times. (display only top 5, and not case sensitive)

if __name__ == "__main__":
    input_str = "The quick brown fox jumps the lazy dog, and jumps off hill with no one but bill"
    str_list = input_str.split()
    res = {}
    for word in str_list:
        keyvar = word.lower()
        if keyvar not in res:
            res[keyvar] = 0
        res[keyvar] += 1

    sorted_words = sorted(res.items(), key=lambda x: (-x[1], x[0]))    

    for count, row in enumerate(sorted_words):
        print(count, row[0], row[1])
        if count == 4:
            break
