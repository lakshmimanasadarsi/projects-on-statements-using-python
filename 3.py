from array import array
numbers = array('i') # Get number of elements 
n = int(input("Enter number of elements: ")) # Insert elements into the array 
for i in range(n): 
    value = int(input(f"Enter element {i + 1}: ")) 
    numbers.append(value) 
print("\nArray:", numbers) # Find largest element 
largest = numbers[0] 
for i in range(1, n): 
        if numbers[i] > largest: 
            largest = numbers[i] # Find smallest element 
smallest = numbers[0] 
for i in range(1, n): 
    if numbers[i] < smallest: 
        smallest = numbers[i] # Find sum 
total = 0 
for i in range(n): 
    total = total + numbers[i] # Find average 
average = total / n # Display results 
print("\n----- Array Statistics -----") 
print("Largest:", largest) 
print("Smallest:", smallest) 
print("Sum:", total) 
print("Average:", average)