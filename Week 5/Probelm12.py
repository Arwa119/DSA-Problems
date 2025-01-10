numbers = [10, -5, 23, -1, 7, -9, 15, 30]

def remove_negatives(numbers):
    return [num for num in numbers if num >= 0]

def Maximum(numbers):
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value

def Minimum(numbers):
    min_value = numbers[0]
    for num in numbers:
        if num < min_value:
            min_value = num
    return min_value

def Average(numbers):
    total_sum = 0
    count = 0
    for num in numbers:
        total_sum += num
        count += 1
    return total_sum / count if count != 0 else 0

if __name__ == "__main__":
    print(f"List with negatives: {numbers}")
    numbers = remove_negatives(numbers)
    print(f"List after removing negatives: {numbers}")

    max_value = Maximum(numbers)
    min_value = Minimum(numbers)
    print(f"Maximum value: {max_value}")
    print(f"Minimum value: {min_value}")

    average = Average(numbers)
    print(f"Average: {average}")
