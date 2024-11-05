import pandas as pd
import numpy as np
import streamlit as st

# MLB全体打者データ
mlb_all_fielder_df = pd.read_csv(".\data\MLB-all-fielder\MLB_all_fielder.csv")

# データの中の'-'を0に変換
mlb_all_fielder_df = mlb_all_fielder_df.replace('-',0)

# 適切なタイプに変換
mlb_all_fielder_df_str = mlb_all_fielder_df[['Team','位置','背番号','選手名']]
mlb_all_fielder_df_float = mlb_all_fielder_df[['打率','出塁率','長打率','ＯＰＳ','得点圏']].astype(np.float64)
mlb_all_fielder_df_int = mlb_all_fielder_df[['試合','打席','打数','安打','二塁打','三塁打','本塁打','塁打','打点','得点','三振','四球','死球','犠打','犠飛','盗塁','盗塁死','併殺打']].astype(np.int64)

# データフレームを結合
mlb_all_fielder_df = pd.concat([mlb_all_fielder_df_str,mlb_all_fielder_df_int],axis=1)
mlb_all_fielder_df = pd.concat([mlb_all_fielder_df,mlb_all_fielder_df_float],axis=1)


# mlb_all_fielder_df = mlb_all_fielder_df.sort_values(['打率'],ascending=False)


# アメリカンリーグの打者データ
AL_all_fielder_df = pd.read_csv(".\data\AL&NL-fielder\AL_all_fielder.csv")

# データの中の'-'を0に変換
AL_all_fielder_df = AL_all_fielder_df.replace('-',0)

# 適切なタイプに変換
AL_all_fielder_df_str = AL_all_fielder_df[['Team','位置','背番号','選手名']]
AL_all_fielder_df_float = AL_all_fielder_df[['打率','出塁率','長打率','ＯＰＳ','得点圏']].astype(np.float64)
AL_all_fielder_df_int = AL_all_fielder_df[['試合','打席','打数','安打','二塁打','三塁打','本塁打','塁打','打点','得点','三振','四球','死球','犠打','犠飛','盗塁','盗塁死','併殺打']].astype(np.int64)

# データフレームを結合
AL_all_fielder_df = pd.concat([AL_all_fielder_df_str,AL_all_fielder_df_int],axis=1)
AL_all_fielder_df = pd.concat([AL_all_fielder_df,AL_all_fielder_df_float],axis=1)


# AL_all_fielder_df = AL_all_fielder_df.sort_values(['打率'],ascending=False)

# ナショナルリーグ全体打者データ
NL_all_fielder_df = pd.read_csv(r".\data\AL&NL-fielder\NL_all_fielder.csv")

# データの中の'-'を0に変換
NL_all_fielder_df = NL_all_fielder_df.replace('-',0)

# 適切なタイプに変換
NL_all_fielder_df_str = NL_all_fielder_df[['Team','位置','背番号','選手名']]
NL_all_fielder_df_float = NL_all_fielder_df[['打率','出塁率','長打率','ＯＰＳ','得点圏']].astype(np.float64)
NL_all_fielder_df_int = NL_all_fielder_df[['試合','打席','打数','安打','二塁打','三塁打','本塁打','塁打','打点','得点','三振','四球','死球','犠打','犠飛','盗塁','盗塁死','併殺打']].astype(np.int64)

# データフレームを結合
NL_all_fielder_df = pd.concat([NL_all_fielder_df_str,NL_all_fielder_df_int],axis=1)
NL_all_fielder_df = pd.concat([NL_all_fielder_df,NL_all_fielder_df_float],axis=1)


# MLB全投手データ
mlb_all_pitcher_df = pd.read_csv(".\data\MLB-all-pitcher\MLB_all_pitcher.csv")
# データの中の'-'を0に変換
mlb_all_pitcher_df = mlb_all_pitcher_df.replace('-',0)

# 適切なタイプに変換
mlb_all_pitcher_df_str = mlb_all_pitcher_df[['Team','背番号','選手名']]
mlb_all_pitcher_df_float = mlb_all_pitcher_df[['防御率','投球回','勝率','奪三振率','被打率','Ｋ／ＢＢ','ＷＨＩＰ']].astype(np.float64)
mlb_all_pitcher_df_int = mlb_all_pitcher_df[['登板', '先発', '完投', '完封', 'ＱＳ','勝利', '敗戦', 'ホールド', 'セーブ', '被安打', '被本塁打', '奪三振','与四球', '与死球', '暴投', 'ボーク', '失点', '自責点']].astype(np.int64)

# データフレームを結合
mlb_all_pitcher_df = pd.concat([mlb_all_pitcher_df_str,mlb_all_pitcher_df_int],axis=1)
mlb_all_pitcher_df = pd.concat([mlb_all_pitcher_df,mlb_all_pitcher_df_float],axis=1)


# AL投手データ
AL_all_pitcher_df = pd.read_csv(".\data\AL&NL-pitcher\AL_all_pitcher.csv")
# データの中の'-'を0に変換
AL_all_pitcher_df = AL_all_pitcher_df.replace('-',0)

# 適切なタイプに変換
AL_all_pitcher_df_str = AL_all_pitcher_df[['Team','背番号','選手名']]
AL_all_pitcher_df_float = AL_all_pitcher_df[['防御率','投球回','勝率','奪三振率','被打率','Ｋ／ＢＢ','ＷＨＩＰ']].astype(np.float64)
AL_all_pitcher_df_int = AL_all_pitcher_df[['登板', '先発', '完投', '完封', 'ＱＳ','勝利', '敗戦', 'ホールド', 'セーブ', '被安打', '被本塁打', '奪三振','与四球', '与死球', '暴投', 'ボーク', '失点', '自責点']].astype(np.int64)

# データフレームを結合
AL_all_pitcher_df = pd.concat([AL_all_pitcher_df_str,AL_all_pitcher_df_int],axis=1)
AL_all_pitcher_df = pd.concat([AL_all_pitcher_df,AL_all_pitcher_df_float],axis=1)


# NL全投手データ
NL_all_pitcher_df = pd.read_csv(r".\data\AL&NL-pitcher\NL_all_pitcher.csv")
# データの中の'-'を0に変換
NL_all_pitcher_df = NL_all_pitcher_df.replace('-',0)

# 適切なタイプに変換
NL_all_pitcher_df_str = NL_all_pitcher_df[['Team','背番号','選手名']]
NL_all_pitcher_df_float = NL_all_pitcher_df[['防御率','投球回','勝率','奪三振率','被打率','Ｋ／ＢＢ','ＷＨＩＰ']].astype(np.float64)
NL_all_pitcher_df_int = NL_all_pitcher_df[['登板', '先発', '完投', '完封', 'ＱＳ','勝利', '敗戦', 'ホールド', 'セーブ', '被安打', '被本塁打', '奪三振','与四球', '与死球', '暴投', 'ボーク', '失点', '自責点']].astype(np.int64)

# データフレームを結合
NL_all_pitcher_df = pd.concat([NL_all_pitcher_df_str,NL_all_pitcher_df_int],axis=1)
NL_all_pitcher_df = pd.concat([NL_all_pitcher_df,NL_all_pitcher_df_float],axis=1)



# MLBの全チームのデータ
MLB_all_team_df = pd.read_csv(".\data\MLB-team\MLB_team.csv")

# データの中の'-'を0に変換
MLB_all_team_df = MLB_all_team_df.replace('-',0)

# 適切なタイプに変換
MLB_all_team_df_str = MLB_all_team_df[['チーム']]
MLB_all_team_df_float = MLB_all_team_df[['勝率','ゲーム差','打率','防御率']].astype(np.float64)
MLB_all_team_df_rank = MLB_all_team_df['順位'].astype(np.int64)
MLB_all_team_df_int = MLB_all_team_df[['試合', '勝', '敗', '引分','得点', '失点', '本塁打', '盗塁', '打率', '防御率', '失策']].astype(np.int64)

# データフレームを結合
MLB_all_team_df_temp = pd.concat([MLB_all_team_df_rank,MLB_all_team_df_str],axis=1)
MLB_all_team_df_temp2 = pd.concat([MLB_all_team_df_float,MLB_all_team_df_int],axis=1)
MLB_all_team_df = pd.concat([MLB_all_team_df_temp,MLB_all_team_df_temp2],axis=1)

# 規定打席に達しているか計算する用
game_avg_batter = MLB_all_team_df['試合'].mean()

# 規定投球回に達しているか計算する用
game_avg_pitcher = MLB_all_team_df['試合'].mean()


# MLBのチームを地区ごとに分ける
AL_east_team_df = MLB_all_team_df[:5]
AL_central_team_df = MLB_all_team_df[5:10]
AL_west_team_df = MLB_all_team_df[10:15]
NL_east_team_df = MLB_all_team_df[15:20]
NL_central_team_df = MLB_all_team_df[20:25]
NL_west_team_df = MLB_all_team_df[25:30]

# 重複を削除するコード（これがないとエラー出る、よくわかってない）
AL_east_team_df = AL_east_team_df.loc[:, ~AL_east_team_df.columns.duplicated()]
AL_central_team_df = AL_central_team_df.loc[:, ~AL_central_team_df.columns.duplicated()]
AL_west_team_df = AL_west_team_df.loc[:, ~AL_west_team_df.columns.duplicated()]
NL_east_team_df = NL_east_team_df.loc[:, ~NL_east_team_df.columns.duplicated()]
NL_central_team_df = NL_central_team_df.loc[:, ~NL_central_team_df.columns.duplicated()]
NL_west_team_df = NL_west_team_df.loc[:, ~NL_west_team_df.columns.duplicated()]

# ワイルドカード順位を出力する
# ア・リーグ
AL_wildcard = pd.concat([MLB_all_team_df[1:5],MLB_all_team_df[6:10]])
AL_wildcard = pd.concat([MLB_all_team_df[11:15],AL_wildcard])
AL_wildcard = AL_wildcard.loc[:, ~AL_wildcard.columns.duplicated()]
AL_wildcard = AL_wildcard.sort_values(['勝率'],ascending=False)

# ナ・リーグ
NL_wildcard = pd.concat([MLB_all_team_df[16:20],MLB_all_team_df[21:25]])
NL_wildcard = pd.concat([MLB_all_team_df[26:30],NL_wildcard])
NL_wildcard = NL_wildcard.loc[:, ~NL_wildcard.columns.duplicated()]
NL_wildcard = NL_wildcard.sort_values(['勝率'],ascending=False)

# ポストシーズン出場チームを出力
# ア・リーグ
# リーグリーダー
AL_league_leader = pd.concat([MLB_all_team_df[0:1],MLB_all_team_df[5:6]])
AL_league_leader = pd.concat([AL_league_leader,MLB_all_team_df[10:11]])
AL_league_leader = AL_league_leader.loc[:, ~AL_league_leader.columns.duplicated()]
# ワイルドカードTOP3
AL_wildcard_top3 = AL_wildcard[0:3]

# ナ・リーグ
# リーグリーダー
NL_league_leader = pd.concat([MLB_all_team_df[15:16],MLB_all_team_df[20:21]])
NL_league_leader = pd.concat([NL_league_leader,MLB_all_team_df[25:26]])
NL_league_leader = NL_league_leader.loc[:, ~NL_league_leader.columns.duplicated()]
# ワイルドカードTOP3
NL_wildcard_top3 = NL_wildcard[0:3]



# アプリ部分
# タイトル
st.title("MLBチーム成績")
team_option = st.selectbox('チームのデータ選択',['アメリカンリーグ','ナショナルリーグ','アメリカンリーグワイルドカード順位','ナショナルリーグワイルドカード順位','ポストシーズン出場チーム'])
# チーム成績選択
if team_option == 'アメリカンリーグ':
    st.write("東地区")
    st.write(AL_east_team_df)
    st.write("中地区")
    st.write(AL_central_team_df)
    st.write("西地区")
    st.write(AL_west_team_df)

elif team_option == 'ナショナルリーグ':
    st.write("東地区")
    st.write(NL_east_team_df)
    st.write("中地区")
    st.write(NL_central_team_df)
    st.write("西地区")
    st.write(NL_west_team_df)

elif team_option == 'アメリカンリーグワイルドカード順位':
    st.write(AL_wildcard.drop(['順位','ゲーム差'],axis=1))
elif team_option == 'ナショナルリーグワイルドカード順位':
    st.write(NL_wildcard.drop(['順位','ゲーム差'],axis=1))
elif team_option == 'ポストシーズン出場チーム':
    st.write("アメリカンリーグ")
    st.write("ディヴィジョン優勝チーム")
    st.write(AL_league_leader.drop(['順位','ゲーム差'],axis=1))
    st.write("ワイルドカード上位3チーム")
    st.write(AL_wildcard_top3.drop(['順位','ゲーム差'],axis=1))

    st.write("ナショナルリーグ")
    st.write("ディヴィジョン優勝チーム")
    st.write(NL_league_leader.drop(['順位','ゲーム差'],axis=1))
    st.write("ワイルドカード上位3チーム")
    st.write(NL_wildcard_top3.drop(['順位','ゲーム差'],axis=1))


# タイトル
st.title("MLB打者個人成績")

# リーグ選択
league_option = st.selectbox('打者のリーグ選択',['MLB全体','アメリカンリーグ','ナショナルリーグ'])

# 個人成績選択
# optionはどの個人成績を見るか選択する変数
if league_option == 'MLB全体':
    option = st.selectbox('個人成績',['打率','出塁率','長打率','ＯＰＳ','得点圏','試合','打席','打数','安打','二塁打','三塁打','本塁打','塁打','打点','得点','三振','四球','死球','犠打','犠飛','盗塁','盗塁死','併殺打'])
    if option == '打率':
        mlb_all_fielder_df_sort = mlb_all_fielder_df.sort_values(['打率'],ascending=False)
        mlb_all_fielder_df_sort = mlb_all_fielder_df_sort[mlb_all_fielder_df_sort['打席'] > int(game_avg_batter)*3.1]
        st.write(mlb_all_fielder_df_sort[['Team','選手名','打率']].head(10))
    elif option == '出塁率':
        mlb_all_fielder_df_sort = mlb_all_fielder_df.sort_values(['出塁率'],ascending=False)
        mlb_all_fielder_df_sort = mlb_all_fielder_df_sort[mlb_all_fielder_df_sort['打席'] > int(game_avg_batter)*3.1]
        st.write(mlb_all_fielder_df_sort[['Team','選手名','出塁率']].head(10))
    elif option == '長打率':
        mlb_all_fielder_df_sort = mlb_all_fielder_df.sort_values(['長打率'],ascending=False)
        mlb_all_fielder_df_sort = mlb_all_fielder_df_sort[mlb_all_fielder_df_sort['打席'] > int(game_avg_batter)*3.1]
        st.write(mlb_all_fielder_df_sort[['Team','選手名','長打率']].head(10))
    elif option == 'ＯＰＳ':
        st.write("OPSは出塁率と長打率の合計")
        mlb_all_fielder_df_sort = mlb_all_fielder_df.sort_values(['ＯＰＳ'],ascending=False)
        mlb_all_fielder_df_sort = mlb_all_fielder_df_sort[mlb_all_fielder_df_sort['打席'] > int(game_avg_batter)*3.1]
        st.write(mlb_all_fielder_df_sort[['Team','選手名','ＯＰＳ']].head(10))
    elif option == '得点圏':
        mlb_all_fielder_df_sort = mlb_all_fielder_df.sort_values(['得点圏'],ascending=False)
        mlb_all_fielder_df_sort = mlb_all_fielder_df_sort[mlb_all_fielder_df_sort['打席'] > int(game_avg_batter)*3.1]
        st.write(mlb_all_fielder_df_sort[['Team','選手名','得点圏']].head(10))
    elif option == '試合':
        mlb_all_fielder_df_sort = mlb_all_fielder_df.sort_values(['試合'],ascending=False)
        st.write(mlb_all_fielder_df_sort[['Team','選手名','試合']].head(10))
    elif option == '打席':
        mlb_all_fielder_df_sort = mlb_all_fielder_df.sort_values(['打席'],ascending=False)
        st.write(mlb_all_fielder_df_sort[['Team','選手名','打席']].head(10))
    elif option == '打数':
        mlb_all_fielder_df_sort = mlb_all_fielder_df.sort_values(['打数'],ascending=False)
        st.write(mlb_all_fielder_df_sort[['Team','選手名','打数']].head(10))
    elif option == '安打':
        mlb_all_fielder_df_sort = mlb_all_fielder_df.sort_values(['安打'],ascending=False)
        st.write(mlb_all_fielder_df_sort[['Team','選手名','安打']].head(10))
    elif option == '二塁打':
        mlb_all_fielder_df_sort = mlb_all_fielder_df.sort_values(['二塁打'],ascending=False)
        st.write(mlb_all_fielder_df_sort[['Team','選手名','二塁打']].head(10))
    elif option == '三塁打':
        mlb_all_fielder_df_sort = mlb_all_fielder_df.sort_values(['三塁打'],ascending=False)
        st.write(mlb_all_fielder_df_sort[['Team','選手名','三塁打']].head(10))
    elif option == '本塁打':
        mlb_all_fielder_df_sort = mlb_all_fielder_df.sort_values(['本塁打'],ascending=False)
        st.write(mlb_all_fielder_df_sort[['Team','選手名','本塁打']].head(10))
    elif option == '塁打':
        mlb_all_fielder_df_sort = mlb_all_fielder_df.sort_values(['塁打'],ascending=False)
        st.write(mlb_all_fielder_df_sort[['Team','選手名','塁打']].head(10))
    elif option == '打点':
        mlb_all_fielder_df_sort = mlb_all_fielder_df.sort_values(['打点'],ascending=False)
        st.write(mlb_all_fielder_df_sort[['Team','選手名','打点']].head(10))
    elif option == '得点':
        mlb_all_fielder_df_sort = mlb_all_fielder_df.sort_values(['得点'],ascending=False)
        st.write(mlb_all_fielder_df_sort[['Team','選手名','得点']].head(10))
    elif option == '三振':
        mlb_all_fielder_df_sort = mlb_all_fielder_df.sort_values(['三振'],ascending=False)
        st.write(mlb_all_fielder_df_sort[['Team','選手名','三振']].head(10))
    elif option == '四球':
        mlb_all_fielder_df_sort = mlb_all_fielder_df.sort_values(['四球'],ascending=False)
        st.write(mlb_all_fielder_df_sort[['Team','選手名','四球']].head(10))
    elif option == '死球':
        mlb_all_fielder_df_sort = mlb_all_fielder_df.sort_values(['死球'],ascending=False)
        st.write(mlb_all_fielder_df_sort[['Team','選手名','死球']].head(10))
    elif option == '犠打':
        mlb_all_fielder_df_sort = mlb_all_fielder_df.sort_values(['犠打'],ascending=False)
        st.write(mlb_all_fielder_df_sort[['Team','選手名','犠打']].head(10))
    elif option == '犠飛':
        mlb_all_fielder_df_sort = mlb_all_fielder_df.sort_values(['犠飛'],ascending=False)
        st.write(mlb_all_fielder_df_sort[['Team','選手名','犠飛']].head(10))
    elif option == '盗塁':
        mlb_all_fielder_df_sort = mlb_all_fielder_df.sort_values(['盗塁'],ascending=False)
        st.write(mlb_all_fielder_df_sort[['Team','選手名','盗塁']].head(10))
    elif option == '盗塁死':
        mlb_all_fielder_df_sort = mlb_all_fielder_df.sort_values(['盗塁死'],ascending=False)
        st.write(mlb_all_fielder_df_sort[['Team','選手名','盗塁死']].head(10))
    elif option == '併殺打':
        mlb_all_fielder_df_sort = mlb_all_fielder_df.sort_values(['併殺打'],ascending=False)
        st.write(mlb_all_fielder_df_sort[['Team','選手名','併殺打']].head(10))

elif league_option == 'アメリカンリーグ':
    option = st.selectbox('個人成績',['打率','出塁率','長打率','ＯＰＳ','得点圏','試合','打席','打数','安打','二塁打','三塁打','本塁打','塁打','打点','得点','三振','四球','死球','犠打','犠飛','盗塁','盗塁死','併殺打'])
    if option == '打率':
        AL_all_fielder_df_sort = AL_all_fielder_df.sort_values(['打率'],ascending=False)
        AL_all_fielder_df_sort = AL_all_fielder_df_sort[AL_all_fielder_df_sort['打席'] > int(game_avg_batter)*3.1]
        st.write(AL_all_fielder_df_sort[['Team','選手名','打率']].head(10))
    elif option == '出塁率':
        AL_all_fielder_df_sort = AL_all_fielder_df.sort_values(['出塁率'],ascending=False)
        AL_all_fielder_df_sort = AL_all_fielder_df_sort[AL_all_fielder_df_sort['打席'] > int(game_avg_batter)*3.1]
        st.write(AL_all_fielder_df_sort[['Team','選手名','出塁率']].head(10))
    elif option == '長打率':
        AL_all_fielder_df_sort = AL_all_fielder_df.sort_values(['長打率'],ascending=False)
        AL_all_fielder_df_sort = AL_all_fielder_df_sort[AL_all_fielder_df_sort['打席'] > int(game_avg_batter)*3.1]
        st.write(AL_all_fielder_df_sort[['Team','選手名','長打率']].head(10))
    elif option == 'ＯＰＳ':
        st.write("OPSは出塁率と長打率の合計")
        AL_all_fielder_df_sort = AL_all_fielder_df.sort_values(['ＯＰＳ'],ascending=False)
        AL_all_fielder_df_sort = AL_all_fielder_df_sort[AL_all_fielder_df_sort['打席'] > int(game_avg_batter)*3.1]
        st.write(AL_all_fielder_df_sort[['Team','選手名','ＯＰＳ']].head(10))
    elif option == '得点圏':
        AL_all_fielder_df_sort = AL_all_fielder_df.sort_values(['得点圏'],ascending=False)
        AL_all_fielder_df_sort = AL_all_fielder_df_sort[AL_all_fielder_df_sort['打席'] > int(game_avg_batter)*3.1]
        st.write(AL_all_fielder_df_sort[['Team','選手名','得点圏']].head(10))
    elif option == '試合':
        AL_all_fielder_df_sort = AL_all_fielder_df.sort_values(['試合'],ascending=False)
        st.write(AL_all_fielder_df_sort[['Team','選手名','試合']].head(10))
    elif option == '打席':
        AL_all_fielder_df_sort = AL_all_fielder_df.sort_values(['打席'],ascending=False)
        st.write(AL_all_fielder_df_sort[['Team','選手名','打席']].head(10))
    elif option == '打数':
        AL_all_fielder_df_sort = AL_all_fielder_df.sort_values(['打数'],ascending=False)
        st.write(AL_all_fielder_df_sort[['Team','選手名','打数']].head(10))
    elif option == '安打':
        AL_all_fielder_df_sort = AL_all_fielder_df.sort_values(['安打'],ascending=False)
        st.write(AL_all_fielder_df_sort[['Team','選手名','安打']].head(10))
    elif option == '二塁打':
        AL_all_fielder_df_sort = AL_all_fielder_df.sort_values(['二塁打'],ascending=False)
        st.write(AL_all_fielder_df_sort[['Team','選手名','二塁打']].head(10))
    elif option == '三塁打':
        AL_all_fielder_df_sort = AL_all_fielder_df.sort_values(['三塁打'],ascending=False)
        st.write(AL_all_fielder_df_sort[['Team','選手名','三塁打']].head(10))
    elif option == '本塁打':
        AL_all_fielder_df_sort = AL_all_fielder_df.sort_values(['本塁打'],ascending=False)
        st.write(AL_all_fielder_df_sort[['Team','選手名','本塁打']].head(10))
    elif option == '塁打':
        AL_all_fielder_df_sort = AL_all_fielder_df.sort_values(['塁打'],ascending=False)
        st.write(AL_all_fielder_df_sort[['Team','選手名','塁打']].head(10))
    elif option == '打点':
        AL_all_fielder_df_sort = AL_all_fielder_df.sort_values(['打点'],ascending=False)
        st.write(AL_all_fielder_df_sort[['Team','選手名','打点']].head(10))
    elif option == '得点':
        AL_all_fielder_df_sort = AL_all_fielder_df.sort_values(['得点'],ascending=False)
        st.write(AL_all_fielder_df_sort[['Team','選手名','得点']].head(10))
    elif option == '三振':
        AL_all_fielder_df_sort = AL_all_fielder_df.sort_values(['三振'],ascending=False)
        st.write(AL_all_fielder_df_sort[['Team','選手名','三振']].head(10))
    elif option == '四球':
        AL_all_fielder_df_sort = AL_all_fielder_df.sort_values(['四球'],ascending=False)
        st.write(AL_all_fielder_df_sort[['Team','選手名','四球']].head(10))
    elif option == '死球':
        AL_all_fielder_df_sort = AL_all_fielder_df.sort_values(['死球'],ascending=False)
        st.write(AL_all_fielder_df_sort[['Team','選手名','死球']].head(10))
    elif option == '犠打':
        AL_all_fielder_df_sort = AL_all_fielder_df.sort_values(['犠打'],ascending=False)
        st.write(AL_all_fielder_df_sort[['Team','選手名','犠打']].head(10))
    elif option == '犠飛':
        AL_all_fielder_df_sort = AL_all_fielder_df.sort_values(['犠飛'],ascending=False)
        st.write(AL_all_fielder_df_sort[['Team','選手名','犠飛']].head(10))
    elif option == '盗塁':
        AL_all_fielder_df_sort = AL_all_fielder_df.sort_values(['盗塁'],ascending=False)
        st.write(AL_all_fielder_df_sort[['Team','選手名','盗塁']].head(10))
    elif option == '盗塁死':
        AL_all_fielder_df_sort = AL_all_fielder_df.sort_values(['盗塁死'],ascending=False)
        st.write(AL_all_fielder_df_sort[['Team','選手名','盗塁死']].head(10))
    elif option == '併殺打':
        AL_all_fielder_df_sort = AL_all_fielder_df.sort_values(['併殺打'],ascending=False)
        st.write(AL_all_fielder_df_sort[['Team','選手名','併殺打']].head(10))


elif league_option == 'ナショナルリーグ':
    option = st.selectbox('個人成績',['打率','出塁率','長打率','ＯＰＳ','得点圏','試合','打席','打数','安打','二塁打','三塁打','本塁打','塁打','打点','得点','三振','四球','死球','犠打','犠飛','盗塁','盗塁死','併殺打'])
    if option == '打率':
        NL_all_fielder_df_sort = NL_all_fielder_df.sort_values(['打率'],ascending=False)
        NL_all_fielder_df_sort = NL_all_fielder_df_sort[NL_all_fielder_df_sort['打席'] > int(game_avg_batter)*3.1]
        st.write(NL_all_fielder_df_sort[['Team','選手名','打率']].head(10))
    elif option == '出塁率':
        NL_all_fielder_df_sort = NL_all_fielder_df.sort_values(['出塁率'],ascending=False)
        NL_all_fielder_df_sort = NL_all_fielder_df_sort[NL_all_fielder_df_sort['打席'] > int(game_avg_batter)*3.1]
        st.write(NL_all_fielder_df_sort[['Team','選手名','出塁率']].head(10))
    elif option == '長打率':
        NL_all_fielder_df_sort = NL_all_fielder_df.sort_values(['長打率'],ascending=False)
        NL_all_fielder_df_sort = NL_all_fielder_df_sort[NL_all_fielder_df_sort['打席'] > int(game_avg_batter)*3.1]
        st.write(NL_all_fielder_df_sort[['Team','選手名','長打率']].head(10))
    elif option == 'ＯＰＳ':
        st.write("OPSは出塁率と長打率の合計")
        NL_all_fielder_df_sort = NL_all_fielder_df.sort_values(['ＯＰＳ'],ascending=False)
        NL_all_fielder_df_sort = NL_all_fielder_df_sort[NL_all_fielder_df_sort['打席'] > int(game_avg_batter)*3.1]
        st.write(NL_all_fielder_df_sort[['Team','選手名','ＯＰＳ']].head(10))
    elif option == '得点圏':
        NL_all_fielder_df_sort = NL_all_fielder_df.sort_values(['得点圏'],ascending=False)
        NL_all_fielder_df_sort = NL_all_fielder_df_sort[NL_all_fielder_df_sort['打席'] > int(game_avg_batter)*3.1]
        st.write(NL_all_fielder_df_sort[['Team','選手名','得点圏']].head(10))
    elif option == '試合':
        NL_all_fielder_df_sort = NL_all_fielder_df.sort_values(['試合'],ascending=False)
        st.write(NL_all_fielder_df_sort[['Team','選手名','試合']].head(10))
    elif option == '打席':
        NL_all_fielder_df_sort = NL_all_fielder_df.sort_values(['打席'],ascending=False)
        st.write(NL_all_fielder_df_sort[['Team','選手名','打席']].head(10))
    elif option == '打数':
        NL_all_fielder_df_sort = NL_all_fielder_df.sort_values(['打数'],ascending=False)
        st.write(NL_all_fielder_df_sort[['Team','選手名','打数']].head(10))
    elif option == '安打':
        NL_all_fielder_df_sort = NL_all_fielder_df.sort_values(['安打'],ascending=False)
        st.write(NL_all_fielder_df_sort[['Team','選手名','安打']].head(10))
    elif option == '二塁打':
        NL_all_fielder_df_sort = NL_all_fielder_df.sort_values(['二塁打'],ascending=False)
        st.write(NL_all_fielder_df_sort[['Team','選手名','二塁打']].head(10))
    elif option == '三塁打':
        NL_all_fielder_df_sort = NL_all_fielder_df.sort_values(['三塁打'],ascending=False)
        st.write(NL_all_fielder_df_sort[['Team','選手名','三塁打']].head(10))
    elif option == '本塁打':
        NL_all_fielder_df_sort = NL_all_fielder_df.sort_values(['本塁打'],ascending=False)
        st.write(NL_all_fielder_df_sort[['Team','選手名','本塁打']].head(10))
    elif option == '塁打':
        NL_all_fielder_df_sort = NL_all_fielder_df.sort_values(['塁打'],ascending=False)
        st.write(NL_all_fielder_df_sort[['Team','選手名','塁打']].head(10))
    elif option == '打点':
        NL_all_fielder_df_sort = NL_all_fielder_df.sort_values(['打点'],ascending=False)
        st.write(NL_all_fielder_df_sort[['Team','選手名','打点']].head(10))
    elif option == '得点':
        NL_all_fielder_df_sort = NL_all_fielder_df.sort_values(['得点'],ascending=False)
        st.write(NL_all_fielder_df_sort[['Team','選手名','得点']].head(10))
    elif option == '三振':
        NL_all_fielder_df_sort = NL_all_fielder_df.sort_values(['三振'],ascending=False)
        st.write(NL_all_fielder_df_sort[['Team','選手名','三振']].head(10))
    elif option == '四球':
        NL_all_fielder_df_sort = NL_all_fielder_df.sort_values(['四球'],ascending=False)
        st.write(NL_all_fielder_df_sort[['Team','選手名','四球']].head(10))
    elif option == '死球':
        NL_all_fielder_df_sort = NL_all_fielder_df.sort_values(['死球'],ascending=False)
        st.write(NL_all_fielder_df_sort[['Team','選手名','死球']].head(10))
    elif option == '犠打':
        NL_all_fielder_df_sort = NL_all_fielder_df.sort_values(['犠打'],ascending=False)
        st.write(NL_all_fielder_df_sort[['Team','選手名','犠打']].head(10))
    elif option == '犠飛':
        NL_all_fielder_df_sort = NL_all_fielder_df.sort_values(['犠飛'],ascending=False)
        st.write(NL_all_fielder_df_sort[['Team','選手名','犠飛']].head(10))
    elif option == '盗塁':
        NL_all_fielder_df_sort = NL_all_fielder_df.sort_values(['盗塁'],ascending=False)
        st.write(NL_all_fielder_df_sort[['Team','選手名','盗塁']].head(10))
    elif option == '盗塁死':
        NL_all_fielder_df_sort = NL_all_fielder_df.sort_values(['盗塁死'],ascending=False)
        st.write(NL_all_fielder_df_sort[['Team','選手名','盗塁死']].head(10))
    elif option == '併殺打':
        NL_all_fielder_df_sort = NL_all_fielder_df.sort_values(['併殺打'],ascending=False)
        st.write(NL_all_fielder_df_sort[['Team','選手名','併殺打']].head(10))




# タイトル
st.title('MLB投手個人成績')

# リーグ選択
league_option = st.selectbox('投手のリーグ選択',['MLB全体','アメリカンリーグ','ナショナルリーグ'])

# 個人成績選択
# optionはどの個人成績を見るか選択する変数
if league_option == 'MLB全体':
    option = st.selectbox('個人成績',['防御率','投球回','勝率','奪三振率','被打率','Ｋ／ＢＢ','ＷＨＩＰ','登板', '先発', '完投', '完封', 'ＱＳ','勝利', '敗戦', 'ホールド', 'セーブ', '被安打', '被本塁打', '奪三振','与四球', '与死球', '暴投', 'ボーク', '失点', '自責点'])
    if option == '防御率':
        mlb_all_pitcher_df_sort = mlb_all_pitcher_df.sort_values(['防御率'])
        mlb_all_pitcher_df_sort = mlb_all_pitcher_df_sort[mlb_all_pitcher_df_sort['投球回'] > int(game_avg_pitcher)]
        st.write(mlb_all_pitcher_df_sort[['Team','選手名','防御率']].head(10))
    elif option == '投球回':
        mlb_all_pitcher_df_sort = mlb_all_pitcher_df.sort_values(['投球回'],ascending=False)
        st.write(mlb_all_pitcher_df_sort[['Team','選手名','投球回']].head(10))
    elif option == '勝率':
        mlb_all_pitcher_df_sort = mlb_all_pitcher_df.sort_values(['勝率'],ascending=False)
        mlb_all_pitcher_df_sort = mlb_all_pitcher_df_sort[mlb_all_pitcher_df_sort['投球回'] > int(game_avg_pitcher)]
        st.write(mlb_all_pitcher_df_sort[['Team','選手名','勝率']].head(10))
    elif option == '奪三振率':
        mlb_all_pitcher_df_sort = mlb_all_pitcher_df.sort_values(['奪三振率'],ascending=False)
        mlb_all_pitcher_df_sort = mlb_all_pitcher_df_sort[mlb_all_pitcher_df_sort['投球回'] > int(game_avg_pitcher)]
        st.write(mlb_all_pitcher_df_sort[['Team','選手名','奪三振率']].head(10))
    elif option == '被打率':
        mlb_all_pitcher_df_sort = mlb_all_pitcher_df.sort_values(['被打率'])
        mlb_all_pitcher_df_sort = mlb_all_pitcher_df_sort[mlb_all_pitcher_df_sort['投球回'] > int(game_avg_pitcher)]
        st.write(mlb_all_pitcher_df_sort[['Team','選手名','被打率']].head(10))
    elif option == 'Ｋ／ＢＢ':
        st.write("K/BBは奪三振と与四球の比率、投手の制球力を示す指標")
        mlb_all_pitcher_df_sort = mlb_all_pitcher_df.sort_values(['Ｋ／ＢＢ'],ascending=False)
        mlb_all_pitcher_df_sort = mlb_all_pitcher_df_sort[mlb_all_pitcher_df_sort['投球回'] > int(game_avg_pitcher)]
        st.write(mlb_all_pitcher_df_sort[['Team','選手名','Ｋ／ＢＢ']].head(10))
    elif option == 'ＷＨＩＰ':
        st.write("WHIPは1投球回あたり何人の走者(与四球と被安打)を出したかを表す数値")
        mlb_all_pitcher_df_sort = mlb_all_pitcher_df.sort_values(['ＷＨＩＰ'])
        mlb_all_pitcher_df_sort = mlb_all_pitcher_df_sort[mlb_all_pitcher_df_sort['投球回'] > int(game_avg_pitcher)]
        st.write(mlb_all_pitcher_df_sort[['Team','選手名','ＷＨＩＰ']].head(10))
    elif option == '登板':
        mlb_all_pitcher_df_sort = mlb_all_pitcher_df.sort_values(['登板'],ascending=False)
        st.write(mlb_all_pitcher_df_sort[['Team','選手名','登板']].head(10))
    elif option == '先発':
        mlb_all_pitcher_df_sort = mlb_all_pitcher_df.sort_values(['先発'],ascending=False)
        st.write(mlb_all_pitcher_df_sort[['Team','選手名','先発']].head(10))
    elif option == '完投':
        mlb_all_pitcher_df_sort = mlb_all_pitcher_df.sort_values(['完投'],ascending=False)
        st.write(mlb_all_pitcher_df_sort[['Team','選手名','完投']].head(10))
    elif option == '完封':
        mlb_all_pitcher_df_sort = mlb_all_pitcher_df.sort_values(['完封'],ascending=False)
        st.write(mlb_all_pitcher_df_sort[['Team','選手名','完封']].head(10))
    elif option == 'ＱＳ':
        mlb_all_pitcher_df_sort = mlb_all_pitcher_df.sort_values(['ＱＳ'],ascending=False)
        st.write(mlb_all_pitcher_df_sort[['Team','選手名','ＱＳ']].head(10))
    elif option == '勝利':
        mlb_all_pitcher_df_sort = mlb_all_pitcher_df.sort_values(['勝利'],ascending=False)
        st.write(mlb_all_pitcher_df_sort[['Team','選手名','勝利']].head(10))
    elif option == '敗戦':
        mlb_all_pitcher_df_sort = mlb_all_pitcher_df.sort_values(['敗戦'],ascending=False)
        st.write(mlb_all_pitcher_df_sort[['Team','選手名','敗戦']].head(10))
    elif option == 'ホールド':
        mlb_all_pitcher_df_sort = mlb_all_pitcher_df.sort_values(['ホールド'],ascending=False)
        st.write(mlb_all_pitcher_df_sort[['Team','選手名','ホールド']].head(10))
    elif option == 'セーブ':
        mlb_all_pitcher_df_sort = mlb_all_pitcher_df.sort_values(['セーブ'],ascending=False)
        st.write(mlb_all_pitcher_df_sort[['Team','選手名','セーブ']].head(10))
    elif option == '被安打':
        mlb_all_pitcher_df_sort = mlb_all_pitcher_df.sort_values(['被安打'],ascending=False)
        st.write(mlb_all_pitcher_df_sort[['Team','選手名','被安打']].head(10))
    elif option == '被本塁打':
        mlb_all_pitcher_df_sort = mlb_all_pitcher_df.sort_values(['被本塁打'],ascending=False)
        st.write(mlb_all_pitcher_df_sort[['Team','選手名','被本塁打']].head(10))
    elif option == '奪三振':
        mlb_all_pitcher_df_sort = mlb_all_pitcher_df.sort_values(['奪三振'],ascending=False)
        st.write(mlb_all_pitcher_df_sort[['Team','選手名','奪三振']].head(10))
    elif option == '与四球':
        mlb_all_pitcher_df_sort = mlb_all_pitcher_df.sort_values(['与四球'],ascending=False)
        st.write(mlb_all_pitcher_df_sort[['Team','選手名','与四球']].head(10))
    elif option == '与死球':
        mlb_all_pitcher_df_sort = mlb_all_pitcher_df.sort_values(['与死球'],ascending=False)
        st.write(mlb_all_pitcher_df_sort[['Team','選手名','与死球']].head(10))
    elif option == '暴投':
        mlb_all_pitcher_df_sort = mlb_all_pitcher_df.sort_values(['暴投'],ascending=False)
        st.write(mlb_all_pitcher_df_sort[['Team','選手名','暴投']].head(10))
    elif option == 'ボーク':
        mlb_all_pitcher_df_sort = mlb_all_pitcher_df.sort_values(['ボーク'],ascending=False)
        st.write(mlb_all_pitcher_df_sort[['Team','選手名','ボーク']].head(10))
    elif option == '失点':
        mlb_all_pitcher_df_sort = mlb_all_pitcher_df.sort_values(['失点'],ascending=False)
        st.write(mlb_all_pitcher_df_sort[['Team','選手名','失点']].head(10))
    elif option == '自責点':
        mlb_all_pitcher_df_sort = mlb_all_pitcher_df.sort_values(['自責点'],ascending=False)
        st.write(mlb_all_pitcher_df_sort[['Team','選手名','自責点']].head(10))

elif league_option == 'アメリカンリーグ':
    option = st.selectbox('個人成績',['防御率','投球回','勝率','奪三振率','被打率','Ｋ／ＢＢ','ＷＨＩＰ','登板', '先発', '完投', '完封', 'ＱＳ','勝利', '敗戦', 'ホールド', 'セーブ', '被安打', '被本塁打', '奪三振','与四球', '与死球', '暴投', 'ボーク', '失点', '自責点'])
    if option == '防御率':
        AL_all_pitcher_df_sort = AL_all_pitcher_df.sort_values(['防御率'])
        AL_all_pitcher_df_sort = AL_all_pitcher_df_sort[AL_all_pitcher_df_sort['投球回'] > int(game_avg_pitcher)]
        st.write(AL_all_pitcher_df_sort[['Team','選手名','防御率']].head(10))
    elif option == '投球回':
        AL_all_pitcher_df_sort = AL_all_pitcher_df.sort_values(['投球回'],ascending=False)
        st.write(AL_all_pitcher_df_sort[['Team','選手名','投球回']].head(10))
    elif option == '勝率':
        AL_all_pitcher_df_sort = AL_all_pitcher_df.sort_values(['勝率'],ascending=False)
        AL_all_pitcher_df_sort = AL_all_pitcher_df_sort[AL_all_pitcher_df_sort['投球回'] > int(game_avg_pitcher)]
        st.write(AL_all_pitcher_df_sort[['Team','選手名','勝率']].head(10))
    elif option == '奪三振率':
        AL_all_pitcher_df_sort = AL_all_pitcher_df.sort_values(['奪三振率'],ascending=False)
        AL_all_pitcher_df_sort = AL_all_pitcher_df_sort[AL_all_pitcher_df_sort['投球回'] > int(game_avg_pitcher)]
        st.write(AL_all_pitcher_df_sort[['Team','選手名','奪三振率']].head(10))
    elif option == '被打率':
        AL_all_pitcher_df_sort = AL_all_pitcher_df.sort_values(['被打率'])
        AL_all_pitcher_df_sort = AL_all_pitcher_df_sort[AL_all_pitcher_df_sort['投球回'] > int(game_avg_pitcher)]
        st.write(AL_all_pitcher_df_sort[['Team','選手名','被打率']].head(10))
    elif option == 'Ｋ／ＢＢ':
        st.write("K/BBは奪三振と与四球の比率、投手の制球力を示す指標")
        AL_all_pitcher_df_sort = AL_all_pitcher_df.sort_values(['Ｋ／ＢＢ'],ascending=False)
        AL_all_pitcher_df_sort = AL_all_pitcher_df_sort[AL_all_pitcher_df_sort['投球回'] > int(game_avg_pitcher)]
        st.write(AL_all_pitcher_df_sort[['Team','選手名','Ｋ／ＢＢ']].head(10))
    elif option == 'ＷＨＩＰ':
        st.write("WHIPは1投球回あたり何人の走者(与四球と被安打)を出したかを表す数値")
        AL_all_pitcher_df_sort = AL_all_pitcher_df.sort_values(['ＷＨＩＰ'])
        AL_all_pitcher_df_sort = AL_all_pitcher_df_sort[AL_all_pitcher_df_sort['投球回'] > int(game_avg_pitcher)]
        st.write(AL_all_pitcher_df_sort[['Team','選手名','ＷＨＩＰ']].head(10))
    elif option == '登板':
        AL_all_pitcher_df_sort = AL_all_pitcher_df.sort_values(['登板'],ascending=False)
        st.write(AL_all_pitcher_df_sort[['Team','選手名','登板']].head(10))
    elif option == '先発':
        AL_all_pitcher_df_sort = AL_all_pitcher_df.sort_values(['先発'],ascending=False)
        st.write(AL_all_pitcher_df_sort[['Team','選手名','先発']].head(10))
    elif option == '完投':
        AL_all_pitcher_df_sort = AL_all_pitcher_df.sort_values(['完投'],ascending=False)
        st.write(AL_all_pitcher_df_sort[['Team','選手名','完投']].head(10))
    elif option == '完封':
        AL_all_pitcher_df_sort = AL_all_pitcher_df.sort_values(['完封'],ascending=False)
        st.write(AL_all_pitcher_df_sort[['Team','選手名','完封']].head(10))
    elif option == 'ＱＳ':
        AL_all_pitcher_df_sort = AL_all_pitcher_df.sort_values(['ＱＳ'],ascending=False)
        st.write(AL_all_pitcher_df_sort[['Team','選手名','ＱＳ']].head(10))
    elif option == '勝利':
        AL_all_pitcher_df_sort = AL_all_pitcher_df.sort_values(['勝利'],ascending=False)
        st.write(AL_all_pitcher_df_sort[['Team','選手名','勝利']].head(10))
    elif option == '敗戦':
        AL_all_pitcher_df_sort = AL_all_pitcher_df.sort_values(['敗戦'],ascending=False)
        st.write(AL_all_pitcher_df_sort[['Team','選手名','敗戦']].head(10))
    elif option == 'ホールド':
        AL_all_pitcher_df_sort = AL_all_pitcher_df.sort_values(['ホールド'],ascending=False)
        st.write(AL_all_pitcher_df_sort[['Team','選手名','ホールド']].head(10))
    elif option == 'セーブ':
        AL_all_pitcher_df_sort = AL_all_pitcher_df.sort_values(['セーブ'],ascending=False)
        st.write(AL_all_pitcher_df_sort[['Team','選手名','セーブ']].head(10))
    elif option == '被安打':
        AL_all_pitcher_df_sort = AL_all_pitcher_df.sort_values(['被安打'],ascending=False)
        st.write(AL_all_pitcher_df_sort[['Team','選手名','被安打']].head(10))
    elif option == '被本塁打':
        AL_all_pitcher_df_sort = AL_all_pitcher_df.sort_values(['被本塁打'],ascending=False)
        st.write(AL_all_pitcher_df_sort[['Team','選手名','被本塁打']].head(10))
    elif option == '奪三振':
        AL_all_pitcher_df_sort = AL_all_pitcher_df.sort_values(['奪三振'],ascending=False)
        st.write(AL_all_pitcher_df_sort[['Team','選手名','奪三振']].head(10))
    elif option == '与四球':
        AL_all_pitcher_df_sort = AL_all_pitcher_df.sort_values(['与四球'],ascending=False)
        st.write(AL_all_pitcher_df_sort[['Team','選手名','与四球']].head(10))
    elif option == '与死球':
        AL_all_pitcher_df_sort = AL_all_pitcher_df.sort_values(['与死球'],ascending=False)
        st.write(AL_all_pitcher_df_sort[['Team','選手名','与死球']].head(10))
    elif option == '暴投':
        AL_all_pitcher_df_sort = AL_all_pitcher_df.sort_values(['暴投'],ascending=False)
        st.write(AL_all_pitcher_df_sort[['Team','選手名','暴投']].head(10))
    elif option == 'ボーク':
        AL_all_pitcher_df_sort = AL_all_pitcher_df.sort_values(['ボーク'],ascending=False)
        st.write(AL_all_pitcher_df_sort[['Team','選手名','ボーク']].head(10))
    elif option == '失点':
        AL_all_pitcher_df_sort = AL_all_pitcher_df.sort_values(['失点'],ascending=False)
        st.write(AL_all_pitcher_df_sort[['Team','選手名','失点']].head(10))
    elif option == '自責点':
        AL_all_pitcher_df_sort = AL_all_pitcher_df.sort_values(['自責点'],ascending=False)
        st.write(AL_all_pitcher_df_sort[['Team','選手名','自責点']].head(10))

elif league_option == 'ナショナルリーグ':
    option = st.selectbox('個人成績',['防御率','投球回','勝率','奪三振率','被打率','Ｋ／ＢＢ','ＷＨＩＰ','登板', '先発', '完投', '完封', 'ＱＳ','勝利', '敗戦', 'ホールド', 'セーブ', '被安打', '被本塁打', '奪三振','与四球', '与死球', '暴投', 'ボーク', '失点', '自責点'])
    if option == '防御率':
        NL_all_pitcher_df_sort = NL_all_pitcher_df.sort_values(['防御率'])
        NL_all_pitcher_df_sort = NL_all_pitcher_df_sort[NL_all_pitcher_df_sort['投球回'] > int(game_avg_pitcher)]
        st.write(NL_all_pitcher_df_sort[['Team','選手名','防御率']].head(10))
    elif option == '投球回':
        NL_all_pitcher_df_sort = NL_all_pitcher_df.sort_values(['投球回'],ascending=False)
        st.write(NL_all_pitcher_df_sort[['Team','選手名','投球回']].head(10))
    elif option == '勝率':
        NL_all_pitcher_df_sort = NL_all_pitcher_df.sort_values(['勝率'],ascending=False)
        NL_all_pitcher_df_sort = NL_all_pitcher_df_sort[NL_all_pitcher_df_sort['投球回'] > int(game_avg_pitcher)]
        st.write(NL_all_pitcher_df_sort[['Team','選手名','勝率']].head(10))
    elif option == '奪三振率':
        NL_all_pitcher_df_sort = NL_all_pitcher_df.sort_values(['奪三振率'],ascending=False)
        NL_all_pitcher_df_sort = NL_all_pitcher_df_sort[NL_all_pitcher_df_sort['投球回'] > int(game_avg_pitcher)]
        st.write(NL_all_pitcher_df_sort[['Team','選手名','奪三振率']].head(10))
    elif option == '被打率':
        NL_all_pitcher_df_sort = NL_all_pitcher_df.sort_values(['被打率'])
        NL_all_pitcher_df_sort = NL_all_pitcher_df_sort[NL_all_pitcher_df_sort['投球回'] > int(game_avg_pitcher)]
        st.write(NL_all_pitcher_df_sort[['Team','選手名','被打率']].head(10))
    elif option == 'Ｋ／ＢＢ':
        st.write("K/BBは奪三振と与四球の比率、投手の制球力を示す指標")
        NL_all_pitcher_df_sort = NL_all_pitcher_df.sort_values(['Ｋ／ＢＢ'],ascending=False)
        NL_all_pitcher_df_sort = NL_all_pitcher_df_sort[NL_all_pitcher_df_sort['投球回'] > int(game_avg_pitcher)]
        st.write(NL_all_pitcher_df_sort[['Team','選手名','Ｋ／ＢＢ']].head(10))
    elif option == 'ＷＨＩＰ':
        st.write("WHIPは1投球回あたり何人の走者(与四球と被安打)を出したかを表す数値")
        NL_all_pitcher_df_sort = NL_all_pitcher_df.sort_values(['ＷＨＩＰ'])
        NL_all_pitcher_df_sort = NL_all_pitcher_df_sort[NL_all_pitcher_df_sort['投球回'] > int(game_avg_pitcher)]
        st.write(NL_all_pitcher_df_sort[['Team','選手名','ＷＨＩＰ']].head(10))
    elif option == '登板':
        NL_all_pitcher_df_sort = NL_all_pitcher_df.sort_values(['登板'],ascending=False)
        st.write(NL_all_pitcher_df_sort[['Team','選手名','登板']].head(10))
    elif option == '先発':
        NL_all_pitcher_df_sort = NL_all_pitcher_df.sort_values(['先発'],ascending=False)
        st.write(NL_all_pitcher_df_sort[['Team','選手名','先発']].head(10))
    elif option == '完投':
        NL_all_pitcher_df_sort = NL_all_pitcher_df.sort_values(['完投'],ascending=False)
        st.write(NL_all_pitcher_df_sort[['Team','選手名','完投']].head(10))
    elif option == '完封':
        NL_all_pitcher_df_sort = NL_all_pitcher_df.sort_values(['完封'],ascending=False)
        st.write(NL_all_pitcher_df_sort[['Team','選手名','完封']].head(10))
    elif option == 'ＱＳ':
        NL_all_pitcher_df_sort = NL_all_pitcher_df.sort_values(['ＱＳ'],ascending=False)
        st.write(NL_all_pitcher_df_sort[['Team','選手名','ＱＳ']].head(10))
    elif option == '勝利':
        NL_all_pitcher_df_sort = NL_all_pitcher_df.sort_values(['勝利'],ascending=False)
        st.write(NL_all_pitcher_df_sort[['Team','選手名','勝利']].head(10))
    elif option == '敗戦':
        NL_all_pitcher_df_sort = NL_all_pitcher_df.sort_values(['敗戦'],ascending=False)
        st.write(NL_all_pitcher_df_sort[['Team','選手名','敗戦']].head(10))
    elif option == 'ホールド':
        NL_all_pitcher_df_sort = NL_all_pitcher_df.sort_values(['ホールド'],ascending=False)
        st.write(NL_all_pitcher_df_sort[['Team','選手名','ホールド']].head(10))
    elif option == 'セーブ':
        NL_all_pitcher_df_sort = NL_all_pitcher_df.sort_values(['セーブ'],ascending=False)
        st.write(NL_all_pitcher_df_sort[['Team','選手名','セーブ']].head(10))
    elif option == '被安打':
        NL_all_pitcher_df_sort = NL_all_pitcher_df.sort_values(['被安打'],ascending=False)
        st.write(NL_all_pitcher_df_sort[['Team','選手名','被安打']].head(10))
    elif option == '被本塁打':
        NL_all_pitcher_df_sort = NL_all_pitcher_df.sort_values(['被本塁打'],ascending=False)
        st.write(NL_all_pitcher_df_sort[['Team','選手名','被本塁打']].head(10))
    elif option == '奪三振':
        NL_all_pitcher_df_sort = NL_all_pitcher_df.sort_values(['奪三振'],ascending=False)
        st.write(NL_all_pitcher_df_sort[['Team','選手名','奪三振']].head(10))
    elif option == '与四球':
        NL_all_pitcher_df_sort = NL_all_pitcher_df.sort_values(['与四球'],ascending=False)
        st.write(NL_all_pitcher_df_sort[['Team','選手名','与四球']].head(10))
    elif option == '与死球':
        NL_all_pitcher_df_sort = NL_all_pitcher_df.sort_values(['与死球'],ascending=False)
        st.write(NL_all_pitcher_df_sort[['Team','選手名','与死球']].head(10))
    elif option == '暴投':
        NL_all_pitcher_df_sort = NL_all_pitcher_df.sort_values(['暴投'],ascending=False)
        st.write(NL_all_pitcher_df_sort[['Team','選手名','暴投']].head(10))
    elif option == 'ボーク':
        NL_all_pitcher_df_sort = NL_all_pitcher_df.sort_values(['ボーク'],ascending=False)
        st.write(NL_all_pitcher_df_sort[['Team','選手名','ボーク']].head(10))
    elif option == '失点':
        NL_all_pitcher_df_sort = NL_all_pitcher_df.sort_values(['失点'],ascending=False)
        st.write(NL_all_pitcher_df_sort[['Team','選手名','失点']].head(10))
    elif option == '自責点':
        NL_all_pitcher_df_sort = NL_all_pitcher_df.sort_values(['自責点'],ascending=False)
        st.write(NL_all_pitcher_df_sort[['Team','選手名','自責点']].head(10))