from checkmate import checkmate

def main():
    board = """\
    ....
    .K..
    ....
    ....\
    """
    
    try:
        print(checkmate(board))  # ทดสอบกระดานนี้
    except ValueError as e:
        print(e)  # จะแสดงข้อความ error ถ้ามี King มากกว่าหนึ่งตัว

if __name__ == "__main__":
    main()
