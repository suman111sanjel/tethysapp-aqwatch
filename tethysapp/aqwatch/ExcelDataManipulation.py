# # import pandas as pd
# #
# a='/home/suman/192.168.11.242 user Suman/max_emiss_ECLIPSE_range_list.xlsx'
# #
# # df = pd.read_excel (a)
# # df1 = pd.DataFrame(df, columns= ['range'])
# #
# # print(df1)
# # sheet['G' + str(i + 6)].value
#
# import ast
# import openpyxl
# wb = openpyxl.load_workbook(a)
# sheet = wb.get_sheet_by_name('Sheet1')
#
#
# for i in range(70):
#     ColG=sheet['G' + str(i + 2)].value
#     res = ast.literal_eval(ColG)
#     lenList=len(res)
#     legendList=[]
#     for n in range(lenList):
#         vv=str(round(res[n],6))
#         if(n==0):
#             legendList.append(['less than '+vv,''])
#             legendList.append([str(round(res[n],6))+' to '+str(round(res[n+1],6)),''])
#         elif(n==(lenList-1)):
#             legendList.append([vv+' or more',''])
#         else:
#             legendList.append([str(round(res[n],6))+' to '+str(round(res[n+1],6)),''])
#
#     print(legendList)
#     # sheet['G' + str(i + 2)].value = legendList
#     sheet['H' + str(i + 2)].value = str(legendList)
#
# wb.save('/home/suman/192.168.11.242 user Suman/example.xlsx')
#












# import pandas as pd
#
a='/home/suman/192.168.11.242 user Suman/New_log_range_list_REAS_GAINS.xlsx'
#
# df = pd.read_excel (a)
# df1 = pd.DataFrame(df, columns= ['range'])
#
# print(df1)
# sheet['G' + str(i + 6)].value
import numpy as np
import ast
import openpyxl
wb = openpyxl.load_workbook(a)
sheet = wb.get_sheet_by_name('new_range_list2')


for i in range(105):
    max_value = sheet['H' + str(i + 2)].value
    min_value = sheet['I' + str(i + 2)].value
    NumberRangee = np.logspace(np.log10(min_value), np.log10(max_value), num=8)
    RangeList=[]
    NumberRange = NumberRangee.tolist()
    for ik in NumberRange:
        fv = str(ik)
        ff = None
        if 'e' in fv:
            fc = abs(int(fv.split('e')[-1]))
            ff = format(ik, '.' + str(fc) + 'f')
        else:
            ff = ik
        RangeList.append(ff)
    sheet['J' + str(i + 2)].value = str(list(reversed(RangeList)))

    NumberRangee=NumberRangee.tolist()
    NumberRangee=list(reversed(NumberRangee))
    lenList=len(NumberRangee)
    legendList=[]
    for n in range(lenList):
        vv=str(format(NumberRangee[n],'.0e'))
        if(n==0):
            legendList.append(['less than '+vv,''])
            legendList.append([str(format(NumberRangee[n],'.0e'))+' to '+str(format(NumberRangee[n+1],'.0e')),''])
        elif(n==(lenList-1)):
            legendList.append([vv+' or more',''])
        else:
            legendList.append([str(format(NumberRangee[n],'.0e'))+' to '+str(format(NumberRangee[n+1],'.0e')),''])

    print(legendList)
    # sheet['G' + str(i + 2)].value = legendList
    sheet['K' + str(i + 2)].value = str(legendList)

wb.save('/home/suman/192.168.11.242 user Suman/example1.xlsx')


