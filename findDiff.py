import difflib


def diff_words(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        text1 = f1.read()
        text2 = f2.read()

    text1_lines = text1.split()
    text2_lines = text2.split()
    d = difflib.Differ()
    diff = d.compare(text1_lines, text2_lines)
    return [line[2:] for line in diff if line.startswith('- ')]
