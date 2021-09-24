# Exercise 25: Even More Practice


# 将句子拆分成单词
def break_words(stuff):
    """This function will break up words for us."""
    # split(): 将句子拆分成单词
    words = stuff.split(' ')
    return words


# 对字符串排序
def sort_words(words):
    """Sorts the words."""
    # sorted(): 对字符串排序
    return sorted(words)


# 第一个字符串出列表
def print_first_word(words):
    """Prints the first word after poping it off."""
    # pop(): 列表的最后一项出列表  ==  pop(-1)
    # pop(i): 列表的第i个项出列表
    word = words.pop(0)
    print(word)


# 最后一个字符串出列表
def print_last_word(words):
    """Prints the last word after popping it off."""
    # pop(-1): 列表的最后一个项出列表
    word = words.pop(-1)
    print(word)


# 将句子拆分成单词并对单词排序
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)  # 将句子打乱成单词
    return sort_words(words)  # 将字符串排序


# 将句子拆分成单词, 并将第一个和最后一个项出队列
def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)  # 将句子拆分成单词
    print_first_word(words)  # 列表的第一个项出列表
    print_last_word(words)  # 列表的最后一个项出列表


# 句子拆分成单词并再排序, 并将第一个项和最后一个项出列表
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)  # 将句子拆分成单词并对单词排序
    print_first_word(words)  # 列表第一个项出列表
    print_last_word(words)  # 列表最后一个项出列表


# Conversation
'''
>>> import ex25
>>> sentence = "All good things come to those who wait."
>>> words = ex25.break_words(sentence)
>>> words
['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']
>>> sorted_words = ex25.sort_words(words)
>>> sorted_words
['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
>>> ex25.print_first_word(words)
All
>>> ex25.print_last_word(words)
wait.
>>> words
['good', 'things', 'come', 'to', 'those', 'who']
>>> ex25.print_first_word(sorted_words)
All
>>> ex25.print_last_word(sorted_words)
who
>>> sorted_words
['come', 'good', 'things', 'those', 'to', 'who']
>>> ex25.print_first_word(sorted_words)
All
>>> ex25.print_last_word(sorted_words)
who
>>> sorted_words
['come', 'good', 'things', 'those', 'to', 'wait.']
>>> sorted_words = ex25.sort_sentence(sentence)
>>> sorted_words
['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
>>> ex25.print_first_and_last(sentence)
All
wait.
>>> ex25.print_first_and_last_sorted(sentence)
All
who
'''
