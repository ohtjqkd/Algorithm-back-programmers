package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	r  = bufio.NewReader(os.Stdin)
	w  = bufio.NewWriter(os.Stdout)
	in = bufio.NewScanner(os.Stdin)
)

func main() {
	defer w.Flush()

	var n, tmp, ans, nxt int
	var l []int

	n = nextInt()
	ans, nxt = 0, n
	for i := 0; i < n; i++ {
		tmp = nextInt()
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

func nextInt() int {
	in.Scan()
	r := 0
	for _, c := range in.Bytes() {
		r = r*10 + int(c-'0')
	}
	return r
}