import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# mlb_all_pitcher_df = pd.read_csv(".\MLB-all-pitcher\MLB_all_pitcher.csv")

# # データの中の'-'を0に変換
# # mlb_all_fielder_df = mlb_all_fielder_df.replace('-',0)

# # # 適切なタイプに変換
# # mlb_all_fielder_df_str = mlb_all_fielder_df[['Team','位置','背番号','選手名']]
# # mlb_all_fielder_df_float = mlb_all_fielder_df[['打率','出塁率','長打率','ＯＰＳ','得点圏']].astype(np.float64)
# # mlb_all_fielder_df_int = mlb_all_fielder_df[['試合','打席','打数','安打','二塁打','三塁打','本塁打','塁打','打点','得点','三振','四球','死球','犠打','犠飛','盗塁','盗塁死','併殺打']].astype(np.int64)

# # # データフレームを結合
# # mlb_all_fielder_df = pd.concat([mlb_all_fielder_df_str,mlb_all_fielder_df_int],axis=1)
# # mlb_all_fielder_df = pd.concat([mlb_all_fielder_df,mlb_all_fielder_df_float],axis=1)


# # mlb_all_fielder_df = mlb_all_fielder_df.sort_values(['打率'],ascending=False)


# print(mlb_all_pitcher_df)
# MLBの全チームのデータ
# MLB_all_team_df = pd.read_csv(".\MLB-team\MLB_team.csv")

# MLB_all_team_df = MLB_all_team_df.replace('-',0)

# # 適切なタイプに変換
# MLB_all_team_df_str = MLB_all_team_df[['チーム']]
# MLB_all_team_df_float = MLB_all_team_df[['勝率','ゲーム差','打率','防御率']].astype(np.float64)
# MLB_all_team_df_int = MLB_all_team_df[['順位', '試合', '勝', '敗', '引分','得点', '失点', '本塁打', '盗塁', '打率', '防御率', '失策']].astype(np.int64)

# # データフレームを結合
# MLB_all_team_df = pd.concat([MLB_all_team_df_str,MLB_all_team_df_int],axis=1)
# MLB_all_team_df = pd.concat([MLB_all_team_df,MLB_all_team_df_float],axis=1)

# game_avg = MLB_all_team_df['試合'].mean()

# AL_east_team_df = MLB_all_team_df[:5]
# AL_central_team_df = MLB_all_team_df[5:10]
# AL_west_team_df = MLB_all_team_df[10:15]
# NL_east_team_df = MLB_all_team_df[15:20]
# NL_central_team_df = MLB_all_team_df[20:25]
# NL_west_team_df = MLB_all_team_df[25:30]

# print(AL_east_team_df)
# print(AL_central_team_df)

# print(int(game_avg))


# values = np.array([10.5, 18, 30, 18, 25.5])
# labels = ["打","投","攻","守","勝率"]

# # 多角形を閉じるためにデータの最後に最初の値を追加する。
# radar_values = np.concatenate([values, [values[0]]])
# # プロットする角度を生成する。
# angles = np.linspace(0, 2 * np.pi, len(labels) + 1, endpoint=True)
# # メモリ軸の生成
# rgrids = [0, 10, 20, 30]


# fig = plt.figure(facecolor="w")
# # # 極座標でaxを作成
# ax = fig.add_subplot(1, 1, 1, polar=True)
# # # レーダーチャートの線を引く
# ax.plot(angles, radar_values)
# # #　レーダーチャートの内側を塗りつぶす
# ax.fill(angles, radar_values, alpha=0.2)
# # # 項目ラベルの表示
# ax.set_thetagrids(angles[:-1] * 180 / np.pi, labels)
# # # 円形の目盛線を消す
# ax.set_rgrids([])
# # # 一番外側の円を消す
# ax.spines['polar'].set_visible(False)
# # # 始点を上(北)に変更
# ax.set_theta_zero_location("N")
# # # 時計回りに変更(デフォルトの逆回り)
# ax.set_theta_direction(-1)

# # # 多角形の目盛線を引く
# for grid_value in rgrids:
#     grid_values = [grid_value] * (len(labels)+1)
#     ax.plot(angles, grid_values, color="gray",  linewidth=0.5)

# # メモリの値を表示する
# for t in rgrids:
#     # xが偏角、yが絶対値でテキストの表示場所が指定される
#     ax.text(x=0, y=t, s=t)

# # rの範囲を指定
# ax.set_rlim([min(rgrids), max(rgrids)])

# ax.set_title("レーダーチャート", pad=20)
# plt.show()


# 打撃ランク
# class RankOptions:

# 盗塁ランク
def pitch_rank(team_name):
    MLB_all_team_df = pd.read_csv('.\MLB-team\MLB_team.csv')
    # データの中の'-'を0に変換
    MLB_all_team_df = MLB_all_team_df.replace('-',0)
    # 適切なタイプに変換
    MLB_all_team_df_str = MLB_all_team_df[['チーム']]
    MLB_all_team_df_float = MLB_all_team_df[['勝率','ゲーム差','打率','防御率']].astype(np.float64)
    MLB_all_team_df_int = MLB_all_team_df[['順位', '試合', '勝', '敗', '引分','得点', '失点', '本塁打', '盗塁', '失策']].astype(np.int64)
    # データフレームを結合
    MLB_all_team_df = pd.concat([MLB_all_team_df_str,MLB_all_team_df_int],axis=1)
    MLB_all_team_df = pd.concat([MLB_all_team_df,MLB_all_team_df_float],axis=1)
    
    pitch = MLB_all_team_df.sort_values(['打率'],ascending=False)

    # 順位のカラムを追加
    pitch['blow_rank'] = range(1,len(pitch) + 1)
    pitch_rank = pitch[pitch['チーム'] == team_name]
    pitch_rank = pitch_rank['blow_rank']

        
    return 30 - pitch_rank
    
steal = pitch_rank('エンゼルス')

a = [int(steal.iloc[0])]

print(a[0])