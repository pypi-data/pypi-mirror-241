from .func import str2date, date2str, mkdir, dateminus, dateplus, showeveryday, splitlist, cartesian, find_pd, \
    chineseloto, list_inter, list_union, list_dif, swapPositions, cos_sim_spatial, cos_sim_npdot, \
    cos_sim_cosine_similarity, pipchina, zip2file, file2zip

from .plt import Stackedbar, multiplebar, pieplt
from .ml import MachineLearningClassify
from .autoinstall import install_package

try:
    from gevent.socket import wait_read
except ImportError:
    install_need_package = ["lupin3==0.0.25"]
    for packageinfo in install_need_package:
        install_package(packageinfo)
