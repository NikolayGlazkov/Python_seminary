def vihipuh(some_str, return_counts=False):
    
    array = some_str.replace("-", "").split(" ")
    vse_gls = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
    counts = []
    for word in array:
        word_counts = {}
        for letter in word:
            if letter in vse_gls:
                if letter in word_counts:
                    word_counts[letter] += 1
                else:
                    word_counts[letter] = 1
        counts.append(word_counts)

    all_counts_equal = all(counts[0] == count for count in counts)
    
    if return_counts:
        return all_counts_equal, counts
    else:
        return all_counts_equal

my_str = "пара-ра-рам рам-пам-папам па-ра-па-дам"
result, counts = vihipuh(my_str, return_counts=True)
print(result, counts)
