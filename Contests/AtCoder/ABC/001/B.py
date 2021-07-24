# ABC001 - B
'''
1. 0.1 km未満： VVの値は00とする。
2. 0.1km以上5km以下：距離(km)を10倍した値とする。1桁の場合は上位に0を付す。
  例えば、2,000m=2.0kmならば、VVは20である
  200mの場合VVは02である。
3. 6km以上30km以下：距離(km)に50を足した値とする。
  例えば、15,000m=15kmならば、VVは65である。
4. 35km以上70km以下：距離(km)から30を引いて5で割った後、80を足した値とする。
  例えば、40,000m=40kmならば、VVは82である。
5. 70kmより大きい：VVの値は89とする。

なお、VVは必ず（上位の 0 を含めて） 2 桁の整数であり、
上記のルールに従って計算した時に整数にならないような入力や、
上記の範囲に入らない入力 (例： 5 k m より大きく 6 k m 未満) などはありません。

0 90
100 900
1000 5000
6000 30000
35000 70000
71000 100000


入力
0 <= m <= 100000
'''
VV = int(input())
ans = ""

if 100 > VV:
    ans = "00"
elif 100 <= VV < 1000:
    ans = "0" + str(VV//100)
elif 1000 <= VV <= 5000:
    ans = str(VV//100)
elif 6000 <= VV <= 30000:
    ans = str(VV//1000 + 50)
elif 35000 <= VV <= 70000:
    ans = str((VV//1000 - 30)//5+80 )
else:
    ans = "89"

print(ans)