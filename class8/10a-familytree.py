# pip3 install ete3 ... it will require you to install this package ....!!
from ete3 import Tree

# Define the specific hierarchical tree structure as requested.
# - Parent is the ancestor of male, female, GrandFather and GrandMother.
# - GrandMother is the ancestor of Father and Mother.
# - Mother is the ancestor of ME, Brother, and Sister.

# Option 1 -- using hte newick strig :: 

# Define your tree structure correctly Code from 
t = Tree('(male,female,(((((ME,Brother,Sister),Father,Mother))GrandFather GrandMother))Parent)Tree;', format=1)


# you should ideally comment out the other option while printing one of the options 

# option 2 --- using the tree and nodes ... 
# Creating the tree manually for more control
# t = Tree()
# t.name = "Tree"


# # Add male and female as direct children of Parent
# male_node = t.add_child(name="male")
# female_node = t.add_child(name="female")
# parent_node = t.add_child(name="parent")

# # Add GrandFather and GrandMother as children of Parent
# grandfather_node = parent_node.add_child(name="GrandFather")
# grandmother_node = parent_node.add_child(name="GrandMother")

# # Add Father and Mother as children of GrandMother
# father_node = grandmother_node.add_child(name="Father")
# mother_node = grandmother_node.add_child(name="Mother")

# # Add ME, Brother, and Sister as children of Mother
# me_node = mother_node.add_child(name="ME")
# brother_node = mother_node.add_child(name="Brother")
# sister_node = mother_node.add_child(name="Sister")

# Print the tree in ASCII format, including names for internal nodes (branches).
print(t.get_ascii(show_internal=True))