from abc import ABC, abstractmethod
import json
import openai


# データをベクトル化するモジュールのインターフェース
class Embedder(ABC):

    @abstractmethod
    def embed(self, texts: list[str]) -> list[list[float]]:
        raise NotImplementedError

    @abstractmethod
    def save(self, texts: list[str], filename: str) -> bool:
        raise NotImplementedError


# Embedderインターフェースの実装
class OpenAIEmbedder(Embedder):
    def __init__(self, api_key: str):
        openai.api_key = api_key

    def embed(self, texts: list[str]) -> list[list[float]]:
        # openai 1.10.0 で動作確認
        response = openai.embeddings.create(input=texts, model="text-embedding-3-small")
        # レスポンスからベクトルを抽出
        return [data.embedding for data in response.data]

    def save(self, texts: list[str], filename: str) -> bool:
        vectors = self.embed(texts)
        data_to_save = [
            {"id": idx, "text": text, "vector": vector}
            for idx, (text, vector) in enumerate(zip(texts, vectors))
        ]
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data_to_save, f, ensure_ascii=False, indent=4)
        print(f"{filename} に保存されました。")
        return True


if __name__ == "__main__":
    import os

    texts = [
        "このアプリケーションはMLB簡易分析アプリです。様々な機能を使って簡易的にMLBを分析することが出来ます。",
        "MLB簡易分析アプリにはMLBチーム個人成績、勝敗分析の機能があります。それらの機能を使いMLBを分析しながら観戦しましょう。",
        "このアプリケーションでは現時点で過去の試合の結果を見ることはできません。試合の結果を見たい場合は別のサイトを参照してください。",
        "MLBチーム個人成績はMLBの個人成績を見ることが出来る機能です。個人成績がランキング形式で見ることが出来ます。",
        "MLBチーム個人成績ではチームの地区ごとの順位などの成績も見ることが出来、チームの現時点での立ち位置などを確認することが出来ます。",
        "MLBチーム個人成績では現時点でポストシーズンに出場できるチームのリストやワイルドカード争いの順位を見ることが出来ます。",
        "MLBチーム個人成績ではタスクバーから打率や防御率などの見たい個人成績を選択して見ることが出来ます。リーグの選択も可能で、MLB全体としての順位も見ることが出来ます。",
        "勝敗分析ではチームとスターティングメンバーを選択することで簡易的にデータ分析をすることが出来ます。",
        "勝敗分析ではチームの打撃や守備などの順位に基づいたパワーチャートを見ることが出来、分析に役立てることが出来ます。",
        "勝敗分析ではスターティングメンバーを入力することでスターティングメンバーの平均成績を見比べて分析することが出来ます。",
        "helpはMLB簡易分析アプリに関しての質問を入力することでAIがアプリについて説明してくれる機能です。",
    ]

    # OpenAI APIキーを事前に環境変数にセットしてください。
    api_key = os.getenv("OPENAI_API_KEY")
    
    if api_key is None:
        raise ValueError("APIキーがセットされていません。")

    embedder = OpenAIEmbedder(api_key)
    embedder.save(texts, "help_rag/sample_data.json")