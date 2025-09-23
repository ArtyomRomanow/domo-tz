def main(input_str: str) -> str:
    parts = input_str.strip().split()
    if len(parts) != 3:
        print("Некорректный формат ввода")

    a_str, op, b_str = parts

    if not (a_str.isdigit() and b_str.isdigit()):
        print("Операнды должны быть целыми числами")

    a = int(a_str)
    b = int(b_str)

    if not (1 <= a <= 10 and 1 <= b <= 10):
        print("Числа должны быть от 1 до 10 включительно")

    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b
    elif op == '/':
        if b == 0:
            print("Деление на ноль")
        result = a // b
    else:
        print("Неверный оператор")

    return str(result)


if __name__ == "__main__":
    while True:
        try:
            user_input = input()
            print(main(user_input))
        except Exception as e:
            print(f"throws Exception")
            break


