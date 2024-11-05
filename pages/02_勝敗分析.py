import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# =================================================================================================================================================================
# 各ランクを出力する関数
# 走ランク
def steal_rank(team_name):
    MLB_all_team_df = pd.read_csv('.\data\MLB-team\MLB_team.csv')
    # データの中の'-'を0に変換
    MLB_all_team_df = MLB_all_team_df.replace('-',0)
    # 適切なタイプに変換
    MLB_all_team_df_str = MLB_all_team_df[['チーム']]
    MLB_all_team_df_float = MLB_all_team_df[['勝率','ゲーム差','打率','防御率']].astype(np.float64)
    MLB_all_team_df_int = MLB_all_team_df[['順位', '試合', '勝', '敗', '引分','得点', '失点', '本塁打', '盗塁', '失策']].astype(np.int64)
    # データフレームを結合
    MLB_all_team_df = pd.concat([MLB_all_team_df_str,MLB_all_team_df_int],axis=1)
    MLB_all_team_df = pd.concat([MLB_all_team_df,MLB_all_team_df_float],axis=1)
    steal = MLB_all_team_df.sort_values(['盗塁'],ascending=False)
    # 順位のカラムを追加
    steal['steal_rank'] = range(1,len(steal) + 1)
    steal_rank = steal[steal['チーム'] == team_name]
    steal_rank = steal_rank['steal_rank']
        
    return 30 - steal_rank

# 守ランク
def protect_rank(team_name):
    MLB_all_team_df = pd.read_csv('.\data\MLB-team\MLB_team.csv')
    # データの中の'-'を0に変換
    MLB_all_team_df = MLB_all_team_df.replace('-',0)
    # 適切なタイプに変換
    MLB_all_team_df_str = MLB_all_team_df[['チーム']]
    MLB_all_team_df_float = MLB_all_team_df[['勝率','ゲーム差','打率','防御率']].astype(np.float64)
    MLB_all_team_df_int = MLB_all_team_df[['順位', '試合', '勝', '敗', '引分','得点', '失点', '本塁打', '盗塁', '失策']].astype(np.int64)
    # データフレームを結合
    MLB_all_team_df = pd.concat([MLB_all_team_df_str,MLB_all_team_df_int],axis=1)
    MLB_all_team_df = pd.concat([MLB_all_team_df,MLB_all_team_df_float],axis=1)
    
    # 失点で昇順ソート
    loss_pts = MLB_all_team_df.sort_values(['失点'])

    # 順位のカラムを追加
    loss_pts['protect_rank'] = range(1,len(loss_pts) + 1)
    loss_pts_rank = loss_pts[loss_pts['チーム'] == team_name]
    loss_pts_rank = loss_pts_rank['protect_rank']

    # 失策で昇順ソート
    faux_pas = MLB_all_team_df.sort_values(['失策'])

    faux_pas['protect_rank2'] = range(1,len(faux_pas) + 1)
    faux_pas_rank = faux_pas[faux_pas['チーム'] == team_name]
    faux_pas_rank = faux_pas_rank['protect_rank2']

    loss_pts_faux_pas_rank = (loss_pts_rank + faux_pas_rank)/2
        
    return 30 - loss_pts_faux_pas_rank

# 攻ランク
def attack_rank(team_name):
    MLB_all_team_df = pd.read_csv('.\data\MLB-team\MLB_team.csv')
    # データの中の'-'を0に変換
    MLB_all_team_df = MLB_all_team_df.replace('-',0)
    # 適切なタイプに変換
    MLB_all_team_df_str = MLB_all_team_df[['チーム']]
    MLB_all_team_df_float = MLB_all_team_df[['勝率','ゲーム差','打率','防御率']].astype(np.float64)
    MLB_all_team_df_int = MLB_all_team_df[['順位', '試合', '勝', '敗', '引分','得点', '失点', '本塁打', '盗塁', '失策']].astype(np.int64)
    # データフレームを結合
    MLB_all_team_df = pd.concat([MLB_all_team_df_str,MLB_all_team_df_int],axis=1)
    MLB_all_team_df = pd.concat([MLB_all_team_df,MLB_all_team_df_float],axis=1)
    
    get_pts = MLB_all_team_df.sort_values(['得点'],ascending=False)

    # 順位のカラムを追加
    get_pts['attack_rank'] = range(1,len(get_pts) + 1)
    get_pts_rank = get_pts[get_pts['チーム'] == team_name]
    get_pts_rank = get_pts_rank['attack_rank']

    hR = MLB_all_team_df.sort_values(['本塁打'],ascending=False)

    hR['attack_rank2'] = range(1,len(hR) + 1)
    hR_rank = hR[hR['チーム'] == team_name]
    hR_rank = hR_rank['attack_rank2']

    get_pts_hR_rank_rank = (get_pts_rank + hR_rank)/2
        
    return 30 - get_pts_hR_rank_rank
    
# 打ランク
def blow_rank(team_name):
    MLB_all_team_df = pd.read_csv('.\data\MLB-team\MLB_team.csv')
    # データの中の'-'を0に変換
    MLB_all_team_df = MLB_all_team_df.replace('-',0)
    # 適切なタイプに変換
    MLB_all_team_df_str = MLB_all_team_df[['チーム']]
    MLB_all_team_df_float = MLB_all_team_df[['勝率','ゲーム差','打率','防御率']].astype(np.float64)
    MLB_all_team_df_int = MLB_all_team_df[['順位', '試合', '勝', '敗', '引分','得点', '失点', '本塁打', '盗塁', '失策']].astype(np.int64)
    # データフレームを結合
    MLB_all_team_df = pd.concat([MLB_all_team_df_str,MLB_all_team_df_int],axis=1)
    MLB_all_team_df = pd.concat([MLB_all_team_df,MLB_all_team_df_float],axis=1)
    
    blow = MLB_all_team_df.sort_values(['打率'],ascending=False)

    # 順位のカラムを追加
    blow['blow_rank'] = range(1,len(blow) + 1)
    blow_rank = blow[blow['チーム'] == team_name]
    blow_rank = blow_rank['blow_rank']

        
    return 30 - blow_rank

# 投ランク
def pitch_rank(team_name):
    MLB_all_team_df = pd.read_csv('.\data\MLB-team\MLB_team.csv')
    # データの中の'-'を0に変換
    MLB_all_team_df = MLB_all_team_df.replace('-',0)
    # 適切なタイプに変換
    MLB_all_team_df_str = MLB_all_team_df[['チーム']]
    MLB_all_team_df_float = MLB_all_team_df[['勝率','ゲーム差','打率','防御率']].astype(np.float64)
    MLB_all_team_df_int = MLB_all_team_df[['順位', '試合', '勝', '敗', '引分','得点', '失点', '本塁打', '盗塁', '失策']].astype(np.int64)
    # データフレームを結合
    MLB_all_team_df = pd.concat([MLB_all_team_df_str,MLB_all_team_df_int],axis=1)
    MLB_all_team_df = pd.concat([MLB_all_team_df,MLB_all_team_df_float],axis=1)
    
    pitch = MLB_all_team_df.sort_values(['防御率'])

    # 順位のカラムを追加
    pitch['pitch_rank'] = range(1,len(pitch) + 1)
    pitch_rank = pitch[pitch['チーム'] == team_name]
    pitch_rank = pitch_rank['pitch_rank']

        
    return 30 - pitch_rank
# =================================================================================================================================================================


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

        # レーダーチャートに使う用
        # 各ランク
        blow = blow_rank(teams_name[i])
        pitch = pitch_rank(teams_name[i])
        attack = attack_rank(teams_name[i])
        protect = protect_rank(teams_name[i])
        steal = steal_rank(teams_name[i])

        # リストに格納
        home_values = np.array([int(blow.iloc[0]), int(pitch.iloc[0]), int(attack.iloc[0]), int(protect.iloc[0]), int(steal.iloc[0])])

        # st.write(home_team_df)
        # st.write(home_team_Individualresults_fielder_df)
        # st.write(home_team_Individualresults_pitcher_df)


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

        # レーダーチャートに使う用
        # 各ランク
        blow = blow_rank(teams_name[i])
        pitch = pitch_rank(teams_name[i])
        attack = attack_rank(teams_name[i])
        protect = protect_rank(teams_name[i])
        steal = steal_rank(teams_name[i])

        # リストに格納
        away_values = np.array([int(blow.iloc[0]), int(pitch.iloc[0]), int(attack.iloc[0]), int(protect.iloc[0]), int(steal.iloc[0])])

        # st.write(away_team_df)
        # st.write(away_team_Individualresults_fielder_df)
        # st.write(away_team_Individualresults_pitcher_df)


# 強さの指標を可視化するレーダーチャート
# ホームとアウェーのグラフを表示する
labels = ["打","投","攻","守","走"]

# 多角形を閉じるためにデータの最後に最初の値を追加する。
radar_values = np.concatenate([home_values, [home_values[0]]])
radar_values2 = np.concatenate([away_values, [away_values[0]]])
# プロットする角度を生成する。
angles = np.linspace(0, 2 * np.pi, len(labels) + 1, endpoint=True)
angles2 = np.linspace(0, 2 * np.pi, len(labels) + 1, endpoint=True)
# メモリ軸の生成
rgrids = [0, 10, 20, 29]


fig = plt.figure(facecolor="w")
# # 極座標でaxを作成
ax = fig.add_subplot(1, 1, 1, polar=True)
# # レーダーチャートの線を引く
ax.plot(angles, radar_values)
ax.plot(angles, radar_values2)
# #　レーダーチャートの内側を塗りつぶす
ax.fill(angles, radar_values, alpha=0.2)
ax.fill(angles2, radar_values2, alpha=0.2)
# # 項目ラベルの表示
ax.set_thetagrids(angles[:-1] * 180 / np.pi, labels, fontsize = 18, fontname = 'MS Gothic')
# # 円形の目盛線を消す
ax.set_rgrids([])
# # 一番外側の円を消す
ax.spines['polar'].set_visible(False)
# # 始点を上(北)に変更
ax.set_theta_zero_location("N")
# # 時計回りに変更(デフォルトの逆回り)
ax.set_theta_direction(-1)

# # 多角形の目盛線を引く
for grid_value in rgrids:
    grid_values = [grid_value] * (len(labels)+1)
    ax.plot(angles, grid_values, color="gray",  linewidth=0.5)

# メモリの値を表示する
for t in rgrids:
    # xが偏角、yが絶対値でテキストの表示場所が指定される
    ax.text(x=0, y=t, s=t)

# rの範囲を指定
ax.set_rlim([min(rgrids), max(rgrids)])

ax.set_title("パワーチャート", fontsize = 18, fontname = 'MS Gothic')

st.pyplot(fig)

st.write(f"※青が{home_team}、オレンジが{away_team}")



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
                           home_fielder_df["ＯＰＳ"].mean(),away_fielder_df["ＯＰＳ"].mean(),
                           home_fielder_df["本塁打"].sum(),away_fielder_df["本塁打"].sum(),
                           home_fielder_df["出塁率"].mean(),away_fielder_df["出塁率"].mean(),
                           home_fielder_df["得点圏"].mean(),away_fielder_df["得点圏"].mean(),
                           float(home_select_player["防御率"]),float(away_select_player["防御率"]),
                           float(home_select_player["被打率"]),float(away_select_player["被打率"]),
                           float(home_select_player["奪三振率"]),float(away_select_player["奪三振率"]),
                           float(home_select_player["勝利"]),float(away_select_player["勝利"]),
                           float(home_select_player["ＷＨＩＰ"]),float(away_select_player["ＷＨＩＰ"]),
                           float(home_select_player["自責点"]),float(away_select_player["自責点"])]

    # numpy配列に変換
    ndarray_startingmember_data = np.array(startingmember_list)

    # データフレームの形に整形
    ndarray_startingmember_data_list = ndarray_startingmember_data.reshape(11,2)

    # データフレームに変換
    startingmember_df = pd.DataFrame(ndarray_startingmember_data_list)

    # カラムを指定
    startingmember_df = startingmember_df.rename(columns={0:"ホーム",1:"アウェー"},index={0:"平均打率",1:"平均ＯＰＳ",2:"合計本塁打",3:"平均出塁率",4:"平均得点圏打率",5:"先発防御率",6:"被打率",7:"奪三振率",8:"勝利数",9:"先発WHIP",10:"自責点"})
    
    st.title("スターティングメンバー数値比較")
    st.write(startingmember_df.transpose())
    


