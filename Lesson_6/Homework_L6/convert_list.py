
from environs import virt_environtment_

def convert ():
    env = virt_environtment_()
    env.read_env()
    arr = env.list("ARR")
    print (arr)


# def if __name__ == '__main__':
#     main()
