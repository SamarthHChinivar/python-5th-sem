def avg(marks):
    assert len(marks) != 0 , "List is empty."
    return sum(marks)/len(marks)

mark2 = []
print("Average of mark2:",avg(mark2))