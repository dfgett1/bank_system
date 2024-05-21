# -*- coding: utf-8 -*-
"""
Created on Mon May 20 16:59:36 2024

@author: wgs
"""

import pandas as pd
import numpy as np

df = pd.DataFrame({'username':['hhh','ddd'],'userPassword':['111111','222222'],'DepositAmount':[45,60]})

# df.to_csv(r'C:\Users\wgs\Desktop\bank_system_roster.csv',index=False)
# df = pd.read_csv(r'C:\Users\wgs\Desktop\bank_system_roster.csv')


while True:
    # 在每次循环开始时，会打印出一些指令供用户选择操作。指令包括查询余额、存钱、取款、显示账户和退出系统。
    print()
    print('a 建立新账号')
    print('b 查询余额')
    print('d 存钱')
    print('w 取款')
    print('t 转账')
    print('q 退出系统')
    print()


    action = input('输入指令： ')
    action = action.lower()  # force lowercase
    action = action[0]  # just use first letter
    print()
    
    name_lis = df['username'].tolist()
    
    if action == 'a':
        # 
        print('建立新账号:')
        username = input('请输入账号名称: ')
        userPassword = input('请输入密码: ')
        userDepositAmount = input('输入存钱数量（整数）: ')
        userDepositAmount = int(userDepositAmount)
        
        # 如果存款数量为非负数且密码验证通过，那么将存款金额加到账户余额accountBalance上
        if userDepositAmount < 0:
            print('不可以存入负数!')
 
        else:
            new_account = {'username':username,'userPassword':userPassword,'DepositAmount':userDepositAmount}
            df.loc[len(df)] = new_account
       
            # df = df.append(new_account)
            print('成功建立新账号:',username )
            print('当前账号余额为:',userDepositAmount )

    elif action == 'b':
         # 查询余额
         print('查询余额:')
         username = input('请输入账号名称: ')
         userPassword = input('请输入密码: ')
         userPassword_1 = str(df[df['username']==username]['userPassword'].reset_index(drop=True)[0])
         if username not in name_lis:
             print('账号错误')
         
         elif userPassword_1!= userPassword:
             print('密码错误')
  
         else: 
             print('当前账号余额为:', df[df['username']==username]['DepositAmount'].reset_index(drop=True)[0])    


    elif action == 'd':
        # 如果用户选择了存钱操作，程序会要求用户输入存款的数量（整数）和密码。
        print('存钱:')
        username = input('请输入账号名称: ')
        userPassword = input('请输入密码: ')
        userDepositAmount = input('输入存钱数量（整数）: ')
        userDepositAmount = int(userDepositAmount)
        
        # 如果存款数量为非负数且密码验证通过，那么将存款金额加到账户余额accountBalance上
        if userDepositAmount < 0:
            print('不可以存入负数!')
            
        elif username not in name_lis:
            print('账号错误')
        
        elif str(df[df['username']==username]['userPassword'].reset_index(drop=True)[0]) != userPassword:
            print('密码错误')
 
        else:  # OK
            df.DepositAmount[df.username==username] += userDepositAmount

            res = df[df['username']==username]['DepositAmount'].reset_index(drop=True)[0]
            print('当前账号余额为:', res)

    elif action == 'w':
        # 如果用户选择了取款操作，
        print('取款:')
        username = input('请输入账号名称: ')
        userPassword = input('请输入密码: ')
        userDepositAmount = input('输入取钱数量（整数）: ')
        userDepositAmount = int(userDepositAmount)
        userDepositAmount_1 = df[df['username']==username]['DepositAmount'].reset_index(drop=True)[0]
        # 
        if userDepositAmount < 0:
            print('不可以存入负数!')
            
        elif username not in name_lis:
            print('账号错误')
        
        elif str(df[df['username']==username]['userPassword'].reset_index(drop=True)[0]) != userPassword:
            print('密码错误')
            
        elif userDepositAmount_1 < userDepositAmount:
            print('转账不可以超过现有存款!')   
        else:  # OK
            df.DepositAmount[df.username==username] -= userDepositAmount

            res = df[df['username']==username]['DepositAmount'].reset_index(drop=True)[0]
            print('当前账号余额为:', res)

    elif action == 't':
        # 
        print('转账:')
        username = input('请输入账号名称: ')
        userPassword = input('请输入密码: ')
        
        
        
        
        # 
        if username not in name_lis:
            print('账号错误')
        
        elif str(df[df['username']==username]['userPassword'].reset_index(drop=True)[0]) != userPassword:
            print('密码错误')
 
        username_2 = input('请输入收款账号名称: ')
        userDepositAmount_1 = df[df['username']==username]['DepositAmount'].reset_index(drop=True)[0]
        
        userDepositAmount = input('输入转账钱数量（整数）: ')
        userDepositAmount = int(userDepositAmount)
        
        if username_2 not in name_lis:
            print('收款账号错误')
        elif userDepositAmount < 0:
            print('转账不可以为负数!')
        elif userDepositAmount_1 < userDepositAmount:
            print('转账不可以超过现有存款!')    
        else:  # OK
            df.DepositAmount[df.username==username] -= userDepositAmount
            df.DepositAmount[df.username==username_2] += userDepositAmount
            
            print('转账成功')
   
            res = df[df['username']==username]['DepositAmount'].reset_index(drop=True)[0]
            print('当前账号余额为:', res)

    elif action == 'q':
        break


df.to_csv(r'C:\Users\wgs\Desktop\bank_system_roster.csv',index=False)














