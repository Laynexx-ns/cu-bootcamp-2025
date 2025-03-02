
## 1️⃣ Установка Python

1. Открой **Терминал** (`Cmd + Пробел` → **Terminal**).
2. Проверь, установлен ли Python:

```sh
python3 --version
```

1. Если Python **не установлен** или версия ниже 3.12, установи его:
    
    - Через Homebrew:
        
        ```sh
        brew install python
        ```
        
    - Или скачай Python с [официального сайта](https://www.python.org/downloads/mac-osx/) и установи его вручную.
4. Проверь успешную установку:
    

```sh
python3 --version
```

Если видишь `Python 3.12.x` – всё ок! 🎉

---

## 2️⃣ Установка Git и клонирование репозитория

1. Проверь, установлен ли Git:

```sh
git --version
```

1. Если Git **не установлен**, установи его:
    
    - Через Homebrew:
        
        ```sh
        brew install git
        ```
        
    - Или скачай с [официального сайта](https://git-scm.com/downloads).
3. Перейди в нужную директорию:
    

```sh
cd your_dir
```

4. Склонируй репозиторий:

```sh
git clone https://github.com/pavelglazunov/cu-butcamp-2025.git
```

5. Перейди в папку с проектом:

```sh
cd cu-butcamp-2025
```

---

## 3️⃣ Установка VS Code

1. Скачай VS Code с [официального сайта](https://code.visualstudio.com/Download).
2. Установи его, переместив в папку **Applications**.
3. Открой VS Code и установи расширение "Python":
    - Перейди в **Extensions** (Cmd+Shift+X).
    - Найди **Python** от Microsoft.
    - Нажми "Install".


![extensions](https://github.com/pavelglazunov/cu-bootcamp-2025/blob/main/docs/static/extansions.png)



---

## 4️⃣ Создание виртуального окружения

1. Открой VS Code и выбери папку проекта (**File** → **Open Folder...** → выбери `cu-butcamp-2025`).
2. Открой **Терминал** (**Terminal** → **New Terminal** или `Ctrl+``).
3. Создай виртуальное окружение:

```sh
python3 -m venv venv
```

1. Активируй его:

```sh
source venv/bin/activate
```

1. Убедись, что в начале строки появился `(venv)`.


![venv_vscode](https://github.com/pavelglazunov/cu-bootcamp-2025/blob/main/docs/static/venv_vscode.png)


---

## 5️⃣ Установка зависимостей из `requirements.txt`

Если ты правильно склонировал репозиторий, то у тебя есть файл `requirements.txt`, установи все нужные пакеты командой:

```sh
pip install -r requirements.txt
```

---

## 6️⃣ Запуск `main.py`

Запусти свой скрипт одной из команд:

```sh
python main.py
```

или

```sh
python3 main.py
```

или через VS Code:

- Открыть `main.py`.
- Нажать `F5` или `Run` → `Run Without Debugging`.

![run_vscode](https://github.com/pavelglazunov/cu-bootcamp-2025/blob/main/docs/static/run_vscode.png)


Если программа **НЕ** вывела

`[status: OK] УРА! Все работает, ждем тебя на буткемпе!`

иди к следующему пункту.

---

## 7️⃣ Ошибки

|Ошибка|Как решить|
|---|---|
|версия Python должна быть минимум 3.12|Установи нужную версию с [сайта](https://www.python.org/downloads/release/python-3120/)|
|Пропущенные библиотеки: <название>|Команда`pip install <название>` или`pip install -r requirements.txt`|
|Библиотеки с ошибкой в версии: <название>|Команда`pip install <название>==<версия>`|

Если у тебя другая ошибка, обратись в чат!
