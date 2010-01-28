#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""金山词霸生词本转换程序
@version: $Id$
@author: U{Liu Qing}
"""
__author__ =  '刘清'
__version__=  '1.0'
__nonsense__ = ''

import os, sys, getopt, codecs, string

trans_dict = {u'æ':u'A',u'ɑ':u'B',u'ə':u'E',u'ʃ':u'F',u'ŋ':u'N',
    u'ʌ':u'Q',u'ɔ':u'R',u'ð':u'T',u'ʒ':u'V',u'θ':u'W',u'ɛ':u'Z',
	u'ˈ':u"5",u'ˌ':u'7',u'ː':u':',u'ɪ':u'I',u'ʊ':u'J',u'ɜ':u'\\',u'ɡ':u'g'}

def convert_phonetic(new_phonetic):
    for new_char in trans_dict.keys():
        if new_char in new_phonetic:
            #print new_char,type(new_char)
            #print unicode(new_char),trans_dict[new_char]
            #print new_char,trans_dict[new_char]
            new_phonetic = new_phonetic.replace(new_char,trans_dict[new_char])
    return new_phonetic

if __name__ == '__main__':
    tmp = raw_input(u'按回车键开始'.encode('gbk'))
    inputfile = codecs.open(u'D:\lhj\gsq\我的生词本.txt','r','utf-16')
    outputfile = codecs.open(u'D:\lhj\gsq\追加.txt','w','gbk')
    line_number = 0
    #outputfile = codecs.open(u'c:/Documents and Settings/lhj.WWW-61E1397B48C/桌面/我的生词本old.txt','w','gbk')
    for line in inputfile.readlines():
        if line[0:1] == '+' :
            line_number += 1
            print line_number			
            wordline = line[1:len(line)-2] + '#'
        if line[0:1] == '#':
            wordline += line[1:len(line)-2]
        if line[0:1] == '&' and line[1:]!=None:
            line = convert_phonetic(line)
            wordline += '#'
            wordline += line[1:len(line)-2]
        if line[0:1] == '$':
            wordline += '\r\n'
            try:
                outputfile.write(wordline)
            except UnicodeEncodeError:
                print wordline.encode('utf-8')
                print wordline.encode('gb18030')

    outputfile.close
    tmp = raw_input(u'按回车键退出'.encode('gbk'))

 