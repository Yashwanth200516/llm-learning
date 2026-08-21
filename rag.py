from pypdf import PdfReader


#extract data from pdf
def extract_text_from_pdf(pdf_path: str) -> str:
    reader=PdfReader(pdf_path)
    ans=""
    for page in reader.pages:
        ans+=page.extract_text()

    return ans

res=extract_text_from_pdf("C:/Users/user/OneDrive/Desktop/llm/Coursera pg.pdf")

#convert it to small chunks
def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> list[str]:
    words = text.split()
    chunks = []
    step = chunk_size - overlap
    start = 0
    while start < len(words):
        chunks.append(" ".join(words[start:start+chunk_size]))
        start += step
    
    return chunks

chunks=chunk_text(res)

print(f"Total chunks: {len(chunks)}")
for i, c in enumerate(chunks):
    print(f"--- Chunk {i} ({len(c.split())} words) ---")
    print(c)
    print()