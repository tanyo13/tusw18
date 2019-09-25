Pythonプログラム自体については，この講義で十分扱っているはずだが，
AtCoderで解答を提出する際には，入出力の扱いに慣れていないと難しい
点がある．
インターネット上には詳しい[記事](https://qiita.com/kyuna/items/8ee8916c2f4e36321a1c) があるので参照すると良いが，ここでも簡単にまとめておく．

AtCoder の問題は，原則として標準入力から問題データが与えられ，
解答データは標準出力に送ることになる．

出力は普通に print() 関数を使えば良いので，あまり問題は
ない．入力はほとんどの場合，input() 関数を使うのだが，
これを使った後でなにがしかの処理が必要になることが多い．

以下，A問題用，B問題用，と分けるが，おおまかな目安である．

## A問題用

### 1つの文字列

文字列が1つ与えられるのが，最も単純な場合である．
input 関数の戻り値を文字列として使えば良い．

{{% panel theme="info" header="例題1" %}}

英小文字からなる文字列 S が与えられる．S の長さが5以上なら `Yes` を，
そうでなければ `No` を出力せよ．

入力は，以下の形式で標準入力から与えられる．

> $S$

{{% /panel %}}

解答例:

```
S = input()  # 文字列を読む．

# 以下，解答を作る．
if len(S) >= 5:
    print('Yes')
else:
    print('No')
```

プログラムが書けたら，テストをしてみる必要がある．
AtCoderサイトの上部に，「コードテスト」というタブがあるので，それを
選択する．
___言語としてPython3 (3.4.3) を選んで___から，
ソースコードを貼り付ける．
「標準入力」の欄に，適当な文字列を入力して「実行」ボタンを押し，
「標準出力」に意図した答が出力されることを確認する．

* 類題: [ABC141A](https://atcoder.jp/contests/abc141/tasks/abc141_a)

### 複数の文字列(各行1つ)

複数の文字列が1行に一つずつ与えられるのであれば，input をその回数だけ
呼べば良い．input関数は，1行の入力を読むのである．

{{% panel theme="info" header="例題2" %}}

英小文字からなる文字列 S と T が与えられる．S の方が T より長ければ `Long`，
同じ長さならば `Equal`，T の方が S より長ければ `Short` と出力せよ．
そうでなければ `No` を出力せよ．

入力は，標準入力から以下の形式で与えられる．

> $S$\\
> $T$

{{% /panel %}}

解答例:

```
S = input()    # 最初の行を読む．
T = input()    # 次の行を読む．

# 以下，解答を作る．
if len(S) > len(T):
    print('Long')
elif len(S) == len(T):
    print('Equal')
else:
    print('Short')
```

* 類題: [ABC139A](https://atcoder.jp/contests/abc139/tasks/abc139_a)

### 1つの整数

整数を読む場合も，___一旦は文字列として読み___，
その後で ___整数に変換___ する．変換には int 関数を用いる．

{{% panel theme="info" header="例題3" %}}

整数 X が与えられる．X を2倍した数を出力せよ．

入力は，標準入力から以下の形式で与えられる．

> $X$


{{% /panel %}}

解答例:

```
line = input()    # 最初の行を読む．この時点ではlineは文字列．
X = int(line)     # 整数に変換するために，int関数を呼ぶ．

# 以下，解答を作る．
print(X * 2)
```

類題: [ABC134A](https://atcoder.jp/contests/abc134/tasks/abc134_a)


#### 複数の整数(1行)

1行に複数個の整数が与えられる場合は，
まず input を1回だけ呼んでその行を取得し，それから split で
分割する．このように分割したものを，1つずつ整数に変換すれば良い．

{{% panel theme="info" header="例題4" %}}

整数 X, Y, Z, W が与えられる．これら4つの整数の積を求めよ．

入力は，標準入力から以下の形式で与えられる．

> $X \quad Y\quad Z\quad W$

{{% /panel %}}

解答例:

```
line = input()                         # 入力は1行なので，inputを1回だけ呼ぶ．
strX, strY, strZ, strW = line.split()  # split を使って分割し，
                                       #     それらを1つずつ変数に格納する．
X = int(strX)                          # 整数に変換する．
Y = int(strY)
Z = int(strZ)
W = int(strW)

# 以下，解答を作る．
print(X * Y * Z * W)
```

インターネットを検索するとmap を使って書く例がたくさん転がっている．
その方が短く書けるし，私も自分ではそう書く．
しかし，慣れていないうちは，愚直に上のように書くことを勧める．

類題: [ABC137A](https://atcoder.jp/contests/abc137/tasks/abc137_a)


## A問題用?

以下の2つは，類題が見つからないが，一応書いておく．

### 複数の文字列(1行)

複数の文字列が1行にすべて与えられる場合には，input関数は1回しか
呼ぶことはできない．一度呼ぶと，その行のすべてを読んでしまうからである．
読んでから分割するためには，splitメソッドを用いれば良い．

{{% panel theme="info" header="例題5" %}}

英小文字からなる文字列 S, T, U が与えられる．
3つの文字列の長さの和を出力せよ．

入力は，標準入力から以下の形式で与えられる．

> $S \quad T \quad U$


{{% /panel %}}

解答例:

```
line = input()
S,T,U = line.split()
print(len(S) + len(T) + len(U))
```

### 複数の整数(各行1つ)

複数の整数が各行1つずつ与えられるなら，
各行を文字列として input で読み，それを整数に変換すれば良い．

{{% panel theme="info" header="例題6" %}}

整数 X, Y, Z が与えられる．これら3つの整数の和を求めよ．

入力は，標準入力から以下の形式で与えられる．

> $X$\\
> $Y$\\
> $Z$

{{% /panel %}}

解答例:

```
line1 = input()
X = int(line1)
line2 = input()
Y = int(line2)
line3 = input()
Z = int(line3)
print(X + Y + Z)
```

## B問題用

#### 個数と1行のデータ

最初の行で個数が与えられ，
次の行にスペース区切りでその戸数分のデータが与えられるという
パターンは，比較的よく現れる．
Python の場合には，最初の個数は使わなくても，データを読むことができる．
データはリストに格納するのが良いであろう．

{{% panel theme="info" header="例題7" %}}

整数 $N$ と，整数 $A_1, A_2, \ldots, A_N$ が与えられる．
$A_1 + A_2 + \cdots + A_N$ を出力せよ．

入力は，標準入力から以下の形式で与えられる．

> $N$\\
> $A_1\quad A_2\quad \cdots \quad A_N$

{{% /panel %}}

解答例:

```
# Nを読む．
N = int(input())

# リストAを読む．
line = input()
A = []
for s in line.split():  # line.split() で，入力行を空白で区切ったリストが
                        #    得られる．これは文字列のリストであることに注意．
    x = int(s)          # 数値に変換する．
    A.append(x)         # リストAに追加する．
# 以上で，入力は終了．

# ここから，答えを求める．
ans = 0
for x in A:
    ans += x
print(ans)
```

このコードの場合，最初のデータ$A_1$ は，`A[0]` に格納され，
最後のデータ$A_N$は，`A[N-1]` に格納されるといったように，
番号が一つずれることに注意する．
多くの場合これで支障はないと思う．

類題: [ABC138B](https://atcoder.jp/contests/abc138/tasks/abc138_b)


#### 個数と各行1つのデータ

データが各行に1つずつ与えられるパターンもある．
この場合には，for文で行数文のループを回して読み込む．

{{% panel theme="info" header="例題8" %}}

整数 $N$ と，整数 $A_1, A_2, \ldots, A_N$ が与えられる．
$A_1 + A_2 + \cdots + A_N$ を出力せよ．

入力は，標準入力から以下の形式で与えられる．

> $N$\\
> $A_1$\\
> $A_2$\\
> $\cdots$\\
> $A_N$

{{% /panel %}}

解答例:

```
# Nを読む．
N = int(input())

# リストAを読む．
A = []
for i in in range(N):
    line = input()
    x = int(line)
    A.append(x)
# 以上で入力は終わり．

# ここから，答えを求める．
ans = 0
for x in A:
    ans += x
print(ans)
```

類題: [ABC115B](https://atcoder.jp/contests/abc115/tasks/abc115_b)

#### 個数と各行複数個のデータ

上のパターンの場合，各行に複数個のデータが与えられることが多い．

{{% panel theme="info" header="例題9" %}}

整数 $N$ と，整数 $A_1, A_2, \ldots, A_N$, 
$B_1, B_2, \ldots, B_N$ が与えられる．
$(A_1 - B_1)^2 + (A_2  - B_2)^2 + \cdots + (A_N - B_N)^2$ を出力せよ．

入力は，標準入力から以下の形式で与えられる．

> $N$\\
> $A_1 \quad B_1$\\
> $A_2 \quad B_2$\\
> $\cdots$\\
> $A_N \quad B_N$

{{% /panel %}}

解答例:

```
# Nを読む．
N = int(input())

# リストA, Bを読む．
A = []
B = []
for i in in range(N):
    line = input()         # 1行読む．ここで，Ai と Bi が読み込まれる．
    sa, sb = line.split()  # 空白で分割する．
	                       #     sa, sb はまだ文字列であることに注意．
    A.append[int(sa)]
    B.append[int(sb)]
# 以上で入力は終わり．

# ここから，答えを求める．
ans = 0
for i in range(N):
    d = A[i] - B[i]
    ans += d * d
print(ans)
```

類題: [ABC140B](https://atcoder.jp/contests/abc140/tasks/abc140_b)


#### 表

長方形型のデータが与えられることもある．2次元リストに格納する．

{{% panel theme="info" header="例題10" %}}

<div>
整数 $N$, $M$ と，整数 
$A_{11}, A_{12}, \ldots, A_{1M}, \ldots, A_{N1}, A_{N2}, \ldots, A_{NM}$ が与えられる．
これらすべての和
$A_{11} + \cdots + A_{1M} + \cdots + A_{N1} + \cdots + A_{NM}$
を出力せよ．
</div>

入力は，標準入力から以下の形式で与えられる．

> $N \quad M$\\
> $A\_{11} \quad \cdots \quad A\_{1M}$\\
> $A\_{21} \quad \cdots \quad A\_{2M}$\\
> $\cdots$\\
> $A\_{N1} \quad \cdots \quad A\_{NM}$


{{% /panel %}}

解答例:

```
# Nを読む．
N = int(input())

A = []
for i in in range(N):
    lst = []
    for s in input().split()
        lst.append(int(s))
    A.append(lst)
# 以上で入力は終わり．

# ここから，答えを求める．
ans = 0
for lst in A:
    for x in lst:
        ans += a
print(ans)
```

上の入力部分は実は冗長で，次のように書けば簡明であるが，
慣れないうちは真似しない方が良いかもしれない．

```
N = int(input())
A = [[int(s) for s in input().split()] for _ in range(N)]
```

類題: [ABC133B](https://atcoder.jp/contests/abc133/tasks/abc133_b)
