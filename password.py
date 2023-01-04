import re
patt = re.compile(r"[a-z0-9A-Z%#$@]{8,}\d")
x = input('type your password please!\n:')
if(patt.match(x)):
    print('password is valid \nstoring the password')
    password = x
    print(f'ur password is: {password}')
    pass1 = input('Type the password again for confirmation\n:')
    if(password == pass1):
        print('password verified.\nThanks!!!')
    else:
        print('Not verified!!!')
else:
    print('password enter not valid \nplease try again')
