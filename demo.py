import logging
import pandas as pd
import numpy as np
import nltk
import os
import re
import ast
import argparse 
from gensim.models import word2vec
from gensim import models
import tensorflow as tf 
from tensorflow import keras
from tensorflow.keras import layers


c_f = False
text =[]

def main():
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    # 模型導入
    embedding = models.Word2Vec.load('./model/embedding.model')
    RNN =  tf.keras.models.load_model('./model/RNN.h5')

    # 讀參數
    arg_parse = argparse.ArgumentParser(description='A static Big-O analysis tool base on Big-O AST.')
    arg_parse.format_help()
    arg_parse.add_argument('filename', type=str, help='target code filename')
    args = arg_parse.parse_args()
    
    # 讀 Source Code 
    source_file_name = args.filename
    f = open(source_file_name, "r",encoding="utf-8")
    r_node = ast.parse(f.read())
    clean_code = nltk.word_tokenize(CodeClean().visit(r_node))
    predict_code = np.zeros([1, 15], dtype='float64')
    for i in range(min(len(clean_code), 15)):
        predict_code[0][i] = 1 + embedding.wv.vocab[clean_code[i]].index

    
    print(RNN.predict_classes(predict_code))
    
class CodeClean(ast.NodeVisitor):
    '''第一步'''

    def visit_Module(self, node):
        self.generic_visit(node)
        return  " ".join(str(i) for i in text)

    def visit_FunctionDef(self, node):
        if not c_f:
            text.append('Func')
            for child in ast.walk(node):
                if isinstance(child, ast.If):
                    text.append('If')
                    for child2 in ast.walk(child):
                        if isinstance(child2, ast.Assign): 
                            for target in child2.targets:
                                if isinstance(target, ast.Tuple):
                                    for element in target.elts:
                                        if isinstance(element, ast.Name):
                                            text.append('Variable')
                                if isinstance(target, ast.Name):
                                    text.append('Variable')
                if isinstance(child, ast.For):
                    text.append('For')
                    for child2 in ast.walk(child):
                        if isinstance(child2, ast.Assign): 
                            for target in child2.targets:
                                if isinstance(target, ast.Tuple):
                                    for element in target.elts:
                                        if isinstance(element, ast.Name):
                                            text.append('Variable')
                                if isinstance(target, ast.Name):
                                    text.append('Variable')
                if isinstance(child, ast.Assign): 
                    for target in child.targets:
                        if isinstance(target, ast.Tuple):
                            for element in target.elts:
                                if isinstance(element, ast.Name):
                                    text.append('Variable')
                        if isinstance(target, ast.Name):
                            text.append('Variable')
                if isinstance(child, ast.Attribute):
                    text.append('Attribute')
            self.generic_visit(node)


    def visit_ClassDef(self, node):
        c_f = True
        text.append('Class')
        for child in ast.walk(node):
            if isinstance(child, ast.FunctionDef):
                text.append('Method')
                for child2 in ast.walk(child):
                    if isinstance(child2, ast.Assign): 
                        for target in child2.targets:
                            if isinstance(target, ast.Tuple):
                                for element in target.elts:
                                    if isinstance(element, ast.Name):
                                        text.append('Variable')
                            if isinstance(target, ast.Name):
                                text.append('Variable')
                    if isinstance(child2, ast.Attribute):
                        text.append('Attribute')
        c_f = False
        self.generic_visit(node)



if __name__ == "__main__":
    main()  