package main

import (
	"fmt"
	"sync"
)

func main() {
	var a, b string

	ans := 0
	var wg sync.WaitGroup
	fmt.Scan(&a, &b)
	wg.Add(len(b) - len(a) + 1)
	for i := 0; i < len(b)-len(a)+1; i++ {
		go func(a, b string, si int, ans *int) {
			defer wg.Done()
			var count int
			for i := 0; i < len(a); i++ {
				if a[i] == b[i+si] {
					count++
				}
			}
			if *ans < count {
				*ans = count
			}
		}(a, b, i, &ans)
	}
	wg.Wait()
	fmt.Println(len(a) - ans)
}
