# 두 개의 함수를 정의한다.
# cube(num) = > num을 세제곱 해주는 함수
# squar(num) => num을 제곱 해주는 함수

def cube(n):
    return n**3
def square(n):
    return n**4
print(__name__)
if __name__ == "__main__":
    print(cube(2))
    print(square(2))