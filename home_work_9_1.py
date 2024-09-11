def popular_words(text, words):

    text_words = text.lower().split()
    count_word = {word: 0 for word in words}


    for word in words:
        count_word[word]= text_words.count(word)

    # print(count_word)
    return count_word






assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
assert popular_words('''Доброго дня, ми з  України ''', ['з', 'ми','я' ]) == {'з': 1, 'ми': 1, 'я': 0}, 'Test2'

print('OK')
