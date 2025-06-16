
# '\n'.join(array) is the same in js as array.join("\n")


def split_ascii(ascii_str, width):
    return '\n'.join(
        # [i:i+wdith] slice the string
        # from i to i + width (each loop)
        # expersion (what to return) for loop 

        # This is list comprehension (A single line of code to do a for loop)
        ascii_str[i:i+width] for i in range(0, len(ascii_str), width)
    )

# Test string
ascii_str = "abcdefghijk"

# Width of each line
width = 4

# Run the function
result = split_ascii(ascii_str, width)

# Print the result
print(result)
