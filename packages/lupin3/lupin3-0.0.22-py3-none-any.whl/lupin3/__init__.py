from .func import str2date, date2str, mkdir, dateminus, dateplus, showeveryday, splitlist, cartesian, find_pd, \
    chineseloto, list_inter, list_union, list_dif, swapPositions, cos_sim_spatial, cos_sim_npdot, \
    cos_sim_cosine_similarity, pipchina, zip2file, file2zip

from .plt import Stackedbar, multiplebar, pieplt
from .ml import MachineLearningClassify
from .autoinstall import install_package

try:
    from gevent.socket import wait_read
except ImportError:
    print("gevent library not found - installing...")
    install_need_package = ["scikit-learn==1.0.2", "numpy==1.21.5", "pandas==1.2.4", "ipython== 7.31.1",
                            "matplotlib==3.5.2", "lupin3"]
    for packageinfo in install_need_package:
        install_package(packageinfo)
