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
	defer writer.Flush()
	var N, M int
	fmt.Fscanf(reader, "%d %d\n", &N, &M)

	pick(N, M, []int{})
}

func pick(n, m int, arr []int) {
	if m == 0 {
		for i := 0; i < len(arr); i++ {
			fmt.Fprintf(writer, "%d ", arr[i])
		}
		fmt.Fprintln(writer)
	} else {
		for i := 1; i <= n; i++ {
			if !contains(arr, i) {
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
