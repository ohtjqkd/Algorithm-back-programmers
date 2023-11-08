package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

var (
	r = bufio.NewReader(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
)

func main() {
	defer w.Flush()

	var t, n int

	fmt.Fscanf(r, "%d\n", &t)
	for i := 0; i < t; i++ {
		var scores [][]int
		ans := 0
		fmt.Fscanf(r, "%d\n", &n)
		for j := 0; j < n; j++ {
			var a, b int
			fmt.Fscanf(r, "%d %d\n", &a, &b)
			scores = append(scores, []int{a, b})
		}
		sort.Slice(scores, func(i2, j int) bool {
			return scores[i2][0] < scores[j][0]
		})
		last := scores[0][1]
		for k := 1; k < n; k++ {
			if last < scores[k][1] {
				ans++
			} else {
				last = scores[k][1]
			}
		}
		fmt.Fprintln(w, n-ans)
	}
}
