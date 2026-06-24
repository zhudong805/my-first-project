#  命令行版记账本
import os

DATA_FILE = "records.txt"

def load_records():
    if not os.path.exists(DATA_FILE):
        return []
    records = []
    with open(DATA_FILE, "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) == 2:
                records.append((parts[0], float(parts[1])))
    return records

def save_records(records):
    with open(DATA_FILE, "w") as f:
        for desc, amount in records:
            f.write(f"{desc},{amount}\n")

def show_balance(records):
    total = sum(a for _, a in records)
    print(f"\n当前余额：{total:.2f} 元")
    print("---")

def add_record(records):
    desc = input("描述：")
    amount = float(input("金额（收入正数，支出负数）："))
    records.append((desc, amount))
    save_records(records)
    print("已记录！")

def show_history(records):
    if not records:
        print("暂无记录")
        return
    print("\n=== 历史记录 ===")
    for desc, amount in records:
        tag = "收入" if amount >= 0 else "支出"
        print(f"  {desc}: {abs(amount):.2f} 元 ({tag})")

def main():
    records = load_records()
    while True:
        print("\n=== 我的记账本 ===")
        print("1. 查看余额")
        print("2. 记一笔")
        print("3. 查看历史")
        print("0. 退出")
        choice = input("请选择：")
        if choice == "1":
            show_balance(records)
        elif choice == "2":
            add_record(records)
        elif choice == "3":
            show_history(records)
        elif choice == "0":
            print("再见！")
            break
        else:
            print("无效选择")

main()