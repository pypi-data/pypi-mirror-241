import sys
import re
import numpy as np
import pickle
from bisect import bisect_left
import time
from tqdm import tqdm,trange

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import matplotlib.pyplot as plt
import random

import matplotlib.font_manager

import pickle
import shutil, os
from io import BytesIO


MAX_UNICODE_INT = int('110000',16)


class TranslateError(Exception):
    """Base class for other exceptions"""
    pass


def savep(var,fn):    
    with open(fn,'wb+') as f:
        pickle.dump(var,f)


def loadp(fn):
    with open(fn,'rb') as f:
        ret = pickle.load(f)
    return ret


def display_class_tree(obj, show_sys=False):
    def print_members(cls):
        print(f"\n{cls.__name__} Members:")

        # 分别存储方法和属性
        methods = []
        properties = []

        for attr_name in dir(cls):
            if show_sys or not attr_name.startswith('_'):
                attr = getattr(cls, attr_name)
                
                # 检查成员是方法还是属性
                if callable(attr):
                    methods.append(attr_name)
                else:
                    properties.append(attr_name)
        # 打印属性及其值（如果有）
        print("  Properties:")
        for property in properties:
            value = getattr(obj, property, None)
            print(f"    {property}: {value}")

        # 打印方法
        print("  Methods:")
        for method in methods:
            print(f"    {method}")

    cls = obj.__class__
    print(f"Class Tree for {obj}:")

    # 显示类的层次结构
    for c in cls.__mro__:
        print_members(c)


def is_chinese(uchar):
    """判断一个unicode是否是汉字"""
    if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
        return True
    else:
        return False
    

def all_chinese(s):
    for s_i in s:
        if not is_chinese(s_i):
            return False
    return True


def label_char(uchar):
    #汉字    
    # or uchar==u'\u3007'
    uord = ord(uchar)
    if (uord>=13312 and uord<=19903 or uord>=19968 and uord<=40956 or
        uord>=63744 and uord<=64109 or uord>=64112 and uord<=64217 or
        uord>=127504 and uord<=127506 or uord>=127508 and uord<=127547 or
        uord>=127552 and uord<=127560 or uord>=131072 and uord<=173789 or
        uord>=173824 and uord<=177972 or uord>=177984 and uord<=178205 or
        uord>=178208 and uord<=183969 or uord>=183984 and uord<=191456 or
        uord>=194560 and uord<=195101 or uord>=196608 and uord<=201546 ):
        return 'CJK'

    if uchar >= u'\u0041' and uchar<=u'\u005a' or uchar >= u'\u0061' and uchar<=u'\u007a' :
        return 'EN'
    
    if (uchar >= u'\u0030' and uchar<=u'\u0039' or uchar >= u'\uff10' and uchar<=u'\uff19' or
       uchar >= u'\u24ea' and uchar<=u'\u24fe' or uchar >= u'\u2460' and uchar<=u'\u249b' ):
        return 'DIGIT'    
    #汉语标点 + 常用英语标点
    if (uchar >= u'\u3000' and uchar<=u'\u3020' or uchar >= u'\u2018' and uchar<=u'\u201f' or
        uchar >= u'\uff01' and uchar<=u'\uff1f' or uchar ==u'\u2014' or uchar ==u'\u2026' or
        uchar ==u'\uff5e' or uchar >= u'\uff62' and uchar<=u'\uff63' or uchar in ['.',',',';','!','?',':']):
        return '标点'
    
    if (uchar >= u'\u0020' and uchar<=u'\u002f' or uchar >= u'\u003a' and uchar<=u'\u0040' or
        uchar >= u'\u005b' and uchar<=u'\u0060' or uchar >= u'\u007b' and uchar<=u'\u007e' or
        uchar >= u'\u00a1' and uchar<=u'\u00bf' or uchar ==u'\u00d7' or uchar ==u'\u00f7' ):
        return 'SIGN'
    #部首
    if (uchar >= u'\u2e80' and uchar<=u'\u2e99f' or uchar >= u'\u2e9b' and uchar<=u'\u2ef3' or
        uchar >= u'\u2f00' and uchar<=u'\u2fd5'):
        return '部首'
    
    if uchar >= u'\u0000' and uchar<=u'\u001f' or uchar >= u'\u007f' and uchar<=u'\u009f' :
        return '<control>'

    if (uchar >= u'\u00c0' and uchar<=u'\u00d6' or
        uchar >= u'\u00d8' and uchar<=u'\u00f6' or uchar >= u'\u00f8' and uchar<=u'\u02af'):
        return 'LATIN'    
    #未知
    return 'Unknown'


def label_str(s):
    return [label_char(c) for c in s]


def peek(dat,n=10,sn=100):
    ty = type(dat)
    if ty is str:
        print(dat[0:sn],end ='')
    elif ty is list:
        print('[',end='')
        for i in dat[0:n]:
            peek(i)
            print(', ',end='')
        if len(dat)>n:
            print('...',end='')
        print(']')
    elif ty is set:
        print('(',end='')
        for i in dat[0:n]:
            peek(i)
            print(', ')
        if len(dat)>n:
            print('...',end='')
        print(')')
    elif ty is dict:
        print('{',end ='')
        for k,v in dat.items():
            peek(k)            
            print(':',end='')
            peek(v)
            print(', ')
        if len(dat)>n:
            print('...',end='')
        print('}',end='')
    else:
        peek(str(dat))


def split_list(listTemp, n):
    for i in range(0, len(listTemp), n):
        yield listTemp[i:i + n]


def get_fn(pre,sub,i,n):
    return pre+f'_{i:0{n}d}'+sub


def center_bbox(from_bbox,wh):
    size_w,size_h = wh
    cx,cy = size_w/2, size_h/2
    dx,dy = cx-(from_bbox[0]+from_bbox[2])/2 ,cy-(from_bbox[1]+from_bbox[3])/2
    return (dx,dy), size_w>=from_bbox[2]-from_bbox[0] and size_h>=from_bbox[3]-from_bbox[1]


def image_char(char,image_size, font_size,font_path = 'C:\\Windows\\Fonts\\msyh.ttc'):
    img = Image.new("RGB", (image_size, image_size), (255,255,255))
    #print(img.getpixel((0,0)))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path, font_size)
    bbox = font.getbbox(char)
    (dx,dy),in_box = center_bbox(bbox,(image_size,image_size))
    draw.text((dx,dy), char, (0,0,0),font=font)
    #img.show()
    return img,in_box


def get_font_wh(font_path, font_size, char):
    font = ImageFont.truetype(font_path, font_size)
    bbox = font.getbbox(char)
    return bbox[2]-bbox[0], bbox[3]-bbox[1]


def get_font_maxwh(font_path,font_size):
    font = ImageFont.truetype(font_path, font_size)
    maxw,maxh = 0,0
    for i in range(MAX_UNICODE_INT):
        bbox = font.getbbox(chr(i))
        w,h = bbox[2]-bbox[0], bbox[3]-bbox[1]
        if w>maxw: maxw=w
        if h>maxh: maxh=h
    return maxw,maxh


if (sys.version_info[0] < 3):
    import urllib2
    import urllib
    import HTMLParser
else:
    import html.parser
    import urllib.request
    import urllib.parse
    import html


USER_AGENTS = [
    "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5"
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60",
    "Opera/8.0 (Windows NT 5.1; U; en)",
    "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; en) Opera 9.50",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36",
]


def unescape(text):
    if (sys.version_info[0] < 3):
        parser = HTMLParser.HTMLParser()
    else:
        parser = html.parser.HTMLParser()
    return (html.unescape(text))


def translate(to_translate, to_language="auto", from_language="auto"):
    """Returns the translation using google translate
    you must shortcut the language you define
    (French = fr, English = en, Spanish = es, etc...)
    if not defined it will detect it or use english by default
    Example:
    print(translate("salut tu vas bien?", "en"))
    hello you alright?
    """
    errflg = False
    header = {'User-Agent': random.choice(USER_AGENTS)}
    try:
        base_link = "http://translate.google.cn/m?tl=%s&sl=%s&q=%s"
        if (sys.version_info[0] < 3):
            to_translate = urllib.quote_plus(to_translate)
            link = base_link % (to_language, from_language, to_translate)
            request = urllib2.Request(link, headers=header)
            raw_data = urllib2.urlopen(request).read()
        else:
            to_translate = urllib.parse.quote(to_translate)
            link = base_link % (to_language, from_language, to_translate)
            request = urllib.request.Request(link, headers=header)
            raw_data = urllib.request.urlopen(request, timeout=2).read()
    except BaseException as e:
        errflg = True
        print(e)
        print(type(e))

    if not errflg:
        data = raw_data.decode("utf-8")
        # expr = r'class="t0">(.*?)<'
        expr = r'class="result-container">(.*?)<'
        re_result = re.findall(expr, data)
        if (len(re_result) == 0):
            result = ""
        else:
            result = unescape(re_result[0])
        return (result)
    else:
        raise  TranslateError()    
        

def translate_com(to_translate, to_language="auto", from_language="auto"):
    """Returns the translation using google translate
    you must shortcut the language you define
    (French = fr, English = en, Spanish = es, etc...)
    if not defined it will detect it or use english by default
    Example:
    print(translate("salut tu vas bien?", "en"))
    hello you alright?
    """
    errflg = False
    header = {'User-Agent': random.choice(USER_AGENTS)}
    try:
        base_link = "http://translate.google.com/m?tl=%s&sl=%s&q=%s"
        if (sys.version_info[0] < 3):
            to_translate = urllib.quote_plus(to_translate)
            link = base_link % (to_language, from_language, to_translate)
            request = urllib2.Request(link, headers=header)
            raw_data = urllib2.urlopen(request).read()
        else:
            to_translate = urllib.parse.quote(to_translate)
            link = base_link % (to_language, from_language, to_translate)
            request = urllib.request.Request(link, headers=header)
            raw_data = urllib.request.urlopen(request, timeout=2).read()
    except BaseException as e:
        errflg = True
        print(e)
        print(type(e))

    if not errflg:
        data = raw_data.decode("utf-8")
        # expr = r'class="t0">(.*?)<'
        expr = r'class="result-container">(.*?)<'
        re_result = re.findall(expr, data)
        if (len(re_result) == 0):
            result = ""
        else:
            result = unescape(re_result[0])
        return (result)
    else:
        raise  TranslateError()    
       

def getUrlData(url, timeout=10, try_times = 5):
    header = {'User-Agent': random.choice(USER_AGENTS)}    
    while try_times >-1:
        try:
            req = urllib.request.Request(url=url, headers=header, method='GET')
            htmlcode = urllib.request.urlopen(req, timeout=timeout)#.read()
            content = htmlcode.read().decode('utf-8',errors='ignore')
            return content
        except Exception as e:
            try_times-=1
            if try_times==4:
                time.sleep(10)
            if try_times==3:
                time.sleep(20)
            if try_times==2:
                time.sleep(30)
            if try_times==1:
                time.sleep(40)
            if try_times==0:
                time.sleep(60)
            time.sleep(0.1)
            if try_times == 0:
                raise e


class Sorted_dict(object):
    def __init__(self, seq=None, keyfunc=lambda v: v, valfunc=lambda v: v, ascending=True):
        super().__init__()
        if seq is None:
            seq = list()
        self.seq = list(seq)
        self.keyfunc = keyfunc
        self.valfunc = valfunc
        self.values = [self.valfunc(data) for data in self.seq]
        self.kvdict = {self.keyfunc(data): self.valfunc(data) for data in self.seq}

    def pop(self, pos=-1):
        val = self.values.pop(pos)
        item = self.seq.pop(pos)
        key = self.keyfunc(item)
        del self.kvdict[key]
        return item, key, val

    def insert(self, item):
        """Insert an item into a sorted list using a separate corresponding
           sorted keys list and a keyfunc() to extract the key from each item.
        """
        key = self.keyfunc(item)
        if key not in self.kvdict:
            val = self.valfunc(item)
            i = bisect_left(self.values, val)  # Determine where to insert item.
            self.values.insert(i, val)  # Insert key of item to keys list.
            self.seq.insert(i, item)  # Insert the item itself in the corresponding place.
            self.kvdict[key] = val
        else:
            old_val = self.kvdict[key]
            i = bisect_left(self.values, old_val)  # Determine where to insert item.
            while i < len(self.seq) and self.keyfunc(self.seq[i]) != key:
                i += 1
            if i < len(self.seq) and self.keyfunc(self.seq[i]) == key:
                self.pop(pos=i)
                self.insert(item)


class ViterbiSegment():
    def __init__(self, mode="train"):
        if mode == "work":  # 如果是工作模式，需要加载已经训练好的参数
            self.vocab, self.word_distance, self.max_word_len = pickle.load(open("model.pkl", 'rb'))

    # 加载人民日报语料https://pan.baidu.com/s/1gd6mslt,形成每个句子的词语列表，用于后面统计词语频数
    def load_corpus(self,fn=None, default_corpus_size=None):
        words_list = []
        #with open('./data/词性标注@人民日报199801.txt', 'r', encoding='utf8') as f:
        if fn is None:
            fn = './data/词性标注@人民日报199801.txt'
        with open(fn, 'r', encoding='utf8') as f:
            lines = f.readlines()
            lines = list(filter(lambda x: len(x) > 0, lines))  # 删除空行
            if default_corpus_size != None: lines = lines[:default_corpus_size]  # 测试阶段截取较小的语料
            print("文档总行数是", len(lines))
            for line in lines:
                line = line.replace('\n', '').split("  ")[1:]
                words = list(map(lambda x: x.split('/')[0], line))
                words = list(filter(lambda x: len(x) > 0, words))
                words_list.append(words)
        return words_list

    # 基于标注语料，训练一份词语的概率分布，以及条件概率分布————当然最终目的，是得到两个词语之间的连接权重(也可以理解为转移概率)
    # 转移概率越大，说明两个词语前后相邻的概率越大，那么，从前一个词转移到后一个词语花费的代价就越小。
    def train_simple(self, default_corpus_size=None):  # 简单的边权重计算方式
        self.word_num = {}
        self.word_pair_num = {}
        for words in self.load_corpus(default_corpus_size=default_corpus_size):
            words = ["<start>"] + words + ["<end>"]  # 首尾添加标记
            for word in words:
                self.word_num[word] = self.word_num.get(word, 0) + 1  # 词语频数

            for i in range(len(words) - 1):
                word_pair = (words[i], words[i + 1])  # 由于要计算的是条件概率，词语先后是需要考虑的
                self.word_pair_num[word_pair] = self.word_pair_num.get(word_pair, 0) + 1  # 词语对的频数
        # p(AB)=p(A)*p(B|A)=(num_A/num_all)*(num_AB/num_A)=num_AB/num_all。
        # 这个权重计算公式的优点是计算效率快；缺点是丢失了num_A带来的信息
        # 这个训练算法的效率不太重要；权重包含的信息量尽量大，或者说更精准地刻画词语对的分布，是最重要的事情。
        # hanlp设计了一个权重计算方式,来综合考虑num_A，num_all， num_A带来的信息。
        num_all = np.sum(list(self.word_num.values()))  # 语料中词语的总数
        word_pair_prob = {}
        for word_pair in self.word_pair_num:
            word_pair_prob[word_pair] = self.word_pair_num[word_pair] / num_all  # 词语对，也就是边出现的概率

        # 由于我们最终要做的是求最短路径，要求图的边权重是一个表示“代价”或者距离的量，即权重越大，两个节点之间的距离就越远。而前面得到的条件概率与这个距离是负相关的
        # 我们需要对条件概率求倒数，来获得符合场景要求的权重
        # 另外，由于条件概率可能是一个非常小的数，比如0.000001，倒数会很大。我们在运行维特比的时候，需要把多条边的权重加起来——可能遇到上溢出的情况。
        # 常用的避免上溢出的策略是去自然对数。
        self.word_distance = {}
        for word_pair in self.word_pair_num:
            self.word_distance[word_pair] = np.log(1 / word_pair_prob[word_pair])

        self.vocab = set(list(self.word_num.keys()))
        self.max_word_len = 0
        for word in self.vocab:
            if len(word) > self.max_word_len: self.max_word_len = len(word)

        model = (self.vocab, self.word_distance, self.max_word_len)
        pickle.dump(model, open("model.pkl", 'wb'))  # 保存参数

    def train_hanlp(self, default_corpus_size=None):
        """
        hanlp里使用的连接器权重计算方式稍微复杂一点，综合考虑了前词出现的概率，以及后词出现的条件规律，有点像全概率p(A)*p(B|A)=p(AB)
        #         dSmoothingPara 平滑参数0.1, frequency A出现的频率, MAX_FREQUENCY 总词频
        #         dTemp 平滑因子 1 / MAX_FREQUENCY + 0.00001, nTwoWordsFreq AB共现频次
        #         -Math.log(dSmoothingPara * frequency / (MAX_FREQUENCY)
        #         + (1 - dSmoothingPara) * ((1 - dTemp) * nTwoWordsFreq / frequency + dTemp));
        """

        self.word_num = {}
        self.word_pair_num = {}
        for words in self.load_corpus(default_corpus_size=default_corpus_size):
            words = ["<start>"] + words + ["<end>"]
            for word in words:
                self.word_num[word] = self.word_num.get(word, 0) + 1

            for i in range(len(words) - 1):
                word_pair = (words[i], words[i + 1])  # 由于要计算的是条件概率，词语先后是需要考虑的
                self.word_pair_num[word_pair] = self.word_pair_num.get(word_pair, 0) + 1

        num_all = np.sum(list(self.word_num.values()))
        dSmoothingPara = 0.1
        dTemp = 1 / num_all + 0.00001
        word_pair_prob = {}
        for word_pair in self.word_pair_num:
            word_A, word_B = word_pair
            # hanlp里的权重计算公式比较复杂，在查不到设计思路的情况下，我们默认hanlp作者是辛苦研制之后，凑出来的~
            word_pair_prob[word_pair] = dSmoothingPara * self.word_num.get(word_A) / num_all + \
                                        (1 - dSmoothingPara) * ((1 - dTemp) * self.word_pair_num[word_pair] / (
                    self.word_num.get(word_A) + dTemp))

        # 由于我们最终要做的是求最短路径，要求图的边权重是一个表示“代价”或者距离的量，即权重越大，两个节点之间的距离就越远。而前面得到的条件概率与这个距离是负相关的
        # 我们需要对条件概率求倒数，来获得符合场景要求的权重
        # 另外，由于条件概率可能是一个非常小的数，比如0.000001，倒数会很大。我们在运行维特比的时候，需要把多条边的权重加起来——可能遇到上溢出的情况。
        # 常用的避免上溢出的策略是去自然对数。
        self.word_distance = {}
        for word_pair in self.word_pair_num:
            word_A, _ = word_pair
            self.word_distance[word_pair] = np.log(1 / word_pair_prob[word_pair])
        #         print(self.word_distance)
        self.vocab = set(list(self.word_num.keys()))
        self.max_word_len = 0
        for word in self.vocab:
            if len(word) > self.max_word_len: self.max_word_len = len(word)

        model = (self.vocab, self.word_distance, self.max_word_len)
        pickle.dump(model, open("model.pkl", 'wb'))

    # 使用改版前向最大匹配法生成词图
    def generate_word_graph(self, text):
        word_graph = []
        for i in range(len(text)):
            cand_words = []
            window_len = self.max_word_len
            # 当索引快到文本右边界时，需要控制窗口长度，以免超出索引
            if i + self.max_word_len >= len(text): window_len = len(text) - i + 1
            for j in range(1, window_len):  # 遍历这个窗口内的子字符串，查看是否有词表中的词语
                cand_word = text[i: i + j]
                next_index = i + len(cand_word) + 1
                if cand_word in self.vocab:
                    cand_words.append([cand_word, next_index])
            if [text[i], i + 1 + 1] not in cand_words:
                cand_words.append([text[i], i + 1 + 1])  # 单字必须保留
            word_graph.append(cand_words)
        return word_graph

    # 使用维特比算法求词图的最短路径
    def viterbi_org(self, word_graph):
        path_length_map = {}  # 用于存储所有的路径，后面的临街词语所在位置，以及对应的长度
        word_graph = [[["<start>", 1]]] + word_graph + [[["<end>", -1]]]
        # 这是一种比较简单的数据结构
        path_length_map[("<start>",)] = [1, 0]  # start处，后面的临接词语在列表的1处，路径长度是0,。

        for i in range(1, len(word_graph)):
            distance_from_start2current = {}
            if len(word_graph[i]) == 0: continue

            for former_path in list(path_length_map.keys()):  # path_length_map内容一直在变，需要深拷贝key,也就是已经积累的所有路径
                # 取出已经积累的路径，后面的临接词语位置，以及路径的长度。
                [next_index_4_former_path, former_distance] = path_length_map[former_path]
                former_word = former_path[-1]
                later_path = list(former_path)
                if next_index_4_former_path == i:  # 如果这条路径的临接词语的位置就是当前索引
                    for current_word in word_graph[i]:  # 遍历词图数据中，这个位置上的所有换选词语，然后与former_path拼接新路径
                        current_word, next_index = current_word
                        new_path = tuple(later_path + [current_word])  # 只有int, string, tuple这种不可修改的数据类型可以hash，
                        # 也就是成为dict的key
                        # 计算新路径的长度
                        new_patn_len = former_distance + self.word_distance.get((former_word, current_word), 100)

                        path_length_map[new_path] = [next_index, new_patn_len]  # 存储新路径后面的临接词语，以及路径长度

                        # 维特比的部分。选择到达当前节点的路径中，最短的那一条
                        if current_word in distance_from_start2current:  # 如果已经有到达当前词语的路径，需要择优
                            if distance_from_start2current[current_word][1] > new_patn_len:  # 如果当前新路径比已有的更短
                                distance_from_start2current[current_word] = [new_path, new_patn_len]  # 用更短的路径数据覆盖原来的
                        else:
                            distance_from_start2current[current_word] = [new_path, new_patn_len]  # 如果还没有这条路径，就记录它
        sortest_path = distance_from_start2current["<end>"][0]
        sortest_path = sortest_path[1:-1]
        return sortest_path

    def viterbi(self, word_graph, timeout=0):
        time_start = time.time()
        word_graph = [[["<start>", 1]]] + word_graph + [[["<end>", -1]]]

        # 准备数据
        pathes = [(("<start>",), 1, 0)]
        valfunc = lambda tup: tup[2]
        keyfunc = lambda tup: tup[0]
        sdict = Sorted_dict(seq=pathes, keyfunc=keyfunc, valfunc=valfunc)

        while len(sdict.seq) > 0 and sdict.seq[0][0][-1] != '<end>':
            if timeout > 0 and time.time() - time_start > timeout:
                return ()
            # 在集合中找出最短路径
            path_item, key, val = sdict.pop(pos=0)

            # 拼接所有可能的最短路径
            former_word = path_item[0][-1]
            for word in word_graph[path_item[1]]:
                current_word, next_index = word
                new_path_item = ((*path_item[0], current_word), next_index,
                                 path_item[2] + self.word_distance.get((former_word, current_word), 250))
                sdict.insert(new_path_item)

        if sdict.seq[0][0][-1] == '<end>':
            sortest_path = sdict.seq[0][0][1:-1]
            return sortest_path

    # 对文本分词
    def segment_org(self, text):
        word_graph = self.generate_word_graph(text)
        shortest_path = self.viterbi_org(word_graph)
        return shortest_path

    # 对文本分词
    def segment(self, text, timeout=0):
        word_graph = self.generate_word_graph(text)
        shortest_path = self.viterbi(word_graph, timeout=timeout)
        return shortest_path

    def segment_multi(self, text, timeout=0):
        txt_list = text.split('。')
        seg_ = tuple()
        for i in range(len(txt_list) - 1):
            txt = txt_list[i]
            seg = self.segment(txt, timeout=timeout)
            seg_ += (seg + ('。',))
        txt = txt_list[-1]
        seg = self.segment(txt, timeout=timeout)
        seg_ += (seg)
        return seg_

    # 基于标注语料，对模型进行评价

    def evaluation(self):
        lines = self.load_corpus()
        N = len(lines)

        time_used = np.zeros(N)
        text_len = np.zeros(N)

        succeed = 0
        time_out_n = 0

        # for i in trange(100):
        for i in range(len(lines)):
            # print(i, end=', ')
            line = lines[i]
            text = ''.join(line)
            text_len[i] = len(text)
            st = time.time()
            seg = self.segment_multi(text, timeout=5)
            time_used[i] = time.time() - st

            if tuple(line) == seg:
                succeed += 1
            elif seg == ():
                time_out_n += 1
                print()
                print('-' * 80)
                print(i, text_len[i])
                print(line)
                print(seg)
            else:
                #print()
                #print('-' * 80)
                #print(i, text_len[i])
                #print(line)
                #print(seg)
                pass

        print('+' * 80)
        print(succeed / len(lines))
        print(time_out_n / len(lines))
        #plt.plot(text_len, time_used)



def block(ch):
    '''
    Return the Unicode block name for ch, or None if ch has no block.

    >>> block(u'a')
    'Basic Latin'
    >>> block(unichr(0x0b80))
    'Tamil'
    >>> block(unichr(0xe0080))

    '''

    assert isinstance(ch, str) and len(ch) == 1, repr(ch)
    cp = ord(ch)
    for start, end, name in _blocks:
        if start <= cp <= end:
            return name

def _initBlocks(text):
    global _blocks
    _blocks = []
    import re
    pattern = re.compile(r'([0-9A-F]+)\.\.([0-9A-F]+);\ (\S.*\S)')
    for line in text.splitlines():
        m = pattern.match(line)
        if m:
            start, end, name = m.groups()
            _blocks.append((int(start, 16), int(end, 16), name))

# retrieved from http://unicode.org/Public/UNIDATA/Blocks.txt
_initBlocks('''
# Blocks-12.0.0.txt
# Date: 2018-07-30, 19:40:00 GMT [KW]
# © 2018 Unicode®, Inc.
# For terms of use, see http://www.unicode.org/terms_of_use.html
#
# Unicode Character Database
# For documentation, see http://www.unicode.org/reports/tr44/
#
# Format:
# Start Code..End Code; Block Name

# ================================================

# Note:   When comparing block names, casing, whitespace, hyphens,
#         and underbars are ignored.
#         For example, "Latin Extended-A" and "latin extended a" are equivalent.
#         For more information on the comparison of property values,
#            see UAX #44: http://www.unicode.org/reports/tr44/
#
#  All block ranges start with a value where (cp MOD 16) = 0,
#  and end with a value where (cp MOD 16) = 15. In other words,
#  the last hexadecimal digit of the start of range is ...0
#  and the last hexadecimal digit of the end of range is ...F.
#  This constraint on block ranges guarantees that allocations
#  are done in terms of whole columns, and that code chart display
#  never involves splitting columns in the charts.
#
#  All code points not explicitly listed for Block
#  have the value No_Block.

# Property: Block
#
# @missing: 0000..10FFFF; No_Block

0000..007F; Basic Latin
0080..00FF; Latin-1 Supplement
0100..017F; Latin Extended-A
0180..024F; Latin Extended-B
0250..02AF; IPA Extensions
02B0..02FF; Spacing Modifier Letters
0300..036F; Combining Diacritical Marks
0370..03FF; Greek and Coptic
0400..04FF; Cyrillic
0500..052F; Cyrillic Supplement
0530..058F; Armenian
0590..05FF; Hebrew
0600..06FF; Arabic
0700..074F; Syriac
0750..077F; Arabic Supplement
0780..07BF; Thaana
07C0..07FF; NKo
0800..083F; Samaritan
0840..085F; Mandaic
0860..086F; Syriac Supplement
08A0..08FF; Arabic Extended-A
0900..097F; Devanagari
0980..09FF; Bengali
0A00..0A7F; Gurmukhi
0A80..0AFF; Gujarati
0B00..0B7F; Oriya
0B80..0BFF; Tamil
0C00..0C7F; Telugu
0C80..0CFF; Kannada
0D00..0D7F; Malayalam
0D80..0DFF; Sinhala
0E00..0E7F; Thai
0E80..0EFF; Lao
0F00..0FFF; Tibetan
1000..109F; Myanmar
10A0..10FF; Georgian
1100..11FF; Hangul Jamo
1200..137F; Ethiopic
1380..139F; Ethiopic Supplement
13A0..13FF; Cherokee
1400..167F; Unified Canadian Aboriginal Syllabics
1680..169F; Ogham
16A0..16FF; Runic
1700..171F; Tagalog
1720..173F; Hanunoo
1740..175F; Buhid
1760..177F; Tagbanwa
1780..17FF; Khmer
1800..18AF; Mongolian
18B0..18FF; Unified Canadian Aboriginal Syllabics Extended
1900..194F; Limbu
1950..197F; Tai Le
1980..19DF; New Tai Lue
19E0..19FF; Khmer Symbols
1A00..1A1F; Buginese
1A20..1AAF; Tai Tham
1AB0..1AFF; Combining Diacritical Marks Extended
1B00..1B7F; Balinese
1B80..1BBF; Sundanese
1BC0..1BFF; Batak
1C00..1C4F; Lepcha
1C50..1C7F; Ol Chiki
1C80..1C8F; Cyrillic Extended-C
1C90..1CBF; Georgian Extended
1CC0..1CCF; Sundanese Supplement
1CD0..1CFF; Vedic Extensions
1D00..1D7F; Phonetic Extensions
1D80..1DBF; Phonetic Extensions Supplement
1DC0..1DFF; Combining Diacritical Marks Supplement
1E00..1EFF; Latin Extended Additional
1F00..1FFF; Greek Extended
2000..206F; General Punctuation
2070..209F; Superscripts and Subscripts
20A0..20CF; Currency Symbols
20D0..20FF; Combining Diacritical Marks for Symbols
2100..214F; Letterlike Symbols
2150..218F; Number Forms
2190..21FF; Arrows
2200..22FF; Mathematical Operators
2300..23FF; Miscellaneous Technical
2400..243F; Control Pictures
2440..245F; Optical Character Recognition
2460..24FF; Enclosed Alphanumerics
2500..257F; Box Drawing
2580..259F; Block Elements
25A0..25FF; Geometric Shapes
2600..26FF; Miscellaneous Symbols
2700..27BF; Dingbats
27C0..27EF; Miscellaneous Mathematical Symbols-A
27F0..27FF; Supplemental Arrows-A
2800..28FF; Braille Patterns
2900..297F; Supplemental Arrows-B
2980..29FF; Miscellaneous Mathematical Symbols-B
2A00..2AFF; Supplemental Mathematical Operators
2B00..2BFF; Miscellaneous Symbols and Arrows
2C00..2C5F; Glagolitic
2C60..2C7F; Latin Extended-C
2C80..2CFF; Coptic
2D00..2D2F; Georgian Supplement
2D30..2D7F; Tifinagh
2D80..2DDF; Ethiopic Extended
2DE0..2DFF; Cyrillic Extended-A
2E00..2E7F; Supplemental Punctuation
2E80..2EFF; CJK Radicals Supplement
2F00..2FDF; Kangxi Radicals
2FF0..2FFF; Ideographic Description Characters
3000..303F; CJK Symbols and Punctuation
3040..309F; Hiragana
30A0..30FF; Katakana
3100..312F; Bopomofo
3130..318F; Hangul Compatibility Jamo
3190..319F; Kanbun
31A0..31BF; Bopomofo Extended
31C0..31EF; CJK Strokes
31F0..31FF; Katakana Phonetic Extensions
3200..32FF; Enclosed CJK Letters and Months
3300..33FF; CJK Compatibility
3400..4DBF; CJK Unified Ideographs Extension A
4DC0..4DFF; Yijing Hexagram Symbols
4E00..9FFF; CJK Unified Ideographs
A000..A48F; Yi Syllables
A490..A4CF; Yi Radicals
A4D0..A4FF; Lisu
A500..A63F; Vai
A640..A69F; Cyrillic Extended-B
A6A0..A6FF; Bamum
A700..A71F; Modifier Tone Letters
A720..A7FF; Latin Extended-D
A800..A82F; Syloti Nagri
A830..A83F; Common Indic Number Forms
A840..A87F; Phags-pa
A880..A8DF; Saurashtra
A8E0..A8FF; Devanagari Extended
A900..A92F; Kayah Li
A930..A95F; Rejang
A960..A97F; Hangul Jamo Extended-A
A980..A9DF; Javanese
A9E0..A9FF; Myanmar Extended-B
AA00..AA5F; Cham
AA60..AA7F; Myanmar Extended-A
AA80..AADF; Tai Viet
AAE0..AAFF; Meetei Mayek Extensions
AB00..AB2F; Ethiopic Extended-A
AB30..AB6F; Latin Extended-E
AB70..ABBF; Cherokee Supplement
ABC0..ABFF; Meetei Mayek
AC00..D7AF; Hangul Syllables
D7B0..D7FF; Hangul Jamo Extended-B
D800..DB7F; High Surrogates
DB80..DBFF; High Private Use Surrogates
DC00..DFFF; Low Surrogates
E000..F8FF; Private Use Area
F900..FAFF; CJK Compatibility Ideographs
FB00..FB4F; Alphabetic Presentation Forms
FB50..FDFF; Arabic Presentation Forms-A
FE00..FE0F; Variation Selectors
FE10..FE1F; Vertical Forms
FE20..FE2F; Combining Half Marks
FE30..FE4F; CJK Compatibility Forms
FE50..FE6F; Small Form Variants
FE70..FEFF; Arabic Presentation Forms-B
FF00..FFEF; Halfwidth and Fullwidth Forms
FFF0..FFFF; Specials
10000..1007F; Linear B Syllabary
10080..100FF; Linear B Ideograms
10100..1013F; Aegean Numbers
10140..1018F; Ancient Greek Numbers
10190..101CF; Ancient Symbols
101D0..101FF; Phaistos Disc
10280..1029F; Lycian
102A0..102DF; Carian
102E0..102FF; Coptic Epact Numbers
10300..1032F; Old Italic
10330..1034F; Gothic
10350..1037F; Old Permic
10380..1039F; Ugaritic
103A0..103DF; Old Persian
10400..1044F; Deseret
10450..1047F; Shavian
10480..104AF; Osmanya
104B0..104FF; Osage
10500..1052F; Elbasan
10530..1056F; Caucasian Albanian
10600..1077F; Linear A
10800..1083F; Cypriot Syllabary
10840..1085F; Imperial Aramaic
10860..1087F; Palmyrene
10880..108AF; Nabataean
108E0..108FF; Hatran
10900..1091F; Phoenician
10920..1093F; Lydian
10980..1099F; Meroitic Hieroglyphs
109A0..109FF; Meroitic Cursive
10A00..10A5F; Kharoshthi
10A60..10A7F; Old South Arabian
10A80..10A9F; Old North Arabian
10AC0..10AFF; Manichaean
10B00..10B3F; Avestan
10B40..10B5F; Inscriptional Parthian
10B60..10B7F; Inscriptional Pahlavi
10B80..10BAF; Psalter Pahlavi
10C00..10C4F; Old Turkic
10C80..10CFF; Old Hungarian
10D00..10D3F; Hanifi Rohingya
10E60..10E7F; Rumi Numeral Symbols
10F00..10F2F; Old Sogdian
10F30..10F6F; Sogdian
10FE0..10FFF; Elymaic
11000..1107F; Brahmi
11080..110CF; Kaithi
110D0..110FF; Sora Sompeng
11100..1114F; Chakma
11150..1117F; Mahajani
11180..111DF; Sharada
111E0..111FF; Sinhala Archaic Numbers
11200..1124F; Khojki
11280..112AF; Multani
112B0..112FF; Khudawadi
11300..1137F; Grantha
11400..1147F; Newa
11480..114DF; Tirhuta
11580..115FF; Siddham
11600..1165F; Modi
11660..1167F; Mongolian Supplement
11680..116CF; Takri
11700..1173F; Ahom
11800..1184F; Dogra
118A0..118FF; Warang Citi
119A0..119FF; Nandinagari
11A00..11A4F; Zanabazar Square
11A50..11AAF; Soyombo
11AC0..11AFF; Pau Cin Hau
11C00..11C6F; Bhaiksuki
11C70..11CBF; Marchen
11D00..11D5F; Masaram Gondi
11D60..11DAF; Gunjala Gondi
11EE0..11EFF; Makasar
11FC0..11FFF; Tamil Supplement
12000..123FF; Cuneiform
12400..1247F; Cuneiform Numbers and Punctuation
12480..1254F; Early Dynastic Cuneiform
13000..1342F; Egyptian Hieroglyphs
13430..1343F; Egyptian Hieroglyph Format Controls
14400..1467F; Anatolian Hieroglyphs
16800..16A3F; Bamum Supplement
16A40..16A6F; Mro
16AD0..16AFF; Bassa Vah
16B00..16B8F; Pahawh Hmong
16E40..16E9F; Medefaidrin
16F00..16F9F; Miao
16FE0..16FFF; Ideographic Symbols and Punctuation
17000..187FF; Tangut
18800..18AFF; Tangut Components
1B000..1B0FF; Kana Supplement
1B100..1B12F; Kana Extended-A
1B130..1B16F; Small Kana Extension
1B170..1B2FF; Nushu
1BC00..1BC9F; Duployan
1BCA0..1BCAF; Shorthand Format Controls
1D000..1D0FF; Byzantine Musical Symbols
1D100..1D1FF; Musical Symbols
1D200..1D24F; Ancient Greek Musical Notation
1D2E0..1D2FF; Mayan Numerals
1D300..1D35F; Tai Xuan Jing Symbols
1D360..1D37F; Counting Rod Numerals
1D400..1D7FF; Mathematical Alphanumeric Symbols
1D800..1DAAF; Sutton SignWriting
1E000..1E02F; Glagolitic Supplement
1E100..1E14F; Nyiakeng Puachue Hmong
1E2C0..1E2FF; Wancho
1E800..1E8DF; Mende Kikakui
1E900..1E95F; Adlam
1EC70..1ECBF; Indic Siyaq Numbers
1ED00..1ED4F; Ottoman Siyaq Numbers
1EE00..1EEFF; Arabic Mathematical Alphabetic Symbols
1F000..1F02F; Mahjong Tiles
1F030..1F09F; Domino Tiles
1F0A0..1F0FF; Playing Cards
1F100..1F1FF; Enclosed Alphanumeric Supplement
1F200..1F2FF; Enclosed Ideographic Supplement
1F300..1F5FF; Miscellaneous Symbols and Pictographs
1F600..1F64F; Emoticons
1F650..1F67F; Ornamental Dingbats
1F680..1F6FF; Transport and Map Symbols
1F700..1F77F; Alchemical Symbols
1F780..1F7FF; Geometric Shapes Extended
1F800..1F8FF; Supplemental Arrows-C
1F900..1F9FF; Supplemental Symbols and Pictographs
1FA00..1FA6F; Chess Symbols
1FA70..1FAFF; Symbols and Pictographs Extended-A
20000..2A6DF; CJK Unified Ideographs Extension B
2A700..2B73F; CJK Unified Ideographs Extension C
2B740..2B81F; CJK Unified Ideographs Extension D
2B820..2CEAF; CJK Unified Ideographs Extension E
2CEB0..2EBEF; CJK Unified Ideographs Extension F
2F800..2FA1F; CJK Compatibility Ideographs Supplement
E0000..E007F; Tags
E0100..E01EF; Variation Selectors Supplement
F0000..FFFFF; Supplementary Private Use Area-A
100000..10FFFF; Supplementary Private Use Area-B

# EOF
''')
