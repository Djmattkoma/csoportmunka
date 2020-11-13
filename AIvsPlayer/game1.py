from AIvsPlayer import player as pr, ai


def aivsplayer():
    for _ in range(10):
        for _ in range(5):
            ai.gongol()
            print("A te kezed: ", pr.tipel())
            print("Ai keze: ", ai.tipel())