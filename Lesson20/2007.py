import sys

def clean_comment(line):
    line = line.lstrip()  
    if line.startswith('#'):
        comment = line[1:].strip()  
        return comment
    return None

comments_with_lines = [
    (index + 1, clean_comment(line))  
    for index, line in enumerate(sys.stdin)
    if clean_comment(line) is not None
]

for line_number, comment in comments_with_lines:
    print(f"Line {line_number}: {comment}")
