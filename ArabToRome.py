#!usr/bin/env python
#encoding:utf-8

def transform_AtoR(one_num):
  '''''
  将阿拉伯数字转化为罗马数字
  '''
  num_list=[1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
  str_list=["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
  res = ""

  if not isinstance(one_num, int):
    res = "Invalid value, Please input int type"
    return res

  if one_num <= 0:
    res = "Negative or Zero, Please input positive number"
    return res

  for i in range(len(num_list)):
    while one_num>=num_list[i]:
      one_num-=num_list[i]
      res+=str_list[i]
  return res

if __name__ == '__main__':

  one_num_list=[77,66,55,8,1200,34,65,3,21,99,40,3999,4000, 0, -1, 3.5, "asd"]
  for one_num in one_num_list:
    print (one_num,'----->',transform_AtoR(one_num))
