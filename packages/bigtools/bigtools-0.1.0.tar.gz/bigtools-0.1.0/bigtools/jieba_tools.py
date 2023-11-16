# -*- coding: UTF-8 -*-
# @Time : 2023/11/15 18:18 
# @Author : 刘洪波
import jieba
from bigtools.stopwords import stopwords


def get_keywords_from_text(text: str):
    """从文本中获取关键词"""
    text_l = jieba.cut(text)
    text_l = [i.strip() for i in text_l]
    key_words = []
    for i in text_l:
        if i not in stopwords:
            key_words.append(i)
    return key_words
