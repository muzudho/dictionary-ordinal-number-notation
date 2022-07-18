"""
python -m test
"""
from src.dicordnum import DicOrdNum

test_data = [
    # 数値
    ['0', DicOrdNum(0)],
    ['9', DicOrdNum(9)],
    ['10', DicOrdNum(10)],
    ['99', DicOrdNum(99)],
    ['100', DicOrdNum(100)],
    ['999', DicOrdNum(999)],
    ['1000', DicOrdNum(1000)],

    # 文字列
    ['"0"', DicOrdNum('0')],
    ['"9"', DicOrdNum('9')],
    ['"10"', DicOrdNum('10')],
    ['"99"', DicOrdNum('99')],
    ['"100"', DicOrdNum('100')],
    ['"999"', DicOrdNum('999')],
    ['"1000"', DicOrdNum('1000')],
]

for datum in test_data:
    print(f"{datum[0]} --> {datum[1]} {datum[1].number}")

try:
    print(f"[Error] -1 --> {DicOrdNum('-1')}")
except:
    print(f"-1 is not DicOrdNum")

# Aの個数が合っているか確認します
try:
    print(f"[Error] A1 --> {DicOrdNum('A1')}")
except:
    print(f"A1 is not DicOrdNum")

try:
    print(f"[Error] AA10 --> {DicOrdNum('AA10')}")
except:
    print(f"AA10 is not DicOrdNum")
