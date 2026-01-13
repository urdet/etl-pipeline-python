from datetime import datetime

def get_last_run():
    with open("checkpoints/last_run.txt", "r") as f:
        return f.read().strip()

def update_last_run():
    with open("checkpoints/last_run.txt", "w") as f:
        f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
