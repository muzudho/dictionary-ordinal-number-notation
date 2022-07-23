![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62dc0fea91b9c.png)  
「  どのフォルダーに入ってるんだぜ？」  

![202101__character__28--kifuwarabe-futsu.png](https://crieit.now.sh/upload_images/e846bc7782a0e037a1665e6b3d51b02462dc100f04369.png)  
「　4番のフォルダーだぜ」

```plaintext
📂 0
📂 1
📂 2
📂 3
📂 4
📂 5
📂 6
📂 7
📂 8
📂 9
📂 10
📂 11
📂 12
📂 13
...
```

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62dc0fea91b9c.png)  
「 👆 Windows のファイルエクスプローラーは 名前順にソートすると 数字は昇順に並ぶのか。
よっしゃ Visual Studio 2022 Preview で開けたろ」  

```plaintext
📂 0
📂 1
📂 11
📂 12
📂 13
📂 14
📂 15
📂 16
📂 17
📂 18
📂 19
📂 2
📂 20
📂 21
📂 22
📂 23
📂 24
...
```

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62dc0fea91b9c.png)  
「 👆 4 のフォルダーはどこだぜ！」  

![202108__character__12--ohkina-hiyoko-futsu2.png](https://crieit.now.sh/upload_images/31f0f35be3a4b6b05ce597c7aab702b762dc10e82743b.png)
「 辞書順に並んでるから　多分 39 の下よ」  

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62dc0fea91b9c.png)  
「 なんで ソートのアルゴリズムが違うんだぜ！」  

![202101__character__28--kifuwarabe-futsu.png](https://crieit.now.sh/upload_images/e846bc7782a0e037a1665e6b3d51b02462dc100f04369.png)  
「 嫌なら Windows を捨てて Linux にしろだぜ」  

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62dc0fea91b9c.png)  
「 Windows の名前ソートを調べたろ」  

## Windowsのファイルエクスプローラーの名前順

```plaintext
📂 0A    # 0 が無視されるとしても A が数字より上なのが分けがわからん
📂 0
📂 1
📂 -1    # ハイフンは負数とは判定されない
📂 2
📂 3
📂 4
📂 5
📂 6
📂 7
📂 08    # 0 は無視される。数字順と思えば納得
📂 8
📂 9
📂 10
📂 99
📂 100
📂 A
```

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62dc0fea91b9c.png)  
「 👆 ワケ分かんね」  

## Visual Studio 2022 Preview のソリューション エクスプローラーの名前順

```plaintext
📂 0
📂 08
📂 0A
📂 1
📂 -1    # ハイフンは負数とは判定されない
📂 10
📂 100
📂 2
📂 3
📂 4
📂 5
📂 6
📂 7
📂 8
📂 9
📂 99
📂 A
```

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62dc0fea91b9c.png)  
「 👆 納得の辞書順だぜ」  

![202108__character__12--ohkina-hiyoko-futsu2.png](https://crieit.now.sh/upload_images/31f0f35be3a4b6b05ce597c7aab702b762dc10e82743b.png)
「 辞書順の方が基本で、  
むしろ Windows ファイルエクスプローラーの方が気を利かせて 数字の部分を並び替えてくれるのよ。  
多分 電話番号とか 想定してんじゃないの？」  

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62dc0fea91b9c.png)  
「 だれが 電話番号なんか想定してフォルダーを並び替えてほしいんだぜ！  
前ゼロを無視したり、負数の符号に対応してないのに 正の整数だけソートしたり、ワケ分からん！」  

![202101__character__28--kifuwarabe-futsu.png](https://crieit.now.sh/upload_images/e846bc7782a0e037a1665e6b3d51b02462dc100f04369.png)  
「 分けの分かる部分だけを使えだぜ」  

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62dc0fea91b9c.png)  
「 わたしの手にかかれば　問題は　解決までの手順に変わるぜ」  

# [解決方法] 零，または正の整数は昇順になる

## 例

```plaintext
📂 1
📂 2
📂 3
📂 4
📂 5
📂 6
📂 7
📂 8
📂 9
📂 A10
```

```plaintext
📂 A91
📂 A92
📂 A93
📂 A94
📂 A95
📂 A96
📂 A97
📂 A98
📂 A99
📂 AA100
```

```plaintext
📂 AA991
📂 AA992
📂 AA993
📂 AA994
📂 AA995
📂 AA996
📂 AA997
📂 AA998
📂 AA999
📂 AAA1000
```

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62dc0fea91b9c.png)  
「 👆 `前A` を付ければいいんだぜ」  

![202108__character__12--ohkina-hiyoko-futsu2.png](https://crieit.now.sh/upload_images/31f0f35be3a4b6b05ce597c7aab702b762dc10e82743b.png)
「 `前A` って何よ！」  

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62dc0fea91b9c.png)  
「 `前ゼロ` の `A` 版だぜ」  

## 手順

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

![202101__character__28--kifuwarabe-futsu.png](https://crieit.now.sh/upload_images/e846bc7782a0e037a1665e6b3d51b02462dc100f04369.png)  
「 負の数は どうすんだぜ？」  

# [解決方法] 負の整数は昇順になる

## 例

👇 例： Windows ファイルエクスプローラーのファイル名，フォルダー名向け

```plaintext
📂 ___900  # -100
📂 __01    # - 99
📂 __09    # - 91
📂 __10    # - 90
📂 __89    # - 11
📂 __90    # - 10
📂 _1      # -  9
📂 _2      # -  8
📂 _7      # -  3
📂 _8      # -  2
📂 _9      # -  1
📂 0       # Zero
```

👇 例： Visual Studio 2022 Preview のメソッド名の並び順向け

```plaintext
add___900()  # -100
add__01()    # - 99
add__90()    # - 10
add_1()      # -  9
add_8()      # -  2
add_9()      # -  1
add0()       # Zero
```

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62dc0fea91b9c.png)  
「 👆 `前_` を付けて ひっくり返った数を使えば 負数も昇順に並ぶぜ」  

![202108__character__12--ohkina-hiyoko-futsu2.png](https://crieit.now.sh/upload_images/31f0f35be3a4b6b05ce597c7aab702b762dc10e82743b.png)
「 `前_` とか `ひっくり返った数` って何よ！」  

![202101__character__28--kifuwarabe-futsu.png](https://crieit.now.sh/upload_images/e846bc7782a0e037a1665e6b3d51b02462dc100f04369.png)  
「 `ひっくり返った数` というのは、その数を1桁増やした数の絶対値の最小の数だな」  

## 手順

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

これが負数の表記だ。辞書順で昇順に並ぶ  

## 備考

* 👆 アンダースコア `_` は使いたくなかった。 `0` が辞書順なら `0` にしたかったが、 Windows ファイルエクスプローラーや、 Visual Studio 2022 Preview のメソッドの並び順は `0` を無視するという 分けの分からない挙動なので仕方なく使用

# -13 ～ 13 の例

```plaintext
📂 __87  # -13
📂 __88  # -12
📂 __89  # -11
📂 __90  # -10
📂 _1    # -9
📂 _2    # -8
📂 _3    # -7
📂 _4    # -6
📂 _5    # -5
📂 _6    # -4
📂 _7    # -3
📂 _8    # -2
📂 _9    # -1
📂 0
📂 1
📂 2
📂 3
📂 4
📂 5
📂 6
📂 7
📂 8
📂 9
📂 A10
📂 A11
📂 A12
📂 A13
```

![202101__character__31--ramen-tabero-futsu2.png](https://crieit.now.sh/upload_images/5b53e954894672b36c716412a272826b62dc0fea91b9c.png)  
「 👆 これで楽になったぜ」  

![202101__character__28--kifuwarabe-futsu.png](https://crieit.now.sh/upload_images/e846bc7782a0e037a1665e6b3d51b02462dc100f04369.png)  
「 こんな おかしな **バッドノウハウ** が流行る前に GUIのリストのソートアルゴリズムを ユーザーが指定できるようにしてほしいぜ」  

# 関連する記事

📖 [Qiita版 辞書順記数法](https://qiita.com/muzudho1/items/95852145eceddecd1503) - 頭が固い説明
📖 [数珠玉記数法](https://crieit.net/posts/Beads-Nested-Number-Notation) - 組み合わせて使える  
📖 [電脳記数法](https://crieit.net/posts/Cyber-Number-Notation) - 辞書順記数法と 数珠玉記数法を組み合わせたもの  

Example: 📖 [dictionary-ordinal-number-notation](https://github.com/muzudho/dictionary-ordinal-number-notation)