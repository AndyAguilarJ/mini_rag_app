import subprocess
import time
import sys
import os
import requests
from app.config import get_path
from scripts.chat import start_chat 

class LlamaServerManager:
    def __init__(self):
        self.process = None

    def start(self):
        server_bin = get_path("llama/llama-server.exe")
        model_path = get_path("models/deepseek-r1-distill-qwen-1.5b-q4_0.gguf")
        llama_dir = os.path.dirname(server_bin)

        cmd = [
            server_bin,
            "-m", model_path,
            "--port", "8080",
            "-c", "4096",
            "--n-gpu-layers", "0", #can use gpu in parallel if needed
            "--parallel", "1"
            "--no-warmup"
        ]

        print("Starting LLM server...")
        print("Server:", server_bin)
        print("Model :", model_path)
        print("CWD   :", llama_dir)

        self.process = subprocess.Popen(
            cmd,
            cwd=llama_dir,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        if not self.wait_until_ready():
            raise RuntimeError("LLM failed to start")

        print("LLM ready")

    def wait_until_ready(self, timeout=60):
        start = time.time()

        while time.time() - start < timeout:
            try:
                requests.get("http://localhost:8080/v1/models")
                return True
            except:
                time.sleep(1)

        return False

    def is_running(self):
        return self.process and self.process.poll() is None

    def restart(self):
        print("LLM crashed — restarting...")
        self.start()

    def monitor(self):
        if not self.is_running():
            self.restart()

if __name__ == "__main__":
    server = LlamaServerManager()

    try:
        server.start()
        start_chat()

    except KeyboardInterrupt:
        print("Shutting down...")
        sys.exit(0)