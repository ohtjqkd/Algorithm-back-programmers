package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

var (
	reader *bufio.Reader = bufio.NewReader(os.Stdin)
	writer *bufio.Writer = bufio.NewWriter(os.Stdout)
)

func main() {
	var na, nb, v int
	var ans []int

	defer writer.Flush()

	fmt.Fscanf(reader, "%d %d\n", &na, &nb)

	dic := make(map[int]bool, 500_000)
	for i := 0; i < na; i++ {
		fmt.Fscan(reader, &v)
		dic[v] = true
	}

	for i := 0; i < nb; i++ {
		fmt.Fscan(reader, &v)
		delete(dic, v)
	}

	for k := range dic {
		ans = append(ans, k)
	}

	sort.Slice(ans, func(i, j int) bool {
		return ans[i] < ans[j]
	})

	fmt.Fprintln(writer, len(ans))
	for i, v := range ans {
		if i+1 == len(ans) {
			fmt.Fprintln(writer, v)
		} else {
			fmt.Fprintf(writer, "%d ", v)
		}
	}
}
