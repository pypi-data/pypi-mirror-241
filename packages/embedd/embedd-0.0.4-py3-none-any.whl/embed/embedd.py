import configparser
import os
import pandas as pd
import openai
from Tools.scripts.dutree import display
from openai import OpenAI
import numpy as np
import ast
from typing import Union


class Embed:
    def __init__(self, api_key=""):
        # 检查 api_key 是否指向有效的文件
        if os.path.isfile(api_key):
            # 尝试从配置文件中读取 API 密钥
            config = configparser.ConfigParser()
            config.read(api_key)
            self.api_key = config.get('openai', 'api_key', fallback='')
        elif api_key != "":
            # 使用直接提供的 API 密钥
            self.api_key = api_key
        else:
            # 从环境变量中获取 API 密钥
            self.api_key = os.getenv('OPENAI_API_KEY', '')

        # 检查是否获取到了有效的 API 密钥
        if not self.api_key:
            raise ValueError("API 密钥未提供或无效。请提供有效的 API 密钥。")

    def create_embedding_file(self, file_path, new_file_path, selected_columns=None):
        # 根据文件扩展名确定文件类型
        # 确定文件类型
        file_extension = os.path.splitext(file_path)[-1].lower()

        # 读取不同格式的文件
        if file_extension == '.csv':
            df = pd.read_csv(file_path)
        elif file_extension in ['.xls', '.xlsx']:
            df = pd.read_excel(file_path, engine='openpyxl')
        elif file_extension == '.json':
            df = pd.read_json(file_path)
        else:
            raise ValueError("不支持的文件格式。仅支持 CSV, XLS 和 XLSX 格式。")

        # 如果未指定选定列，则使用文件的所有列
        if selected_columns is None:
            selected_columns = df.columns.tolist()

        # 合并每行数据为文本
        text_data = []
        for index, row in df.iterrows():
            row_text = " ".join([f"{col}: {row[col]}" for col in selected_columns])
            text_data.append(row_text)

        df['text'] = text_data
        # 将文本数据转换为矢量
        df['ada_embedding'] = df['text'].apply(
            lambda x: self.get_embedding(x, model='text-embedding-ada-002'))

        # 创建新 DataFrame
        new_df = pd.DataFrame(columns=['text', 'ada_embedding'])
        new_df['text'] = text_data
        for col in df.columns:
            new_df[col] = df[col]

        # 检查 new_file_path 是否包含文件扩展名
        _, ext = os.path.splitext(new_file_path)
        if not ext:
            # 如果没有扩展名，则默认使用 embeddfile.json
            new_file_path = os.path.join(new_file_path, "embeddfile.json")
            output_format = 'json'
        else:
            # 如果有扩展名，则检查扩展名是否为 'csv' 或 'json'
            if ext.lower() in ['.csv', '.json']:
                output_format = ext.lower().strip('.')
            else:
                # 如果扩展名不是 'csv' 或 'json'，则默认改为 'json'
                new_file_path = os.path.splitext(new_file_path)[0] + ".json"
                output_format = 'json'
                raise ValueError("不支持的输出格式。仅支持 'csv' 和 'json' 格式。已将格式转化为json")

        # 根据输出格式保存文件
        if output_format == 'csv':
            new_df.to_csv(new_file_path, index=True)
        elif output_format == 'json':
            new_df.to_json(new_file_path, orient='records', lines=True, force_ascii=False)
        else:
            raise ValueError("不支持的输出格式。仅支持 'csv' 和 'json' 格式。")

        print(f"转换后的数据已保存到 {new_file_path}")

    def upload_embedding(self, file_path):
        pass

    @staticmethod
    def cosine_similarity(a, b):
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

    def get_embedding(self, text, model="text-embedding-ada-002"):  # model = "deployment_name"
        client = OpenAI(api_key=self.api_key)
        return client.embeddings.create(input=[text], model=model).data[0].embedding

    def search_from_file(self, file_path, user_query, top_n=4, to_print=False):

        file_extension = os.path.splitext(file_path)[-1].lower()

        if file_extension == '.csv':
            df = pd.read_csv(file_path)
        elif file_extension in ['.xls', '.xlsx']:
            df = pd.read_excel(file_path, engine='openpyxl')
        elif file_extension == '.json':
            df = pd.read_json(file_path)
        else:
            raise ValueError("Unsupported file format. Only CSV, XLS, JSON, and XLSX formats are supported.")

        embedding = self.get_embedding(
            user_query,
            model="text-embedding-ada-002",
        )
        df['ada_embedding'] = df['ada_embedding'].apply(ast.literal_eval)
        df["similarities"] = df.ada_embedding.apply(lambda x: self.cosine_similarity(x, embedding))

        res = (
            df.sort_values("similarities", ascending=False)
            .head(top_n)
        )
        if to_print:
            pd.set_option('display.max_columns', 100)
            print(res)
        return res

    def search_docs_server(self, file_path, user_query, top_n=4, to_print=False):
        pass
