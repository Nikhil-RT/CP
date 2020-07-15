// # Write the function pascalsTriangleValue(row, col) 
// # that takes int values row and col, and returns the 
// # value in the given row and column of Pascal's 
// # Triangle where the triangle starts at row 0, and 
// # each row starts at column 0. If either row or col 
// # are not legal values, return None, instead of crashing. 

class pascaltrianglevalue {
	public int fun_pascaltrianglevalue(int row, int col){
		// your code goes here
		int res = 1;
		if (row < col) {
			return 0;
		}
		if (col > (row - col)) {
			col = row - col;
		}
		int i = 0;
		while(i < col) {
			res = res*(row - i);
			res = res/(i + 1);
			i++;
		}
		return res;
	}

}