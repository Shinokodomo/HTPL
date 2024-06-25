import numpy as np

def min_moves_to_equal_elements(filename):
    # Чтение чисел из файла
    with open(filename, 'r') as file:
        nums = [int(line.strip()) for line in file.readlines()]

    # Нахождение медианы
    median = int(np.median(nums))
    
    # Вычисление минимального количества ходов
    moves = sum(abs(num - median) for num in nums)
    
    return moves

if __name__ == "__main__":
    filename = 'numbers.txt'
    result = min_moves_to_equal_elements(filename)
    print(result)