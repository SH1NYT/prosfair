
#Original Author : Sachin Kukreja (skad5455[at]gmail[dot]com)
import json
#chess_board = json.load(open("../common/initial_state.json"))

opposite_army = { "white" : "black" , "black" : "white" }


def legal_king_moves(board,color,king='king'):
	x , y = board[color][king] 

	king_moves = []
	for i in xrange(3):
		for j in xrange(3):
			if  9 > x+i-1 > 0 and 9 > y+j-1 >0:
				if x+i-1 != x or y+j-1 != y:
					king_moves  = king_moves +  [[x+i-1,y+j-1]]

	return [ x for x in king_moves if x not in board[color].values() ]


def legal_pawn_moves(board,color,pawn):
	if color == "white" :	

		x , y = board[color][pawn]

		pawn_moves = []
	
		if x < 8:
			for j in xrange(3):
				if  9 > y+j-1 > 0:
                        		pawn_moves  = pawn_moves +  [[x+1,y+j-1]]

		return pawn_moves

	else:
		x , y = board[color][pawn]

                pawn_moves = []

		if x > 1:
                	for j in xrange(3):
                        	if  9 > y+j-1 > 0:
                                	pawn_moves  = pawn_moves +  [[x-1,y+j-1]]

                return [x for x in pawn_moves if x not in board[color].values()]

	
def legal_bishop_moves(board,color,bishop):

	x , y = board[color][bishop]

        bishop_moves = []
 
	for i in xrange(8):
		if x-i-1>0 and y+i+1<9:
			if [x-i-1,y+i+1] in board[color].values(): break
			bishop_moves = bishop_moves + [[x-i-1,y+i+1]]
			if [x-i-1,y+i+1] in board[opposite_army[color]].values(): break

	for i in xrange(8):
		if x-i-1 > 0 and y-i-1 > 0:
			if [x-i-1,y-i-1] in board[color].values(): break
			bishop_moves = bishop_moves + [[x-i-1,y-i-1]]
			if [x-i-1,y-i-1] in board[opposite_army[color]].values(): break

	for i in xrange(8):
		if x+i+1 < 9 and y-i-1 > 0:
			if [x+i+1,y-i-1] in board[color].values(): break
			bishop_moves = bishop_moves + [[x+i+1,y-i-1]]
			if [x+i+1,y-i-1] in board[opposite_army[color]].values(): break

	for i in xrange(8):
        	if x+i+1 < 9 and y+i+1 < 9:
			if [x+i+1,y+i+1] in board[color].values(): break
                        bishop_moves = bishop_moves + [[x+i+1,y+i+1]]
			if [x+i+1,y+i+1] in board[opposite_army[color]].values(): break

	return [x for x in bishop_moves if x not in board[color].values()]


#print legal_king_moves(chess_board,"white")
#print legal_pawn_moves(chess_board,"black","pawn_2")
#print legal_bishop_moves(chess_board,"black","bishop_1")

def legal_knight_moves(board, color, knight):
	
	x , y = board[color][knight]

	knight_moves = []

	if x+2 < 9 and y+1 < 9:
		knight_moves = knight_moves + [[x+2,y+1]]

	if x+1 < 9 and y+2 < 9:
		knight_moves = knight_moves + [[x+1,y+2]]

	if x-1 > 0 and y+2 < 9:
		knight_moves = knight_moves + [[x-1,y+2]]
	
	if x-1 > 0 and y-2 > 0:
		knight_moves = knight_moves + [[x-1,y-2]]

	if x+2 < 9 and y-1 > 0:
		knight_moves = knight_moves + [[x+2,y-1]]

	if x+1 < 9 and y-2 > 0:
		knight_moves = knight_moves + [[x+1,y-2]]

	if x-2 > 0 and y-1 > 0:
		knight_moves = knight_moves + [[x-2,y-1]]

	if x-2 > 0 and y+1 < 9:
		knight_moves = knight_moves + [[x-2,y+1]]	

	return [x for x in knight_moves if x not in board[color].values()]




def legal_rook_moves(board,color,rook):

	x , y = board[color][rook]

	rook_moves = []

	for i in xrange(8):
                if x+i+1 < 9:
			if [x+i+1,y] in board[color].values(): break
                        rook_moves = rook_moves + [[x+i+1,y]]
			if [x+i+1,y] in board[opposite_army[color]].values(): break

        for i in xrange(8):
                if x-i-1 > 0:
			if [x-i-1,y] in board[color].values(): break
                        rook_moves = rook_moves + [[x-i-1,y]]
			if [x-i-1,y] in board[opposite_army[color]].values(): break

        for i in xrange(8):
                if y+i+1 < 9:
			if [x,y+i+1] in board[color].values(): break
                        rook_moves = rook_moves + [[x,y+i+1]]
			if [x,y+i+1] in board[opposite_army[color]].values(): break

        for i in xrange(8):
                if y-i-1 > 0:
			if [x,y-i-1] in board[color].values(): break
                        rook_moves = rook_moves + [[x,y-i-1]]
			if [x,y-i-1] in board[opposite_army[color]].values(): break
	
	return [x for x in rook_moves if x not in board[color].values()]


def legal_queen_moves(board, color,queen="queen"):
	
	x , y = board[color][queen]

	queen_moves = legal_rook_moves(board,color,queen) + legal_bishop_moves(board,color,queen)

	return [x for x in queen_moves if x not in board[color].values()]


#print legal_knight_moves(chess_board,"black","knight_2")
#print legal_queen_moves(chess_board,"black")
#print legal_rook_moves(chess_board,"white","rook_1");


#Valid moves are yet to be debugged - - - Piece striking another piece just skipped that block and couldn't skip the other blocks in that horizontal/vertical/diagonal line.


