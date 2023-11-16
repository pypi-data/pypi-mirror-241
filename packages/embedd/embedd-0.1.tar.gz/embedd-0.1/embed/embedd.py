import os
import pandas as pd
import openai
from Tools.scripts.dutree import display
from openai import OpenAI
import numpy as np
import ast
from typing import Union
from fastapi import FastAPI


app = FastAPI()



@app.get("/create_embfile")
def create_embedding_file(file_path,new_file_path, selected_columns=None,output_format='json'):
   # 根据文件扩展名确定文件类型
   file_extension = os.path.splitext(file_path)[-1].lower()

   if file_extension == '.csv':
      df = pd.read_csv(file_path)
   elif file_extension in ['.xls', '.xlsx']:
      df = pd.read_excel(file_path, engine='openpyxl')
   elif file_extension == '.json':
      df = pd.read_json(file_path)
   else:
      raise ValueError("Unsupported file format. Only CSV, XLS, and XLSX formats are supported.")

   # 如果没有传递selected_columns参数，使用文件的列名作为选定的列
   if selected_columns is None:
      selected_columns = df.columns.tolist()

   # 合并每一行的数据为文本
   text_data = []

   for index, row in df.iterrows():
      # 将表头信息和每列的值合并为文本
      row_text = " ".join([f"{col}: {row[col]}" for col in selected_columns])
      text_data.append(row_text)

   df['text'] = text_data
   # 使用模型将文本数据转换为矢量
   df['ada_embedding'] = df['text'].apply(lambda x: get_embedding(x, model='text-embedding-ada-002'))
   print(df['ada_embedding'])
   # 创建 new_df with the text vectors
   new_df = pd.DataFrame(columns=['text', 'ada_embedding'])

   new_df['text'] = text_data

   for col in df.columns:
         new_df[col] = df[col]

   # new_df['values1'] = [data[1][:len(data[1]) // 2] for data in text_vector]
   # new_df['values2'] = [data[1][len(data[1]) // 2:] for data in text_vector]
   # 根据输出格式保存文件
   if output_format == 'csv':
      new_df.to_csv(new_file_path, index=True)
   elif output_format == 'json':
      new_df.to_json(new_file_path, orient='records', lines=True)
   else:
      raise ValueError("Unsupported output format. Only 'csv' and 'json' formats are supported.")


   print(f"Transformed data saved to {new_file_path}")

def upload_embedding(file_path):
   pass

def cosine_similarity(a, b):
   return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def get_embedding(text, model="text-embedding-ada-002"):  # model = "deployment_name"
   client = OpenAI(api_key="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")
   return client.embeddings.create(input=[text], model=model).data[0].embedding


@app.get("/search_local")
def search_docs_locally(file_path, user_query, top_n=4, to_print=False):
   file_extension = os.path.splitext(file_path)[-1].lower()

   if file_extension == '.csv':
      df = pd.read_csv(file_path)
   elif file_extension in ['.xls', '.xlsx']:
      df = pd.read_excel(file_path, engine='openpyxl')
   elif file_extension == '.json':
      df = pd.read_json(file_path)
   else:
      raise ValueError("Unsupported file format. Only CSV, XLS, JSON, and XLSX formats are supported.")

   embedding = get_embedding(
      user_query,
      model="text-embedding-ada-002"
      # model should be set to the deployment name you chose when you deployed the text-embedding-ada-002 (Version 2) model
   )
   df['ada_embedding'] = df['ada_embedding'].apply(ast.literal_eval)
   df["similarities"] = df.ada_embedding.apply(lambda x: cosine_similarity(x, embedding))

   res = (
      df.sort_values("similarities", ascending=False)
      .head(top_n)
   )
   if to_print:
      pd.set_option('display.max_columns', 100)
      print(res)
   return res


def search_docs_server(file_path, user_query, top_n=4, to_print=False):
  pass





