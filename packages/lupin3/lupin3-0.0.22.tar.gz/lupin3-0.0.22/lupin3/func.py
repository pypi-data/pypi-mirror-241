import os
import random
import zipfile
import datetime
import itertools
import numpy as np
import pandas as pd
from scipy import spatial
from sklearn.metrics.pairwise import cosine_similarity
from IPython.core.interactiveshell import InteractiveShell

InteractiveShell.ast_node_interactivity = "all"


def str2date(datestring):
    try:
        return datetime.datetime.strptime(datestring, '%Y-%m-%d %H:%M:%S')
    except:
        return datetime.datetime.strptime(datestring, '%Y-%m-%d')


def date2str(datestring, second = False):  # only save date
    if second == True:
        return str(datetime.datetime.strftime(datestring, '%Y-%m-%d  %H:%M:%S'))
    return str(datetime.datetime.strftime(datestring, '%Y-%m-%d'))

def mkdir(path):
    folder = os.path.exists(path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print("---  new folder...  ---")
        print("---  OK  ---")

    else:
        print("---  There is this folder!  ---")


def dateminus(startdate, daynum):
    if type(startdate) == str:
        return date2str(str2date(startdate) - datetime.timedelta(days=daynum))
    elif type(startdate) == datetime.datetime:
        return date2str(startdate - datetime.timedelta(days=daynum))


def dateplus(startdate, daynum):
    if type(startdate) == str:
        return date2str(str2date(startdate) + datetime.timedelta(days=daynum))
    elif type(startdate) == datetime.datetime:
        return date2str(startdate + datetime.timedelta(days=daynum))


def showeveryday(startday, endday):  # input string of date
    startd = str2date(startday)
    endd = str2date(endday)
    if startd > endd:
        print('startday must more than endday')
    else:
        daynum = (endd - startd).days
    outputdays = []
    for dayn in range(daynum + 1):
        newdate = dateplus(startd, dayn)
        outputdays.append(newdate)
    return outputdays


def splitlist(listsample, size=1000):
    donelist = [listsample[i:i + size] for i in range(0, len(listsample), size)]
    return donelist


def cartesian(l1, l2):
    carte = []
    for i in itertools.product(l1, l2):
        carte.append(i)
    df = pd.DataFrame(carte)
    return df


def find_pd(word, pd):
    index_ = []
    for num_row in range(pd.shape[0]):  # 5
        for num_col in range(pd.shape[1]):  # 4
            if pd.iloc[num_row, num_col] == word:
                # print([num_row, num_col])
                index_.append([num_row, num_col])
            else:
                pass
    return index_


def chineseloto(N=1000):
    def rand_num():
        n_l, e_l = [], []
        while len(n_l) < 5:
            t = random.randint(1, 35)
            if t in n_l:
                pass
            else:
                n_l.append(t)
        n_l.sort()
        while len(e_l) < 2:
            t = random.randint(1, 12)
            if t in e_l:
                pass
            else:
                e_l.append(t)
        e_l.sort()
        l = n_l + e_l
        return l

    sum_ = []
    for n in range(N):
        sum_.append(str(rand_num()))

    dict_ = {}
    for key in sum_:
        dict_[key] = dict_.get(key, 0) + 1

    def top_n_scores(n, score_dict):
        lot = [(k, v) for k, v in dict_.items()]  # make list of tuple from scores dict
        nl = []
        while len(lot) > 0:
            nl.append(max(lot, key=lambda x: x[1]))
            lot.remove(nl[-1])
        return nl[0:n]

    return top_n_scores(4, dict_)

def list_inter(a,b):
    return list(set(a).intersection(set(b)))

def list_union(a,b):
    return list(set(a).union(set(b)))

def list_dif(a,b):
    return list(set(b).difference(set(a)))


def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list



def cos_sim_spatial(vec1,vec2):
    return 1 - spatial.distance.cosine(vec1, vec2)

def cos_sim_npdot(vec1,vec2):
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    return vec1.dot(vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

def cos_sim_cosine_similarity(vec1,vec2):
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    return  cosine_similarity(vec1.reshape(1, -1), vec2.reshape(1, -1))[0][0]


def pipchina():
    print('douban')
    print('-i http://pypi.douban.com/simple --trusted-host pypi.douban.com')
    print('------')
    print('tsinghua')
    print('-i https://pypi.tuna.tsinghua.edu.cn/simple some-package')
    print('------')
    print('aliyun')
    print('-i http://mirrors.aliyun.com/pypi/simple/')
    print('------')
    print('ustc')
    print('-i https://pypi.mirrors.ustc.edu.cn/simple/')
    print('------')
    print('hustunique')
    print('-i http://pypi.hustunique.com/simple/')
    print('------')
    print('sjtu')
    print('-i https://mirror.sjtu.edu.cn/pypi/web/simple/')




def zip2file(zip_path):
    save_path = zip_path[:(zip_path.rfind('/') + 1)]
    print(save_path)
    file = zipfile.ZipFile(zip_path)
    print('Start decompress...')
    file.extractall(save_path)
    print('decompress is over.')
    file.close()


def file2zip(input_path):
    if input_path.count('/') == 1:
        print("input_path is wrong, should be ./AAA/")
    else:
        output_path = input_path[:-1] + '.zip'
    print('Start compress...')
    zip = zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED)
    for path, dirnames, filenames in os.walk(input_path):
        # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
        fpath = path.replace(path, '')

        for filename in filenames:
            zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
    print('compress is over.')
    zip.close()