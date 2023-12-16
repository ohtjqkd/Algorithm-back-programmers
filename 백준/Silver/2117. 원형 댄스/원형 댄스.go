package main

import (
	"fmt"
	"math"
)

func main() {
	var n int

	fmt.Scan(&n)
	convertN := int(math.Ceil(float64(n) / 2))
	ans := convertN * (convertN - 1)
	if n%2 == 1 {
		ans -= (convertN - 1)
	}
	fmt.Println(ans)
}