def calculate_average(numbers):
    if not numbers:
        return None
    average = sum(numbers) / len(numbers)
    return average
calculate_average([])