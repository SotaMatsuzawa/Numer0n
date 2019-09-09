# -*- coding: utf-8 -*-
"""
Created on Mon Jul  8 15:24:51 2019

@author: souta
"""



import random

ca="0123456789"

#ex_num,ca_numの要素は文字列でok
def squeeze(eat,bite,ex_nums,ca_num,old_list):
    ca_list=[]
    new_ca_list=[]
    li=[]
    if eat==0 and bite==0:
        for i in range(len(ca_num)):
            if ca_num[i]!=ex_nums[0] and ca_num[i]!=ex_nums[1] and ca_num[i]!=ex_nums[2]:
                li.append(str(ca_num[i]))
        ca_num="".join(li)

        for i in ca_num:
            for j in ca_num:
                    for k in ca_num:
                        if i!=j and i!=k and j!=k:
                            ca_list.append(i+j+k)
            
    elif eat==0 and bite==1:
        for i in ca_num:
            for j in ca_num:
                if i!=j and i!=ex_nums[0] and i!=ex_nums[1] and i!=ex_nums[2] and j!=ex_nums[0] and j!=ex_nums[1] and j!=ex_nums[2]:
                    ca_list.append(i+ex_nums[0]+j)
                    ca_list.append(i+j+ex_nums[0])
                    ca_list.append(ex_nums[1]+i+j)
                    ca_list.append(i+j+ex_nums[1])
                    ca_list.append(ex_nums[2]+i+j)
                    ca_list.append(i+ex_nums[2]+j)
           
    elif eat==0 and bite==2:
        for i in ca_num:
            if  i!=ex_nums[0] and i!=ex_nums[1] and i!=ex_nums[2]:
                ca_list.append(i+ex_nums[0]+ex_nums[1])
                ca_list.append(i+ex_nums[2]+ex_nums[0])
                ca_list.append(i+ex_nums[2]+ex_nums[1])
                ca_list.append(ex_nums[1]+ex_nums[0]+i)
                ca_list.append(ex_nums[1]+i+ex_nums[0])
                ca_list.append(ex_nums[1]+ex_nums[2]+i)
                ca_list.append(ex_nums[2]+i+ex_nums[0])
                ca_list.append(ex_nums[2]+i+ex_nums[1])
                ca_list.append(ex_nums[2]+ex_nums[0]+i)
                
    elif eat==0 and bite==3:
        ca_list.append(ex_nums[1]+ex_nums[2]+ex_nums[0])
        ca_list.append(ex_nums[2]+ex_nums[0]+ex_nums[1]) 
        
    elif eat==1 and bite==0:
        for i in ca_num:
            for j in ca_num:
                if i!=j and i!=ex_nums[0] and i!=ex_nums[1] and i!=ex_nums[2] and j!=ex_nums[0] and j!=ex_nums[1] and j!=ex_nums[2]:
                    ca_list.append(ex_nums[0]+i+j)
                    ca_list.append(i+ex_nums[1]+j)
                    ca_list.append(i+j+ex_nums[2])
                    
    elif eat==1 and bite==1:
        for i in ca_num:
            if  i!=ex_nums[0] and i!=ex_nums[1] and i!=ex_nums[2]:
                ca_list.append(ex_nums[0]+i+ex_nums[1])
                ca_list.append(ex_nums[0]+ex_nums[2]+i)
                ca_list.append(i+ex_nums[1]+ex_nums[0])
                ca_list.append(ex_nums[2]+ex_nums[1]+i)
                ca_list.append(ex_nums[1]+i+ex_nums[2])
                ca_list.append(i+ex_nums[0]+ex_nums[2])
     
    elif eat==1 and bite==2:
        ca_list.append(ex_nums[0]+ex_nums[2]+ex_nums[1])
        ca_list.append(ex_nums[2]+ex_nums[1]+ex_nums[0])
        ca_list.append(ex_nums[1]+ex_nums[0]+ex_nums[2])
    
    elif eat==2 and bite==0:
        for i in ca_num:
            if  i!=ex_nums[0] and i!=ex_nums[1] and i!=ex_nums[2]:
                ca_list.append(ex_nums[0]+ex_nums[1]+i)
                ca_list.append(ex_nums[0]+i+ex_nums[2])
                ca_list.append(i+ex_nums[1]+ex_nums[2])
    
    elif eat==3 and bite==0:
        ca_list.append(ex)
        

                
    if len(old_list)!=0:
        new_ca_list=[num for num in ca_list if num in old_list]
        ca_list=new_ca_list.copy()
        if len(ca_list)==0:
            return ca_list,ca_num
    return ca_list,ca_num




def dubbling_check(num):
    if len(num)==len(set(num)):
        return True
    else:
        return False

def count_cand(ex_nums,ca_num,ca_list):
    info_list=[[0,0],[0,1],[0,2],[0,3],[1,0],[1,1],[1,2],[2,0],[2,1],[3,0]]
    sum_ex=0
    sum_ex2=0
    ave_ca=0
    old_count_list=ca_list.copy()
    ca_count_num=ca_num
    for info in info_list:
        ca_list,ca_num=squeeze(info[0],info[1],ex_nums,ca_count_num,old_count_list)
        sum_ex=sum_ex+len(ca_list)
        sum_ex2=sum_ex2+len(ca_list)**2
    if sum_ex!=0:
        ave_ca=sum_ex2/sum_ex
    return ave_ca
    

def choice(ca_list,ca_num):
    ave_list=[]
    for num in ca_list:
        ave_ca=count_cand(num,ca_num,ca_list)
        ave_list.append(ave_ca)    
    return ca_list[ave_list.index(min(ave_list))]
        
    
    

my_num="802"
first_ex="926"
print("最初の予測値は"+str(first_ex))
old_list=[]
ex=first_ex


while True:
    eat=int(input("eat:"))
    bite=int(input("bite:"))
    ca_list,ca_num=squeeze(eat,bite,ex,ca,old_list)
    if len(ca_list)<300:
        ex_number=choice(ca_list,ca_num)
    else:
        ex_number=random.choice(ca_list)    
    old_list=ca_list.copy()
    print("予測値は"+ex_number+"  残り候補数は"+str(len(ca_list)))
    if len(ca_list)<20:
        print(ca_list)
    ex=ex_number
    ca=ca_num
    if ex_number==my_num or ca_list==0:
        print("あったたよん")
        break