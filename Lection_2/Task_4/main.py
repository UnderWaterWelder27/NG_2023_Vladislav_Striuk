library = [
    {"Title": "NO_BOOK",
     "Author": "NO_AUTHOR",
     "Pages": 0,
     "Genre": "NO_GENRE",
     "Binding": "NO_BINDING"
     }
]

while True:
    print("Choose what to do in library:  \n"
          "(1) Add book \n"
          "(2) Remove book \n"
          "(3) Edit book \n"
          "(4) Search book \n"
          "(5) Show library content \n"
          "(6) Exit \n")

    match choose_action := input(">_ "):
        case "1":
            new_book = {"Title": "NO_BOOK",
                        "Author": "NO_AUTHOR",
                        "Pages": 0,
                        "Genre": "NO_GENRE",
                        "Binding": "NO_BINDING"
                        }

            title = input("Book title: ")
            author = input("Book author: ")
            pages = input("Book pages: ")
            genre = input("Book genre: ")
            binding = input("Book binding: ")

            new_book.update(
                {"Title": title,
                 "Author": author,
                 "Pages": pages,
                 "Genre": genre,
                 "Binding": binding
                 }
            )

            library.append(new_book)

        case "2":
            pass

        case "3":
            pass

        case "4":
            pass

        case "5":
            for i in range(len(library)):
                print(str(i + 1), f") {library[i]['Title']} - {library[i]['Author']} "
                                  f"(Genre {library[i]['Genre']}, {library[i]['Pages']} p., "
                                  f"{library[i]['Binding']})", end="\n")

        case "6":
            break

        case _:
            pass
