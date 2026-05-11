from langchain_community.document_loaders import CSVLoader

loader=CSVLoader(file_path="./data/sample_data.csv",  #CSVLoader 是 LangChain 提供的一个文档加载器（Document Loader），它的核心作用是将 CSV 格式的文件转换为 LangChain 能够处理的 Document 对象列表
                 csv_args={"delimiter":",",   #指定分隔符
                           "quotechar":'"',
                           #如果数据原本有表头，就不要下面的代码，如果没有可以使用
                           "fieldnames":['a','b','c','d']
                           },
                 encoding="utf-8")
#批量加载 .load  ->  [Document,Document.....]

documents=loader.load()
# print(documents)
#
# for document in documents:
#     print(type(document),document)

#懒加载 .lazy_load()  迭代器[Document]

for document in loader.lazy_load():
    print(document)