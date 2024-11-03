def is_anagram(s, t):
    return sorted(s) == sorted(t)

# Пример использования
s = "anagram"
t = "nagaram"
print(is_anagram(s, t))  # Ожидаемый результат: True
