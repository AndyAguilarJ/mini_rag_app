import os
from app.rag import answer
from ingest.ingest import process_single_file 


def start_chat():
    print("Qwen Local RAG Ready!")
    print("Commands: '/ingest <path>' to add a PDF, 'exit' to quit")

    while True:
        q = input("\nYou: ")

        if q.lower() == "exit":
            break
        
        # Handle Drag & Drop / Manual Ingest
        if q.startswith("/ingest"):
            file_path = q.replace("/ingest", "").strip().strip('"')
            
            if os.path.exists(file_path):
                print(f"[*] Processing {os.path.basename(file_path)}...")
                process_single_file(file_path)
                print("[+] Done! You can now ask questions about this file.")
            else:
                print("[!] File not found. Make sure the path is correct.")
            
            continue

        print("\nAssistant:", answer(q))