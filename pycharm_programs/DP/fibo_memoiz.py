import time

def time_it(func):
    def decorated_func(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        return (end_time - start_time)*1000
    return decorated_func

@time_it
def fibonacci_dp(n):
    fibo = [0,1]
    for i in range(n):
        if i==0 or i==1:
            continue
        fibo.append(fibo[i-1] +fibo[i-2])
    print (fibo)

print (fibonacci_dp(50))
