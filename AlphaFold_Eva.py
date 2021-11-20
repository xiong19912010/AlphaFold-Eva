#!/usr/bin/env python3
import fire
import logging
import os, sys, traceback
from fire import core
from keras.models import Sequential
from keras.layers.core import Dense
from keras.optimizers import SGD
from keras.layers import SimpleRNN, LSTM
from keras.layers import Dense, Dropout, Flatten
from keras.callbacks import EarlyStopping
from  sklearn import metrics
from sklearn.model_selection import cross_val_score
from keras.wrappers.scikit_learn import KerasRegressor

os.environ['TF_XLA_FLAGS'] = '--tf_xla_enable_xla_devices'


class EVA:
    """
    EVA: this program is to evaluate the reliability of AlphaFold 2 on unknown complex structures\n
    for detail discription, run one of the following commands:

    AlphaFold_Eva.py One -h
    AlphaFold_Eva.py Multi -h
    """
    #log_file = "log.txt"


    def One(self, total_surface: float=None,
        contact_surface:float=None,
        surface_ratio: float=None,
        dimension_ratio: float=None):
        """
        follow the input sequence strickly, where four parameters can be obtained from Chimera X
        This function is used to predict only one complex structure
        """
        foldername=os.path.dirname(sys.argv[0])
        #print(foldername +'/M.save')
        
        from keras.models import load_model
        import joblib
        import pandas as pd
        import numpy as np
        # load model (trained neural network and MinMaxScaler)
        mm = joblib.load(foldername+'/MM.save')
        model = load_model(foldername+'/NN.h5')
        input_feature=[total_surface,contact_surface,surface_ratio,dimension_ratio]
        input_feature=np.array(input_feature).reshape(-1,4)
        scale_input_feature=mm.transform(input_feature)
        pred=model.predict(scale_input_feature)
        with open(foldername+'/output.txt','w') as f:
             f.write(str(pred))
        print ('prediction value :' + str(pred))
        logging.basicConfig(format='%(asctime)s, %(levelname)-8s %(message)s',datefmt="%m-%d %H:%M:%S",level=logging.INFO)
        logging.info('\n######AlphaFold_Eva is done######\n')
       


    def Multi(self, input:str):
        """
        This function is used to prediction multiple complex structures
        """
        foldername=os.path.dirname(sys.argv[0])
        #print(foldername +'/M.save')
        
        from keras.models import load_model
        import joblib
        import pandas as pd
        import numpy as np
        # load model (trained neural network and MinMaxScaler)
        mm = joblib.load(foldername+'/MM.save')
        model = load_model(foldername+'/NN.h5')
        #
        extension=os.path.splitext(input)[1]
        if extension not in ['.xlsx','.xls']:
           print("please provide excel file")
           exit(-1)
        ## Data preprocessing and output the prediction value.
        input_feature=pd.read_excel(input)
        print(input_feature)
        input_feature=np.array(input_feature).reshape(-1,4)
        scale_input_feature=mm.transform(input_feature)
        pred=model.predict(scale_input_feature)
        with open(foldername+'/output.txt','w') as f:
             f.write(str(pred))
        print ('prediction value :' + str(pred))
        logging.basicConfig(format='%(asctime)s, %(levelname)-8s %(message)s',datefmt="%m-%d %H:%M:%S",level=logging.INFO)
        logging.info('\n######AlphaFold_Eva is done######\n')
        
        
    def check(self):
        import pandas as pd
        import numpy as np
        import keras
        import platform
        from keras.models import Sequential
        from keras.layers.core import Dense, Activation
        from sklearn.preprocessing import MinMaxScaler
        from keras.models import Sequential
        from keras.layers.core import Dense
        from keras.optimizers import SGD
        from keras.layers import SimpleRNN, LSTM
        from keras.layers import Dense, Dropout, Flatten
        from keras.callbacks import EarlyStopping
        from sklearn import metrics
        from sklearn.model_selection import cross_val_score
        from keras.wrappers.scikit_learn import KerasRegressor
        from keras.models import load_model
        import joblib
        print('AlphaFold-Eva --version 0.1')
        print("python version: " + platform.python_version())
        print("keras version: "+keras.__version__)


def check_parse(args_list):
    if args_list[0] in ['One','Multi']:
       #print(len(args_list))
       if args_list[0] in ['One']:
            if len(args_list) < 9:
               print("please include all the parameters")
               print("Usage: " + sys.argv[0] + " "+ args_list[0]+ " [total_surface] [contact_surface] [surface_ratio] [dimension_ratio]")
               exit(-1)
            
       else:
            if len(args_list) < 2:
               print("Usage: " + sys.argv[0] +" "+ args_list[0]+ " [Input file path] ")
               exit(-1)
    else:
         print('please provide either [One] or [Multi] keywords')
         exit(-1)

if __name__ == "__main__":
    # logging.basicConfig(format='%(asctime)s, %(levelname)-8s %(message)s',datefmt="%m-%d %H:%M:%S",level=logging.INFO)
    
    if len(sys.argv) > 1:
       check_parse(sys.argv[1:])
    fire.Fire(EVA)
