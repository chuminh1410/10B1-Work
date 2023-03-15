# Open the input file in read mode and output file in write mode
with open('input_file.txt', 'r') as input_file, open('output_file.txt', 'w') as output_file:
    
    # Read the first line of the input file
    first_line = input_file.readline()
    
    # Write the first line to the output file
    output_file.write(first_line)

# In this code, we use the function open() to open both the input file and the output file.

# We use "with" keyword so that the files are properly closed after we're done with them.

# We read the first line of the input file using the readline() method, which reads until it reaches the end of the line.

# Then, we write that same line to the output file using the write() method.

# And finally, when the with block is exited, both files will be properly closed because of the way we opened them .