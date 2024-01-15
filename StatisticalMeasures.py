import math, os

# Function to calculate the average of a list of numbers
def CalculateAverage(numbers):
    return sum(numbers)/len(numbers)

# Function to calculate the median of a list of numbers
def CalculateMedian(numbers):
    numbers = sorted(numbers)
    
    # If the list has an odd length, the median is the middle element
    if len(numbers)%2 != 0:
        Midan = numbers[len(numbers)//2]
    # If the list has an even length, the median is the average of the two middle elements
    else:
        mid = round(len(numbers)/2)
        Midan = (numbers[mid]+numbers[mid - 1])/2

    return Midan

# Function to calculate the variance of a list of numbers, given the average
def CalculateVariance(numbers, average):
    total = 0
    for num in numbers:
    # Calculate the sum of squared differences from the average
        total += pow(num-average, 2)
        
    return  total/len(numbers)

# Function to calculate the standard deviation from the variance
def CalculateStandardDeviation(Variance):
    return math.sqrt(Variance)

# Function to read data from a file and return a list of numbers
def ReadTheData():
    number_list = []
    if os.path.exists(os.sys.argv[1]):
        # Open the file for reading
        file = open(os.sys.argv[1], "r")
        for line in file:
            # Remove trailing newline characters
            line = line.rstrip()
            # Validate each character in the line
            for char in line:
                if char < '0' or char > '9': 
                    print("Error, invalid inbut")
                    os._exit(1)
            if len(line) == 0 :
                print("Error, invalid inbut")
                os._exit(1)
            # Append the line as an integer to the number list
            number_list.append(int(line))
        file.close()
    else:
        print("Error, File not found")
        os._exit(1)
    return number_list

# Check if the correct number of command-line arguments is provided
if len(os.sys.argv) == 2:
    # Read data from the file
    number_list = ReadTheData()
    # Calculate the statistical measures and print them
    average = CalculateAverage(number_list)
    median = CalculateMedian(number_list)
    Variance = CalculateVariance(number_list, average)
    StandardDeviation = CalculateStandardDeviation(Variance)
    print("Average:", round(average))
    print("Median:", math.ceil(median))
    print("Variance:", round(Variance))
    print("Standard Deviation:", round(StandardDeviation))
else:
    print("Error, for help please read the read me file.")