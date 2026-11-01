import os

from Date import Date
from Dog import Dog


class FileManager:
    def __init__(self, filename, folder="save"):
        self.folder = folder
        self.filename = os.path.join(folder, filename)
        os.makedirs(folder, exist_ok=True)

    def save(self, date, dog):
        with open(self.filename, "w", encoding="utf-8") as f:
            f.write(f"name={dog.name}\n")
            f.write(f"feel={dog.feel}\n")
            f.write(f"bored={dog.bored}\n")
            f.write(f"day={date.day}\n")
            f.write(f"period={date.period}\n")
            f.write(f"try_chance={date.try_chance}\n")

    def load(self):
        try:
            data = {}
            with open(self.filename, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line == "":
                        continue
                    key, value = line.split("=", 1)
                    data[key] = value
            dog = Dog(data["name"], int(data["feel"]), int(data["bored"]))
            date = Date(int(data["day"]), data["period"], int(data["try_chance"]))
            return dog, date
        except FileNotFoundError:
            print()
            print()
            print("저장된 데이터가 없습니다.")
            print()
            print()
        except (KeyError, ValueError):
            print()
            print()
            print("저장 파일이 손상되었습니다.")
            print()
            print()
        return None
