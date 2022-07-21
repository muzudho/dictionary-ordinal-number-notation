"""
python -m tests.test
"""
from src.dicordnum import DicOrdNum

test_data = [
    # 正の零
    ['0', DicOrdNum(0), '0'],
    # --                ---
    # 1                 2
    # 1. Actual
    # 2. Expected

    # 正の整数
    ['9', DicOrdNum(9), '9', '9'],
    ['10', DicOrdNum(10), 'A10'],
    ['99', DicOrdNum(99), 'A99'],
    ['100', DicOrdNum(100), 'AA100'],
    ['999', DicOrdNum(999), 'AA999'],
    ['1000', DicOrdNum(1000), 'AAA1000'],

    # 負の零（正の零扱い）
    ['-0', DicOrdNum(-0), '0'],

    # 負の整数
    ['-1', DicOrdNum(-1), '_9'],
    ['-2', DicOrdNum(-2), '_8'],
    ['-9', DicOrdNum(-9), '_1'],
    ['-10', DicOrdNum(-10), '__90'],
    ['-99', DicOrdNum(-99), '__01'],
    ['-100', DicOrdNum(-100), '___900'],
    ['-999', DicOrdNum(-999), '___001'],
    ['-1000', DicOrdNum(-1000), '____9000'],
    ['-9999', DicOrdNum(-9999), '____0001'],

    # 正の整数の文字列
    ['"0"', DicOrdNum('0'), '0'],
    ['"9"', DicOrdNum('9'), '9'],
    ['"10"', DicOrdNum('10'), 'A10'],
    ['"99"', DicOrdNum('99'), 'A99'],
    ['"100"', DicOrdNum('100'), 'AA100'],
    ['"999"', DicOrdNum('999'), 'AA999'],
    ['"1000"', DicOrdNum('1000'), 'AAA1000'],

    # 辞書順記数法
    ['"A77"', DicOrdNum('A77'), 'A77'],
    ['"AA777"', DicOrdNum('AA777'), 'AA777'],
    ['"AAA7777"', DicOrdNum('AAA7777'), 'AAA7777'],
    ['"AAAA77777"', DicOrdNum('AAAA77777'), 'AAAA77777'],

    # 小文字, snake_case への寛容
    ['"a77"', DicOrdNum('a77'), 'A77'],
    ['"aa777"', DicOrdNum('aa777'), 'AA777'],
    ['"aaa7777"', DicOrdNum('aaa7777'), 'AAA7777'],
    ['"aaaa77777"', DicOrdNum('aaaa77777'), 'AAAA77777'],
]

for datum in test_data:
    if f"{datum[1]}" == datum[2]:
        print(f"{datum[0]} --> {datum[1]} {datum[1].number}")
    else:
        print(
            f"[Error] {datum[0]} --> {datum[1]} {datum[1].number} Expected: {datum[2]}")

# 間違ったAの個数を例外にできるか確認します
try:
    print(f"[Error] A1 --> {DicOrdNum('A1')}")
except:
    print(f"A1 is not DicOrdNum")

try:
    print(f"[Error] AA10 --> {DicOrdNum('AA10')}")
except:
    print(f"AA10 is not DicOrdNum")
