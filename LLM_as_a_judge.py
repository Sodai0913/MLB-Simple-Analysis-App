import json
import pandas as pd
from tqdm import tqdm
import time
import os
import openai
from loguru import logger
import sys
from functools import wraps

# OpenAI APIキーの設定
openai.api_key = os.getenv("OPENAI_API_KEY")

def retry_on_error(max_retries=5, wait_time=30):
    """
    関数実行時のエラーを処理し、指定回数リトライするデコレータ
    
    Args:
        max_retries (int): 最大リトライ回数
        wait_time (int): リトライ間隔（秒）
    
    Returns:
        function: デコレートされた関数
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_retries - 1:
                        logger.error(f"最大リトライ回数に達しました: {str(e)}")
                        raise
                    logger.warning(f"エラーが発生しました。{wait_time}秒後にリトライします。(試行 {attempt + 1}/{max_retries}): {str(e)}")
                    time.sleep(wait_time)
            return None
        return wrapper
    return decorator

class EvaluationPrompts:
    """評価プロンプトを管理するクラス"""
    
    @staticmethod
    def get_judge_prompt():
        return """
        あなたはLLMの回答を評価する審査員です。
        質問と模範解答、そしてLLMの回答のセットを評価してください。

        評価は1から4の整数スケールで行ってください：
        1: 全く役に立たない回答：質問に対して無関係か、部分的すぎる
        2: あまり役に立たない回答：質問の重要な側面を見落としている
        3: おおむね役立つ回答：支援を提供しているが、改善の余地がある
        4: 優れた回答：関連性があり、直接的で、詳細で、質問で提起されたすべての懸念に対応している

        以下のフォーマットで評価を提供してください：

        Feedback:::
        評価理由: (評価の根拠を説明してください)
        総合評価: (1から4の整数で評価してください)

        これから質問、模範解答、LLMの回答を提示します：

        質問: {question}
        模篜解答: {correct_answer}
        LLMの回答: {llm_answer}

        フィードバックをお願いします。
        Feedback:::
        評価理由: """

class EvaluationParser:
    """評価結果を解析するクラス"""
    
    @staticmethod
    def extract_score(response_text):
        """
        評価テキストからスコアを抽出する
        
        Args:
            response_text (str): 評価テキスト
        
        Returns:
            int or None: 抽出されたスコア
        """
        try:
            score_text = response_text.split("総合評価:")[1].strip()
            score = int(score_text.split()[0])
            return score
        except:
            logger.error(f"スコア抽出に失敗しました: {response_text}")
            return None

    @staticmethod
    def extract_reason(evaluation_text):
        """
        評価テキストから評価理由を抽出する
        
        Args:
            evaluation_text (str): 評価テキスト
        
        Returns:
            str: 抽出された評価理由
        """
        try:
            reason = evaluation_text.split("評価理由:")[1].split("総合評価:")[0].strip()
            return reason
        except:
            logger.warning("評価理由の抽出に失敗しました")
            return ""

class LLMEvaluator:
    """LLMの回答を評価するメインクラス"""
    
    def __init__(self, model_name="gpt-4"):
        """
        評価器を初期化する
        
        Args:
            model_name (str): 使用するLLMモデル名
        """
        self.model_name = model_name
        self.prompts = EvaluationPrompts()
        self.parser = EvaluationParser()
        logger.info(f"評価器を初期化しました。使用モデル: {model_name}")

    @retry_on_error()


    def evaluate_response(self, question, correct_answer, llm_answer):
        prompt = self.prompts.get_judge_prompt().format(
            question=question,
            correct_answer=correct_answer,
            llm_answer=llm_answer
        )

        try:
            # v1/chat/completionsエンドポイントを使用
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # 使用するモデル名
                messages=[
                    {"role": "system", "content": "あなたは評価者です。"},
                    {"role": "user", "content": prompt},
                ],
                max_tokens=1000  # 必要に応じて最大トークン数を調整
            )
            
            evaluation = response['choices'][0]['message']['content'].strip()  # レスポンスのメッセージ部分を取得
            score = self.parser.extract_score(evaluation)

            if score:
                logger.debug(f"評価完了 - スコア: {score}")

            return {
                'score': score,
                'evaluation': evaluation
            }
        except Exception as e:
            logger.error(f"評価中にエラーが発生しました: {str(e)}")
            raise


    @retry_on_error()
    def evaluate_dataset(self, json_file_path, output_file="evaluation_results.json"):
        """
        データセット全体を評価する

        Args:
            json_file_path (str): 評価対象のJSONファイルパス
            output_file (str): 評価結果の出力先ファイルパス

        Returns:
            dict: 評価結果と分析データを含む辞書
        """
        logger.info(f"データセット評価を開始します: {json_file_path}")
        
        with open(json_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        results = []
        qa_pairs = data['qa_pairs_simple']
        total_pairs = len(qa_pairs)
        
        logger.info(f"合計 {total_pairs} 件のQAペアを評価します")
        
        progress_bar = tqdm(qa_pairs, desc="評価進捗", unit="件")
        for qa in progress_bar:
            eval_result = self.evaluate_response(
                qa['question'],
                qa['correct_answer'],
                qa['llm_answer']
            )
            
            if eval_result:
                results.append({
                    'question': qa['question'],
                    'correct_answer': qa['correct_answer'],
                    'llm_answer': qa['llm_answer'],
                    'score': eval_result['score'],
                    'evaluation': eval_result['evaluation']
                })
                
                # 進捗状況を更新
                progress_bar.set_postfix(
                    completed=f"{len(results)}/{total_pairs}",
                    last_score=eval_result['score']
                )
            
            time.sleep(1)  # API制限考慮

        # 結果を分析
        scores = [r['score'] for r in results if r['score'] is not None]
        analysis = {
            'total_evaluations': len(results),
            'average_score': sum(scores) / len(scores) if scores else 0,
            'score_distribution': {
                '1': scores.count(1),
                '2': scores.count(2),
                '3': scores.count(3),
                '4': scores.count(4)
            }
        }

        # 分析結果をログに出力
        logger.success("評価が完了しました")
        logger.info(f"総評価数: {analysis['total_evaluations']}")
        logger.info(f"平均スコア: {analysis['average_score']:.2f}")
        logger.info("スコア分布:")
        for score, count in analysis['score_distribution'].items():
            percentage = (count / len(scores) * 100) if scores else 0
            logger.info(f"スコア {score}: {count}件 ({percentage:.1f}%)")

        # 結果をJSONとして保存
        output_data = {
            'analysis': analysis,
            'detailed_results': results
        }
        
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(output_data, f, ensure_ascii=False, indent=2)
        
        logger.info(f"評価結果を保存しました: {output_file}")
        return output_data

class ResultExporter:
    """評価結果をエクスポートするクラス"""
    
    @staticmethod
    def export_to_csv(evaluation_results, output_file="evaluation_results.csv"):
        """
        評価結果をCSVファイルに出力する
        
        Args:
            evaluation_results (dict): 評価結果
            output_file (str): 出力ファイルパス
        
        Returns:
            pd.DataFrame: 出力されたDataFrame
        """
        detailed_results = evaluation_results.get('detailed_results', [])
        
        df = pd.DataFrame(detailed_results)
        df.to_csv(output_file, index=False, encoding='utf-8')
        
        logger.info(f"評価結果をCSVとして保存しました: {output_file}")
        return df

# メイン処理
def main():
    # ここでファイルパスや必要な設定を指定します
    input_json_file = ".\QA_data\qa_data.json"  # 例: "qa_data.json"というJSONファイルを指定
    output_json_file = ".\evaluation_results\evaluation_results.json"  # 出力する評価結果のJSONファイル名
    
    evaluator = LLMEvaluator(model_name="gpt-4")
    evaluation_results = evaluator.evaluate_dataset(input_json_file, output_file=output_json_file)
    
    # CSVとしてエクスポート
    exporter = ResultExporter()
    exporter.export_to_csv(evaluation_results, output_file=".\evaluation_results\evaluation_results.csv")

if __name__ == "__main__":
    main()
