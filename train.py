import logging
import pandas as pd
import numpy as np
import nltk
from gensim.models import word2vec
import tensorflow as tf 
from tensorflow import keras
from tensorflow.keras import layers
from keras.models import load_model
import pydotplus
from sklearn.model_selection import train_test_split

def main():

    ## word embedding 訓練
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    TB =  pd.read_csv('./data/data.csv')
    TB['text'] = TB.struc.apply(lambda x: nltk.word_tokenize(x))
    model = word2vec.Word2Vec(TB.text, size=250, iter=10, sg=1, min_count=1)
    # print(model)
    # print(model.wv.vocab)

    ## 整理資料
    # text = [1+model.wv.vocab[sen].index for sen in TB.text[0]]
    embedding_matrix = model.wv.vectors
    embedding_matrix = np.vstack((np.array(np.zeros(250)),embedding_matrix))
    length = 15
    X = np.zeros([len(TB.text), length], dtype='float64')
    for i in range(len(TB.text)):
        for j in range(min(len(TB.text[i]), length)):
            X[i,j] = 1 + model.wv.vocab[TB.text[i][j]].index 
    Y = TB.label
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.33, random_state=0)

    ## RNN 訓練
    RNN = keras.Sequential(name='RNN')
    RNN.add(layers.Embedding(len(model.wv.vocab)+1, 250))
    RNN.add(layers.SimpleRNN(64))
    RNN.add(layers.Dense(4 , activation='softmax'))
    keras.utils.plot_model(RNN, show_shapes=True, to_file='model.png')
    RNN.layers[0].set_weights([embedding_matrix])
    RNN.layers[0].trainable = False
    print(RNN.summary())
    RNN.compile(optimizer='Adam', 
                loss=keras.losses.sparse_categorical_crossentropy,
                metrics=['accuracy'])
    RNN.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=20)

    ## 評估
    # print(RNN.predict_classes(x_train)[100:110])
    print(RNN.evaluate(x_test, y_test))


    # 保存模型，供日後使用
    model.save("./model/embedding.model")
    tf.keras.Model.save(RNN, "./model/RNN.h5")

    # 模型讀取方式
    # model = word2vec.Word2Vec.load("your_model_name")

if __name__ == "__main__":
    main()