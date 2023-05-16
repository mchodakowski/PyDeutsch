# PyNiemiecki - program do nauki niemieckich słówek
# import sqlite3 i połączenie
import sqlite3
conn = sqlite3.connect(
    '/Users/mateusz/Documents/Programowanie/PyDeutsch/germanbase.db')
c = conn.cursor()

print("PyNiemiecki v.0.85\nOstatnia aktualizacja: 06.03.2022.\n + Wybór rodziału także w tłumaczeniu na niemiecki")

choice = '99'

while choice != "0":
    print(
        """\nMenu:
      1 - dodaj słowa do bazy
      2 - losuj słowo do przetłumaczenia na polski
      3 - losuj słowo do przetłumaczenia na niemiecki
      4 - pokaż bazę
      5 - pokaż listę odcinków
      0 - wyjdź      
      """)
    choice = input("Wybieram: ")

    if choice == "1":
        chapterAdd = input("Podaj nazwę odcinka: ")
        wordtype = input("Część mowy: ")
        while choice != "Z!":
            wordde = input("Słówko po niemiecku: ")
            wordpl = input("Tłumaczenie na polski: ")
            if wordtype == "rzeczownik":
                wordplural = input("Liczba mnoga: ")
                c.execute("""
                INSERT INTO vocab (word_de, word_pl, word_type, word_plural, word_source)
                VALUES (?,?,?,?,?)""", (wordde, wordpl, wordtype, wordplural, chapterAdd))
                # Zapisz zmiany
                conn.commit()
                print("\nSłówko dodane do bazy.")
                choice = input("Dalej? ")
            if wordtype == "czasownik":
                wordperfekt = input("Partizip Perfekt: ")
                # Wstaw dane
                c.execute("""
                INSERT INTO vocab (word_de, word_pl, word_type, word_perfekt, word_source)
                VALUES (?,?,?,?,?)""", (wordde, wordpl, wordtype, wordperfekt, chapterAdd))
                # Zapisz zmiany
                conn.commit()
                print("\nSłówko dodane do bazy.")
                # 3   c.close()
                choice = input("Dalej? ")
            if wordtype == "przymiotnik":
                # Wstaw dane
                c.execute("""
                INSERT INTO vocab (word_de, word_pl, word_type, word_source)
                VALUES (?,?,?,?)""", (wordde, wordpl, wordtype, chapterAdd))
                # Zapisz zmiany
                conn.commit()
                print("\nSłówko dodane do bazy.")
                # 3   c.close()
                choice = input("Dalej? ")
            if wordtype == "przysłówek":
                # Wstaw dane
                c.execute("""
                INSERT INTO vocab (word_de, word_pl, word_type, word_source)
                VALUES (?,?,?,?)""", (wordde, wordpl, wordtype, chapterAdd))
                # Zapisz zmiany
                conn.commit()
                print("\nSłówko dodane do bazy.")
                # 3   c.close()
                choice = input("Dalej? ")
    if choice == '2':
        finisher = '0'
        chapterRead = input("Słówka z którego odcinka powtarzamy? ")
        while finisher != 'Z!':  
            for row in c.execute('select word_de, word_pl from vocab where word_source = ? order by random() limit 1', (chapterRead,)):
                print("\n", row[0])
                translate = input("\nTłumaczenie: ")
                if translate == row[1]:
                    print("Sehr gut!")
                else:
                    print("Nie o to chodziło. W bazie wygląda to tak: ", row[1])
                if translate == 'Z!':
                    finisher = 'Z!'
    if choice == '3':
        finisher = '0'
        chapterRead = input("Słówka z którego odcinka powtarzamy? ")
        while finisher != 'Z!':
            for row in c.execute('select word_pl, word_de from vocab where word_source = ? order by random() limit 1', (chapterRead,)):
                print("\n", row[0])
                translate = input("\nTłumaczenie: ")
                if translate == row[1]:
                    print("Sehr gut!")
                else:
                    print("Nie o to chodziło. W bazie wygląda to tak: ", row[1])
                if translate == 'Z!':
                    finisher = 'Z!'

    if choice == '4':
        for row in c.execute('SELECT * FROM vocab ORDER BY id'):
            print(row)
#        c.close()
#        choice = input("Wybieram: ")
    if choice == '5':
        for row in c.execute('SELECT DISTINCT word_source FROM vocab ORDER BY id'):
            print(row)
#        c.close()
#        choice = input("Wybieram: ")

# zakończenie programu
    if choice == "0":
        print("Auf wiedersehen")

# for row in c.execute('SELECT * FROM vocab ORDER BY id'):
#     print(row)
# c.close()
# # Zamknięcie połączenia z bazą danych
# conn.close()
