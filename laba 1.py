def to_octal(n):
    return oct(n)[2:]
def number_to_words(n):

    ones = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    teens = ["десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать",
             "семнадцать", "восемнадцать", "девятнадцать"]
    tens = ["", "десять", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят",
            "девяносто"]
    hundreds = ["", "сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]

    if n == 0:
        return "ноль"

    words = []

    h = n // 100
    n %= 100
    d = n // 10
    u = n % 10

    if h > 0:
        words.append(hundreds[h])
    if d == 1 and u > 0:
        words.append(teens[u])
    else:
        if d > 0:
            words.append(tens[d])
        if u > 0:
            words.append(ones[u])

    return ' '.join(words).strip()



octal_numbers = []
for i in range(1024):
    octal = to_octal(i)
    if len(octal) > 1 and octal[-2] == '1':
        octal_numbers.append(octal)


for octal in octal_numbers:
    print(octal[:-2])


min_octal = min(int(octal, 8) for octal in octal_numbers)
max_octal = max(int(octal, 8) for octal in octal_numbers)


average = (min_octal + max_octal) // 2


print("Среднее число между минимальным и максимальным:", number_to_words(average))
