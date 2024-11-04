from info import status_catalogs, actions, elements, tags, templates
import os

class Generator:
    def __init__(self):
        self.project_dir = "project/"
        self.file = f"{self.project_dir}index.html"
        self.status = "menu"

        self.tags = []
        self.update_tags()
        self.chat()

    def chat(self) -> None:
        while True:
            self.catalog_info()
            try:
                query: int = int(input("Введи номер запроса\n>> "))
            except ValueError:
                print("Нужно ввести номер запроса")
                continue
            if self.status in ["menu"]:
                action: str = status_catalogs[self.status][query-1]
                self.go_to(actions[action])
            elif self.status in ["construct"]:
                self.check_file()
                act: str = status_catalogs[self.status][query-1]
                if act in list(elements):
                    in_data: str = input(f"Введите {elements[act]}\n>> ")
                    tag: str = tags[act.split(' ')[1]]
                    self.add_in(in_data, tag, act.split(' ')[1])

    def add_in(self, data: str, label_type: str, template_tag: str) -> None:
        if len(self.tags) == 0:
            string_num: int = self.get_strings("<body>")
            html_code = f'''
            {label_type}
            {templates[template_tag].format(text=data)}
            {label_type.replace('-t', '-e')}
            \n'''
            self.edit_file(html_code, string_num)
        print(f"Добавлено: {label_type}\nДанные: {data}")

    def edit_file(self, html_code: str, line: int):
        with open(self.file, 'r+', encoding='utf-8') as f:
            lines = f.readlines()
            lines[line] = html_code
        with open(self.file, 'w+', encoding='utf-8') as f:
            f.writelines(lines)

    def go_to(self, status: str) -> None:
        self.status = status
        print(f"Вы перешли в {self.status}")

    def catalog_info(self) -> None:
        if self.status in list(status_catalogs):
            btns = status_catalogs[self.status]
            j = 1
            for i in btns:
                print(f"{j} - {i}")
                j += 1

    def check_file(self):
        if not os.path.isfile(self.file):
            with open(self.file, 'w+', encoding='utf-8') as f:
                f.write(templates["mainframe"])
                print("Макет создан")

    def get_strings(self, tag: str) -> int:
        with open(self.file, 'r+', encoding='utf-8') as f:
            line = 0
            for string in f.readlines():
                line += 1
                if string.replace('\n', '') == tag:
                    return line

    def update_tags(self):
        if os.path.isfile(self.file):
            with open(self.file, 'r+', encoding='utf-8') as f:
                for string in f.readlines():
                    if string[0:5] == "<!--t":
                        self.tags.append(string)


def start():
    Generator()