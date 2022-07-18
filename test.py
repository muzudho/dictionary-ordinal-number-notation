"""
python -m test
"""
from src.dicordnum import DicOrdNum

print(f"0 --> {str(DicOrdNum(0))}")
print(f"9 --> {str(DicOrdNum(9))}")
print(f"10 --> {str(DicOrdNum(10))}")
print(f"99 --> {str(DicOrdNum(99))}")
print(f"100 --> {str(DicOrdNum(100))}")
print(f"999 --> {str(DicOrdNum(999))}")
print(f"1000 --> {str(DicOrdNum(1000))}")

print(f"'0' --> {str(DicOrdNum('0'))}")
print(f"'9' --> {str(DicOrdNum('9'))}")
print(f"'10' --> {str(DicOrdNum('10'))}")
print(f"'99' --> {str(DicOrdNum('99'))}")
print(f"'100' --> {str(DicOrdNum('100'))}")
print(f"'999' --> {str(DicOrdNum('999'))}")
print(f"'1000' --> {str(DicOrdNum('1000'))}")

print(f"'0' --> {str(DicOrdNum('0'))}")
print(f"'9' --> {str(DicOrdNum('9'))}")
print(f"'A10' --> {str(DicOrdNum('10'))}")
print(f"'A99' --> {str(DicOrdNum('99'))}")
print(f"'AA100' --> {str(DicOrdNum('100'))}")
print(f"'AA999' --> {str(DicOrdNum('999'))}")
print(f"'AAA1000' --> {str(DicOrdNum('1000'))}")

try:
    print(f"[Error] -1 --> {str(DicOrdNum('-1'))}")
except:
    print(f"-1 is not DicOrdNum")

# Aの個数が合っているか確認します
try:
    print(f"[Error] A1 --> {str(DicOrdNum('A1'))}")
except:
    print(f"A1 is not DicOrdNum")

try:
    print(f"[Error] AA10 --> {str(DicOrdNum('AA10'))}")
except:
    print(f"AA10 is not DicOrdNum")
