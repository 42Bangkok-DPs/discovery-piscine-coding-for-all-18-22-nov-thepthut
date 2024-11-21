def checkmate(board):
    # แปลงกระดานเป็น list of lists
    board_rows = board.split("\n")
    board_matrix = [list(row) for row in board_rows]

    # ค้นหาตำแหน่งของ King
    king_position = None
    for i, row in enumerate(board_matrix):
        for j, cell in enumerate(row):
            if cell == 'K':
                king_position = (i, j)
                break
        if king_position:
            break

    if not king_position:
        return "Fail"  # กรณีไม่มี King บนกระดาน

    king_row, king_col = king_position
    directions = {
        'P': [(-1, -1), (-1, 1)],  # Pawn เดินเฉียง
        'R': [(0, 1), (0, -1), (1, 0), (-1, 0)],  # Rook เดินแนวตั้ง-แนวนอน
        'B': [(1, 1), (1, -1), (-1, 1), (-1, -1)],  # Bishop เดินทแยง
        'Q': [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]  # Queen เดินทุกทิศ
    }

    # วนหาหมากทุกตัวบนกระดาน
    for i, row in enumerate(board_matrix):
        for j, cell in enumerate(row):
            if cell in directions:  # ถ้าเป็นหมากที่มีทิศทาง
                for dr, dc in directions[cell]:  # วนตรวจสอบทุกทิศทาง
                    r, c = i + dr, j + dc
                    while 0 <= r < len(board_matrix) and 0 <= c < len(board_matrix[0]):  # อยู่ในขอบเขต
                        if (r, c) == king_position:  # ถ้าตรงกับตำแหน่ง King
                            return "Success"
                        if board_matrix[r][c] != '.':  # ถ้ามีตัวขวาง
                            break
                        # ถ้าหมากเป็น Rook, Bishop หรือ Queen เดินได้หลายช่อง
                        if cell in ['R', 'B', 'Q']:
                            r += dr
                            c += dc
                            continue
                        break  # สำหรับ Pawn (P) จะเดินได้แค่ช่องเดียว

    return "Fail"  # ถ้าไม่มีหมากตัวไหน Check King ได้

