from main import Downloader

proxy = {
    "http": "89.145.162.81:3128",
    "http": "51.124.209.11:80",
    "http": "8.209.114.72:3129",
    "http": "194.182.187.78:3128",
    "http": "78.47.186.43:6666",
    "http": "87.123.56.163:80",
}

if __name__ == "__main__":
    d = Downloader()
    d.start(
        "https://gamedownloads.rockstargames.com/public/installer/Rockstar-Games-Launcher.exe",
        filepath="pypdl/test/t.exe",
        # block=False,
    )
    # d.stop()
    # # # d.main_thread.join()
    # # d.main_thread.
    # d.start(
    #     "https://gamedownloads.rockstargames.com/public/installer/Rockstar-Games-Launcher.exe",
    #     "test/t.exe",
    #     # block=False,
    # )
