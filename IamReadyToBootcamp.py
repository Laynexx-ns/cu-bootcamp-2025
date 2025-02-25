import importlib.metadata
import platform

errors_count = 0

python_version = platform.python_version()
if not (python_version.startswith("3.11") or python_version.startswith("3.12")):
    errors_count += 1
    print(f"[error] версия питона должна быть минимум 3.12, твоя версия: {python_version} "
          f"ссылка на скачивание: https://www.python.org/downloads/release/python-3120/")
    exit(1)

with open("requirements.txt", "r") as file:
    libs = [lib.removesuffix("\n").split("==") for lib in file.readlines()]

libs_errors = {
    "version": [],
    "missing": []
}
for lib, version in libs:

    try:
        installed_version = importlib.metadata.version(lib)
        if installed_version != version:
            libs_errors["version"].append(lib)
            errors_count += 1
    except importlib.metadata.PackageNotFoundError:
        libs_errors["missing"].append(lib)
        errors_count += 1

print(f"[info] всего ошибок: {errors_count}")
if errors_count == 0:
    print("[ok] УРА! Все работает, ждем тебя на буткемпе!")
    exit(0)

print("Чет многовато ошибок, попробуй еще раз, мы в тебя верим!\n"
      "Инструкция: https://github.com/pavelglazunov/cu-bootcamp-2025\n")
print(f"Пропущенные библиотеки: {', '.join(libs_errors['missing'])}")
print(f"Библиотеки с ошибкой в версии: {', '.join(libs_errors['version'])}\n")
print(f"Используй pip3 install -r requirements.txt")

exit(1)
