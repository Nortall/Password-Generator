from variables import characters


def calculate_psd_protection(A: int, L: int, T: int, V: int):
    return (V * T)/(A ** L)


def read_file(filename: str):
    with open(filename, 'r+') as f:
        data = f.read()
    return data


if __name__ == "__main__":
    file_name = "pswd.txt"
    A = len(characters)
    password = read_file(file_name)
    L = len(password)
    print(A)
    print(L)
    T = 180 * 24 * 60 * 60
    V = 2000000
    P = calculate_psd_protection(A, L, T, V)
    print(f"Вероятность подбора пароля злоумышленником: {P}")
