#Set Operations
set1 = {'apple', 'orange', 'banana', 'strawberry'}
set2 = {'kiwi',  'pear','strawberry' , 'apple'}

common_items = set1 & set2
print("\nCommon items:", common_items)

unique_items = set1 ^ set2
print("Unique items:", unique_items)

total_items = set1 | set2
print("Total items:", total_items)
