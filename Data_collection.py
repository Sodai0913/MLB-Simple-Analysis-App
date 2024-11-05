import pandas as pd
import numpy as np
import streamlit as st


st.title("勝敗分析")

# チーム選択
home_team = st.selectbox('ホームチーム選択',['ボルチモア・オリオールズ','ボストン・レッドソックス','ニューヨーク・ヤンキース','トロント・ブルージェイズ','タンパベイ・レイズ','シカゴ・ホワイトソックス','クリーブランド・ガーディアンズ','デトロイト・タイガース','カンザスシティ・ロイヤルズ','ミネソタ・ツインズ','ロサンゼルス・エンゼルス','オークランド・アスレチックス','シアトル・マリナーズ','テキサス・レンジャーズ','ヒューストン・アストロズ','アトランタ・ブレーブス','ワシントン・ナショナルズ','ニューヨーク・メッツ','フィラデルフィア・フィリーズ','マイアミ・マーリンズ','ミルウォーキー・ブリュワーズ','シカゴ・カブス','シンシナティ・レッズ','ピッツバーグ・パイレーツ','セントルイス・カージナルス','ロサンゼルス・ドジャース','サンディエゴ・パドレス','サンフランシスコ・ジャイアンツ','コロラド・ロッキーズ','アリゾナ・ダイヤモンドバックス'])
away_team = st.selectbox('アウェーチーム選択',['ボルチモア・オリオールズ','ボストン・レッドソックス','ニューヨーク・ヤンキース','トロント・ブルージェイズ','タンパベイ・レイズ','シカゴ・ホワイトソックス','クリーブランド・ガーディアンズ','デトロイト・タイガース','カンザスシティ・ロイヤルズ','ミネソタ・ツインズ','ロサンゼルス・エンゼルス','オークランド・アスレチックス','シアトル・マリナーズ','テキサス・レンジャーズ','ヒューストン・アストロズ','アトランタ・ブレーブス','ワシントン・ナショナルズ','ニューヨーク・メッツ','フィラデルフィア・フィリーズ','マイアミ・マーリンズ','ミルウォーキー・ブリュワーズ','シカゴ・カブス','シンシナティ・レッズ','ピッツバーグ・パイレーツ','セントルイス・カージナルス','ロサンゼルス・ドジャース','サンディエゴ・パドレス','サンフランシスコ・ジャイアンツ','コロラド・ロッキーズ','アリゾナ・ダイヤモンドバックス'])

teams = ['ボルチモア・オリオールズ','ボストン・レッドソックス','ニューヨーク・ヤンキース','トロント・ブルージェイズ','タンパベイ・レイズ','シカゴ・ホワイトソックス','クリーブランド・ガーディアンズ','デトロイト・タイガース','カンザスシティ・ロイヤルズ','ミネソタ・ツインズ','ロサンゼルス・エンゼルス','オークランド・アスレチックス','シアトル・マリナーズ','テキサス・レンジャーズ','ヒューストン・アストロズ','アトランタ・ブレーブス','ワシントン・ナショナルズ','ニューヨーク・メッツ','フィラデルフィア・フィリーズ','マイアミ・マーリンズ','ミルウォーキー・ブリュワーズ','シカゴ・カブス','シンシナティ・レッズ','ピッツバーグ・パイレーツ','セントルイス・カージナルス','ロサンゼルス・ドジャース','サンディエゴ・パドレス','サンフランシスコ・ジャイアンツ','コロラド・ロッキーズ','アリゾナ・ダイヤモンドバックス']
teams_name = ['オリオールズ','Rソックス','ヤンキース','ブルージェイズ','レイズ','Wソックス','ガーディアンズ','タイガース','ロイヤルズ','ツインズ','エンゼルス','アスレチックス','マリナーズ','レンジャーズ','アストロズ','ブレーブス','ナショナルズ','メッツ','フィリーズ','マーリンズ','ブリュワーズ','カブス','レッズ','パイレーツ','カージナルス','ドジャース','パドレス','ジャイアンツ','ロッキーズ','Dバックス']
fielder_csv = ['.\data\MLB-fielder\Baltimore_Orioles_fielder.csv','.\data\MLB-fielder\Boston_Redsox_fielder.csv',r'.\data\MLB-fielder\New_York_Yanks_fielder.csv','.\data\MLB-fielder\Tronto_Blue_Jays_fielder.csv','.\data\MLB-fielder\Tampa_Bay_Rays_fielder.csv','.\data\MLB-fielder\Chicago_White_Sox_fielder.csv','.\data\MLB-fielder\Cleveland_Guardians_fielder.csv','.\data\MLB-fielder\Detroit_Tigers_fielder.csv','.\data\MLB-fielder\Kansas_City_Royals_fielder.csv','.\data\MLB-fielder\Minnesota_Twins_fielder.csv','.\data\MLB-fielder\Los_Angeles_Angeles_fielder.csv','.\data\MLB-fielder\Oakland_Athletics_fielder.csv','.\data\MLB-fielder\Seattle_Mariners_fielder.csv','.\data\MLB-fielder\Texas_Rangers_fielder.csv','.\data\MLB-fielder\Houston_Astros_fielder.csv','.\data\MLB-fielder\Atlanta_Braves_fielder.csv','.\data\MLB-fielder\Washington_Nationals_fielder.csv',r'.\data\MLB-fielder\New_York_Mets_fielder.csv','.\data\MLB-fielder\Philadelphia_Phillies_fielder.csv','.\data\MLB-fielder\Miami_Marlins_fielder.csv','.\data\MLB-fielder\Milwaukee_Brewers_fielder.csv','.\data\MLB-fielder\Chicago_Cubs_fielder.csv','.\data\MLB-fielder\Cincinnati_Reds_fielder.csv','.\data\MLB-fielder\Pittsburgh_Pirates_fielder.csv','.\data\MLB-fielder\St_Louis_Cardinals_fielder.csv','.\data\MLB-fielder\Los_Angeles_Dodgers_fielder.csv','.\data\MLB-fielder\San_Diego_Padres_fielder.csv','.\data\MLB-fielder\San_Francisco_Giants_fielder.csv','.\data\MLB-fielder\Colorado_Rockes_fielder.csv','.\data\MLB-fielder\Arizona_Diamondbacks_fielder.csv']
pitcher_csv = ['.\data\MLB-pitcher\Baltimore_Orioles_pitcher.csv','.\data\MLB-pitcher\Boston_Redsox_pitcher.csv',r'.\data\MLB-pitcher\New_York_Yanks_pitcher.csv','.\data\MLB-pitcher\Tronto_Blue_Jays_pitcher.csv','.\data\MLB-pitcher\Tampa_Bay_Rays_pitcher.csv','.\data\MLB-pitcher\Chicago_White_Sox_pitcher.csv','.\data\MLB-pitcher\Cleveland_Guardians_pitcher.csv','.\data\MLB-pitcher\Detroit_Tigers_pitcher.csv','.\data\MLB-pitcher\Kansas_City_Royals_pitcher.csv','.\data\MLB-pitcher\Minnesota_Twins_pitcher.csv','.\data\MLB-pitcher\Los_Angeles_Angeles_pitcher.csv','.\data\MLB-pitcher\Oakland_Athletics_pitcher.csv','.\data\MLB-pitcher\Seattle_Mariners_pitcher.csv','.\data\MLB-pitcher\Texas_Rangers_pitcher.csv','.\data\MLB-pitcher\Houston_Astros_pitcher.csv','.\data\MLB-pitcher\Atlanta_Braves_pitcher.csv','.\data\MLB-pitcher\Washington_Nationals_pitcher.csv',r'.\data\MLB-pitcher\New_York_Mets_pitcher.csv','.\data\MLB-pitcher\Philadelphia_Phillies_pitcher.csv','.\data\MLB-pitcher\Miami_Marlins_pitcher.csv','.\data\MLB-pitcher\Milwaukee_Brewers_pitcher.csv','.\data\MLB-pitcher\Chicago_Cubs_pitcher.csv','.\data\MLB-pitcher\Cincinnati_Reds_pitcher.csv','.\data\MLB-pitcher\Pittsburgh_Pirates_pitcher.csv','.\data\MLB-pitcher\St_Louis_Cardinals_pitcher.csv','.\data\MLB-pitcher\Los_Angeles_Dodgers_pitcher.csv','.\data\MLB-pitcher\San_Diego_Padres_pitcher.csv','.\data\MLB-pitcher\San_Francisco_Giants_pitcher.csv','.\data\MLB-pitcher\Colorado_Rockes_pitcher.csv','.\data\MLB-pitcher\Arizona_Diamondbacks_pitcher.csv']

# ホームチームの処理
for i in range(len(teams)):
    if home_team == teams[i]:

        # 必要なcsvの読み込み
        home_team_df = pd.read_csv('.\data\MLB-team\MLB_team.csv')
        home_team_Individualresults_fielder_df = pd.read_csv(fielder_csv[i])
        home_team_Individualresults_pitcher_df = pd.read_csv(pitcher_csv[i])

        # 対応するチームのみ表示
        home_team_df = home_team_df[home_team_df['チーム'] == teams_name[i]]

        # 不要なカラムを削除
        home_team_df = home_team_df.drop(home_team_df.columns[0], axis=1)
        home_team_Individualresults_fielder_df = home_team_Individualresults_fielder_df.drop(home_team_Individualresults_fielder_df.columns[0], axis=1)
        home_team_Individualresults_pitcher_df = home_team_Individualresults_pitcher_df.drop(home_team_Individualresults_pitcher_df.columns[0], axis=1)


# アウェイチームの処理
for i in range(len(teams)):
    if away_team == teams[i]:

        # 必要なcsvの読み込み
        away_team_df = pd.read_csv('.\data\MLB-team\MLB_team.csv')
        away_team_Individualresults_fielder_df = pd.read_csv(fielder_csv[i])
        away_team_Individualresults_pitcher_df = pd.read_csv(pitcher_csv[i])

        # 対応するチームのみ表示
        away_team_df = away_team_df[away_team_df['チーム'] == teams_name[i]]

        # 不要なカラムを削除
        away_team_df = away_team_df.drop(away_team_df.columns[0], axis=1)
        away_team_Individualresults_fielder_df = away_team_Individualresults_fielder_df.drop(away_team_Individualresults_fielder_df.columns[0], axis=1)
        away_team_Individualresults_pitcher_df = away_team_Individualresults_pitcher_df.drop(away_team_Individualresults_pitcher_df.columns[0], axis=1)





# 適切なタイプに変換
# home
# データの中の'-'を0に変換
home_team_Individualresults_fielder_df = home_team_Individualresults_fielder_df.replace('-',0)

# 適切なタイプに変換
home_team_Individualresults_fielder_df_str = home_team_Individualresults_fielder_df[['Team','位置','背番号','選手名']]
home_team_Individualresults_fielder_df_float = home_team_Individualresults_fielder_df[['打率','出塁率','長打率','ＯＰＳ','得点圏']].astype(np.float64)
home_team_Individualresults_fielder_df_int = home_team_Individualresults_fielder_df[['試合','打席','打数','安打','二塁打','三塁打','本塁打','塁打','打点','得点','三振','四球','死球','犠打','犠飛','盗塁','盗塁死','併殺打']].astype(np.int64)

# データフレームを結合
home_team_Individualresults_fielder_df = pd.concat([home_team_Individualresults_fielder_df_str,home_team_Individualresults_fielder_df_int],axis=1)
home_team_Individualresults_fielder_df = pd.concat([home_team_Individualresults_fielder_df,home_team_Individualresults_fielder_df_float],axis=1)

# away
# データの中の'-'を0に変換
away_team_Individualresults_fielder_df = away_team_Individualresults_fielder_df.replace('-',0)

# 適切なタイプに変換
away_team_Individualresults_fielder_df_str = away_team_Individualresults_fielder_df[['Team','位置','背番号','選手名']]
away_team_Individualresults_fielder_df_float = away_team_Individualresults_fielder_df[['打率','出塁率','長打率','ＯＰＳ','得点圏']].astype(np.float64)
away_team_Individualresults_fielder_df_int = away_team_Individualresults_fielder_df[['試合','打席','打数','安打','二塁打','三塁打','本塁打','塁打','打点','得点','三振','四球','死球','犠打','犠飛','盗塁','盗塁死','併殺打']].astype(np.int64)

# データフレームを結合
away_team_Individualresults_fielder_df = pd.concat([away_team_Individualresults_fielder_df_str,away_team_Individualresults_fielder_df_int],axis=1)
away_team_Individualresults_fielder_df = pd.concat([away_team_Individualresults_fielder_df,away_team_Individualresults_fielder_df_float],axis=1)

# 投手
# home
# データの中の'-'を0に変換
home_team_Individualresults_pitcher_df = home_team_Individualresults_pitcher_df.replace('-',0)

# 適切なタイプに変換
home_team_Individualresults_pitcher_df_str = home_team_Individualresults_pitcher_df[['Team','背番号','選手名']]
home_team_Individualresults_pitcher_df_float = home_team_Individualresults_pitcher_df[['防御率','投球回','勝率','奪三振率','被打率','Ｋ／ＢＢ','ＷＨＩＰ']].astype(np.float64)
home_team_Individualresults_pitcher_df_int = home_team_Individualresults_pitcher_df[['登板', '先発', '完投', '完封', 'ＱＳ','勝利', '敗戦', 'ホールド', 'セーブ', '被安打', '被本塁打', '奪三振','与四球', '与死球', '暴投', 'ボーク', '失点', '自責点']].astype(np.int64)

# データフレームを結合
home_team_Individualresults_pitcher_df = pd.concat([home_team_Individualresults_pitcher_df_str,home_team_Individualresults_pitcher_df_int],axis=1)
home_team_Individualresults_pitcher_df = pd.concat([home_team_Individualresults_pitcher_df,home_team_Individualresults_pitcher_df_float],axis=1)


# away
# データの中の'-'を0に変換
away_team_Individualresults_pitcher_df = away_team_Individualresults_pitcher_df.replace('-',0)

# 適切なタイプに変換
away_team_Individualresults_pitcher_df_str = away_team_Individualresults_pitcher_df[['Team','背番号','選手名']]
away_team_Individualresults_pitcher_df_float = away_team_Individualresults_pitcher_df[['防御率','投球回','勝率','奪三振率','被打率','Ｋ／ＢＢ','ＷＨＩＰ']].astype(np.float64)
away_team_Individualresults_pitcher_df_int = away_team_Individualresults_pitcher_df[['登板', '先発', '完投', '完封', 'ＱＳ','勝利', '敗戦', 'ホールド', 'セーブ', '被安打', '被本塁打', '奪三振','与四球', '与死球', '暴投', 'ボーク', '失点', '自責点']].astype(np.int64)

# データフレームを結合
away_team_Individualresults_pitcher_df = pd.concat([away_team_Individualresults_pitcher_df_str,away_team_Individualresults_pitcher_df_int],axis=1)
away_team_Individualresults_pitcher_df = pd.concat([away_team_Individualresults_pitcher_df,away_team_Individualresults_pitcher_df_float],axis=1)


# スターティングメンバ―を選択したデータ分析
# スターティングメンバーを選択する
st.title("スターティングメンバー選択")
# 野手のスタメンを選択
# ホームチームのスタメン選択
home_player_name_fielder_list = []

for i in range(len(home_team_Individualresults_fielder_df)):
    player_name = home_team_Individualresults_fielder_df.loc[i,'選手名']
    home_player_name_fielder_list.append(player_name)

home_fielder_list = st.multiselect(f'ホーム：{home_team}のスターティングメンバー（9人）を選択してください（打順通りに）',home_player_name_fielder_list)

# 9人以外が選択されたらエラーメッセージ
if len(home_fielder_list) == 9:
    for i in range(len(home_fielder_list)):
        if i == 0:
            home_fielder_df = home_team_Individualresults_fielder_df[home_team_Individualresults_fielder_df['選手名'] == home_fielder_list[i]]
        else:
            home_fielder_df_tmp = home_team_Individualresults_fielder_df[home_team_Individualresults_fielder_df['選手名'] == home_fielder_list[i]]
            home_fielder_df = pd.concat([home_fielder_df,home_fielder_df_tmp])

elif len(home_fielder_list) > 9:
    st.write("9人を超えています。9人だけ選んでください。")

else:
    st.write("9人未満です。9人だけ選んでください。")


# アウェーチームスタメン選択
away_player_name_fielder_list = []

for i in range(len(away_team_Individualresults_fielder_df)):
    player_name = away_team_Individualresults_fielder_df.loc[i,'選手名']
    away_player_name_fielder_list.append(player_name)

away_fielder_list = st.multiselect(f'アウェー：{away_team}のスターティングメンバー（9人）を選択してください（打順通りに）',away_player_name_fielder_list)

# 9人以外が選択されたらエラーメッセージ
if len(away_fielder_list) == 9:
    for i in range(len(away_fielder_list)):
        if i == 0:
            away_fielder_df = away_team_Individualresults_fielder_df[away_team_Individualresults_fielder_df['選手名'] == away_fielder_list[i]]
        else:
            away_fielder_df_tmp = away_team_Individualresults_fielder_df[away_team_Individualresults_fielder_df['選手名'] == away_fielder_list[i]]
            away_fielder_df = pd.concat([away_fielder_df,away_fielder_df_tmp])

elif len(away_fielder_list) > 9:
    st.write("9人を超えています。9人だけ選んでください。")

else:
    st.write("9人未満です。9人だけ選んでください。")


# ホームチーム
# 選手の名前を格納
home_player_name_pitcher_list = []

for i in range(len(home_team_Individualresults_pitcher_df)):
    player_name = home_team_Individualresults_pitcher_df.loc[i,'選手名']
    home_player_name_pitcher_list.append(player_name)

# セレクトボックスによる先発投手選択
home_selectbox = st.selectbox(f"ホーム：{home_team}の先発投手を選んでください", (home_player_name_pitcher_list))
# 投手
home_select_player = home_team_Individualresults_pitcher_df[home_team_Individualresults_pitcher_df['選手名'] == home_selectbox]


# アウェーチーム
# 選手の名前を格納
away_player_name_pitcher_list = []

for i in range(len(away_team_Individualresults_pitcher_df)):
    player_name = away_team_Individualresults_pitcher_df.loc[i,'選手名']
    away_player_name_pitcher_list.append(player_name)

# セレクトボックスによる先発投手選択
away_selectbox = st.selectbox(f"アウェー：{away_team}の先発投手を選んでください", (away_player_name_pitcher_list))
# 投手
away_select_player = away_team_Individualresults_pitcher_df[away_team_Individualresults_pitcher_df['選手名'] == away_selectbox]



# スタメンの比較
if len(home_fielder_list) == 9 and len(away_fielder_list) == 9:

    st.title("スターティングメンバー")
    st.write(f"ホームチーム : {home_team}")
    st.write(home_fielder_df.drop('Team',axis=1),home_select_player.drop('Team',axis=1))
    st.write(f"アウェーチーム : {away_team}")
    st.write(away_fielder_df.drop('Team',axis=1),away_select_player.drop('Team',axis=1))

    # 比較用データフレーム作成
    # 元のリスト作成
    startingmember_list = [home_fielder_df["打率"].mean(),away_fielder_df["打率"].mean(),
                           home_fielder_df["安打"].sum()-away_fielder_df["安打"].sum(),away_fielder_df["安打"].sum()-home_fielder_df["安打"].sum(),
                           home_fielder_df["二塁打"].sum()-away_fielder_df["二塁打"].sum(),away_fielder_df["二塁打"].sum()-home_fielder_df["二塁打"].sum(),
                           home_fielder_df["三塁打"].sum()-away_fielder_df["三塁打"].sum(),away_fielder_df["三塁打"].sum()-home_fielder_df["三塁打"].sum(),
                           home_fielder_df["本塁打"].sum()-away_fielder_df["本塁打"].sum(),away_fielder_df["本塁打"].sum()-home_fielder_df["本塁打"].sum(),
                           home_fielder_df["塁打"].sum()-away_fielder_df["塁打"].sum(),away_fielder_df["塁打"].sum()-home_fielder_df["塁打"].sum(),
                           home_fielder_df["得点"].sum()-away_fielder_df["得点"].sum(),away_fielder_df["得点"].sum()-home_fielder_df["得点"].sum(),
                           home_fielder_df["三振"].sum()-away_fielder_df["三振"].sum(),away_fielder_df["三振"].sum()-home_fielder_df["三振"].sum(),
                           home_fielder_df["四球"].sum()-away_fielder_df["四球"].sum(),away_fielder_df["四球"].sum()-home_fielder_df["四球"].sum(),
                           home_fielder_df["死球"].sum()-away_fielder_df["死球"].sum(),away_fielder_df["死球"].sum()-home_fielder_df["死球"].sum(),
                           home_fielder_df["犠打"].sum()-away_fielder_df["犠打"].sum(),away_fielder_df["犠打"].sum()-home_fielder_df["犠打"].sum(),
                           home_fielder_df["犠飛"].sum()-away_fielder_df["犠飛"].sum(),away_fielder_df["犠飛"].sum()-home_fielder_df["犠飛"].sum(),
                           home_fielder_df["盗塁"].sum()-away_fielder_df["盗塁"].sum(),away_fielder_df["盗塁"].sum()-home_fielder_df["盗塁"].sum(),
                           home_fielder_df["盗塁死"].sum()-away_fielder_df["盗塁死"].sum(),away_fielder_df["盗塁死"].sum()-home_fielder_df["盗塁死"].sum(),
                           home_fielder_df["併殺打"].sum()-away_fielder_df["併殺打"].sum(),away_fielder_df["併殺打"].sum()-home_fielder_df["併殺打"].sum(),
                           home_fielder_df["出塁率"].mean(),away_fielder_df["出塁率"].mean(),
                           home_fielder_df["長打率"].mean(),away_fielder_df["長打率"].mean(),
                           home_fielder_df["ＯＰＳ"].mean(),away_fielder_df["ＯＰＳ"].mean(),
                           home_fielder_df["得点圏"].mean(),away_fielder_df["得点圏"].mean(),
                           float(away_select_player["登板"])-float(home_select_player["登板"]),float(home_select_player["登板"])-float(away_select_player["登板"]),
                           float(away_select_player["先発"])-float(home_select_player["先発"]),float(home_select_player["先発"])-float(away_select_player["先発"]),
                           float(away_select_player["完投"])-float(home_select_player["完投"]),float(home_select_player["完投"])-float(away_select_player["完投"]),
                           float(away_select_player["ＱＳ"])-float(home_select_player["ＱＳ"]),float(home_select_player["ＱＳ"])-float(away_select_player["ＱＳ"]),
                           float(away_select_player["勝利"])-float(home_select_player["勝利"]),float(home_select_player["勝利"])-float(away_select_player["勝利"]),
                           float(away_select_player["敗戦"])-float(home_select_player["敗戦"]),float(home_select_player["敗戦"])-float(away_select_player["敗戦"]),
                           float(away_select_player["ホールド"])-float(home_select_player["ホールド"]),float(home_select_player["ホールド"])-float(away_select_player["ホールド"]),
                           float(away_select_player["セーブ"])-float(home_select_player["セーブ"]),float(home_select_player["セーブ"])-float(away_select_player["セーブ"]),
                           float(away_select_player["被安打"])-float(home_select_player["被安打"]),float(home_select_player["被安打"])-float(away_select_player["被安打"]),
                           float(away_select_player["被本塁打"])-float(home_select_player["被本塁打"]),float(home_select_player["被本塁打"])-float(away_select_player["被本塁打"]),
                           float(away_select_player["奪三振"])-float(home_select_player["奪三振"]),float(home_select_player["奪三振"])-float(away_select_player["奪三振"]),
                           float(away_select_player["与四球"])-float(home_select_player["与四球"]),float(home_select_player["与四球"])-float(away_select_player["与四球"]),
                           float(away_select_player["与死球"])-float(home_select_player["与死球"]),float(home_select_player["与死球"])-float(away_select_player["与死球"]),
                           float(away_select_player["暴投"])-float(home_select_player["暴投"]),float(home_select_player["暴投"])-float(away_select_player["暴投"]),
                           float(away_select_player["ボーク"])-float(home_select_player["ボーク"]),float(home_select_player["ボーク"])-float(away_select_player["ボーク"]),
                           float(away_select_player["失点"])-float(home_select_player["失点"]),float(home_select_player["失点"])-float(away_select_player["失点"]),
                           float(away_select_player["自責点"])-float(home_select_player["自責点"]),float(home_select_player["自責点"])-float(away_select_player["自責点"]),
                           float(away_select_player["防御率"]),float(home_select_player["防御率"]),
                           float(away_select_player["投球回"]),float(home_select_player["投球回"]),
                           float(away_select_player["勝率"]),float(home_select_player["勝率"]),
                           float(away_select_player["奪三振率"]),float(home_select_player["奪三振率"]),
                           float(away_select_player["被打率"]),float(home_select_player["被打率"]),
                           float(away_select_player["Ｋ／ＢＢ"]),float(home_select_player["Ｋ／ＢＢ"]),
                           float(away_select_player["ＷＨＩＰ"]),float(home_select_player["ＷＨＩＰ"]),]


    # numpy配列に変換
    ndarray_startingmember_data = np.array(startingmember_list)

    # データフレームの形に整形
    ndarray_startingmember_data_list = ndarray_startingmember_data.reshape(43,2)

    # データフレームに変換
    startingmember_df = pd.DataFrame(ndarray_startingmember_data_list)

    # カラムを指定
    startingmember_df = startingmember_df.rename(columns={0:"ホーム",1:"アウェー"},index={0:"平均打率",1:"安打差",2:"二塁打差",3:"三塁打差",4:"本塁打差",5:"塁打差",6:"得点差",7:"三振差",8:"四球差",9:"死球差",
                                                                                   10:"犠打差",11:"犠飛差",12:"盗塁差",13:"盗塁死差",14:"併殺打差",15:"平均出塁率",16:"平均長打率",17:"平均ＯＰＳ",18:"平均得点圏",
                                                                                   19:"登板差",20:"先発差",21:"完投差",22:"ＱＳ差",23:"勝利差",24:"敗戦差",25:"ホールド差",26:"セーブ差",27:"被安打差",
                                                                                   28:"被本塁打差",29:"奪三振差",30:"与四球差",31:"与死球差",32:"暴投差",33:"ボーク差",34:"失点差",35:"自責点差",36:"防御率",
                                                                                   37:"投球回",38:"勝率",39:"奪三振率",40:"被打率",41:"Ｋ／ＢＢ",42:"ＷＨＩＰ"})
    
    st.title("スターティングメンバー数値比較")
    startingmember_df = startingmember_df.transpose()
    st.write(startingmember_df)
    
    homepoint = st.text_input("ホームチームの得点入力")
    awaypoint = st.text_input("アウェーチームの得点入力")

    startingmember_df["point"] = [homepoint,awaypoint]

    st.write(startingmember_df)

    csv_button = st.button("CSVに書き出し")

    if csv_button == True:
        startingmember_df.to_csv(".\data\Data_collection\MLB_Point_ML_train.csv", mode='a', header=False)
