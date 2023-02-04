import gui
import findDiff

file1 = "text1.txt"
file2 = "text2.txt"

test = findDiff.diff_words(file1, file2) #call the function to find the deferent word
print("Different words:", test)

root = gui.display_text(file1, file2)
root.mainloop()