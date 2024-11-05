# import urllib.request
# from bs4 import BeautifulSoup
# import pandas as pd
# import numpy as np

# # 対象のサイトURL
# url = "https://baseball.yahoo.co.jp/mlb/player/2100396/top"

# # URLリソースを開く
# res = urllib.request.urlopen(url)

# # インスタンスの作成
# soup = BeautifulSoup(res, 'html.parser')

# # 必要な要素とclass名
# # 選手の個人成績
# player_data = soup.find_all("td", class_="bb-playerStatsTable__data")

# # 取得した選手の個人成績を出力
# player_data_list = []
# for player_data_text in player_data:
#   player_data_list.append(player_data_text.text)

# # list内の改行と空白を削除
# for i in range(len(player_data_list)):
#   player_data_list[i] = player_data_list[i].replace('\n','')
#   player_data_list[i] = player_data_list[i].replace(' ','')

# # 2014年までのデータがあるインデックス番号
# for i in range(len(player_data_list)):
#   if player_data_list[i] == "2014":
#     index = i
#     break
#   elif player_data_list[i] == "2015":
#     index = i
#     break
#   elif player_data_list[i] == "2016":
#     index = i
#     break
#   elif player_data_list[i] == "2017":
#     index = i
#     break
#   elif player_data_list[i] == "2018":
#     index = i
#     break
#   elif player_data_list[i] == "2019":
#     index = i
#     break
#   elif player_data_list[i] == "2020":
#     index = i
#     break
#   elif player_data_list[i] == "2021":
#     index = i
#     break
#   elif player_data_list[i] == "2022":
#     index = i

# # print(player_data_list[index])

# del player_data_list[0:index]

# for i in range(len(player_data_list)):
#   if player_data_list[i] == "2023":
#     index = i

# del player_data_list[index:]

# # print(player_data_list)

# # numpyに変換
# player_data_list_np = np.array(player_data_list)

# label = len(player_data_list)/26

# # データフレームに適した形にreshape
# player_data_list_np = player_data_list_np.reshape([int(label),26])
# # print(player_data_list_np)

# # # データフレームに変換
# until_last_year_df = pd.DataFrame(player_data_list_np)

# # until_last_year_df

# # カラム名の取得
# player_data_columns = soup.find_all("th", class_="bb-playerStatsTable__head")

# # 取得したカラム名を出力
# player_data_columns_list = []
# for player_data_columns_text in player_data_columns:
#   player_data_columns_list.append(player_data_columns_text.text)

# for i in range(len(player_data_columns_list)):
#   if player_data_columns_list[i] == "年度":
#     index = i

# del player_data_columns_list[0:index]

# for i in range(len(player_data_columns_list)):
#   if player_data_columns_list[i] == "通算成績":
#     index = i

# del player_data_columns_list[index:]

# # print(player_data_columns_list)


# # カラムにplayer_data_columns_listを指定している
# until_last_year_df = until_last_year_df.set_axis(player_data_columns_list, axis=1)

# # until_last_year_df


# # 選手の名前を取ってくる
# # 対象のサイトURL
# url = "https://baseball.yahoo.co.jp/mlb/teams/2021001/memberlist?kind=b"

# # URLリソースを開く
# res = urllib.request.urlopen(url)

# # インスタンスの作成
# soup = BeautifulSoup(res, 'html.parser')

# # 必要な要素とclass名
# # 選手の個人成績
# player_name = soup.find_all("td", class_="bb-playerTable__data--player")

# player_name_list = []
# for player_data_text in player_name:
#   player_name_list.append(player_data_text.text)

# # list内の改行と空白を削除
# for i in range(len(player_name_list)):
#   player_name_list[i] = player_name_list[i].replace('\n','')
#   player_name_list[i] = player_name_list[i].replace(' ','')

# # print(player_name_list)

# # 対象のサイトURL
# url = "https://baseball.yahoo.co.jp/mlb/player/2100396/top"

# # URLリソースを開く
# res = urllib.request.urlopen(url)

# # インスタンスの作成
# soup = BeautifulSoup(res, 'html.parser')

# # 必要な要素とclass名
# # 選手の個人成績
# player_data = soup.find_all("h1")

# # 取得した選手の個人成績を出力
# data_list = []
# for player_data_text in player_data:
#   data_list.append(player_data_text.text)

# # list内の改行と空白を削除
# for i in range(len(data_list)):
#   data_list[i] = data_list[i].replace('\n','')
#   data_list[i] = data_list[i].replace(' ','')

# # print(data_list)

# # player_name_listとdata_listを比較して==になるものが選手名
# for i in range(len(player_name_list)):
#   for j in range(len(data_list)):
#     if player_name_list[i] == data_list[j]:
#       name = player_name_list[i]

# until_last_year_df.insert(loc = 1, column= '選手名', value= name)

# until_last_year_df.to_csv("./MLB-past-data/MLB_fielder_past_data.csv")



# # 関数化(二つ目のデータ以降使用)
# def past_data(url_data,url_name,url_name_data):
# # 対象のサイトURL
#   url = url_data

#   # URLリソースを開く
#   res = urllib.request.urlopen(url)

#   # インスタンスの作成
#   soup = BeautifulSoup(res, 'html.parser')

#   # 必要な要素とclass名
#   # 選手の個人成績
#   player_data = soup.find_all("td", class_="bb-playerStatsTable__data")

#   # 取得した選手の個人成績を出力
#   player_data_list = []
#   for player_data_text in player_data:
#     player_data_list.append(player_data_text.text)

#   # list内の改行と空白を削除
#   for i in range(len(player_data_list)):
#     player_data_list[i] = player_data_list[i].replace('\n','')
#     player_data_list[i] = player_data_list[i].replace(' ','')

#   # 2014年までのデータがあるインデックス番号
#   for i in range(len(player_data_list)):
#     if player_data_list[i] == "2009":
#         index = i
#         break
#     elif player_data_list[i] == "2010":
#         index = i
#         break
#     elif player_data_list[i] == "2011":
#         index = i
#         break
#     elif player_data_list[i] == "2012":
#         index = i
#         break
#     elif player_data_list[i] == "2013":
#         index = i
#         break
#     elif player_data_list[i] == "2014":
#         index = i
#         break
#     elif player_data_list[i] == "2015":
#         index = i
#         break
#     elif player_data_list[i] == "2016":
#         index = i
#         break
#     elif player_data_list[i] == "2017":
#         index = i
#         break
#     elif player_data_list[i] == "2018":
#         index = i
#         break
#     elif player_data_list[i] == "2019":
#         index = i
#         break
#     elif player_data_list[i] == "2020":
#         index = i
#         break
#     elif player_data_list[i] == "2021":
#         index = i
#         break
#     elif player_data_list[i] == "2022":
#         index = i

#   # print(player_data_list[index])

#   del player_data_list[0:index]


#   # 投手の経験があった場合その場所を削除
#   for i in range(9):
#     num = len(player_data_list)/26
#     if num %1 != 0.0:
#       del player_data_list[0:30]
#     else:
#       break


#   # numpyに変換
#   player_data_list_np = np.array(player_data_list)

#   label = len(player_data_list)/26

#   # データフレームに適した形にreshape
#   player_data_list_np = player_data_list_np.reshape([int(label),26])
#   # print(player_data_list_np)

#   # # データフレームに変換
#   until_last_year_df = pd.DataFrame(player_data_list_np)

#   # until_last_year_df

#   # カラム名の取得
#   player_data_columns = soup.find_all("th", class_="bb-playerStatsTable__head")

#   # 取得したカラム名を出力
#   player_data_columns_list = []
#   for player_data_columns_text in player_data_columns:
#     player_data_columns_list.append(player_data_columns_text.text)

#   for i in range(len(player_data_columns_list)):
#     if player_data_columns_list[i] == "年度":
#       index = i

#   del player_data_columns_list[0:index]

#   for i in range(len(player_data_columns_list)):
#     if player_data_columns_list[i] == "通算成績":
#       index = i

#   del player_data_columns_list[index:]

#   # print(player_data_columns_list)


#   # カラムにplayer_data_columns_listを指定している
#   until_last_year_df = until_last_year_df.set_axis(player_data_columns_list, axis=1)

#   # until_last_year_df


#   # 選手の名前を取ってくる
#   # 対象のサイトURL
#   url = url_name

#   # URLリソースを開く
#   res = urllib.request.urlopen(url)

#   # インスタンスの作成
#   soup = BeautifulSoup(res, 'html.parser')

#   # 必要な要素とclass名
#   player_name = soup.find_all("td", class_="bb-playerTable__data--player")

#   player_name_list = []
#   for player_data_text in player_name:
#     player_name_list.append(player_data_text.text)

#   # list内の改行と空白を削除
#   for i in range(len(player_name_list)):
#     player_name_list[i] = player_name_list[i].replace('\n','')
#     player_name_list[i] = player_name_list[i].replace(' ','')

#   # print(player_name_list)

#   # 対象のサイトURL
#   url = url_name_data

#   # URLリソースを開く
#   res = urllib.request.urlopen(url)

#   # インスタンスの作成
#   soup = BeautifulSoup(res, 'html.parser')

#   # 必要な要素とclass名
#   player_data = soup.find_all("h1")

#   data_list = []
#   for player_data_text in player_data:
#     data_list.append(player_data_text.text)

#   # list内の改行と空白を削除
#   for i in range(len(data_list)):
#     data_list[i] = data_list[i].replace('\n','')
#     data_list[i] = data_list[i].replace(' ','')

#   # print(data_list)

#   # player_name_listとdata_listを比較して==になるものが選手名
#   for i in range(len(player_name_list)):
#     for j in range(len(data_list)):
#       if player_name_list[i] == data_list[j]:
#         name = player_name_list[i]
  
#   # カラムを追加    
#   until_last_year_df.insert(loc = 1, column= '選手名', value= name)

#   # csvに追加
#   until_last_year_df.to_csv("./MLB-past-data/MLB_fielder_past_data.csv", mode='a', header=False)



# url = ["https://baseball.yahoo.co.jp/mlb/teams/2021001/memberlist?kind=b","https://baseball.yahoo.co.jp/mlb/teams/2021002/memberlist?kind=b","https://baseball.yahoo.co.jp/mlb/teams/2021010/memberlist?kind=b","https://baseball.yahoo.co.jp/mlb/teams/2021014/memberlist?kind=b","https://baseball.yahoo.co.jp/mlb/teams/2021030/memberlist?kind=b","https://baseball.yahoo.co.jp/mlb/teams/2021004/memberlist?kind=b","https://baseball.yahoo.co.jp/mlb/teams/2021005/memberlist?kind=b","https://baseball.yahoo.co.jp/mlb/teams/2021006/memberlist?kind=b","https://baseball.yahoo.co.jp/mlb/teams/2021007/memberlist?kind=b","https://baseball.yahoo.co.jp/mlb/teams/2021009/memberlist?kind=b","https://baseball.yahoo.co.jp/mlb/teams/2021003/memberlist?kind=b","https://baseball.yahoo.co.jp/mlb/teams/2021011/memberlist?kind=b","https://baseball.yahoo.co.jp/mlb/teams/2021012/memberlist?kind=b","https://baseball.yahoo.co.jp/mlb/teams/2021013/memberlist?kind=b","https://baseball.yahoo.co.jp/mlb/teams/2021018/memberlist?kind=b","https://baseball.yahoo.co.jp/mlb/teams/2021015/memberlist?kind=b","https://baseball.yahoo.co.jp/mlb/teams/2021020/memberlist?kind=b","https://baseball.yahoo.co.jp/mlb/teams/2021021/memberlist?kind=b","https://baseball.yahoo.co.jp/mlb/teams/2021022/memberlist?kind=b","https://baseball.yahoo.co.jp/mlb/teams/2021028/memberlist?kind=b","https://baseball.yahoo.co.jp/mlb/teams/2021008/memberlist?kind=b","https://baseball.yahoo.co.jp/mlb/teams/2021016/memberlist?kind=b","https://baseball.yahoo.co.jp/mlb/teams/2021017/memberlist?kind=b","https://baseball.yahoo.co.jp/mlb/teams/2021023/memberlist?kind=b","https://baseball.yahoo.co.jp/mlb/teams/2021024/memberlist?kind=b","https://baseball.yahoo.co.jp/mlb/teams/2021019/memberlist?kind=b","https://baseball.yahoo.co.jp/mlb/teams/2021025/memberlist?kind=b","https://baseball.yahoo.co.jp/mlb/teams/2021026/memberlist?kind=b","https://baseball.yahoo.co.jp/mlb/teams/2021027/memberlist?kind=b","https://baseball.yahoo.co.jp/mlb/teams/2021029/memberlist?kind=b"]


# # MLB_past_data.csvの下にデータを追加していく
# past_data("https://baseball.yahoo.co.jp/mlb/player/2102053/top",url[0],"https://baseball.yahoo.co.jp/mlb/player/2102053/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101721/top",url[0],"https://baseball.yahoo.co.jp/mlb/player/2101721/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100476/top",url[0],"https://baseball.yahoo.co.jp/mlb/player/2100476/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100780/top",url[0],"https://baseball.yahoo.co.jp/mlb/player/2100780/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100017/top",url[0],"https://baseball.yahoo.co.jp/mlb/player/2100017/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100735/top",url[0],"https://baseball.yahoo.co.jp/mlb/player/2100735/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100781/top",url[0],"https://baseball.yahoo.co.jp/mlb/player/2100781/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2102462/top",url[0],"https://baseball.yahoo.co.jp/mlb/player/2102462/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100084/top",url[0],"https://baseball.yahoo.co.jp/mlb/player/2100084/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2102225/top",url[0],"https://baseball.yahoo.co.jp/mlb/player/2102225/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100070/top",url[0],"https://baseball.yahoo.co.jp/mlb/player/2100070/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100992/top",url[0],"https://baseball.yahoo.co.jp/mlb/player/2100992/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2102790/top",url[0],"https://baseball.yahoo.co.jp/mlb/player/2102790/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100165/top",url[0],"https://baseball.yahoo.co.jp/mlb/player/2100165/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100007/top",url[0],"https://baseball.yahoo.co.jp/mlb/player/2100007/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100741/top",url[1],"https://baseball.yahoo.co.jp/mlb/player/2100741/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100473/top",url[1],"https://baseball.yahoo.co.jp/mlb/player/2100473/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101002/top",url[1],"https://baseball.yahoo.co.jp/mlb/player/2101002/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101004/top",url[1],"https://baseball.yahoo.co.jp/mlb/player/2101004/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100883/top",url[1],"https://baseball.yahoo.co.jp/mlb/player/2100883/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100728/top",url[1],"https://baseball.yahoo.co.jp/mlb/player/2100728/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101664/top",url[1],"https://baseball.yahoo.co.jp/mlb/player/2101664/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100953/top",url[1],"https://baseball.yahoo.co.jp/mlb/player/2100953/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100104/top",url[1],"https://baseball.yahoo.co.jp/mlb/player/2100104/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2102131/top",url[1],"https://baseball.yahoo.co.jp/mlb/player/2102131/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100184/top",url[1],"https://baseball.yahoo.co.jp/mlb/player/2100184/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100013/top",url[1],"https://baseball.yahoo.co.jp/mlb/player/2100013/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/202100515/top",url[1],"https://baseball.yahoo.co.jp/mlb/player/202100515/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101808/top",url[1],"https://baseball.yahoo.co.jp/mlb/player/2101808/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101229/top",url[1],"https://baseball.yahoo.co.jp/mlb/player/2101229/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101809/top",url[1],"https://baseball.yahoo.co.jp/mlb/player/2101809/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100040/top",url[1],"https://baseball.yahoo.co.jp/mlb/player/2100040/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101162/top",url[1],"https://baseball.yahoo.co.jp/mlb/player/2101162/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101062/top",url[2],"https://baseball.yahoo.co.jp/mlb/player/2101062/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100482/top",url[2],"https://baseball.yahoo.co.jp/mlb/player/2100482/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100559/top",url[2],"https://baseball.yahoo.co.jp/mlb/player/2100559/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100336/top",url[2],"https://baseball.yahoo.co.jp/mlb/player/2100336/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101018/top",url[2],"https://baseball.yahoo.co.jp/mlb/player/2101018/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100485/top",url[2],"https://baseball.yahoo.co.jp/mlb/player/2100485/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100069/top",url[2],"https://baseball.yahoo.co.jp/mlb/player/2100069/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101032/top",url[2],"https://baseball.yahoo.co.jp/mlb/player/2101032/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101019/top",url[2],"https://baseball.yahoo.co.jp/mlb/player/2101019/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100364/top",url[2],"https://baseball.yahoo.co.jp/mlb/player/2100364/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100348/top",url[2],"https://baseball.yahoo.co.jp/mlb/player/2100348/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101863/top",url[2],"https://baseball.yahoo.co.jp/mlb/player/2101863/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100314/top",url[2],"https://baseball.yahoo.co.jp/mlb/player/2100314/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100099/top",url[2],"https://baseball.yahoo.co.jp/mlb/player/2100099/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2102575/top",url[2],"https://baseball.yahoo.co.jp/mlb/player/2102575/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100008/top",url[2],"https://baseball.yahoo.co.jp/mlb/player/2100008/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100932/top",url[2],"https://baseball.yahoo.co.jp/mlb/player/2100932/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100333/top",url[2],"https://baseball.yahoo.co.jp/mlb/player/2100333/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100235/top",url[3],"https://baseball.yahoo.co.jp/mlb/player/2100235/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100032/top",url[3],"https://baseball.yahoo.co.jp/mlb/player/2100032/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2102186/top",url[3],"https://baseball.yahoo.co.jp/mlb/player/2102186/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100968/top",url[3],"https://baseball.yahoo.co.jp/mlb/player/2100968/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100799/top",url[3],"https://baseball.yahoo.co.jp/mlb/player/2100799/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100164/top",url[3],"https://baseball.yahoo.co.jp/mlb/player/2100164/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100103/top",url[3],"https://baseball.yahoo.co.jp/mlb/player/2100103/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100924/top",url[3],"https://baseball.yahoo.co.jp/mlb/player/2100924/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100621/top",url[3],"https://baseball.yahoo.co.jp/mlb/player/2100621/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100917/top",url[3],"https://baseball.yahoo.co.jp/mlb/player/2100917/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101034/top",url[3],"https://baseball.yahoo.co.jp/mlb/player/2101034/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100971/top",url[3],"https://baseball.yahoo.co.jp/mlb/player/2100971/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100242/top",url[3],"https://baseball.yahoo.co.jp/mlb/player/2100242/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100539/top",url[3],"https://baseball.yahoo.co.jp/mlb/player/2100539/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100114/top",url[3],"https://baseball.yahoo.co.jp/mlb/player/2100114/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101856/top",url[4],"https://baseball.yahoo.co.jp/mlb/player/2101856/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100316/top",url[4],"https://baseball.yahoo.co.jp/mlb/player/2100316/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101632/top",url[4],"https://baseball.yahoo.co.jp/mlb/player/2101632/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100940/top",url[4],"https://baseball.yahoo.co.jp/mlb/player/2100940/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101634/top",url[4],"https://baseball.yahoo.co.jp/mlb/player/2101634/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100852/top",url[4],"https://baseball.yahoo.co.jp/mlb/player/2100852/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100977/top",url[4],"https://baseball.yahoo.co.jp/mlb/player/2100977/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100118/top",url[4],"https://baseball.yahoo.co.jp/mlb/player/2100118/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100362/top",url[4],"https://baseball.yahoo.co.jp/mlb/player/2100362/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/202100173/top",url[4],"https://baseball.yahoo.co.jp/mlb/player/202100173/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100609/top",url[4],"https://baseball.yahoo.co.jp/mlb/player/2100609/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100978/top",url[4],"https://baseball.yahoo.co.jp/mlb/player/2100978/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101784/top",url[4],"https://baseball.yahoo.co.jp/mlb/player/2101784/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101164/top",url[4],"https://baseball.yahoo.co.jp/mlb/player/2101164/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100737/top",url[4],"https://baseball.yahoo.co.jp/mlb/player/2100737/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100347/top",url[4],"https://baseball.yahoo.co.jp/mlb/player/2100347/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100941/top",url[5],"https://baseball.yahoo.co.jp/mlb/player/2100941/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101934/top",url[5],"https://baseball.yahoo.co.jp/mlb/player/2101934/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101042/top",url[5],"https://baseball.yahoo.co.jp/mlb/player/2101042/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100296/top",url[5],"https://baseball.yahoo.co.jp/mlb/player/2100296/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100859/top",url[5],"https://baseball.yahoo.co.jp/mlb/player/2100859/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100952/top",url[5],"https://baseball.yahoo.co.jp/mlb/player/2100952/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2102888/top",url[5],"https://baseball.yahoo.co.jp/mlb/player/2102888/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101553/top",url[5],"https://baseball.yahoo.co.jp/mlb/player/2101553/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101043/top",url[5],"https://baseball.yahoo.co.jp/mlb/player/2101043/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101913/top",url[5],"https://baseball.yahoo.co.jp/mlb/player/2101913/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100192/top",url[5],"https://baseball.yahoo.co.jp/mlb/player/2100192/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100051/top",url[5],"https://baseball.yahoo.co.jp/mlb/player/2100051/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101044/top",url[5],"https://baseball.yahoo.co.jp/mlb/player/2101044/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100018/top",url[5],"https://baseball.yahoo.co.jp/mlb/player/2100018/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100596/top",url[5],"https://baseball.yahoo.co.jp/mlb/player/2100596/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100295/top",url[5],"https://baseball.yahoo.co.jp/mlb/player/2100295/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2102246/top",url[6],"https://baseball.yahoo.co.jp/mlb/player/2102246/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100151/top",url[6],"https://baseball.yahoo.co.jp/mlb/player/2100151/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100058/top",url[6],"https://baseball.yahoo.co.jp/mlb/player/2100058/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100044/top",url[6],"https://baseball.yahoo.co.jp/mlb/player/2100044/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101616/top",url[6],"https://baseball.yahoo.co.jp/mlb/player/2101616/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100510/top",url[6],"https://baseball.yahoo.co.jp/mlb/player/2100510/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101031/top",url[6],"https://baseball.yahoo.co.jp/mlb/player/2101031/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100492/top",url[6],"https://baseball.yahoo.co.jp/mlb/player/2100492/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100676/top",url[6],"https://baseball.yahoo.co.jp/mlb/player/2100676/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/202100434/top",url[6],"https://baseball.yahoo.co.jp/mlb/player/202100434/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101650/top",url[6],"https://baseball.yahoo.co.jp/mlb/player/2101650/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2102492/top",url[6],"https://baseball.yahoo.co.jp/mlb/player/2102492/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100484/top",url[6],"https://baseball.yahoo.co.jp/mlb/player/2100484/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2102065/top",url[7],"https://baseball.yahoo.co.jp/mlb/player/2102065/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2102788/top",url[7],"https://baseball.yahoo.co.jp/mlb/player/2102788/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101052/top",url[7],"https://baseball.yahoo.co.jp/mlb/player/2101052/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100687/top",url[7],"https://baseball.yahoo.co.jp/mlb/player/2100687/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100990/top",url[7],"https://baseball.yahoo.co.jp/mlb/player/2100990/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2102032/top",url[7],"https://baseball.yahoo.co.jp/mlb/player/2102032/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100405/top",url[7],"https://baseball.yahoo.co.jp/mlb/player/2100405/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101872/top",url[7],"https://baseball.yahoo.co.jp/mlb/player/2101872/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101054/top",url[7],"https://baseball.yahoo.co.jp/mlb/player/2101054/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101768/top",url[7],"https://baseball.yahoo.co.jp/mlb/player/2101768/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101855/top",url[7],"https://baseball.yahoo.co.jp/mlb/player/2101855/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100086/top",url[7],"https://baseball.yahoo.co.jp/mlb/player/2100086/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2102465/top",url[7],"https://baseball.yahoo.co.jp/mlb/player/2102465/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2102024/top",url[7],"https://baseball.yahoo.co.jp/mlb/player/2102024/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100960/top",url[7],"https://baseball.yahoo.co.jp/mlb/player/2100960/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100693/top",url[7],"https://baseball.yahoo.co.jp/mlb/player/2100693/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101055/top",url[7],"https://baseball.yahoo.co.jp/mlb/player/2101055/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100652/top",url[7],"https://baseball.yahoo.co.jp/mlb/player/2100652/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100789/top",url[8],"https://baseball.yahoo.co.jp/mlb/player/2100789/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101914/top",url[8],"https://baseball.yahoo.co.jp/mlb/player/2101914/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2102190/top",url[8],"https://baseball.yahoo.co.jp/mlb/player/2102190/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100695/top",url[8],"https://baseball.yahoo.co.jp/mlb/player/2100695/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/202100379/top",url[8],"https://baseball.yahoo.co.jp/mlb/player/202100379/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/202100128/top",url[8],"https://baseball.yahoo.co.jp/mlb/player/202100128/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101543/top",url[8],"https://baseball.yahoo.co.jp/mlb/player/2101543/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/202100388/top",url[8],"https://baseball.yahoo.co.jp/mlb/player/202100388/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100619/top",url[8],"https://baseball.yahoo.co.jp/mlb/player/2100619/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2102008/top",url[8],"https://baseball.yahoo.co.jp/mlb/player/2102008/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2102349/top",url[8],"https://baseball.yahoo.co.jp/mlb/player/2102349/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100289/top",url[8],"https://baseball.yahoo.co.jp/mlb/player/2100289/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2103084/top",url[8],"https://baseball.yahoo.co.jp/mlb/player/2103084/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101622/top",url[8],"https://baseball.yahoo.co.jp/mlb/player/2101622/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101649/top",url[8],"https://baseball.yahoo.co.jp/mlb/player/2101649/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2103161/top",url[8],"https://baseball.yahoo.co.jp/mlb/player/2103161/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100185/top",url[9],"https://baseball.yahoo.co.jp/mlb/player/2100185/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100777/top",url[9],"https://baseball.yahoo.co.jp/mlb/player/2100777/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101064/top",url[9],"https://baseball.yahoo.co.jp/mlb/player/2101064/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100154/top",url[9],"https://baseball.yahoo.co.jp/mlb/player/2100154/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100478/top",url[9],"https://baseball.yahoo.co.jp/mlb/player/2100478/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100552/top",url[9],"https://baseball.yahoo.co.jp/mlb/player/2100552/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100439/top",url[9],"https://baseball.yahoo.co.jp/mlb/player/2100439/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100038/top",url[9],"https://baseball.yahoo.co.jp/mlb/player/2100038/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2102753/top",url[9],"https://baseball.yahoo.co.jp/mlb/player/2102753/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100272/top",url[9],"https://baseball.yahoo.co.jp/mlb/player/2100272/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101829/top",url[9],"https://baseball.yahoo.co.jp/mlb/player/2101829/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100639/top",url[9],"https://baseball.yahoo.co.jp/mlb/player/2100639/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101714/top",url[9],"https://baseball.yahoo.co.jp/mlb/player/2101714/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101066/top",url[9],"https://baseball.yahoo.co.jp/mlb/player/2101066/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100631/top",url[9],"https://baseball.yahoo.co.jp/mlb/player/2100631/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2102905/top",url[9],"https://baseball.yahoo.co.jp/mlb/player/2102905/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100929/top",url[9],"https://baseball.yahoo.co.jp/mlb/player/2100929/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100145/top",url[9],"https://baseball.yahoo.co.jp/mlb/player/2100145/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2102163/top",url[10],"https://baseball.yahoo.co.jp/mlb/player/2102163/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100625/top",url[10],"https://baseball.yahoo.co.jp/mlb/player/2100625/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100636/top",url[10],"https://baseball.yahoo.co.jp/mlb/player/2100636/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100170/top",url[10],"https://baseball.yahoo.co.jp/mlb/player/2100170/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100595/top",url[10],"https://baseball.yahoo.co.jp/mlb/player/2100595/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101831/top",url[10],"https://baseball.yahoo.co.jp/mlb/player/2101831/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100287/top",url[10],"https://baseball.yahoo.co.jp/mlb/player/2100287/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100068/top",url[10],"https://baseball.yahoo.co.jp/mlb/player/2100068/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100334/top",url[10],"https://baseball.yahoo.co.jp/mlb/player/2100334/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101656/top",url[10],"https://baseball.yahoo.co.jp/mlb/player/2101656/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100400/top",url[10],"https://baseball.yahoo.co.jp/mlb/player/2100400/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100246/top",url[10],"https://baseball.yahoo.co.jp/mlb/player/2100246/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101864/top",url[10],"https://baseball.yahoo.co.jp/mlb/player/2101864/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2102725/top",url[10],"https://baseball.yahoo.co.jp/mlb/player/2102725/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100853/top",url[10],"https://baseball.yahoo.co.jp/mlb/player/2100853/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100428/top",url[10],"https://baseball.yahoo.co.jp/mlb/player/2100428/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100354/top",url[10],"https://baseball.yahoo.co.jp/mlb/player/2100354/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100650/top",url[10],"https://baseball.yahoo.co.jp/mlb/player/2100650/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100665/top",url[10],"https://baseball.yahoo.co.jp/mlb/player/2100665/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2102308/top",url[11],"https://baseball.yahoo.co.jp/mlb/player/2102308/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100608/top",url[11],"https://baseball.yahoo.co.jp/mlb/player/2100608/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101699/top",url[11],"https://baseball.yahoo.co.jp/mlb/player/2101699/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101701/top",url[11],"https://baseball.yahoo.co.jp/mlb/player/2101701/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101874/top",url[11],"https://baseball.yahoo.co.jp/mlb/player/2101874/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100870/top",url[11],"https://baseball.yahoo.co.jp/mlb/player/2100870/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2102082/top",url[11],"https://baseball.yahoo.co.jp/mlb/player/2102082/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100906/top",url[11],"https://baseball.yahoo.co.jp/mlb/player/2100906/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100031/top",url[11],"https://baseball.yahoo.co.jp/mlb/player/2100031/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/202100141/top",url[11],"https://baseball.yahoo.co.jp/mlb/player/202100141/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/202100140/top",url[11],"https://baseball.yahoo.co.jp/mlb/player/202100140/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/202100385/top",url[11],"https://baseball.yahoo.co.jp/mlb/player/202100385/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100814/top",url[11],"https://baseball.yahoo.co.jp/mlb/player/2100814/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2102227/top",url[11],"https://baseball.yahoo.co.jp/mlb/player/2102227/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100733/top",url[11],"https://baseball.yahoo.co.jp/mlb/player/2100733/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100124/top",url[11],"https://baseball.yahoo.co.jp/mlb/player/2100124/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101730/top",url[11],"https://baseball.yahoo.co.jp/mlb/player/2101730/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100863/top",url[12],"https://baseball.yahoo.co.jp/mlb/player/2100863/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2102050/top",url[12],"https://baseball.yahoo.co.jp/mlb/player/2102050/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100792/top",url[12],"https://baseball.yahoo.co.jp/mlb/player/2100792/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100368/top",url[12],"https://baseball.yahoo.co.jp/mlb/player/2100368/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100311/top",url[12],"https://baseball.yahoo.co.jp/mlb/player/2100311/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101155/top",url[12],"https://baseball.yahoo.co.jp/mlb/player/2101155/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100659/top",url[12],"https://baseball.yahoo.co.jp/mlb/player/2100659/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100892/top",url[12],"https://baseball.yahoo.co.jp/mlb/player/2100892/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100308/top",url[12],"https://baseball.yahoo.co.jp/mlb/player/2100308/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101074/top",url[12],"https://baseball.yahoo.co.jp/mlb/player/2101074/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101798/top",url[12],"https://baseball.yahoo.co.jp/mlb/player/2101798/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100285/top",url[12],"https://baseball.yahoo.co.jp/mlb/player/2100285/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100857/top",url[12],"https://baseball.yahoo.co.jp/mlb/player/2100857/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101799/top",url[12],"https://baseball.yahoo.co.jp/mlb/player/2101799/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100003/top",url[12],"https://baseball.yahoo.co.jp/mlb/player/2100003/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2102480/top",url[12],"https://baseball.yahoo.co.jp/mlb/player/2102480/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100669/top",url[13],"https://baseball.yahoo.co.jp/mlb/player/2100669/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100457/top",url[13],"https://baseball.yahoo.co.jp/mlb/player/2100457/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100796/top",url[13],"https://baseball.yahoo.co.jp/mlb/player/2100796/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100969/top",url[13],"https://baseball.yahoo.co.jp/mlb/player/2100969/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100211/top",url[13],"https://baseball.yahoo.co.jp/mlb/player/2100211/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2102295/top",url[13],"https://baseball.yahoo.co.jp/mlb/player/2102295/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101742/top",url[13],"https://baseball.yahoo.co.jp/mlb/player/2101742/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100677/top",url[13],"https://baseball.yahoo.co.jp/mlb/player/2100677/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2102638/top",url[13],"https://baseball.yahoo.co.jp/mlb/player/2102638/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100573/top",url[13],"https://baseball.yahoo.co.jp/mlb/player/2100573/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100753/top",url[13],"https://baseball.yahoo.co.jp/mlb/player/2100753/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101901/top",url[13],"https://baseball.yahoo.co.jp/mlb/player/2101901/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101823/top",url[13],"https://baseball.yahoo.co.jp/mlb/player/2101823/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101757/top",url[13],"https://baseball.yahoo.co.jp/mlb/player/2101757/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101207/top",url[13],"https://baseball.yahoo.co.jp/mlb/player/2101207/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2102194/top",url[14],"https://baseball.yahoo.co.jp/mlb/player/2102194/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100616/top",url[14],"https://baseball.yahoo.co.jp/mlb/player/2100616/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/202100422/top",url[14],"https://baseball.yahoo.co.jp/mlb/player/202100422/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100033/top",url[14],"https://baseball.yahoo.co.jp/mlb/player/2100033/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101785/top",url[14],"https://baseball.yahoo.co.jp/mlb/player/2101785/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100628/top",url[14],"https://baseball.yahoo.co.jp/mlb/player/2100628/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100480/top",url[14],"https://baseball.yahoo.co.jp/mlb/player/2100480/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/202100147/top",url[14],"https://baseball.yahoo.co.jp/mlb/player/202100147/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100988/top",url[14],"https://baseball.yahoo.co.jp/mlb/player/2100988/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100500/top",url[14],"https://baseball.yahoo.co.jp/mlb/player/2100500/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101817/top",url[14],"https://baseball.yahoo.co.jp/mlb/player/2101817/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100175/top",url[14],"https://baseball.yahoo.co.jp/mlb/player/2100175/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101110/top",url[14],"https://baseball.yahoo.co.jp/mlb/player/2101110/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/202100229/top",url[14],"https://baseball.yahoo.co.jp/mlb/player/202100229/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100566/top",url[14],"https://baseball.yahoo.co.jp/mlb/player/2100566/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100950/top",url[14],"https://baseball.yahoo.co.jp/mlb/player/2100950/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/202100412/top",url[14],"https://baseball.yahoo.co.jp/mlb/player/202100412/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100807/top",url[15],"https://baseball.yahoo.co.jp/mlb/player/2100807/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100875/top",url[15],"https://baseball.yahoo.co.jp/mlb/player/2100875/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100171/top",url[15],"https://baseball.yahoo.co.jp/mlb/player/2100171/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100705/top",url[15],"https://baseball.yahoo.co.jp/mlb/player/2100705/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101811/top",url[15],"https://baseball.yahoo.co.jp/mlb/player/2101811/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100703/top",url[15],"https://baseball.yahoo.co.jp/mlb/player/2100703/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/202100404/top",url[15],"https://baseball.yahoo.co.jp/mlb/player/202100404/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100089/top",url[15],"https://baseball.yahoo.co.jp/mlb/player/2100089/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100623/top",url[15],"https://baseball.yahoo.co.jp/mlb/player/2100623/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101037/top",url[15],"https://baseball.yahoo.co.jp/mlb/player/2101037/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100764/top",url[15],"https://baseball.yahoo.co.jp/mlb/player/2100764/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100794/top",url[15],"https://baseball.yahoo.co.jp/mlb/player/2100794/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101220/top",url[15],"https://baseball.yahoo.co.jp/mlb/player/2101220/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101850/top",url[15],"https://baseball.yahoo.co.jp/mlb/player/2101850/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100292/top",url[15],"https://baseball.yahoo.co.jp/mlb/player/2100292/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101236/top",url[15],"https://baseball.yahoo.co.jp/mlb/player/2101236/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100749/top",url[16],"https://baseball.yahoo.co.jp/mlb/player/2100749/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100529/top",url[16],"https://baseball.yahoo.co.jp/mlb/player/2100529/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2102204/top",url[16],"https://baseball.yahoo.co.jp/mlb/player/2102204/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100591/top",url[16],"https://baseball.yahoo.co.jp/mlb/player/2100591/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101978/top",url[16],"https://baseball.yahoo.co.jp/mlb/player/2101978/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101659/top",url[16],"https://baseball.yahoo.co.jp/mlb/player/2101659/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100640/top",url[16],"https://baseball.yahoo.co.jp/mlb/player/2100640/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100161/top",url[16],"https://baseball.yahoo.co.jp/mlb/player/2100161/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100415/top",url[16],"https://baseball.yahoo.co.jp/mlb/player/2100415/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100361/top",url[16],"https://baseball.yahoo.co.jp/mlb/player/2100361/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100271/top",url[16],"https://baseball.yahoo.co.jp/mlb/player/2100271/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100914/top",url[16],"https://baseball.yahoo.co.jp/mlb/player/2100914/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2102244/top",url[16],"https://baseball.yahoo.co.jp/mlb/player/2102244/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100208/top",url[16],"https://baseball.yahoo.co.jp/mlb/player/2100208/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100572/top",url[16],"https://baseball.yahoo.co.jp/mlb/player/2100572/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2103180/top",url[16],"https://baseball.yahoo.co.jp/mlb/player/2103180/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/202100399/top",url[16],"https://baseball.yahoo.co.jp/mlb/player/202100399/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100702/top",url[17],"https://baseball.yahoo.co.jp/mlb/player/2100702/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2102368/top",url[17],"https://baseball.yahoo.co.jp/mlb/player/2102368/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100646/top",url[17],"https://baseball.yahoo.co.jp/mlb/player/2100646/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100413/top",url[17],"https://baseball.yahoo.co.jp/mlb/player/2100413/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100315/top",url[17],"https://baseball.yahoo.co.jp/mlb/player/2100315/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100593/top",url[17],"https://baseball.yahoo.co.jp/mlb/player/2100593/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100236/top",url[17],"https://baseball.yahoo.co.jp/mlb/player/2100236/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100719/top",url[17],"https://baseball.yahoo.co.jp/mlb/player/2100719/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101990/top",url[17],"https://baseball.yahoo.co.jp/mlb/player/2101990/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101961/top",url[17],"https://baseball.yahoo.co.jp/mlb/player/2101961/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100832/top",url[17],"https://baseball.yahoo.co.jp/mlb/player/2100832/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100119/top",url[17],"https://baseball.yahoo.co.jp/mlb/player/2100119/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100613/top",url[17],"https://baseball.yahoo.co.jp/mlb/player/2100613/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100861/top",url[17],"https://baseball.yahoo.co.jp/mlb/player/2100861/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100867/top",url[17],"https://baseball.yahoo.co.jp/mlb/player/2100867/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100232/top",url[17],"https://baseball.yahoo.co.jp/mlb/player/2100232/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101204/top",url[18],"https://baseball.yahoo.co.jp/mlb/player/2101204/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101203/top",url[18],"https://baseball.yahoo.co.jp/mlb/player/2101203/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100327/top",url[18],"https://baseball.yahoo.co.jp/mlb/player/2100327/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100489/top",url[18],"https://baseball.yahoo.co.jp/mlb/player/2100489/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101857/top",url[18],"https://baseball.yahoo.co.jp/mlb/player/2101857/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100876/top",url[18],"https://baseball.yahoo.co.jp/mlb/player/2100876/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100744/top",url[18],"https://baseball.yahoo.co.jp/mlb/player/2100744/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101834/top",url[18],"https://baseball.yahoo.co.jp/mlb/player/2101834/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101778/top",url[18],"https://baseball.yahoo.co.jp/mlb/player/2101778/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100029/top",url[18],"https://baseball.yahoo.co.jp/mlb/player/2100029/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100286/top",url[18],"https://baseball.yahoo.co.jp/mlb/player/2100286/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2102096/top",url[18],"https://baseball.yahoo.co.jp/mlb/player/2102096/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100683/top",url[18],"https://baseball.yahoo.co.jp/mlb/player/2100683/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101244/top",url[18],"https://baseball.yahoo.co.jp/mlb/player/2101244/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101081/top",url[18],"https://baseball.yahoo.co.jp/mlb/player/2101081/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100215/top",url[18],"https://baseball.yahoo.co.jp/mlb/player/2100215/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101208/top",url[18],"https://baseball.yahoo.co.jp/mlb/player/2101208/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100384/top",url[18],"https://baseball.yahoo.co.jp/mlb/player/2100384/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100140/top",url[18],"https://baseball.yahoo.co.jp/mlb/player/2100140/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101843/top",url[19],"https://baseball.yahoo.co.jp/mlb/player/2101843/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100377/top",url[19],"https://baseball.yahoo.co.jp/mlb/player/2100377/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100326/top",url[19],"https://baseball.yahoo.co.jp/mlb/player/2100326/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100586/top",url[19],"https://baseball.yahoo.co.jp/mlb/player/2100586/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100455/top",url[19],"https://baseball.yahoo.co.jp/mlb/player/2100455/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100410/top",url[19],"https://baseball.yahoo.co.jp/mlb/player/2100410/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100955/top",url[19],"https://baseball.yahoo.co.jp/mlb/player/2100955/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2102107/top",url[19],"https://baseball.yahoo.co.jp/mlb/player/2102107/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100443/top",url[19],"https://baseball.yahoo.co.jp/mlb/player/2100443/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100324/top",url[19],"https://baseball.yahoo.co.jp/mlb/player/2100324/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100408/top",url[19],"https://baseball.yahoo.co.jp/mlb/player/2100408/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101960/top",url[19],"https://baseball.yahoo.co.jp/mlb/player/2101960/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100422/top",url[19],"https://baseball.yahoo.co.jp/mlb/player/2100422/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101988/top",url[19],"https://baseball.yahoo.co.jp/mlb/player/2101988/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100092/top",url[19],"https://baseball.yahoo.co.jp/mlb/player/2100092/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100459/top",url[19],"https://baseball.yahoo.co.jp/mlb/player/2100459/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101230/top",url[19],"https://baseball.yahoo.co.jp/mlb/player/2101230/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100479/top",url[19],"https://baseball.yahoo.co.jp/mlb/player/2100479/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100911/top",url[20],"https://baseball.yahoo.co.jp/mlb/player/2100911/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100930/top",url[20],"https://baseball.yahoo.co.jp/mlb/player/2100930/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100599/top",url[20],"https://baseball.yahoo.co.jp/mlb/player/2100599/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101617/top",url[20],"https://baseball.yahoo.co.jp/mlb/player/2101617/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100772/top",url[20],"https://baseball.yahoo.co.jp/mlb/player/2100772/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100012/top",url[20],"https://baseball.yahoo.co.jp/mlb/player/2100012/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100934/top",url[20],"https://baseball.yahoo.co.jp/mlb/player/2100934/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100731/top",url[20],"https://baseball.yahoo.co.jp/mlb/player/2100731/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101760/top",url[20],"https://baseball.yahoo.co.jp/mlb/player/2101760/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100130/top",url[20],"https://baseball.yahoo.co.jp/mlb/player/2100130/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100909/top",url[20],"https://baseball.yahoo.co.jp/mlb/player/2100909/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100187/top",url[20],"https://baseball.yahoo.co.jp/mlb/player/2100187/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100419/top",url[20],"https://baseball.yahoo.co.jp/mlb/player/2100419/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100239/top",url[20],"https://baseball.yahoo.co.jp/mlb/player/2100239/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100939/top",url[21],"https://baseball.yahoo.co.jp/mlb/player/2100939/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100888/top",url[21],"https://baseball.yahoo.co.jp/mlb/player/2100888/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100685/top",url[21],"https://baseball.yahoo.co.jp/mlb/player/2100685/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100696/top",url[21],"https://baseball.yahoo.co.jp/mlb/player/2100696/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100237/top",url[21],"https://baseball.yahoo.co.jp/mlb/player/2100237/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101550/top",url[21],"https://baseball.yahoo.co.jp/mlb/player/2101550/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100194/top",url[21],"https://baseball.yahoo.co.jp/mlb/player/2100194/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2102750/top",url[21],"https://baseball.yahoo.co.jp/mlb/player/2102750/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/202100103/top",url[21],"https://baseball.yahoo.co.jp/mlb/player/202100103/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101138/top",url[21],"https://baseball.yahoo.co.jp/mlb/player/2101138/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100360/top",url[21],"https://baseball.yahoo.co.jp/mlb/player/2100360/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101633/top",url[21],"https://baseball.yahoo.co.jp/mlb/player/2101633/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/202100102/top",url[21],"https://baseball.yahoo.co.jp/mlb/player/202100102/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100884/top",url[21],"https://baseball.yahoo.co.jp/mlb/player/2100884/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100664/top",url[21],"https://baseball.yahoo.co.jp/mlb/player/2100664/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100291/top",url[21],"https://baseball.yahoo.co.jp/mlb/player/2100291/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100216/top",url[22],"https://baseball.yahoo.co.jp/mlb/player/2100216/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100602/top",url[22],"https://baseball.yahoo.co.jp/mlb/player/2100602/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100905/top",url[22],"https://baseball.yahoo.co.jp/mlb/player/2100905/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100481/top",url[22],"https://baseball.yahoo.co.jp/mlb/player/2100481/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101792/top",url[22],"https://baseball.yahoo.co.jp/mlb/player/2101792/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101741/top",url[22],"https://baseball.yahoo.co.jp/mlb/player/2101741/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100692/top",url[22],"https://baseball.yahoo.co.jp/mlb/player/2100692/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100442/top",url[22],"https://baseball.yahoo.co.jp/mlb/player/2100442/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100540/top",url[22],"https://baseball.yahoo.co.jp/mlb/player/2100540/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101171/top",url[22],"https://baseball.yahoo.co.jp/mlb/player/2101171/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100387/top",url[22],"https://baseball.yahoo.co.jp/mlb/player/2100387/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2102154/top",url[22],"https://baseball.yahoo.co.jp/mlb/player/2102154/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101703/top",url[22],"https://baseball.yahoo.co.jp/mlb/player/2101703/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2103139/top",url[22],"https://baseball.yahoo.co.jp/mlb/player/2103139/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100085/top",url[23],"https://baseball.yahoo.co.jp/mlb/player/2100085/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2102169/top",url[23],"https://baseball.yahoo.co.jp/mlb/player/2102169/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100527/top",url[23],"https://baseball.yahoo.co.jp/mlb/player/2100527/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100761/top",url[23],"https://baseball.yahoo.co.jp/mlb/player/2100761/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101128/top",url[23],"https://baseball.yahoo.co.jp/mlb/player/2101128/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100890/top",url[23],"https://baseball.yahoo.co.jp/mlb/player/2100890/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100158/top",url[23],"https://baseball.yahoo.co.jp/mlb/player/2100158/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101840/top",url[23],"https://baseball.yahoo.co.jp/mlb/player/2101840/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101643/top",url[23],"https://baseball.yahoo.co.jp/mlb/player/2101643/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101838/top",url[23],"https://baseball.yahoo.co.jp/mlb/player/2101838/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101841/top",url[23],"https://baseball.yahoo.co.jp/mlb/player/2101841/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100139/top",url[23],"https://baseball.yahoo.co.jp/mlb/player/2100139/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2102061/top",url[23],"https://baseball.yahoo.co.jp/mlb/player/2102061/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101871/top",url[23],"https://baseball.yahoo.co.jp/mlb/player/2101871/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100493/top",url[23],"https://baseball.yahoo.co.jp/mlb/player/2100493/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/202100109/top",url[23],"https://baseball.yahoo.co.jp/mlb/player/202100109/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100055/top",url[23],"https://baseball.yahoo.co.jp/mlb/player/2100055/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100424/top",url[23],"https://baseball.yahoo.co.jp/mlb/player/2100424/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100054/top",url[24],"https://baseball.yahoo.co.jp/mlb/player/2100054/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100933/top",url[24],"https://baseball.yahoo.co.jp/mlb/player/2100933/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101150/top",url[24],"https://baseball.yahoo.co.jp/mlb/player/2101150/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100714/top",url[24],"https://baseball.yahoo.co.jp/mlb/player/2100714/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101534/top",url[24],"https://baseball.yahoo.co.jp/mlb/player/2101534/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100701/top",url[24],"https://baseball.yahoo.co.jp/mlb/player/2100701/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/202100105/top",url[24],"https://baseball.yahoo.co.jp/mlb/player/202100105/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100716/top",url[24],"https://baseball.yahoo.co.jp/mlb/player/2100716/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101697/top",url[24],"https://baseball.yahoo.co.jp/mlb/player/2101697/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100282/top",url[24],"https://baseball.yahoo.co.jp/mlb/player/2100282/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100865/top",url[24],"https://baseball.yahoo.co.jp/mlb/player/2100865/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2102188/top",url[24],"https://baseball.yahoo.co.jp/mlb/player/2102188/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100903/top",url[24],"https://baseball.yahoo.co.jp/mlb/player/2100903/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/202100428/top",url[24],"https://baseball.yahoo.co.jp/mlb/player/202100428/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/202100097/top",url[24],"https://baseball.yahoo.co.jp/mlb/player/202100097/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100079/top",url[25],"https://baseball.yahoo.co.jp/mlb/player/2100079/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100928/top",url[25],"https://baseball.yahoo.co.jp/mlb/player/2100928/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100183/top",url[25],"https://baseball.yahoo.co.jp/mlb/player/2100183/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100320/top",url[25],"https://baseball.yahoo.co.jp/mlb/player/2100320/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100329/top",url[25],"https://baseball.yahoo.co.jp/mlb/player/2100329/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100654/top",url[25],"https://baseball.yahoo.co.jp/mlb/player/2100654/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100633/top",url[25],"https://baseball.yahoo.co.jp/mlb/player/2100633/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101673/top",url[25],"https://baseball.yahoo.co.jp/mlb/player/2101673/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101764/top",url[25],"https://baseball.yahoo.co.jp/mlb/player/2101764/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100249/top",url[25],"https://baseball.yahoo.co.jp/mlb/player/2100249/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100403/top",url[25],"https://baseball.yahoo.co.jp/mlb/player/2100403/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101624/top",url[25],"https://baseball.yahoo.co.jp/mlb/player/2101624/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101671/top",url[25],"https://baseball.yahoo.co.jp/mlb/player/2101671/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100674/top",url[25],"https://baseball.yahoo.co.jp/mlb/player/2100674/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100367/top",url[25],"https://baseball.yahoo.co.jp/mlb/player/2100367/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100587/top",url[26],"https://baseball.yahoo.co.jp/mlb/player/2100587/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100087/top",url[26],"https://baseball.yahoo.co.jp/mlb/player/2100087/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100328/top",url[26],"https://baseball.yahoo.co.jp/mlb/player/2100328/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100937/top",url[26],"https://baseball.yahoo.co.jp/mlb/player/2100937/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101196/top",url[26],"https://baseball.yahoo.co.jp/mlb/player/2101196/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100385/top",url[26],"https://baseball.yahoo.co.jp/mlb/player/2100385/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101660/top",url[26],"https://baseball.yahoo.co.jp/mlb/player/2101660/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100607/top",url[26],"https://baseball.yahoo.co.jp/mlb/player/2100607/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2102589/top",url[26],"https://baseball.yahoo.co.jp/mlb/player/2102589/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2102835/top",url[26],"https://baseball.yahoo.co.jp/mlb/player/2102835/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100770/top",url[26],"https://baseball.yahoo.co.jp/mlb/player/2100770/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101546/top",url[26],"https://baseball.yahoo.co.jp/mlb/player/2101546/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100877/top",url[26],"https://baseball.yahoo.co.jp/mlb/player/2100877/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100514/top",url[26],"https://baseball.yahoo.co.jp/mlb/player/2100514/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100312/top",url[26],"https://baseball.yahoo.co.jp/mlb/player/2100312/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2102464/top",url[26],"https://baseball.yahoo.co.jp/mlb/player/2102464/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100620/top",url[26],"https://baseball.yahoo.co.jp/mlb/player/2100620/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100760/top",url[27],"https://baseball.yahoo.co.jp/mlb/player/2100760/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100438/top",url[27],"https://baseball.yahoo.co.jp/mlb/player/2100438/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100366/top",url[27],"https://baseball.yahoo.co.jp/mlb/player/2100366/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100363/top",url[27],"https://baseball.yahoo.co.jp/mlb/player/2100363/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100569/top",url[27],"https://baseball.yahoo.co.jp/mlb/player/2100569/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2102684/top",url[27],"https://baseball.yahoo.co.jp/mlb/player/2102684/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100117/top",url[27],"https://baseball.yahoo.co.jp/mlb/player/2100117/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100858/top",url[27],"https://baseball.yahoo.co.jp/mlb/player/2100858/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100935/top",url[27],"https://baseball.yahoo.co.jp/mlb/player/2100935/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100666/top",url[27],"https://baseball.yahoo.co.jp/mlb/player/2100666/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100641/top",url[27],"https://baseball.yahoo.co.jp/mlb/player/2100641/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101932/top",url[27],"https://baseball.yahoo.co.jp/mlb/player/2101932/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100090/top",url[27],"https://baseball.yahoo.co.jp/mlb/player/2100090/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100670/top",url[27],"https://baseball.yahoo.co.jp/mlb/player/2100670/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100592/top",url[27],"https://baseball.yahoo.co.jp/mlb/player/2100592/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2102741/top",url[27],"https://baseball.yahoo.co.jp/mlb/player/2102741/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101140/top",url[27],"https://baseball.yahoo.co.jp/mlb/player/2101140/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101679/top",url[28],"https://baseball.yahoo.co.jp/mlb/player/2101679/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101722/top",url[28],"https://baseball.yahoo.co.jp/mlb/player/2101722/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100293/top",url[28],"https://baseball.yahoo.co.jp/mlb/player/2100293/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/202100418/top",url[28],"https://baseball.yahoo.co.jp/mlb/player/202100418/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100123/top",url[28],"https://baseball.yahoo.co.jp/mlb/player/2100123/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101642/top",url[28],"https://baseball.yahoo.co.jp/mlb/player/2101642/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/202100113/top",url[28],"https://baseball.yahoo.co.jp/mlb/player/202100113/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100779/top",url[28],"https://baseball.yahoo.co.jp/mlb/player/2100779/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101775/top",url[28],"https://baseball.yahoo.co.jp/mlb/player/2101775/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100346/top",url[28],"https://baseball.yahoo.co.jp/mlb/player/2100346/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101189/top",url[28],"https://baseball.yahoo.co.jp/mlb/player/2101189/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100736/top",url[28],"https://baseball.yahoo.co.jp/mlb/player/2100736/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101036/top",url[28],"https://baseball.yahoo.co.jp/mlb/player/2101036/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100547/top",url[28],"https://baseball.yahoo.co.jp/mlb/player/2100547/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101197/top",url[28],"https://baseball.yahoo.co.jp/mlb/player/2101197/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100173/top",url[28],"https://baseball.yahoo.co.jp/mlb/player/2100173/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101692/top",url[29],"https://baseball.yahoo.co.jp/mlb/player/2101692/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100322/top",url[29],"https://baseball.yahoo.co.jp/mlb/player/2100322/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100160/top",url[29],"https://baseball.yahoo.co.jp/mlb/player/2100160/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101170/top",url[29],"https://baseball.yahoo.co.jp/mlb/player/2101170/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100309/top",url[29],"https://baseball.yahoo.co.jp/mlb/player/2100309/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100535/top",url[29],"https://baseball.yahoo.co.jp/mlb/player/2100535/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100494/top",url[29],"https://baseball.yahoo.co.jp/mlb/player/2100494/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100681/top",url[29],"https://baseball.yahoo.co.jp/mlb/player/2100681/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101648/top",url[29],"https://baseball.yahoo.co.jp/mlb/player/2101648/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100186/top",url[29],"https://baseball.yahoo.co.jp/mlb/player/2100186/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2102574/top",url[29],"https://baseball.yahoo.co.jp/mlb/player/2102574/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2103005/top",url[29],"https://baseball.yahoo.co.jp/mlb/player/2103005/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2102009/top",url[29],"https://baseball.yahoo.co.jp/mlb/player/2102009/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100583/top",url[29],"https://baseball.yahoo.co.jp/mlb/player/2100583/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2101691/top",url[29],"https://baseball.yahoo.co.jp/mlb/player/2101691/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100561/top",url[29],"https://baseball.yahoo.co.jp/mlb/player/2100561/top")
# past_data("https://baseball.yahoo.co.jp/mlb/player/2100717/top",url[29],"https://baseball.yahoo.co.jp/mlb/player/2100717/top")
