def print_document(pages):
    for page in pages:
        if page.startswith('Секретно'):
            print('Дальнейшие материалы засекречены')
            return
        print(page)
    print('Напечатано без купюр') 
    
print_document(["Обычная страница", "И еще страница", "Секретно Вот этот воттекст не показывать", "Никому","Никогда"])
print_document(["Пустой трёп", "который","никому не интересен"])