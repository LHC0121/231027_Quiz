a = [number1, number2, number3, number4, number5, number6, number7, number8, number9, number10, number11, number12, number13] #실제 실행시에는 각 자리에 숫자 대입
b = a[0]*2 + a[1]*3 + a[2]*4 + a[3]*5 + a[4]*6 + a[5]*7 + a[6]*8 + a[7]*9 + a[8]*2 + a[9]*3 + a[10]*4 + a[11]*5
c = b%11
d = 11-c
if number13 == d :
    print("유효한 주민등록번호입니다.")
else :
    print("유효하지 않은 주민등록번호입니다.")