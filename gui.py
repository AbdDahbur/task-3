import findDiff
import tkinter as tk

def display_text(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        text1 = f1.read()
        text2 = f2.read()

    root = tk.Tk()

    text_widget1 = tk.Text(root, height=10, width=50)
    text_widget1.pack()
    text_widget1.insert(tk.END, text1)

    Dwords = findDiff.diff_words(file1,file2)
    for word in Dwords:
        index = text1.find(word)
        while index != -1:
            line_num = text1[:index].count('\n') +1
            char_num = index - text1.rfind('\n', 0, index)-1
            initial = str(line_num) + '.' + str(char_num)
            final = str(line_num) + '.' + str(char_num + len(word))

            text_widget1.tag_configure("red", foreground="red")
            text_widget1.tag_add("red", initial, final)

            index = text1.find(word, index + len(word))

    text_widget2 = tk.Text(root, height=10, width=50)
    text_widget2.pack()
    text_widget2.insert(tk.END, text2)

    return root