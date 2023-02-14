import re

str1 = "Chinmay Patel: The owner of the greatest startup of sll time"
match = re.search("Chinmay", str1)
print("Starting index: ", match.start())
print("Ending index: ", match.end())
