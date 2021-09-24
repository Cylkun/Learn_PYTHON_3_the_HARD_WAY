# 导入文件 ex25.py, 即导入模块, 但引用 ex25 内的函数时需要键入 ex25.
# 使用 from ex25 import * 可以不用每次键入 ex25.
import ex25

sentence = "All good things come to those who wait."
words = ex25.break_words(sentence)  # 将句子拆分成单词
words  # 在命令行中会输出列表 words
sorted_words = ex25.sort_words(words)  # 将上一步拆分的单词进行排序
sorted_words  # 在命令行中会输出列表 sorted_words
ex25.print_first_word(words)  # 将列表第一项出列表
ex25.print_last_word(words)  # 将列表最后一项出列表
words  # 在命令行中会输出列表 words
ex25.print_first_word(sorted_words)  # 将列表第一项出列表
ex25.print_last_word(sorted_words)  # 将列表最后一项出列表
sorted_words  # 在命令行中会输出列表 sorted_words
sorted_words = ex25.sort_sentence(sentence)  # 将句子拆分成单词并对单词排序
sorted_words  # 在命令行中会输出列表 sorted_words
ex25.print_first_and_last(sentence)  # 将句子拆分成单词, 并将第一个项和最后一个项出列表
ex25.print_first_and_last_sorted(sentence)  # 将句子拆分成单词再排序, 第一项和最后一项出列表


# output
'''
All
wait.
come
who
All
wait.
All
who
'''
