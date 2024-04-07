
from cx_Freeze import setup, Executable


build_exe_options = {
    "packages": ["pytube", "threading", "tqdm"],
    "include_files": ["youtube.ico"]
}

setup(
    name="YouTube Downloader",
    version="1.0",
    description="Aplicação para baixar vídeos do YouTube na melhora qualidade possível.",
    options={"build_exe": build_exe_options},
    executables = [Executable("main.py", icon="youtube.ico")]
)