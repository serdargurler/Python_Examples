def Fibonacci(n):
    if n<0:
        print("Yanlış Giriş Yapıldı")
    # İlk Fibonacci_value=0
    elif n==1:
        return 0
    # İkinci Fibonacci_value=0
    elif n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
#Yazdırmak için;

print(Fibonacci(7))