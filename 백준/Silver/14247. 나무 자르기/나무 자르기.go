package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

var r = bufio.NewReader(os.Stdin)

func main() {
	var n, v int
	var a, b []int

	ans := 0
	fmt.Fscan(r, &n)
	for i := 0; i < n; i++ {
		fmt.Fscan(r, &v)
		a = append(a, v)
	}
	for i := 0; i < n; i++ {
		fmt.Fscan(r, &v)
		b = append(b, v)
	}
	sort.Slice(b, func(i, j int) bool {
		return b[i] < b[j]
	})
	for i := 0; i < n; i++ {
		ans += a[i] + b[i]*i
	}
	fmt.Println(ans)
}
