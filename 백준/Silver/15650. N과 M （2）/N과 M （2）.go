package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	reader *bufio.Reader = bufio.NewReader(os.Stdin)
	writer *bufio.Writer = bufio.NewWriter(os.Stdout)
)

func main() {
	var n, m int

	defer writer.Flush()
	fmt.Scan(&n, &m)

	for i := 1; i <= n; i++ {
		pick(n, m-1, []int{i})
	}
}

func pick(n, m int, arr []int) {
	if m == 0 {
		for i := 0; i < len(arr); i++ {
			if i == len(arr)-1 {
				fmt.Fprintln(writer, arr[i])
			} else {
				fmt.Fprint(writer, arr[i], " ")
			}
		}
	} else {
		for i := 1; i <= n; i++ {
			if !contains(arr, i) && i > arr[len(arr)-1] {
				pick(n, m-1, append(arr, i))
			}
		}
	}
}

func contains(arr []int, i int) bool {
	for j := 0; j < len(arr); j++ {
		if arr[j] == i {
			return true
		}
	}
	return false
}
