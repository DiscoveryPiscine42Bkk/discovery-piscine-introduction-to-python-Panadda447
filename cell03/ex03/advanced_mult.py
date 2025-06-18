# advanced_mult.py
i = 0  # เริ่มจากตารางสูตรคูณของ 0

while i <= 10:
    j = 0  # เริ่มคูณจาก 0 ถึง 10
    print(f"Table de {i}:", end=" ")

    while j <= 10:
        print(i * j, end=" ")
        j += 1

    print()  # ขึ้นบรรทัดใหม่หลังจบ 1 แถว
    i += 1
