# 透過程式碼中的人為命名去進行題目分類

## 介紹

多數同學在各種課堂上，分配各種作業，而課堂上要求檔案命名上大致都是相同的，很難作出分別，我們打算透過程式中的命名透過word2vec+RNN去作分類，便可分辨出各個作業的不同，可使同學注意到自己的命名問題。

## gensim套件安裝

~~~python
pip install -U gensim
~~~

## sklearn套件相關安裝
~~~python=
pip install numpy
pip install pandas
pip install sklearn
~~~

## tensorflow套件安裝
~~~
pip install tensorflow == 2.2.0
~~~

## nltk安裝
~~~python=
# 進入python直譯器
python
>> import nltk 
>> nltk.download('wordnet')
~~~

## 訓練過程
1. 透過`data資料夾`中的`ast_data.py`，會對`clean_data資料夾`中的各個題目給予Label，並輸出成`data.csv`以及`error_data.txt`
    ~~~
    cd data
    py .\ast_data.py
    ~~~
    注意: 現在`clean_data資料夾`目前有四個題目，如果有新題目可以作新增，但必須分類成各個資料夾才行
       
2. 輸出的`error_data.txt`請對`data.csv`中去進行刪除，如何沒有的話，這步驟就不用了

3. 開始訓練模型，其中程式中的RNN部分，由於本研究只分4個類別，未來有多組題目，請再進行作更改
    ~~~python
    py train.py
    ~~~
    注意: 請到該檔案的位置去編譯
4. 測試訓練出的模型
    ~~~python
    py demo.py testcase.py # testcase.py為你要測試的程式
    ~~~
    
## 結論
產出的模型效果很好，覺得這是一個可以延伸下去的小專案，只不過需要多組程式題目去作Label才會更有價值，期望未來展望部分可以完成。

## 未來展望
* 需要多組程式碼題目進行分類
* 給予使用者標記註明，好讓使用者得知各個程式的差別

## 相關文件

### word2vec+RNN學習影片
* [我的第一支快速利用TensorFlow 2.0建立RNN搭配Word2Vec Embedding進行文本分類](https://www.youtube.com/watch?v=BAP6l2uGAHU)


### word2vec
* [以 gensim 訓練中文詞向量](http://zake7749.github.io/2016/08/28/word2vec-with-gensim/)
* [使用自己的语料训练word2vec模型](https://www.jianshu.com/p/0425bfe619c3)
* [NL2Bash](https://github.com/TellinaTool/nl2bash?fbclid=IwAR2DKk4-qRGEJKUOkcnbK1L8fWeLIKJBTiedyV-aQl7fh7q7OAbCwOKw734)
* [深入淺出Word2Vec原理解析](https://www.jishuwen.com/d/pVET/zh-tw)



