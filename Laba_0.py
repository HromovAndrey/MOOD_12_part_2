# створіть програму що відтворює історію відвідувань веб сторінок
# кожна відвідна сторінка додається до стеку
# Можга реалізувати можливість повернуться  до попередньої сторінки
# за допомогою видалення вершини стеку

class WebHistory:
    def __init__(self):
        self.stack = []

    def visit_page(self, page):
        self.stack.append(page)
        print(f"Відвідана сторінка: {page}")

    def go_back(self):
        if not self.stack:
            print("Історія відвідувань порожня")
        else:
            previous_page = self.stack.pop()
            print(f"Повернення до попередньої сторінки: {previous_page}")
def display_menu():
    print("Меню:")
    print("1. Відвідати нову сторінку")
    print("2. Повернутися до попередньої сторінки")
    print("3. Вийти")
def main():
    web_history = WebHistory()

    while True:
        display_menu()
        choice = input("Виберіть опцію: ")

        if choice == "1":
            page = input("Введіть URL відвідуваної сторінки: ")
            web_history.visit_page(page)
        elif choice == "2":
            web_history.go_back()
        elif choice == "3":
            print("До побачення!")
            break
        else:
            print("Невідома опція. Спробуйте ще раз.")


if __name__ == "__main__":
    main()






