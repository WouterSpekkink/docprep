import json
import os  
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import DirectoryLoader, TextLoader

# Set paths
document_dir = './txt/'
output_file = 'prodigy_input.jsonl'

# Create document loader
text_loader_kwargs={'autodetect_encoding': True}
loader = DirectoryLoader(document_dir,
                         show_progress=True,
                         use_multithreading=True,
                         loader_cls=TextLoader,
                         loader_kwargs=text_loader_kwargs)

documents = loader.load()
    
# Split documents
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1500,
    chunk_overlap  = 0,
    length_function = len,
    add_start_index = True,
)

chunks = text_splitter.split_documents(documents)

# Create prodigy data
prodigy_data = []

for chunk in chunks:
    cleaned_text = chunk.page_content.replace('\n', ' ')
    item = {
        "text": cleaned_text,
        "meta": {
            **chunk.metadata  # This unpacks all metadata key-value pairs
        }
    }
    prodigy_data.append(item)
 
# Write file
with open(output_file, 'w', encoding='utf-8') as outfile:
    for item in prodigy_data:
        json.dump(item, outfile)
        outfile.write('\n')  # JSON Lines format requires a newline delimiter

print("Conversion complete. Data is ready for Prodigy.")
