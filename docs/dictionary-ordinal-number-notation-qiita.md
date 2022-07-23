一度に説明すると複雑なので、要点を分けて１つずつ説明する  

# 零，または正の整数を 辞書順記数法 に変換する手順

👇 零，または正の整数があるとする

```plaintext
0  1   21    321     4321
-  -   --    ---     ----
```

👇 `桁数×2-1` の横幅があると考えてほしい

```plaintext
0  1   21    321     4321
-  -  ---  -----  -------
```

👇 `前A` で埋める

```plaintext
0  1  A21  AA321  AAA4321
-  -  ---  -----  -------
```

これで正の数は辞書順に並ぶ  

## 備考

* アスキーコードの順を考えると A(大文字) が好ましいが、 a(小文字) でも構わない  

# 負の整数を 辞書順記数法 に変換する手順

👇 負の整数があるとする  

```plaintext
  -1     -21      -321       -4321
  --     ---      ----       -----
```

👇 負の符号を除去する  

```plaintext
   1      21       321        4321
   -      --       ---        ----
```

👇 `桁数×2` の横幅があると考えてほしい  

```plaintext
   1      21       321        4321
  --    ----    ------    --------
```

👇 `その数を1桁増やした数の最小の数` を求め、上に置く  

```plaintext
  10     100      1000       10000
   1      21       321        4321
  --    ----    ------    --------
```

👇 引き算をする  

```plaintext
  10     100      1000       10000
-  1  -   21  -    321  -     4321
  --    ----    ------    --------
   9      79       679        5679
```

👇 差の横幅を `前_` で埋める  

```plaintext
  --    ----    ------    --------
  _9    __79    ___679    ____5679
```

👇 差を残す  

```
  _9    __79    ___679    ____5679
```

これが負数の表記だ。辞書順で昇順に並ぶ  

## 備考

* 👆 アンダースコア `_` は使いたくなかった。 `0` が Windows ファイルエクスプローラーや Visual Studio 2022 Preview のメソッドの並び順で 辞書順になるなら `前0` にしたかったが、 ならなかった。 分けの分からない挙動なので仕方なく `前_` を使用

# 関連する記事

📖 [Crieit版 辞書順記数法 (Dictionary Ordinal Number Notation) を解説しようぜ（＾～＾）？](https://crieit.net/posts/Dictionary-Ordinal-Number-Notation)  
📖 [数珠玉記数法](https://crieit.net/posts/Beads-Nested-Number-Notation) - 組み合わせて使える  
📖 [電脳記数法](https://crieit.net/posts/Cyber-Number-Notation) - 辞書順記数法と 数珠玉記数法を組み合わせたもの  

Example: 📖 [dictionary-ordinal-number-notation](https://github.com/muzudho/dictionary-ordinal-number-notation)