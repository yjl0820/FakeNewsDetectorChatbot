import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from keras.models import Model
from keras.layers import LSTM, Activation, Dense, Dropout, Input, Embedding
from keras.optimizers import RMSprop
from keras.preprocessing.text import Tokenizer
from keras.preprocessing import sequence
from keras.utils import to_categorical
from keras.callbacks import EarlyStopping

def preprocessing(Fake,True_):
        df1 = pd.read_csv(Fake,delimiter=',',encoding='latin-1')
        df2 = pd.read_csv(True_,delimiter=',',encoding='latin-1')
        df1.drop(['text', 'subject', 'date'],axis=1,inplace=True)
        df2.drop(['text', 'subject', 'date'],axis=1,inplace=True)
        df1['fake'] = 1
        df2['fake'] = 0
        df = pd.concat([df1, df2])
        X = df.title
        Y = df.fake
        le = LabelEncoder()
        Y = le.fit_transform(Y)
        Y = Y.reshape(-1,1)
        return X, Y

def RNN(max_len, max_words):
        inputs = Input(name='inputs',shape=[max_len])
        layer = Embedding(max_words,50,input_length=max_len)(inputs)
        layer = LSTM(64)(layer)
        layer = Dense(256,name='FC1')(layer)
        layer = Activation('relu')(layer)
        layer = Dropout(0.5)(layer)
        layer = Dense(1,name='out_layer')(layer)
        layer = Activation('sigmoid')(layer)
        model = Model(inputs=inputs,outputs=layer)
        return model

def modeling(X,Y):
        X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.15)
        max_words = 1000
        max_len = 150
        tok = Tokenizer(num_words=max_words)
        tok.fit_on_texts(X_train)
        sequences = tok.texts_to_sequences(X_train)
        sequences_matrix = sequence.pad_sequences(sequences,maxlen=max_len)
        model = RNN(max_len, max_words)
        model.summary()
        model.compile(loss='binary_crossentropy',optimizer=RMSprop(),metrics=['accuracy'])
        model.fit(sequences_matrix,Y_train,batch_size=128,epochs=10,validation_split=0.2,callbacks=[EarlyStopping(monitor='val_loss',min_delta=0.0001)])
        return model, tok
    
def input_(model, val, tok):
        max_len = 150
        new_text = pd.Series([val])
        test_sequences_new = tok.texts_to_sequences(new_text)
        test_sequences_matrix_new = sequence.pad_sequences(test_sequences_new,maxlen=max_len)
        return_value = model.predict(test_sequences_matrix_new)[0][0]
        return return_value





    

