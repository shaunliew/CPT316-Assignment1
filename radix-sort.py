import time
import psutil
import matplotlib.pyplot as plt
txt_array = []
# Open the file and read the lines into an array
with open('sgb-words.txt', 'r') as f:
    for line in f:
        txt_array.append(line.strip())


#radix sort for string
def radix_sort_string(txt_array,start_time, end_time):
    start_time = time.time()
    # Find the maximum length of the strings
    max_length = len(max(txt_array, key=len))
    # Pad all the strings with spaces to make them all the same length
    txt_array = [x.ljust(max_length) for x in txt_array]

    # Loop through the strings from the last character to the first
    for i in range(max_length-1, -1, -1):
        # Create a list of 256 empty lists
        #this bucket is for the 256 ASCII characters
        buckets = [[] for _ in range(256)]
        # Loop through the strings in the array
        for string in txt_array:
            # Get the character code for the current character
            char_code = ord(string[i])
            # Add the string to the appropriate bucket
            buckets[char_code].append(string)
        

        # Flatten the buckets into a single array
        txt_array = [item for sublist in buckets for item in sublist]
    end_time = time.time()
    return txt_array, start_time, end_time


timeTakenForSorting= []
NumberOfWords = []
#radix sort for n = 1 to  5757, increment by 100
for i in range(2,5803,100):
    if i > 5758:
        i = 5758
    sub_array = txt_array[0:i]
    start_time = 0
    end_time = 0
    sorted_array, start_time, end_time = radix_sort_string(sub_array, start_time, end_time)
    time_needed = (end_time-start_time)*1000.0
    timeTakenForSorting.append(time_needed)
    NumberOfWords.append(i-1)
    if i == 5758:
        break
    #print("This program took {} milliseconds to execute when n is {}".format(time_needed,i))


#plot the graph
plt.plot(NumberOfWords,timeTakenForSorting)
plt.ylabel('Time Taken For String Sorting(Milliseconds)')
plt.xlabel('Number Of Words')
plt.title('Radix Sort for String in Python')
#plt.show()
plt.savefig('radix_sorted_string_graph.png')
print("The graph is generated. Please check the file radix_sorted_string_graph.png\n")

start_time = 0
end_time = 0
sorted_txt_array, start_time,end_time =  radix_sort_string(txt_array,start_time,end_time)

# Calculate total execution time and display it
#print("This program took %.f milliseconds to execute " % ((end_time - start_time) * 1000))
time_needed = (end_time-start_time)*1000.0
print("This program took %.4f milliseconds to sort the texts "%(time_needed))
print("Memory allocated for Radix Sort is %.4f MB " % (psutil.Process().memory_info().rss / (1024 * 1024)))
# Save the sorted array to a file
file = open("sorted_string.txt", "w")  # write mode
for i in sorted_txt_array:
    file.write(i)
    file.write("\n")
file.close()
