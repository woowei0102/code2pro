import os
import re
import ast
import logging
import csv

# data = open("data.txt", 'w', encoding='utf-8')
csvFile = open('data.csv', 'w', newline='')
writer = csv.writer(csvFile, delimiter=',')
writer.writerow(['label', 'path' ,'struc'])
error_data = open('error_data.txt', 'w', encoding='utf-8')
proID = -1
text = []
yourPath = './clean_data/'
texts_num = 0
c_f = False    

def read_py(dir):
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    global texts_num, proID
    allFileList = os.listdir(dir)
    for file in allFileList:
        if os.path.isdir(os.path.join(dir,file)):
            proID += 1
            read_py(dir + file + '/')
        elif os.path.isfile(dir+file):   
            if os.path.splitext(dir+file)[1][1:].lower() == 'py':
                f = open(dir + file, "r", encoding='utf-8', errors='ignore')
                try:
                    r_node = ast.parse(f.read()) 
                    CodeClean().visit(r_node)
                    
                    writer.writerow([proID, dir+file, " ".join(str(i) for i in text)])
                    text.clear()
                    texts_num += 1
                    logging.info(str(dir+file) +" ,已處理 %d 個py檔" % texts_num)
                except:
                    error_data.write(dir+file + '\n')
            else:

                pass


class CodeClean(ast.NodeVisitor):
    '''第一步'''

    def visit_Module(self, node):
        self.generic_visit(node)
    
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
          #  self.generic_visit(node)


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
        # self.generic_visit(node)


if __name__ == '__main__':
    read_py(yourPath)
    error_data.close()