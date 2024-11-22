def checkmate(board):
    # แปลงกระดานเป็น list of lists
    board_rows = board.split("\n")
    board_matrix = [list(row) for row in board_rows]

    
    king_position = None
    king_count = 0  

    for i, row in enumerate(board_matrix):
        for j, cell in enumerate(row):
            if cell == 'K':
                king_position = (i, j)
                king_count += 1  
                if king_count > 1:  
                    raise ValueError("error")

    if not king_position:
        return "Fail"  

    king_row, king_col = king_position
    directions = {
        'P': [(-1, -1), (-1, 1)],  # Pawn เดินเฉียง
        'R': [(0, 1), (0, -1), (1, 0), (-1, 0)],  # Rook เดินแนวตั้ง-แนวนอน
        'B': [(1, 1), (1, -1), (-1, 1), (-1, -1)],  # Bishop เดินทแยง
        'Q': [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]  # Queen เดินทุกทิศ
    }

    
    for i, row in enumerate(board_matrix):
        for j, cell in enumerate(row):
            if cell in directions:  
                for dr, dc in directions[cell]:  
                    r, c = i + dr, j + dc
                    while 0 <= r < len(board_matrix) and 0 <= c < len(board_matrix[0]): 
                        if (r, c) == king_position:  
                            return "Success"
                        if board_matrix[r][c] != '.':  
                            break
                        
                        if cell in ['R', 'B', 'Q']:
                            r += dr
                            c += dc
                            continue
                        break  

    return "Fail"  # ถ้าไม่มีหมากตัวไหน Check King ได้
