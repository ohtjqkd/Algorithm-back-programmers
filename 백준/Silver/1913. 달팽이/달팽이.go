package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	var n, t, cal int
	var dx, dy = [4]int{1, 0, -1, 0}, [4]int{0, 1, 0, -1}
	var curr = [2]int{0, 0}
	var tLoc []string

	fmt.Scanf("%d\n", &n)
	fmt.Scanf("%d\n", &t)

	dir := 0

	board := make([][]string, n)
	for i := 0; i < n; i++ {
		board[i] = make([]string, n)
	}
	for i := 0; i < n*n; i++ {
		x, y := curr[0], curr[1]
		cal = n*n - i
		board[x][y] = strconv.Itoa(cal)
		if cal == t {
			tLoc = []string{strconv.Itoa(x + 1), strconv.Itoa(y + 1)}
		}
		xx, yy := x+dx[dir], y+dy[dir]
		if xx < 0 || xx >= n || yy < 0 || yy >= n || board[xx][yy] != "" {
			dir = (dir + 1) % 4
		}
		curr = [2]int{x + dx[dir], y + dy[dir]}
	}
	for _, v := range board {
		fmt.Println(strings.Join(v, " "))
	}
	fmt.Println(strings.Join(tLoc, " "))
}
