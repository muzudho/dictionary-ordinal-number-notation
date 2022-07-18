# import traceback
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
    print(f"-1 --> {str(DicOrdNum('-1'))} is bad")
except:
    print(f"-1 is not DicOrdNum")
    # t = traceback.format_exc()
    # print(t)

# Aの個数が合っているか確認します
try:
    print(f"A1 --> {str(DicOrdNum('A1'))} is bad")
except:
    print(f"A1 is not DicOrdNum")

try:
    print(f"AA10 --> {str(DicOrdNum('AA10'))} is bad")
except:
    print(f"AA10 is not DicOrdNum")
