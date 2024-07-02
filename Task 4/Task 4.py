import sys

def min_moves_to_equal_elements(filename):
    # Чтение чисел из файла
    with open(filename, 'r') as file:
        nums = [int(line.strip()) for line in file.readlines()]

    # Сортировка чисел
    nums.sort()
    
    # Нахождение медианы
    n = len(nums)
    if n % 2 == 1:
        median = nums[n // 2]
    else:
        median = (nums[n // 2 - 1] + nums[n // 2]) // 2
    
    # Вычисление минимального количества ходов
    moves = sum(abs(num - median) for num in nums)
    
    return moves

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python Task4.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    result = min_moves_to_equal_elements(filename)
    print(result)
