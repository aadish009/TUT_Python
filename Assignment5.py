# task 1 

students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 90
}

n = input("Enter the student Name: ")

if n in students:
    print(f"{n}'s Marks: {students[n]}")
else:
    print("Student not found")

# task 2 

# original list 
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 5 Elements from the original list
list2 = list1[0:5]
 
# Reversed List 
list3 = list2[::-1]

print("Original list:", list1,"\n","Extracted first 5 elements:", list2,"\n","Reversed list:",list3)