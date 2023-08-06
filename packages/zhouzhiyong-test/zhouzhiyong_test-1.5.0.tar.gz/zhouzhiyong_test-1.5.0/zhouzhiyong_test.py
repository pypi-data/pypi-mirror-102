'''这是nester模块，提供了一个名为print_list()函数，这个函数的作用是打印列表，
其中也可能包含（也可能不包含）镶嵌列表，同时将列表每个单词首字母大写。'''
def print_lst(the_lst,contral=False,level=0):
    """这个函数取一个位置参数the_lst，这可以使任何pyhon列表（也可以是包含镶嵌列表），
所指定的每个数据都会递归的输出到屏幕上，同时将列表每个单词首字母大写，各数据占一行"""
    for each_lst in the_lst:
          if isinstance(each_lst,list):
               print_lst(each_lst,contral,level+1)
          elif isinstance(each_lst,str):
               if contral:
                    for tab_stop in range(level):
                         print('\t','')
               print (each_lst.title())
          else:
              if contral:
                    for tab_stop in range(level):
                         print('\t','')
                    print(each_lst)
