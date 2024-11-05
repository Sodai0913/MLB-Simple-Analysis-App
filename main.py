#モジュールのインポート
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

# 対象のサイトURL(エンゼルス野手)
url = "https://baseball.yahoo.co.jp/mlb/teams/2021003/memberlist?kind=b"

# URLリソースを開く
res = urllib.request.urlopen(url)

# インスタンスの作成
soup = BeautifulSoup(res, 'html.parser')

# 必要な要素(タグ)とclass名
# 選手の個人成績
player_data = soup.find_all("td", class_="bb-playerTable__data")

# カラム名の取得
player_data_columns = soup.find_all("p", class_="bb-playerTable__linkLabel")

# 取得したカラム名を出力
player_data_columns_list = []
for player_data_columns_text in player_data_columns:
  player_data_columns_list.append(player_data_columns_text.text)

# 選手名のカラムを追加
player_data_columns_list.insert(2, "選手名")

# 全角スペースを削除
for i in range(len(player_data_columns_list)):
  player_data_columns_list[i] = player_data_columns_list[i].replace('\u3000','')

# 余分なものを削除
del player_data_columns_list[26:52]

# 取得した選手の個人成績を出力
player_data_list = []
for player_data_text in player_data:
    player_data_list.append(player_data_text.text)


# list内の改行と空白を削除
for i in range(len(player_data_list)):
  player_data_list[i] = player_data_list[i].replace('\n','')
  player_data_list[i] = player_data_list[i].replace(' ','')


# print(player_data_list)

# 標準リストをNumPy配列に変換
ndarray_player_data = np.array(player_data_list)

# reshapeで指定する行の数(listの要素数 / 27)
label_num = len(ndarray_player_data)/27

# reshapeで2次元配列に変換(len(ndarray_player_data)/27行、27列)
ndarray_player_data_list = ndarray_player_data.reshape(int(label_num),27)

# DataFrameに変換
df_Los_Angeles_Angeles_fielder = pd.DataFrame(ndarray_player_data_list)

# カラムにplayer_data_columns_listを指定している
df_Los_Angeles_Angeles_fielder = df_Los_Angeles_Angeles_fielder.set_axis(player_data_columns_list, axis=1)

# チーム名のカラムを追加
df_Los_Angeles_Angeles_fielder = df_Los_Angeles_Angeles_fielder.assign(Team="ロサンゼルス・エンゼルス")


# 関数化
# 野手用の関数 
# fielderはエンゼルス以外の球団に使える
def fielder(url_str,teamname):
# 対象のサイトURL
  url = url_str

  # URLリソースを開く
  res = urllib.request.urlopen(url)

  # インスタンスの作成
  soup = BeautifulSoup(res, 'html.parser')

  # 必要な要素とclass名
  # 選手の個人成績
  player_data = soup.find_all("td", class_="bb-playerTable__data")

  # カラム名の取得
  player_data_columns = soup.find_all("p", class_="bb-playerTable__linkLabel")

  # 取得したカラム名を出力
  player_data_columns_list = []
  for player_data_columns_text in player_data_columns:
    player_data_columns_list.append(player_data_columns_text.text)

  # 選手名のカラムを追加
  player_data_columns_list.insert(2, "選手名")

  # 全角スペースを削除
  for i in range(len(player_data_columns_list)):
    player_data_columns_list[i] = player_data_columns_list[i].replace('\u3000','')

  # 余分なものを削除
  del player_data_columns_list[26:52]

  # 取得した選手の個人成績を出力
  player_data_list = []
  for player_data_text in player_data:
      player_data_list.append(player_data_text.text)

  # list内の改行と空白を削除
  for i in range(len(player_data_list)):
    player_data_list[i] = player_data_list[i].replace('\n','')
    player_data_list[i] = player_data_list[i].replace(' ','')

  # 標準リストをNumPy配列に変換
  ndarray_player_data = np.array(player_data_list)

  # reshapeで指定する行の数(listの要素数 / 27)
  label_num = len(ndarray_player_data)/27

  # reshapeで2次元配列に変換(len(ndarray_player_data)/27行、27列)
  ndarray_player_data_list = ndarray_player_data.reshape(int(label_num),27)

  # DataFrameに変換
  df = pd.DataFrame(ndarray_player_data_list)

  # カラムにplayer_data_columns_listを指定している
  df = df.set_axis(player_data_columns_list, axis=1)

  # チーム名のカラムを追加
  df = df.assign(Team = teamname)

  return df


# 投手用の関数
def pitcher(url_str,teamname):
# 対象のサイトURL
  url = url_str

  # URLリソースを開く
  res = urllib.request.urlopen(url)

  # インスタンスの作成
  soup = BeautifulSoup(res, 'html.parser')

  # 必要な要素とclass名
  # 選手の個人成績
  player_data = soup.find_all("td", class_="bb-playerTable__data")

  # カラム名の取得
  player_data_columns = soup.find_all("p", class_="bb-playerTable__linkLabel")

  # 取得したカラム名を出力
  player_data_columns_list = []
  for player_data_columns_text in player_data_columns:
    player_data_columns_list.append(player_data_columns_text.text)

  # 選手名のカラムを追加
  player_data_columns_list.insert(1, "選手名")

  # 全角スペースを削除
  for i in range(len(player_data_columns_list)):
    player_data_columns_list[i] = player_data_columns_list[i].replace('\u3000','')

  # 余分なものを削除
  del player_data_columns_list[26:52]

  # 取得した選手の個人成績を出力
  player_data_list = []
  for player_data_text in player_data:
      player_data_list.append(player_data_text.text)

  # list内の改行と空白を削除
  for i in range(len(player_data_list)):
    player_data_list[i] = player_data_list[i].replace('\n','')
    player_data_list[i] = player_data_list[i].replace(' ','')

  # 標準リストをNumPy配列に変換
  ndarray_player_data = np.array(player_data_list)

  # reshapeで指定する行の数(listの要素数 / 27)
  label_num = len(ndarray_player_data)/27

  # reshapeで2次元配列に変換
  ndarray_player_data_list = ndarray_player_data.reshape(int(label_num),27)

  # DataFrameに変換
  df = pd.DataFrame(ndarray_player_data_list)

  # カラムにplayer_data_columns_listを指定している
  df = df.set_axis(player_data_columns_list, axis=1)

  # チーム名のカラムを追加
  df = df.assign(Team = teamname)

  return df


# MLBのチームのデータを取得するコード
# チームのデータを取得
# 対象のサイトURL
url = "https://baseball.yahoo.co.jp/mlb/standings/"

# URLリソースを開く
res = urllib.request.urlopen(url)

# インスタンスの作成
soup = BeautifulSoup(res, 'html.parser')

# 必要な要素とclass名
AL_team_list_data = soup.find_all("td", class_="bb-rankTable__data")

# 取得したチームのデータを出力
AL_team_list = []
for teamlist_text in AL_team_list_data:
  AL_team_list.append(teamlist_text.text)

# print(player_data_list)

# list内の改行と空白を削除
for i in range(len(AL_team_list)):
  AL_team_list[i] = AL_team_list[i].replace('\n','')
  AL_team_list[i] = AL_team_list[i].replace(' ','')


# numpyに変換
AL_team_list_np = np.array(AL_team_list)

# データフレームに適した形にreshape
AL_team_list_np = AL_team_list_np.reshape([30,15])


# データフレームに変換
AL_team_list_df = pd.DataFrame(AL_team_list_np)

AL_team_list_columns = ["順位","チーム","試合","勝","敗","引分","勝率","ゲーム差","得点","失点","本塁打","盗塁","打率","防御率","失策"]


# カラムにplayer_data_columns_listを指定している
AL_team_list_df = AL_team_list_df.set_axis(AL_team_list_columns, axis=1)




# 関数の呼び出し
# fielder(野手の関数),pitcher(投手の関数)
# ボルティモア・オリオールズ
df_Baltimore_Orioles_fielder = fielder("https://baseball.yahoo.co.jp/mlb/teams/2021001/memberlist?kind=b","ボルチモア・オリオールズ")
# print(df_Baltimore_Orioles_fielder)

df_Baltimore_Orioles_pitcher = pitcher("https://baseball.yahoo.co.jp/mlb/teams/2021001/memberlist?kind=p","ボルチモア・オリオールズ")
# print(df_Baltimore_Orioles_pitcher)

# ボストン・レッドソックス
df_Boston_Redsox_fielder = fielder("https://baseball.yahoo.co.jp/mlb/teams/2021002/memberlist?kind=b","ボストン・レッドソックス")
# print(df_Boston_Redsox_fielder)

df_Boston_Redsox_pitcher = pitcher("https://baseball.yahoo.co.jp/mlb/teams/2021002/memberlist?kind=p","ボストン・レッドソックス")
# print(df_Boston_Redsox_pitcher)

# ニューヨーク・ヤンキース
df_New_York_Yanks_fielder = fielder("https://baseball.yahoo.co.jp/mlb/teams/2021010/memberlist?kind=b","ニューヨーク・ヤンキース")
# print(df_New_York_Yanks_fielder)

df_New_York_Yanks_pitcher = pitcher("https://baseball.yahoo.co.jp/mlb/teams/2021010/memberlist?kind=p","ニューヨーク・ヤンキース")
# print(df_New_York_Yanks_pitcher)
# 
# トロント・ブルージェイズ
df_Tronto_Blue_Jays_fielder = fielder("https://baseball.yahoo.co.jp/mlb/teams/2021014/memberlist?kind=b","トロント・ブルージェイズ")
# print(df_Tronto_Blue_Jays_fielder)

df_Tronto_Blue_Jays_pitcher = pitcher("https://baseball.yahoo.co.jp/mlb/teams/2021014/memberlist?kind=p","トロント・ブルージェイズ")
# print(df_Tronto_Blue_Jays_pitcher)

# タンパベイ・レイズ
df_Tampa_Bay_Rays_fielder = fielder("https://baseball.yahoo.co.jp/mlb/teams/2021030/memberlist?kind=b","タンパベイ・レイズ")
# print(df_Tampa_Bay_Rays_fielder)

df_Tampa_Bay_Rays_pitcher = pitcher("https://baseball.yahoo.co.jp/mlb/teams/2021030/memberlist?kind=p","タンパベイ・レイズ")
# print(df_Tampa_Bay_Rays_pitcher)

# シカゴ・ホワイトソックス
df_Chicago_White_Sox_fielder = fielder("https://baseball.yahoo.co.jp/mlb/teams/2021004/memberlist?kind=b","シカゴ・ホワイトソックス")
# print(df_Chicago_White_Sox_fielder)

df_Chicago_White_Sox_pitcher = pitcher("https://baseball.yahoo.co.jp/mlb/teams/2021004/memberlist?kind=p","シカゴ・ホワイトソックス")
# print(df_Chicago_White_Sox_pitcher)

# クリーブランド・ガーディアンズ
df_Cleveland_Guardians_fielder = fielder("https://baseball.yahoo.co.jp/mlb/teams/2021005/memberlist?kind=b","クリーブランド・ガーディアンズ")
# print(df_Cleveland_Guardians_fielder)

df_Cleveland_Guardians_pitcher = pitcher("https://baseball.yahoo.co.jp/mlb/teams/2021005/memberlist?kind=p","クリーブランド・ガーディアンズ")
# print(df_Cleveland_Guardians_pitcher)

# デトロイト・タイガース
df_Detroit_Tigers_fielder = fielder("https://baseball.yahoo.co.jp/mlb/teams/2021006/memberlist?kind=b","デトロイト・タイガース")
# print(df_Detroit_Tigers_fielder)

df_Detroit_Tigers_pitcher = pitcher("https://baseball.yahoo.co.jp/mlb/teams/2021006/memberlist?kind=p","デトロイト・タイガース")
# print(df_Detroit_Tigers_pitcher)

# カンザスシティ・ロイヤルズ
df_Kansas_City_Royals_fielder = fielder("https://baseball.yahoo.co.jp/mlb/teams/2021007/memberlist?kind=b","カンザスシティ・ロイヤルズ")
# print(df_Kansas_City_Royals_fielder)

df_Kansas_City_Royals_pitcher = pitcher("https://baseball.yahoo.co.jp/mlb/teams/2021007/memberlist?kind=p","カンザスシティ・ロイヤルズ")
# print(df_Kansas_City_Royals_pitcher)

# ミネソタ・ツインズ
df_Minnesota_Twins_fielder = fielder("https://baseball.yahoo.co.jp/mlb/teams/2021009/memberlist?kind=b","ミネソタ・ツインズ")
# print(df_Minnesota_Twins_fielder)

df_Minnesota_Twins_pitcher = pitcher("https://baseball.yahoo.co.jp/mlb/teams/2021009/memberlist?kind=p","ミネソタ・ツインズ")
# print(df_Minnesota_Twins_pitcher)

# ロサンゼルス・エンゼルス
# print(df_Los_Angeles_Angeles_fielder)

df_Los_Angeles_Angeles_pitcher = pitcher("https://baseball.yahoo.co.jp/mlb/teams/2021003/memberlist?kind=p","ロサンゼルス・エンゼルス")
# print(df_Los_Angeles_Angeles_pitcher)

# オークランド・アスレチックス
df_Oakland_Athletics_fielder = fielder("https://baseball.yahoo.co.jp/mlb/teams/2021011/memberlist?kind=b","オークランド・アスレチックス")
# print(df_Oakland_Athletics_fielder)

df_Oakland_Athletics_pitcher = pitcher("https://baseball.yahoo.co.jp/mlb/teams/2021011/memberlist?kind=p","オークランド・アスレチックス")
# print(df_Oakland_Athletics_pitcher)

# シアトル・マリナーズ
df_Seattle_Mariners_fielder = fielder("https://baseball.yahoo.co.jp/mlb/teams/2021012/memberlist?kind=b","シアトル・マリナーズ")
# print(df_Seattle_Mariners_fielder)

df_Seattle_Mariners_pitcher = pitcher("https://baseball.yahoo.co.jp/mlb/teams/2021012/memberlist?kind=p","シアトル・マリナーズ")
# print(df_Seattle_Mariners_pitcher)

# テキサス・レンジャーズ
df_Texas_Rangers_fielder = fielder("https://baseball.yahoo.co.jp/mlb/teams/2021013/memberlist?kind=b","テキサス・レンジャーズ")
# print(df_Texas_Rangers_fielder)

df_Texas_Rangers_pitcher = pitcher("https://baseball.yahoo.co.jp/mlb/teams/2021013/memberlist?kind=p","テキサス・レンジャーズ")
# print(df_Texas_Rangers_pitcher)

# ヒューストン・アストロズ
df_Houston_Astros_fielder = fielder("https://baseball.yahoo.co.jp/mlb/teams/2021018/memberlist?kind=b","ヒューストン・アストロズ")
# print(df_Houston_Astros_fielder)

df_Houston_Astros_pitcher = pitcher("https://baseball.yahoo.co.jp/mlb/teams/2021018/memberlist?kind=p","ヒューストン・アストロズ")
# print(df_Houston_Astros_pitcher)

# アトランタ・ブレーブス
df_Atlanta_Braves_fielder = fielder("https://baseball.yahoo.co.jp/mlb/teams/2021015/memberlist?kind=b","アトランタ・ブレーブス")
# print(df_Atlanta_Braves_fielder)

df_Atlanta_Braves_pitcher = pitcher("https://baseball.yahoo.co.jp/mlb/teams/2021015/memberlist?kind=p","アトランタ・ブレーブス")
# print(df_Atlanta_Braves_pitcher)

# ワシントン・ナショナルズ
df_Washington_Nationals_fielder = fielder("https://baseball.yahoo.co.jp/mlb/teams/2021020/memberlist?kind=b","ワシントン・ナショナルズ")
# print(df_Washington_Nationals_fielder)

df_Washington_Nationals_pitcher = pitcher("https://baseball.yahoo.co.jp/mlb/teams/2021020/memberlist?kind=p","ワシントン・ナショナルズ")
# print(df_Washington_Nationals_pitcher)

# ニューヨーク・メッツ
df_New_York_Mets_fielder = fielder("https://baseball.yahoo.co.jp/mlb/teams/2021021/memberlist?kind=b","ニューヨーク・メッツ")
# print(df_New_York_Mets_fielder)

df_New_York_Mets_pitcher = pitcher("https://baseball.yahoo.co.jp/mlb/teams/2021021/memberlist?kind=p","ニューヨーク・メッツ")
# print(df_New_York_Mets_pitcher)

# フィラデルフィア・フィリーズ
df_Philadelphia_Phillies_fielder = fielder("https://baseball.yahoo.co.jp/mlb/teams/2021022/memberlist?kind=b","フィラデルフィア・フィリーズ")
# print(df_Philadelphia_Phillies_fielder)

df_Philadelphia_Phillies_pitcher = pitcher("https://baseball.yahoo.co.jp/mlb/teams/2021022/memberlist?kind=p","フィラデルフィア・フィリーズ")
# print(df_Philadelphia_Phillies_pitcher)

# マイアミ・マーリンズ
df_Miami_Marlins_fielder = fielder("https://baseball.yahoo.co.jp/mlb/teams/2021028/memberlist?kind=b","マイアミ・マーリンズ")
# print(df_Miami_Marlins_fielder)

df_Miami_Marlins_pitcher = pitcher("https://baseball.yahoo.co.jp/mlb/teams/2021028/memberlist?kind=p","マイアミ・マーリンズ")
# print(df_Miami_Marlins_pitcher)

# ミルウォーキー・ブリュワーズ
df_Milwaukee_Brewers_fielder = fielder("https://baseball.yahoo.co.jp/mlb/teams/2021008/memberlist?kind=b","ミルウォーキー・ブリュワーズ")
# print(df_Milwaukee_Brewers_fielder)

df_Milwaukee_Brewers_pitcher = pitcher("https://baseball.yahoo.co.jp/mlb/teams/2021008/memberlist?kind=p","ミルウォーキー・ブリュワーズ")
# print(df_Milwaukee_Brewers_pitcher)

# シカゴ・カブス
df_Chicago_Cubs_fielder = fielder("https://baseball.yahoo.co.jp/mlb/teams/2021016/memberlist?kind=b","シカゴ・カブス")
# print(df_Chicago_Cubs_fielder)

df_Chicago_Cubs_pitcher = pitcher("https://baseball.yahoo.co.jp/mlb/teams/2021016/memberlist?kind=p","シカゴ・カブス")
# print(df_Chicago_Cubs_pitcher)

# シンシナティ・レッズ
df_Cincinnati_Reds_fielder = fielder("https://baseball.yahoo.co.jp/mlb/teams/2021017/memberlist?kind=b","シンシナティ・レッズ")
# print(df_Cincinnati_Reds_fielder)

df_Cincinnati_Reds_pitcher = pitcher("https://baseball.yahoo.co.jp/mlb/teams/2021017/memberlist?kind=p","シンシナティ・レッズ")
# print(df_Cincinnati_Reds_pitcher)

#ピッツバーグ・パイレーツ
df_Pittsburgh_Pirates_fielder = fielder("https://baseball.yahoo.co.jp/mlb/teams/2021023/memberlist?kind=b","ピッツバーグ・パイレーツ") 
# print(df_Pittsburgh_Pirates_fielder)

df_Pittsburgh_Pirates_pitcher = pitcher("https://baseball.yahoo.co.jp/mlb/teams/2021023/memberlist?kind=p","ピッツバーグ・パイレーツ") 
# print(df_Pittsburgh_Pirates_pitcher)

# セントルイス・カージナルス
df_St_Louis_Cardinals_fielder = fielder("https://baseball.yahoo.co.jp/mlb/teams/2021024/memberlist?kind=b","セントルイス・カージナルス")
# print(df_St_Louis_Cardinals_fielder)

df_St_Louis_Cardinals_pitcher = pitcher("https://baseball.yahoo.co.jp/mlb/teams/2021024/memberlist?kind=p","セントルイス・カージナルス")
# print(df_St_Louis_Cardinals_pitcher)

# ロサンゼルス・ドジャース
df_Los_Angeles_Dodgers_fielder = fielder("https://baseball.yahoo.co.jp/mlb/teams/2021019/memberlist?kind=b","ロサンゼルス・ドジャース")
# print(df_Los_Angeles_Dodgers_fielder)

df_Los_Angeles_Dodgers_pitcher = pitcher("https://baseball.yahoo.co.jp/mlb/teams/2021019/memberlist?kind=p","ロサンゼルス・ドジャース")
# print(df_Los_Angeles_Dodgers_pitcher)

# サンディエゴ・パドレス
df_San_Diego_Padres_fielder = fielder("https://baseball.yahoo.co.jp/mlb/teams/2021025/memberlist?kind=b","サンディエゴ・パドレス")
# print(df_San_Diego_Padres_fielder)

df_San_Diego_Padres_pitcher = pitcher("https://baseball.yahoo.co.jp/mlb/teams/2021025/memberlist?kind=p","サンディエゴ・パドレス")
# print(df_San_Diego_Padres_pitcher)

# サンフランシスコ・ジャイアンツ
df_San_Francisco_Giants_fielder = fielder("https://baseball.yahoo.co.jp/mlb/teams/2021026/memberlist?kind=b","サンフランシスコ・ジャイアンツ")
# print(df_San_Francisco_Giants_fielder)

df_San_Francisco_Giants_pitcher = pitcher("https://baseball.yahoo.co.jp/mlb/teams/2021026/memberlist?kind=p","サンフランシスコ・ジャイアンツ")
# print(df_San_Francisco_Giants_pitcher)

# コロラド・ロッキーズ
df_Colorado_Rockes_fielder = fielder("https://baseball.yahoo.co.jp/mlb/teams/2021027/memberlist?kind=b","コロラド・ロッキーズ")
# print(df_Colorado_Rockes_fielder)

df_Colorado_Rockes_pitcher = pitcher("https://baseball.yahoo.co.jp/mlb/teams/2021027/memberlist?kind=p","コロラド・ロッキーズ")
# print(df_Colorado_Rockes_pitcher)

# アリゾナ・ダイヤモンドバックス
df_Arizona_Diamondbacks_fielder = fielder("https://baseball.yahoo.co.jp/mlb/teams/2021029/memberlist?kind=b","アリゾナ・ダイヤモンドバックス")
# print(df_Arizona_Diamondbacks_fielder)

df_Arizona_Diamondbacks_pitcher = pitcher("https://baseball.yahoo.co.jp/mlb/teams/2021029/memberlist?kind=p","アリゾナ・ダイヤモンドバックス")
# print(df_Arizona_Diamondbacks_pitcher)


# csvファイルに書き出し
# チームごとにcsvファイルに書き出し
# 野手
df_Baltimore_Orioles_fielder.to_csv(".\data\MLB-fielder\Baltimore_Orioles_fielder.csv")
df_Boston_Redsox_fielder.to_csv(".\data\MLB-fielder\Boston_Redsox_fielder.csv")
df_New_York_Yanks_fielder.to_csv(r".\data\MLB-fielder\New_York_Yanks_fielder.csv")
df_Tronto_Blue_Jays_fielder.to_csv(".\data\MLB-fielder\Tronto_Blue_Jays_fielder.csv")
df_Tampa_Bay_Rays_fielder.to_csv(".\data\MLB-fielder\Tampa_Bay_Rays_fielder.csv")
df_Chicago_White_Sox_fielder.to_csv(".\data\MLB-fielder\Chicago_White_Sox_fielder.csv")
df_Cleveland_Guardians_fielder.to_csv(".\data\MLB-fielder\Cleveland_Guardians_fielder.csv")
df_Detroit_Tigers_fielder.to_csv(".\data\MLB-fielder\Detroit_Tigers_fielder.csv")
df_Kansas_City_Royals_fielder.to_csv(".\data\MLB-fielder\Kansas_City_Royals_fielder.csv")
df_Minnesota_Twins_fielder.to_csv(".\data\MLB-fielder\Minnesota_Twins_fielder.csv")
df_Los_Angeles_Angeles_fielder.to_csv(".\data\MLB-fielder\Los_Angeles_Angeles_fielder.csv")
df_Oakland_Athletics_fielder.to_csv(".\data\MLB-fielder\Oakland_Athletics_fielder.csv")
df_Seattle_Mariners_fielder.to_csv(".\data\MLB-fielder\Seattle_Mariners_fielder.csv")
df_Texas_Rangers_fielder.to_csv(".\data\MLB-fielder\Texas_Rangers_fielder.csv")
df_Houston_Astros_fielder.to_csv(".\data\MLB-fielder\Houston_Astros_fielder.csv")
df_Atlanta_Braves_fielder.to_csv(".\data\MLB-fielder\Atlanta_Braves_fielder.csv")
df_Washington_Nationals_fielder.to_csv(".\data\MLB-fielder\Washington_Nationals_fielder.csv")
df_New_York_Mets_fielder.to_csv(r".\data\MLB-fielder\New_York_Mets_fielder.csv")
df_Philadelphia_Phillies_fielder.to_csv(".\data\MLB-fielder\Philadelphia_Phillies_fielder.csv")
df_Miami_Marlins_fielder.to_csv(".\data\MLB-fielder\Miami_Marlins_fielder.csv")
df_Milwaukee_Brewers_fielder.to_csv(".\data\MLB-fielder\Milwaukee_Brewers_fielder.csv")
df_Chicago_Cubs_fielder.to_csv(".\data\MLB-fielder\Chicago_Cubs_fielder.csv")
df_Cincinnati_Reds_fielder.to_csv(".\data\MLB-fielder\Cincinnati_Reds_fielder.csv")
df_Pittsburgh_Pirates_fielder.to_csv(".\data\MLB-fielder\Pittsburgh_Pirates_fielder.csv")
df_St_Louis_Cardinals_fielder.to_csv(".\data\MLB-fielder\St_Louis_Cardinals_fielder.csv")
df_Los_Angeles_Dodgers_fielder.to_csv(".\data\MLB-fielder\Los_Angeles_Dodgers_fielder.csv")
df_San_Diego_Padres_fielder.to_csv(".\data\MLB-fielder\San_Diego_Padres_fielder.csv")
df_San_Francisco_Giants_fielder.to_csv(".\data\MLB-fielder\San_Francisco_Giants_fielder.csv")
df_Colorado_Rockes_fielder.to_csv(".\data\MLB-fielder\Colorado_Rockes_fielder.csv")
df_Arizona_Diamondbacks_fielder.to_csv(".\data\MLB-fielder\Arizona_Diamondbacks_fielder.csv")



# 投手
df_Baltimore_Orioles_pitcher.to_csv(".\data\MLB-pitcher\Baltimore_Orioles_pitcher.csv")
df_Boston_Redsox_pitcher.to_csv(".\data\MLB-pitcher\Boston_Redsox_pitcher.csv")
df_New_York_Yanks_pitcher.to_csv(r".\data\MLB-pitcher\New_York_Yanks_pitcher.csv")
df_Tronto_Blue_Jays_pitcher.to_csv(".\data\MLB-pitcher\Tronto_Blue_Jays_pitcher.csv")
df_Tampa_Bay_Rays_pitcher.to_csv(".\data\MLB-pitcher\Tampa_Bay_Rays_pitcher.csv")
df_Chicago_White_Sox_pitcher.to_csv(".\data\MLB-pitcher\Chicago_White_Sox_pitcher.csv")
df_Cleveland_Guardians_pitcher.to_csv(".\data\MLB-pitcher\Cleveland_Guardians_pitcher.csv")
df_Detroit_Tigers_pitcher.to_csv(".\data\MLB-pitcher\Detroit_Tigers_pitcher.csv")
df_Kansas_City_Royals_pitcher.to_csv(".\data\MLB-pitcher\Kansas_City_Royals_pitcher.csv")
df_Minnesota_Twins_pitcher.to_csv(".\data\MLB-pitcher\Minnesota_Twins_pitcher.csv")
df_Los_Angeles_Angeles_pitcher.to_csv(".\data\MLB-pitcher\Los_Angeles_Angeles_pitcher.csv")
df_Oakland_Athletics_pitcher.to_csv(".\data\MLB-pitcher\Oakland_Athletics_pitcher.csv")
df_Seattle_Mariners_pitcher.to_csv(".\data\MLB-pitcher\Seattle_Mariners_pitcher.csv")
df_Texas_Rangers_pitcher.to_csv(".\data\MLB-pitcher\Texas_Rangers_pitcher.csv")
df_Houston_Astros_pitcher.to_csv(".\data\MLB-pitcher\Houston_Astros_pitcher.csv")
df_Atlanta_Braves_pitcher.to_csv(".\data\MLB-pitcher\Atlanta_Braves_pitcher.csv")
df_Washington_Nationals_pitcher.to_csv(".\data\MLB-pitcher\Washington_Nationals_pitcher.csv")
df_New_York_Mets_pitcher.to_csv(r".\data\MLB-pitcher\New_York_Mets_pitcher.csv")
df_Philadelphia_Phillies_pitcher.to_csv(".\data\MLB-pitcher\Philadelphia_Phillies_pitcher.csv")
df_Miami_Marlins_pitcher.to_csv(".\data\MLB-pitcher\Miami_Marlins_pitcher.csv")
df_Milwaukee_Brewers_pitcher.to_csv(".\data\MLB-pitcher\Milwaukee_Brewers_pitcher.csv")
df_Chicago_Cubs_pitcher.to_csv(".\data\MLB-pitcher\Chicago_Cubs_pitcher.csv")
df_Cincinnati_Reds_pitcher.to_csv(".\data\MLB-pitcher\Cincinnati_Reds_pitcher.csv")
df_Pittsburgh_Pirates_pitcher.to_csv(".\data\MLB-pitcher\Pittsburgh_Pirates_pitcher.csv")
df_St_Louis_Cardinals_pitcher.to_csv(".\data\MLB-pitcher\St_Louis_Cardinals_pitcher.csv")
df_Los_Angeles_Dodgers_pitcher.to_csv(".\data\MLB-pitcher\Los_Angeles_Dodgers_pitcher.csv")
df_San_Diego_Padres_pitcher.to_csv(".\data\MLB-pitcher\San_Diego_Padres_pitcher.csv")
df_San_Francisco_Giants_pitcher.to_csv(".\data\MLB-pitcher\San_Francisco_Giants_pitcher.csv")
df_Colorado_Rockes_pitcher.to_csv(".\data\MLB-pitcher\Colorado_Rockes_pitcher.csv")
df_Arizona_Diamondbacks_pitcher.to_csv(".\data\MLB-pitcher\Arizona_Diamondbacks_pitcher.csv")



# 全チームの野手をcsvファイルに保存
# MLB_all_fielder.csvに最初のデータを書き出す
df_Baltimore_Orioles_fielder.to_csv(".\data\MLB-all-fielder\MLB_all_fielder.csv")

# MLB_all_fielder.csvの後ろからどんどんデータを追加していく
df_Boston_Redsox_fielder.to_csv(".\data\MLB-all-fielder\MLB_all_fielder.csv", mode='a', header=False)
df_New_York_Yanks_fielder.to_csv(".\data\MLB-all-fielder\MLB_all_fielder.csv", mode='a', header=False)
df_Tronto_Blue_Jays_fielder.to_csv(".\data\MLB-all-fielder\MLB_all_fielder.csv", mode='a', header=False)
df_Tampa_Bay_Rays_fielder.to_csv(".\data\MLB-all-fielder\MLB_all_fielder.csv", mode='a', header=False)
df_Chicago_White_Sox_fielder.to_csv(".\data\MLB-all-fielder\MLB_all_fielder.csv", mode='a', header=False)
df_Cleveland_Guardians_fielder.to_csv(".\data\MLB-all-fielder\MLB_all_fielder.csv", mode='a', header=False)
df_Detroit_Tigers_fielder.to_csv(".\data\MLB-all-fielder\MLB_all_fielder.csv", mode='a', header=False)
df_Kansas_City_Royals_fielder.to_csv(".\data\MLB-all-fielder\MLB_all_fielder.csv", mode='a', header=False)
df_Minnesota_Twins_fielder.to_csv(".\data\MLB-all-fielder\MLB_all_fielder.csv", mode='a', header=False)
df_Los_Angeles_Angeles_fielder.to_csv(".\data\MLB-all-fielder\MLB_all_fielder.csv", mode='a', header=False)
df_Oakland_Athletics_fielder.to_csv(".\data\MLB-all-fielder\MLB_all_fielder.csv", mode='a', header=False)
df_Seattle_Mariners_fielder.to_csv(".\data\MLB-all-fielder\MLB_all_fielder.csv", mode='a', header=False)
df_Texas_Rangers_fielder.to_csv(".\data\MLB-all-fielder\MLB_all_fielder.csv", mode='a', header=False)
df_Houston_Astros_fielder.to_csv(".\data\MLB-all-fielder\MLB_all_fielder.csv", mode='a', header=False)
df_Atlanta_Braves_fielder.to_csv(".\data\MLB-all-fielder\MLB_all_fielder.csv", mode='a', header=False)
df_Washington_Nationals_fielder.to_csv(".\data\MLB-all-fielder\MLB_all_fielder.csv", mode='a', header=False)
df_New_York_Mets_fielder.to_csv(".\data\MLB-all-fielder\MLB_all_fielder.csv", mode='a', header=False)
df_Philadelphia_Phillies_fielder.to_csv(".\data\MLB-all-fielder\MLB_all_fielder.csv", mode='a', header=False)
df_Miami_Marlins_fielder.to_csv(".\data\MLB-all-fielder\MLB_all_fielder.csv", mode='a', header=False)
df_Milwaukee_Brewers_fielder.to_csv(".\data\MLB-all-fielder\MLB_all_fielder.csv", mode='a', header=False)
df_Chicago_Cubs_fielder.to_csv(".\data\MLB-all-fielder\MLB_all_fielder.csv", mode='a', header=False)
df_Cincinnati_Reds_fielder.to_csv(".\data\MLB-all-fielder\MLB_all_fielder.csv", mode='a', header=False)
df_Pittsburgh_Pirates_fielder.to_csv(".\data\MLB-all-fielder\MLB_all_fielder.csv", mode='a', header=False)
df_St_Louis_Cardinals_fielder.to_csv(".\data\MLB-all-fielder\MLB_all_fielder.csv", mode='a', header=False)
df_Los_Angeles_Dodgers_fielder.to_csv(".\data\MLB-all-fielder\MLB_all_fielder.csv", mode='a', header=False)
df_San_Diego_Padres_fielder.to_csv(".\data\MLB-all-fielder\MLB_all_fielder.csv", mode='a', header=False)
df_San_Francisco_Giants_fielder.to_csv(".\data\MLB-all-fielder\MLB_all_fielder.csv", mode='a', header=False)
df_Colorado_Rockes_fielder.to_csv(".\data\MLB-all-fielder\MLB_all_fielder.csv", mode='a', header=False)
df_Arizona_Diamondbacks_fielder.to_csv(".\data\MLB-all-fielder\MLB_all_fielder.csv", mode='a', header=False)


# 全チームの投手をcsvファイルに保存
df_Baltimore_Orioles_pitcher.to_csv(".\data\MLB-all-pitcher\MLB_all_pitcher.csv")
df_Boston_Redsox_pitcher.to_csv(".\data\MLB-all-pitcher\MLB_all_pitcher.csv", mode='a', header=False)
df_New_York_Yanks_pitcher.to_csv(".\data\MLB-all-pitcher\MLB_all_pitcher.csv", mode='a', header=False)
df_Tronto_Blue_Jays_pitcher.to_csv(".\data\MLB-all-pitcher\MLB_all_pitcher.csv", mode='a', header=False)
df_Tampa_Bay_Rays_pitcher.to_csv(".\data\MLB-all-pitcher\MLB_all_pitcher.csv", mode='a', header=False)
df_Chicago_White_Sox_pitcher.to_csv(".\data\MLB-all-pitcher\MLB_all_pitcher.csv", mode='a', header=False)
df_Cleveland_Guardians_pitcher.to_csv(".\data\MLB-all-pitcher\MLB_all_pitcher.csv", mode='a', header=False)
df_Detroit_Tigers_pitcher.to_csv(".\data\MLB-all-pitcher\MLB_all_pitcher.csv", mode='a', header=False)
df_Kansas_City_Royals_pitcher.to_csv(".\data\MLB-all-pitcher\MLB_all_pitcher.csv", mode='a', header=False)
df_Minnesota_Twins_pitcher.to_csv(".\data\MLB-all-pitcher\MLB_all_pitcher.csv", mode='a', header=False)
df_Los_Angeles_Angeles_pitcher.to_csv(".\data\MLB-all-pitcher\MLB_all_pitcher.csv", mode='a', header=False)
df_Oakland_Athletics_pitcher.to_csv(".\data\MLB-all-pitcher\MLB_all_pitcher.csv", mode='a', header=False)
df_Seattle_Mariners_pitcher.to_csv(".\data\MLB-all-pitcher\MLB_all_pitcher.csv", mode='a', header=False)
df_Texas_Rangers_pitcher.to_csv(".\data\MLB-all-pitcher\MLB_all_pitcher.csv", mode='a', header=False)
df_Houston_Astros_pitcher.to_csv(".\data\MLB-all-pitcher\MLB_all_pitcher.csv", mode='a', header=False)
df_Atlanta_Braves_pitcher.to_csv(".\data\MLB-all-pitcher\MLB_all_pitcher.csv", mode='a', header=False)
df_Washington_Nationals_pitcher.to_csv(".\data\MLB-all-pitcher\MLB_all_pitcher.csv", mode='a', header=False)
df_New_York_Mets_pitcher.to_csv(".\data\MLB-all-pitcher\MLB_all_pitcher.csv", mode='a', header=False)
df_Philadelphia_Phillies_pitcher.to_csv(".\data\MLB-all-pitcher\MLB_all_pitcher.csv", mode='a', header=False)
df_Miami_Marlins_pitcher.to_csv(".\data\MLB-all-pitcher\MLB_all_pitcher.csv", mode='a', header=False)
df_Milwaukee_Brewers_pitcher.to_csv(".\data\MLB-all-pitcher\MLB_all_pitcher.csv", mode='a', header=False)
df_Chicago_Cubs_pitcher.to_csv(".\data\MLB-all-pitcher\MLB_all_pitcher.csv", mode='a', header=False)
df_Cincinnati_Reds_pitcher.to_csv(".\data\MLB-all-pitcher\MLB_all_pitcher.csv", mode='a', header=False)
df_Pittsburgh_Pirates_pitcher.to_csv(".\data\MLB-all-pitcher\MLB_all_pitcher.csv", mode='a', header=False)
df_St_Louis_Cardinals_pitcher.to_csv(".\data\MLB-all-pitcher\MLB_all_pitcher.csv", mode='a', header=False)
df_Los_Angeles_Dodgers_pitcher.to_csv(".\data\MLB-all-pitcher\MLB_all_pitcher.csv", mode='a', header=False)
df_San_Diego_Padres_pitcher.to_csv(".\data\MLB-all-pitcher\MLB_all_pitcher.csv", mode='a', header=False)
df_San_Francisco_Giants_pitcher.to_csv(".\data\MLB-all-pitcher\MLB_all_pitcher.csv", mode='a', header=False)
df_Colorado_Rockes_pitcher.to_csv(".\data\MLB-all-pitcher\MLB_all_pitcher.csv", mode='a', header=False)
df_Arizona_Diamondbacks_pitcher.to_csv(".\data\MLB-all-pitcher\MLB_all_pitcher.csv", mode='a', header=False)


# ALの全野手の成績
# 最初のデータ書き出し
df_Baltimore_Orioles_fielder.to_csv(".\data\AL&NL-fielder\AL_all_fielder.csv")
# 
df_Boston_Redsox_fielder.to_csv(".\data\AL&NL-fielder\AL_all_fielder.csv", mode='a', header=False)
df_New_York_Yanks_fielder.to_csv(".\data\AL&NL-fielder\AL_all_fielder.csv", mode='a', header=False)
df_Tronto_Blue_Jays_fielder.to_csv(".\data\AL&NL-fielder\AL_all_fielder.csv", mode='a', header=False)
df_Tampa_Bay_Rays_fielder.to_csv(".\data\AL&NL-fielder\AL_all_fielder.csv", mode='a', header=False)
df_Chicago_White_Sox_fielder.to_csv(".\data\AL&NL-fielder\AL_all_fielder.csv", mode='a', header=False)
df_Cleveland_Guardians_fielder.to_csv(".\data\AL&NL-fielder\AL_all_fielder.csv", mode='a', header=False)
df_Detroit_Tigers_fielder.to_csv(".\data\AL&NL-fielder\AL_all_fielder.csv", mode='a', header=False)
df_Kansas_City_Royals_fielder.to_csv(".\data\AL&NL-fielder\AL_all_fielder.csv", mode='a', header=False)
df_Minnesota_Twins_fielder.to_csv(".\data\AL&NL-fielder\AL_all_fielder.csv", mode='a', header=False)
df_Los_Angeles_Angeles_fielder.to_csv(".\data\AL&NL-fielder\AL_all_fielder.csv", mode='a', header=False)
df_Oakland_Athletics_fielder.to_csv(".\data\AL&NL-fielder\AL_all_fielder.csv", mode='a', header=False)
df_Seattle_Mariners_fielder.to_csv(".\data\AL&NL-fielder\AL_all_fielder.csv", mode='a', header=False)
df_Texas_Rangers_fielder.to_csv(".\data\AL&NL-fielder\AL_all_fielder.csv", mode='a', header=False)
df_Houston_Astros_fielder.to_csv(".\data\AL&NL-fielder\AL_all_fielder.csv", mode='a', header=False)

# NLの全野手の成績
# 最初のデータ書き出し
df_Atlanta_Braves_fielder.to_csv(r".\data\AL&NL-fielder\NL_all_fielder.csv")
# 
df_Washington_Nationals_fielder.to_csv(r".\data\AL&NL-fielder\NL_all_fielder.csv", mode='a', header=False)
df_New_York_Mets_fielder.to_csv(r".\data\AL&NL-fielder\NL_all_fielder.csv", mode='a', header=False)
df_Philadelphia_Phillies_fielder.to_csv(r".\data\AL&NL-fielder\NL_all_fielder.csv", mode='a', header=False)
df_Miami_Marlins_fielder.to_csv(r".\data\AL&NL-fielder\NL_all_fielder.csv", mode='a', header=False)
df_Milwaukee_Brewers_fielder.to_csv(r".\data\AL&NL-fielder\NL_all_fielder.csv", mode='a', header=False)
df_Chicago_Cubs_fielder.to_csv(r".\data\AL&NL-fielder\NL_all_fielder.csv", mode='a', header=False)
df_Cincinnati_Reds_fielder.to_csv(r".\data\AL&NL-fielder\NL_all_fielder.csv", mode='a', header=False)
df_Pittsburgh_Pirates_fielder.to_csv(r".\data\AL&NL-fielder\NL_all_fielder.csv", mode='a', header=False)
df_St_Louis_Cardinals_fielder.to_csv(r".\data\AL&NL-fielder\NL_all_fielder.csv", mode='a', header=False)
df_Los_Angeles_Dodgers_fielder.to_csv(r".\data\AL&NL-fielder\NL_all_fielder.csv", mode='a', header=False)
df_San_Diego_Padres_fielder.to_csv(r".\data\AL&NL-fielder\NL_all_fielder.csv", mode='a', header=False)
df_San_Francisco_Giants_fielder.to_csv(r".\data\AL&NL-fielder\NL_all_fielder.csv", mode='a', header=False)
df_Colorado_Rockes_fielder.to_csv(r".\data\AL&NL-fielder\NL_all_fielder.csv", mode='a', header=False)
df_Arizona_Diamondbacks_fielder.to_csv(r".\data\AL&NL-fielder\NL_all_fielder.csv", mode='a', header=False)


# ALの全投手の成績
# 最初のデータ書き出し
df_Baltimore_Orioles_pitcher.to_csv(".\data\AL&NL-pitcher\AL_all_pitcher.csv")
# 
df_Boston_Redsox_pitcher.to_csv(".\data\AL&NL-pitcher\AL_all_pitcher.csv", mode='a', header=False)
df_New_York_Yanks_pitcher.to_csv(".\data\AL&NL-pitcher\AL_all_pitcher.csv", mode='a', header=False)
df_Tronto_Blue_Jays_pitcher.to_csv(".\data\AL&NL-pitcher\AL_all_pitcher.csv", mode='a', header=False)
df_Tampa_Bay_Rays_pitcher.to_csv(".\data\AL&NL-pitcher\AL_all_pitcher.csv", mode='a', header=False)
df_Chicago_White_Sox_pitcher.to_csv(".\data\AL&NL-pitcher\AL_all_pitcher.csv", mode='a', header=False)
df_Cleveland_Guardians_pitcher.to_csv(".\data\AL&NL-pitcher\AL_all_pitcher.csv", mode='a', header=False)
df_Detroit_Tigers_pitcher.to_csv(".\data\AL&NL-pitcher\AL_all_pitcher.csv", mode='a', header=False)
df_Kansas_City_Royals_pitcher.to_csv(".\data\AL&NL-pitcher\AL_all_pitcher.csv", mode='a', header=False)
df_Minnesota_Twins_pitcher.to_csv(".\data\AL&NL-pitcher\AL_all_pitcher.csv", mode='a', header=False)
df_Los_Angeles_Angeles_pitcher.to_csv(".\data\AL&NL-pitcher\AL_all_pitcher.csv", mode='a', header=False)
df_Oakland_Athletics_pitcher.to_csv(".\data\AL&NL-pitcher\AL_all_pitcher.csv", mode='a', header=False)
df_Seattle_Mariners_pitcher.to_csv(".\data\AL&NL-pitcher\AL_all_pitcher.csv", mode='a', header=False)
df_Texas_Rangers_pitcher.to_csv(".\data\AL&NL-pitcher\AL_all_pitcher.csv", mode='a', header=False)
df_Houston_Astros_pitcher.to_csv(".\data\AL&NL-pitcher\AL_all_pitcher.csv", mode='a', header=False)


# NLの全投手の成績
# 最初のデータ書き出し
df_Atlanta_Braves_pitcher.to_csv(r".\data\AL&NL-pitcher\NL_all_pitcher.csv")
# 
df_Washington_Nationals_pitcher.to_csv(r".\data\AL&NL-pitcher\NL_all_pitcher.csv", mode='a', header=False)
df_New_York_Mets_pitcher.to_csv(r".\data\AL&NL-pitcher\NL_all_pitcher.csv", mode='a', header=False)
df_Philadelphia_Phillies_pitcher.to_csv(r".\data\AL&NL-pitcher\NL_all_pitcher.csv", mode='a', header=False)
df_Miami_Marlins_pitcher.to_csv(r".\data\AL&NL-pitcher\NL_all_pitcher.csv", mode='a', header=False)
df_Milwaukee_Brewers_pitcher.to_csv(r".\data\AL&NL-pitcher\NL_all_pitcher.csv", mode='a', header=False)
df_Chicago_Cubs_pitcher.to_csv(r".\data\AL&NL-pitcher\NL_all_pitcher.csv", mode='a', header=False)
df_Cincinnati_Reds_pitcher.to_csv(r".\data\AL&NL-pitcher\NL_all_pitcher.csv", mode='a', header=False)
df_Pittsburgh_Pirates_pitcher.to_csv(r".\data\AL&NL-pitcher\NL_all_pitcher.csv", mode='a', header=False)
df_St_Louis_Cardinals_pitcher.to_csv(r".\data\AL&NL-pitcher\NL_all_pitcher.csv", mode='a', header=False)
df_Los_Angeles_Dodgers_pitcher.to_csv(r".\data\AL&NL-pitcher\NL_all_pitcher.csv", mode='a', header=False)
df_San_Diego_Padres_pitcher.to_csv(r".\data\AL&NL-pitcher\NL_all_pitcher.csv", mode='a', header=False)
df_San_Francisco_Giants_pitcher.to_csv(r".\data\AL&NL-pitcher\NL_all_pitcher.csv", mode='a', header=False)
df_Colorado_Rockes_pitcher.to_csv(r".\data\AL&NL-pitcher\NL_all_pitcher.csv", mode='a', header=False)
df_Arizona_Diamondbacks_pitcher.to_csv(r".\data\AL&NL-pitcher\NL_all_pitcher.csv", mode='a', header=False)


# MLBチームのデータをcsvに保存
AL_team_list_df.to_csv(".\data\MLB-team\MLB_team.csv")