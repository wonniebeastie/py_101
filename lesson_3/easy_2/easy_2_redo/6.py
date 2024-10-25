# Back in the stone age (before CSS), we used spaces to align things 
# on the screen. If we have a 40-character wide table of Flintstone 
# family members, how can we center the following title above the table 
# with spaces?

title = "Flintstone Family Members"

print(title.center(40))
# The `.center()` method lets you center a string in a given width.
# I had to look this one up. 

centered = title.center(40)

print(repr(centered)) # '       Flintstone Family Members        '
print(len(centered)) # 40

# 40 characters wide - as in the entire thing/string