def take_large_banknotes(banknotes):

    notes = list()
    for i in banknotes:
        if i > 10:
            notes.append(i)
    return notes

print(*take_large_banknotes([]))