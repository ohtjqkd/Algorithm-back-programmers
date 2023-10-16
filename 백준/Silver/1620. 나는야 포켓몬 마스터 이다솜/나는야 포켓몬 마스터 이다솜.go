package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	var n, m int

	reader := bufio.NewReader(os.Stdin)
	s := make(map[string]int, 10000)
	fmt.Fscan(reader, &n, &m)
	a := make([]string, n)

	for i := 0; i < n; i++ {
		var str string
		fmt.Fscan(reader, &str)
		s[str] = i + 1
		a[i] = str
	}

	for i := 0; i < m; i++ {
		var str string
		fmt.Fscan(reader, &str)
		value, err := strconv.Atoi(str)
		if err == nil {
			fmt.Println(a[value-1])
		} else {
			fmt.Println(s[str])
		}
	}
}