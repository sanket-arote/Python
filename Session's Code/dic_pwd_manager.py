import pyperclip
import time
dic_var = {'github_acc': 'sanket@2001',
           'hackerrank_acc': 'sanket@123',
           'superset_acc': 'sanket@1997'}
key = input('Enter your Account Name:')

#print('This your Account Password:',dic_var[key])
# It will wait for some time to display the o/p

time.sleep(1)

# this pyper py will directly copy the text without letting us know

pyperclip.copy(dic_var[key])
time.sleep(1)
