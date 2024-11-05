import os
from help_rag.embedder import OpenAIEmbedder
from help_rag.searcher import CosineNearestNeighborsFinder
from help_rag.chatBot import GPTBasedChatBot
import streamlit as st

# OpenAI APIキーを事前に環境変数にセットしてください。
api_key = os.getenv("OPENAI_API_KEY")

if api_key is None:
    raise ValueError("APIキーがセットされていません。")

st.title("HELP")

def main():

    embedder = OpenAIEmbedder(api_key)
    searcher = CosineNearestNeighborsFinder("help_rag/sample_data.json")

    user_query = ""
    user_query = st.text_input("質問を入力")
    button = st.button("送信")

    if button :
        if user_query :
            user_query_vector: list[float] = embedder.embed([user_query])[0]
            search_results: list[dict] = searcher.find_nearest(user_query_vector, topk=2)
            chat_bot = GPTBasedChatBot()
            response: str = chat_bot.generate_response(
                user_query, [search_result["text"] for search_result in search_results]
            )

            st.write("【AIの返答】")
            st.write(response)


if __name__ == "__main__":
    main()

