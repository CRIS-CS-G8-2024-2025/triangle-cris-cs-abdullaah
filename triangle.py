'''
Abdullaah Lagkar(Ab),Computer Science g.8, Nested loop triangle
'''

# Number of rows for the triangle
rows = 8

# Outer loop for each row
for i in range(1, rows + 1):
    # Inner loop for printing stars
    for j in range(i):
        print("*", end="")
    # Move to the next line
    print()
