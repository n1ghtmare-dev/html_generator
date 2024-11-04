status_catalogs = {
    "menu": ["Конструировать сайт"],
    "construct": ["Добавить h1", "Добавить button"]
}

actions = {
    "Конструировать сайт": "construct",
}

tags = {
    "button": "<!--t BUTTON -->",
    "h1": "<!--t h1 -->"
}

elements = {
    "Добавить h1": "текст",
    "Добавить button": "имя кнопки"
}

mainframe = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    
</body>
</html>
'''

h1 = "<h1>{text}</h1>"

templates = {
    "mainframe": mainframe,
    "h1": h1,
}
