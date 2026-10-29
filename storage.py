#我这个是从json库里读取数据的
import json#先导入json
from pathlib import Path#导入path方法
DATA_FILE=Path(__file__).resolve().parent / 'tasks.json'#找到json的地址把他拼起来
def load_tasks():
    if not DATA_FILE.exists():
        return []
    with DATA_FILE.open("r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            print("JSON文件格式错误")
            raise
def save_tasks(tasks):
    with DATA_FILE.open("w",encoding="utf-8") as file:
         json.dump(tasks,file,ensure_ascii=False,indent=4)#把这个python转成json语言




