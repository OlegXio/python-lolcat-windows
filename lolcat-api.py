from os import system, remove
from random import choice
def lolcat(text):
    fn = f'lolcprint_{''.join([choice(list('QAZXSWEDCVFRTGBNHYUJMKIOLPqazxswdecfvrgbtnhhjmukilp')) for _ in range(6)])}'
    with open(fn,'w') as f:
        f.write(text)
        f.close()
    system(f'lolcat {fn')
    remove(str(fn))