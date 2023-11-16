Embedd
简介
Embedd 是一个 Python 工具，用于处理和搜索文本嵌入。它支持从不同格式的文件中读取数据，生成文本嵌入，并提供了一种方法来搜索这些嵌入以找到与给定查询最相似的记录。

功能
生成文本嵌入。
提供本地文档搜索功能。

安装
您可以通过 pip 安装此包：
pip install embedd

使用前的配置
在使用此包之前，您需要一个 OpenAI API 密钥。您可以通过以下几种方式提供 API 密钥：

直接在创建 Embed 实例时传入。
通过配置文件传入。
从环境变量 OPENAI_API_KEY 中读取。

基本使用
创建嵌入文件
embedder = Embed(api_key="您的API密钥")
embedder.create_embedding_file("path/to/input.csv", "path/to/output")

从文件中搜索
python
Copy code
results = embedder.search_from_file("path/to/data.csv", "用户查询", top_n=3, to_print=True)

功能说明
create_embedding_file: 从指定的文件中读取数据，并创建文本嵌入。支持的文件格式包括 CSV、XLS、XLSX 和 JSON。输出文件格式可以是 CSV 或 JSON。
search_from_file: 在提供的数据文件中搜索与用户查询最相似的文档。支持的文件格式同上。

注意事项
某些方法（如 upload_embedding 和 search_docs_server）目前还在开发中，暂时不可用。
贡献
欢迎对此项目进行贡献。请确保在提交 Pull Request 之前测试您的代码。

许可证
此项目根据 MIT 许可证发布。