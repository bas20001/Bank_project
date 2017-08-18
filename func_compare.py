
# coding: utf-8

# In[1]:


# encoding utf-8


# In[2]:


def func_cal(func_x,func_x_time):
    func_money = int(func_x)/365*int(func_x_time)
    return func_money


# In[3]:


def func_compare(func_a_info,func_b_info):
    turn = True
    func_a = func_a_info[0]
    func_a_time = func_a_info[1]
    func_b = func_b_info[0]
    func_b_time = func_b_info[1]
    while turn == True:
        console = input('是否开始比较理财收益？（Y/N）')
        if console == 'N':
            turn = False
        else :
            if int(func_a_time) > int(func_b_time):
                func_lost_time = int(func_a_time) - int(func_b_time)
                func_lost = 490
                if func_cal(func_a,func_a_time) > func_cal(func_b,func_b_time) + func_cal(func_lost,func_lost_time):
                    result =  func_cal(func_a,func_a_time) - func_cal(func_b,func_b_time) + func_cal(func_lost,func_lost_time)
                    print('理财A是最棒的！每万元高于B理财+补足时间T计划理财：')
                    print(result)
                elif func_cal(func_a,func_a_time) < func_cal(func_b,func_b_time) + func_cal(func_lost,func_lost_time):
                    result =  func_cal(func_b,func_b_time) + func_cal(func_lost,func_lost_time) - func_cal(func_a,func_a_time) 
                    print('理财B是最棒的，需要购买补足时间的T计划产品！每万元高于A理财：')
                    print(result)
                else :
                    print('两个产品一样棒')
            elif int(func_b_time) > int(func_a_time):
                func_lost_time = int(func_b_time) - int(func_a_time)
                func_lost = 490
                if func_cal(func_b,func_b_time) > func_cal(func_a,func_a_time) + func_cal(func_lost,func_lost_time):
                    result =  func_cal(func_b,func_b_time) - func_cal(func_a,func_a_time) + func_cal(func_lost,func_lost_time)
                    print('理财B是最棒的！每万元高于B理财+补足时间T计划理财：')
                    print(result)
                elif func_cal(func_b,func_b_time) < func_cal(func_a,func_a_time) + func_cal(func_lost,func_lost_time):
                    result =  func_cal(func_a,func_a_time) + func_cal(func_lost,func_lost_time) - func_cal(func_b,func_b_time)
                    print('理财A是最棒的，需要购买补足时间的T计划产品！每万元高于B理财：')
                    print(result)
                else :
                    print('两个产品一样棒')
            else :
                if func_cal(func_a,func_a_time) > func_cal(func_b,func_b_time):
                    result = func_cal(func_a,func_a_time) - func_cal(func_b,func_b_time)
                    print('理财A是最棒的，每万元收益比理财B高：')
                    print(result)
                elif func_cal(func_b,func_b_time) > func_cal(func_a,func_a_time):
                    result = func_cal(func_b,func_b_time) - func_cal(func_a,func_a_time)
                    print('理财B是最棒的,每万元收益比理财A高：')
                    print(result)
                else :
                    print('两个产品一样棒')
                    


# In[4]:


func_a = input('请输入理财产品A的收益率: ')
func_a_time = input('请输入理财产品A的时间: ')
func_b = input('请输入理财产品B的收益率: ')
func_b_time = input('请输入理财产品B的时间: ')
func_a_info = [func_a,func_a_time]
func_b_info = [func_b,func_b_time]
func_compare(func_a_info,func_b_info)


# In[ ]:




# Bank_project
# Bank_project
