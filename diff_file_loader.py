from langchain_community.document_loaders import NotionDirectoryLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import UnstructuredEmailLoader

#Creating Notion file loader
notion_loader = NotionDirectoryLoader("notionfile.notion")
notion_docs = notion_loader.load()

#creating pdf file loader
pdf_loader = PyPDFLoader("pdffile.pdf")
pdf_docs = pdf_loader.load()

#creating email file loader
email_loader = UnstructuredEmailLoader("email.eml")
email_docs = email_loader.load()
