from checkmate import checkmate 
def main():
    board = """\
    R...
    .K..
    ..P.
    ....\
    """
    print(checkmate(board))  # ทดสอบกระดานนี้

if __name__ == "__main__":
    main()