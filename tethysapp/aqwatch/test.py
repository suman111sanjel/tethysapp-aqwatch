import numpy as np
min_value=0.00000001
max_value=0.1



NumberRange = np.logspace(np.log10(min_value), np.log10(max_value), num=8)

print(NumberRange)
NumberRange=NumberRange.tolist()
for i in NumberRange:
    fv=str(i)
    ff=None
    if 'e' in fv:
        fc=abs(int(fv.split('e')[-1]))
        ff=format(i,'.'+str(fc)+'f')
    else:
        ff=i
    print(ff)
    # print("{:.9f}".format(i))
