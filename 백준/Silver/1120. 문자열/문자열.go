package main

import (
	"fmt"
)

func main() {
	var a, b string

	ans := 0
	fmt.Scan(&a, &b)
	for i := 0; i <= len(b)-len(a); i++ {
		cnt := countSame(a, b, i)
		if cnt > ans {
			ans = cnt
		}
	}
	fmt.Println(len(a) - ans)
}

func countSame(a, b string, si int) int {
	var count int
	for i := 0; i < len(a); i++ {
		if a[i] == b[i+si] {
			count++
		}
	}
	return count
}
