import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

# 最近6試合の成績
# 対象のサイトURL
url = "https://baseball.yahoo.co.jp/mlb/player/2100825/top"

# URLリソースを開く
res = urllib.request.urlopen(url)

# インスタンスの作成
soup = BeautifulSoup(res, 'html.parser')

# 必要な要素とclass名
# 選手の個人成績
player_data = soup.find_all("td", class_="bb-playerStatsTable__data")

# 取得した選手の個人成績を出力
player_data_list = []
for player_data_text in player_data:
  player_data_list.append(player_data_text.text)

# print(player_data_list)

# list内の改行と空白を削除
for i in range(len(player_data_list)):
  player_data_list[i] = player_data_list[i].replace('\n','')
  player_data_list[i] = player_data_list[i].replace(' ','')

for i in range(len(player_data_list)):
  if player_data_list[i] == "オリオールズ":
    index = i
del player_data_list[index:]

del player_data_list[0:index-66]

# print(player_data_list)

# numpyに変換
player_data_list_np = np.array(player_data_list)

# データフレームに適した形にreshape
player_data_list_np = player_data_list_np.reshape([6,11])

# print(player_data_list_np)

# データフレームに変換
otani_sixgame_df = pd.DataFrame(player_data_list_np) 

# otani_sixgame_df

# カラム名の取得
player_data_columns = soup.find_all("th", class_="bb-playerStatsTable__head")

# 取得したカラム名を出力
player_data_columns_list = []
for player_data_columns_text in player_data_columns:
  player_data_columns_list.append(player_data_columns_text.text)

del player_data_columns_list[0:181]
del player_data_columns_list[11:]

# カラムにplayer_data_columns_listを指定している
otani_sixgame_df = otani_sixgame_df.set_axis(player_data_columns_list, axis=1)

# otani_sixgame_df


# 対チーム別成績
# 対象のサイトURL
url = "https://baseball.yahoo.co.jp/mlb/player/2100825/top"

# URLリソースを開く
res = urllib.request.urlopen(url)

# インスタンスの作成
soup = BeautifulSoup(res, 'html.parser')

# 必要な要素とclass名
# 選手の個人成績
player_data = soup.find_all("td", class_="bb-playerStatsTable__data")

# 取得した選手の個人成績を出力
player_data_list = []
for player_data_text in player_data:
  player_data_list.append(player_data_text.text)

# print(player_data_list)

# list内の改行と空白を削除
for i in range(len(player_data_list)):
  player_data_list[i] = player_data_list[i].replace('\n','')
  player_data_list[i] = player_data_list[i].replace(' ','')

for i in range(len(player_data_list)):
  if player_data_list[i] == "3月":
    index = i
del player_data_list[index:]

for i in range(len(player_data_list)):
  if player_data_list[i] == "オリオールズ":
    index = i
del player_data_list[0:index]

# print(player_data_list)

# numpyに変換
player_data_list_np = np.array(player_data_list)

label = len(player_data_list)/25

# データフレームに適した形にreshape
player_data_list_np = player_data_list_np.reshape([int(label),25])

# print(player_data_list_np)

# データフレームに変換
otani_team_df = pd.DataFrame(player_data_list_np) 

# otani_team_df

# カラム名の取得
player_data_columns = soup.find_all("th", class_="bb-playerStatsTable__head")

# 取得したカラム名を出力
player_data_columns_list = []
for player_data_columns_text in player_data_columns:
  player_data_columns_list.append(player_data_columns_text.text)

del player_data_columns_list[0:192]
del player_data_columns_list[25:]

# print(player_data_columns_list)

# カラムにplayer_data_columns_listを指定している
otani_team_df = otani_team_df.set_axis(player_data_columns_list, axis=1)

# otani_team_df


# 月別成績
# 対象のサイトURL
url = "https://baseball.yahoo.co.jp/mlb/player/2100825/top"

# URLリソースを開く
res = urllib.request.urlopen(url)

# インスタンスの作成
soup = BeautifulSoup(res, 'html.parser')

# 必要な要素とclass名
# 選手の個人成績
player_data = soup.find_all("td", class_="bb-playerStatsTable__data")

# 取得した選手の個人成績を出力
player_data_list = []
for player_data_text in player_data:
  player_data_list.append(player_data_text.text)

# print(player_data_list)

# list内の改行と空白を削除
for i in range(len(player_data_list)):
  player_data_list[i] = player_data_list[i].replace('\n','')
  player_data_list[i] = player_data_list[i].replace(' ','')

for i in range(len(player_data_list)):
  if player_data_list[i] == "右投":
    index = i
del player_data_list[index:]

for i in range(len(player_data_list)):
  if player_data_list[i] == "3月":
    index = i
del player_data_list[0:index]

# print(player_data_list)

# numpyに変換
player_data_list_np = np.array(player_data_list)

label = len(player_data_list)/25

# データフレームに適した形にreshape
player_data_list_np = player_data_list_np.reshape([int(label),25])

# print(player_data_list_np)

# データフレームに変換
otani_month_df = pd.DataFrame(player_data_list_np) 

# otani_month_df

# カラム名の取得
player_data_columns = soup.find_all("th", class_="bb-playerStatsTable__head")

# 取得したカラム名を出力
player_data_columns_list = []
for player_data_columns_text in player_data_columns:
  player_data_columns_list.append(player_data_columns_text.text)

del player_data_columns_list[0:217]
del player_data_columns_list[25:]

# print(player_data_columns_list)

# カラムにplayer_data_columns_listを指定している
otani_month_df = otani_month_df.set_axis(player_data_columns_list, axis=1)

# otani_month_df


# 対左右別成績
# 対象のサイトURL
url = "https://baseball.yahoo.co.jp/mlb/player/2100825/top"

# URLリソースを開く
res = urllib.request.urlopen(url)

# インスタンスの作成
soup = BeautifulSoup(res, 'html.parser')

# 必要な要素とclass名
# 選手の個人成績
player_data = soup.find_all("td", class_="bb-playerStatsTable__data")

# 取得した選手の個人成績を出力
player_data_list = []
for player_data_text in player_data:
  player_data_list.append(player_data_text.text)

# print(player_data_list)

# list内の改行と空白を削除
for i in range(len(player_data_list)):
  player_data_list[i] = player_data_list[i].replace('\n','')
  player_data_list[i] = player_data_list[i].replace(' ','')

for i in range(len(player_data_list)):
  if player_data_list[i] == "右投":
    index = i
del player_data_list[0:index]

for i in range(len(player_data_list)):
  if player_data_list[i] == "左投":
    index = i
del player_data_list[index+23:]

player_data_list.insert(12,"右投")
player_data_list.insert(36,"左投")

# print(player_data_list)

# numpyに変換
player_data_list_np = np.array(player_data_list)

label = len(player_data_list)/12

# データフレームに適した形にreshape
player_data_list_np = player_data_list_np.reshape([int(label),12])

# print(player_data_list_np)

# データフレームに変換
otani_right_left_df = pd.DataFrame(player_data_list_np) 

# otani_right_left_df

# カラム名の取得
player_data_columns = soup.find_all("th", class_="bb-playerStatsTable__head")

# 取得したカラム名を出力
player_data_columns_list = []
for player_data_columns_text in player_data_columns:
  player_data_columns_list.append(player_data_columns_text.text)

del player_data_columns_list[0:242]
del player_data_columns_list[12:]

# print(player_data_columns_list)

# # カラムにplayer_data_columns_listを指定している
otani_right_left_df = otani_right_left_df.set_axis(player_data_columns_list, axis=1)

# otani_right_left_df


# 球場別成績
# 対象のサイトURL
url = "https://baseball.yahoo.co.jp/mlb/player/2100825/top"

# URLリソースを開く
res = urllib.request.urlopen(url)

# インスタンスの作成
soup = BeautifulSoup(res, 'html.parser')

# 必要な要素とclass名
# 選手の個人成績
player_data = soup.find_all("td", class_="bb-playerStatsTable__data")

# 取得した選手の個人成績を出力
player_data_list = []
for player_data_text in player_data:
  player_data_list.append(player_data_text.text)

# print(player_data_list)

# list内の改行と空白を削除
for i in range(len(player_data_list)):
  player_data_list[i] = player_data_list[i].replace('\n','')
  player_data_list[i] = player_data_list[i].replace(' ','')

for i in range(len(player_data_list)):
  if player_data_list[i] == "左投":
    index = i
del player_data_list[:index+23]

for i in range(len(player_data_list)):
  if player_data_list[i] == "0-0":
    index = i
del player_data_list[index:]

# print(player_data_list)

# numpyに変換
player_data_list_np = np.array(player_data_list)

label = len(player_data_list)/25

# データフレームに適した形にreshape
player_data_list_np = player_data_list_np.reshape([int(label),25])

# print(player_data_list_np)

# データフレームに変換
otani_stadiam_df = pd.DataFrame(player_data_list_np) 

# otani_stadiam_df

# カラム名の取得
player_data_columns = soup.find_all("th", class_="bb-playerStatsTable__head")

# 取得したカラム名を出力
player_data_columns_list = []
for player_data_columns_text in player_data_columns:
  player_data_columns_list.append(player_data_columns_text.text)

del player_data_columns_list[0:254]
del player_data_columns_list[25:]

# print(player_data_columns_list)

# # カラムにplayer_data_columns_listを指定している
otani_stadiam_df = otani_stadiam_df.set_axis(player_data_columns_list, axis=1)

# otani_stadiam_df


# カウント別成績
# 対象のサイトURL
url = "https://baseball.yahoo.co.jp/mlb/player/2100825/top"

# URLリソースを開く
res = urllib.request.urlopen(url)

# インスタンスの作成
soup = BeautifulSoup(res, 'html.parser')

# 必要な要素とclass名
# 選手の個人成績
player_data = soup.find_all("td", class_="bb-playerStatsTable__data")

# 取得した選手の個人成績を出力
player_data_list = []
for player_data_text in player_data:
  player_data_list.append(player_data_text.text)

# print(player_data_list)

# list内の改行と空白を削除
for i in range(len(player_data_list)):
  player_data_list[i] = player_data_list[i].replace('\n','')
  player_data_list[i] = player_data_list[i].replace(' ','')

for i in range(len(player_data_list)):
  if player_data_list[i] == "なし":
    index = i
del player_data_list[index:]

for i in range(len(player_data_list)):
  if player_data_list[i] == "0-0":
    index = i
del player_data_list[:index]

# print(player_data_list)

# numpyに変換
player_data_list_np = np.array(player_data_list)

label = len(player_data_list)/11

# データフレームに適した形にreshape
player_data_list_np = player_data_list_np.reshape([int(label),11])

# print(player_data_list_np)

# データフレームに変換
otani_count_df = pd.DataFrame(player_data_list_np) 

# otani_count_df

# カラム名の取得
player_data_columns = soup.find_all("th", class_="bb-playerStatsTable__head")

# 取得したカラム名を出力
player_data_columns_list = []
for player_data_columns_text in player_data_columns:
  player_data_columns_list.append(player_data_columns_text.text)

del player_data_columns_list[0:279]
del player_data_columns_list[11:]

# print(player_data_columns_list)

# # カラムにplayer_data_columns_listを指定している
otani_count_df = otani_count_df.set_axis(player_data_columns_list, axis=1)

# otani_count_df


# 塁状況別成績
# 対象のサイトURL
url = "https://baseball.yahoo.co.jp/mlb/player/2100825/top"

# URLリソースを開く
res = urllib.request.urlopen(url)

# インスタンスの作成
soup = BeautifulSoup(res, 'html.parser')

# 必要な要素とclass名
# 選手の個人成績
player_data = soup.find_all("td", class_="bb-playerStatsTable__data")

# 取得した選手の個人成績を出力
player_data_list = []
for player_data_text in player_data:
  player_data_list.append(player_data_text.text)

# print(player_data_list)

# list内の改行と空白を削除
for i in range(len(player_data_list)):
  player_data_list[i] = player_data_list[i].replace('\n','')
  player_data_list[i] = player_data_list[i].replace(' ','')

for i in range(len(player_data_list)):
  if player_data_list[i] == "なし":
    index = i
del player_data_list[0:index]

for i in range(len(player_data_list)):
  if player_data_list[i] == "満塁":
    index = i
del player_data_list[index+11:]

# print(player_data_list)

# numpyに変換
player_data_list_np = np.array(player_data_list)

label = len(player_data_list)/11

# データフレームに適した形にreshape
player_data_list_np = player_data_list_np.reshape([int(label),11])

# print(player_data_list_np)

# データフレームに変換
otani_base_df = pd.DataFrame(player_data_list_np) 

# otani_base_df

# カラム名の取得
player_data_columns = soup.find_all("th", class_="bb-playerStatsTable__head")

# 取得したカラム名を出力
player_data_columns_list = []
for player_data_columns_text in player_data_columns:
  player_data_columns_list.append(player_data_columns_text.text)

del player_data_columns_list[0:290]
del player_data_columns_list[11:]

# print(player_data_columns_list)

# # カラムにplayer_data_columns_listを指定している
otani_base_df = otani_base_df.set_axis(player_data_columns_list, axis=1)

# otani_base_df


# 大谷の個人成績
otani_sixgame_df.to_csv(".\otani-data\otani_sixgame.csv")
otani_team_df.to_csv(".\otani-data\otnai_team.csv")
otani_month_df.to_csv(".\otani-data\otani_month.csv")
otani_right_left_df.to_csv(".\otani-data\otani_right_left.csv")
otani_count_df.to_csv(".\otani-data\otani_count.csv")
otani_base_df.to_csv(".\otani-data\otani_base.csv")