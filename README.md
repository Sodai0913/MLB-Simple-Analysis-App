# MLB-Simple-Analysis-App

streamlitローカル起動
streamlit run 01_⚾MLBチーム_個人成績.py

LLM as a judgeとRAGで使っているopneaiのバージョンが違うため下記で変更
LLM as a judgeを使う場合はこっち
pip install openai==0.28

RAGを動かす場合はこっち
pip install --upgrade openai

# 各ファイルの説明
メインのアプリ部分
01_⚾MLBチーム_個人成績.py:MLBのチーム成績や個人成績を見ることができるところ

02_勝敗分析.py:パワーチャートなどを見て分析をすることができるところ

03_help.py:RAGによるアプリの説明を見ることができる機能

Data_collection.py:機械学習で使う用のデータを集めるプログラム

main.py:MLB簡易分析アプリに使うデータをスクレイピングするプログラム

LLM_as_a_judge.py:help.pyの回答を評価するプログラム

# 各フォルダの説明
data:MLB簡易分析アプリに使うデータを入れるフォルダ

evaluation_resault:LLM_as_a_judge.pyの結果を入れるフォルダ

pages:02_勝敗分析.py,03_help.pyを入れるフォルダ

QA_data:LLM_as_a_judge.pyで評価する評価対象を入れるフォルダ
