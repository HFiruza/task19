def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        if root_word.lower() in i.lower() or i.lower() in root_word.lower():
            same_words.append(i)
    return same_words

result_1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result_2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result_1)
print(result_2)


# def single_root_words(root_word, *other_words):
#     same_words = []
#     upper_word = root_word.upper()
#     for word in other_words:
#         if upper_word in word.upper():
#             same_words.append(word)
#     return same_words