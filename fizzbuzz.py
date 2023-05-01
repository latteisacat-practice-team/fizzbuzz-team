def do_fizzbuzz(num: int):
    for i in range(1, num+1):
        if i%3==0:
            print('fizz')
        else:
            print(i)
    print(f'hello {num}')


if __name__ == '__main__':
    do_fizzbuzz(16)
