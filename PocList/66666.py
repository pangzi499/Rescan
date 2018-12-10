# -*- coding: utf-8 -*-   
      
import os  
      
def file_name(file_dir): 
    poc_list = []
    path = "..\Rescan\PocList"
   
    for root, dirs, files in os.walk('PocList'): 
         
        
        for file in files: 
            poc_dict = {'xtype':'','xname':'','xpath':''} 
            if os.path.splitext(file)[1] == '.py': 
                poc_dict['xtype'] = "Python"
                poc_dict['xname'] = os.path.splitext(file)[0]
                # print os.path.splitext(file)[0]  
                poc_dict['xpath'] = path + '\\'+ os.path.join(file) 
                # print os.path.join(file) 
            elif os.path.splitext(file)[1] == '.jar':
                poc_dict['xtype'] = "Java"
                poc_dict['xname'] = os.path.splitext(file)[0] 
                poc_dict['xpath'] = path + '\\'+ os.path.join(file)
            
            poc_list.append(poc_dict)
        print poc_list
    return poc_list

if __name__ == '__main__':
    print "======================"
    ls = []

    ls = file_name("PocList")
    print ls
    print "OK"

