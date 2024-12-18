from abc import ABC, abstractmethod
from openai import OpenAI
import streamlit as st


class ChatBot(ABC):
    @abstractmethod
    def generate_response(self, user_query: str, refs: list[str]) -> str:
        pass


class GPTBasedChatBot(ChatBot):
    def __init__(self):
        self.client = OpenAI()

    def generate_response(self, user_query: str, refs: list[str]) -> str:

        # GPTによる応答を生成
        context = "\n".join(refs) + "\n"

        prompt = f"以下の情報に基づいてユーザーの質問に答えてください。分からないことやアプリケーションのこと以外の質問には答えないでください。:\n\n{context}\n\n質問: {user_query}"
        print("#" * 30)
        print("#" * 30)
        print(f"\nprompt:\n {prompt}\n")
        print("#" * 30)
        print("#" * 30)
        st.write("=" * 88)
        st.write(f"\nprompt:\n {prompt}\n")
        st.write("=" * 88)

        completion = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
        )
        return completion.choices[0].message.content
