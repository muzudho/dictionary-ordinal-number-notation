"""
python -m test
"""
from src.dicordnum import DicOrdNum

test_data = [
    # 正の整数
    ['0', DicOrdNum(0)],
    ['9', DicOrdNum(9)],
    ['10', DicOrdNum(10)],
    ['99', DicOrdNum(99)],
    ['100', DicOrdNum(100)],
    ['999', DicOrdNum(999)],
    ['1000', DicOrdNum(1000)],

    # 正の整数の文字列
    ['"0"', DicOrdNum('0')],
    ['"9"', DicOrdNum('9')],
    ['"10"', DicOrdNum('10')],
    ['"99"', DicOrdNum('99')],
    ['"100"', DicOrdNum('100')],
    ['"999"', DicOrdNum('999')],
    ['"1000"', DicOrdNum('1000')],

    # 辞書順記数法
    ['"A77"', DicOrdNum('A77')],
    ['"AA777"', DicOrdNum('AA777')],
    ['"AAA7777"', DicOrdNum('AAA7777')],
    ['"AAAA77777"', DicOrdNum('AAAA77777')],

    # 小文字, snake_case への寛容
    ['"a77"', DicOrdNum('a77')],
    ['"aa777"', DicOrdNum('aa777')],
    ['"aaa7777"', DicOrdNum('aaa7777')],
    ['"aaaa77777"', DicOrdNum('aaaa77777')],
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
