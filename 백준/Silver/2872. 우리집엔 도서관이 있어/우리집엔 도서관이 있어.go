package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	r = bufio.NewReader(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
)

func main() {
	defer w.Flush()

	var n, tmp, ans, nxt int
	var l []int

	fmt.Fscan(r, &n)
	ans, nxt = 0, n
	for i := 0; i < n; i++ {
		fmt.Fscan(r, &tmp)
		l = append(l, tmp)
	}
	for i := n - 1; i >= 0; i-- {
		if l[i] == nxt {
			nxt--
		} else {
			ans++
		}
	}
	fmt.Fprintln(w, ans)
}
