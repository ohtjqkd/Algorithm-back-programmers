package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

var (
	r = bufio.NewReader(os.Stdin)
	w = bufio.NewWriter(os.Stdout)
)

func main() {
	defer w.Flush()

	var t, n int
	var a, b int

	fmt.Fscanf(r, "%d\n", &t)
	for i := 0; i < t; i++ {
		var scores [][]int
		ans := 0
		fmt.Fscanf(r, "%d\n", &n)
		for j := 0; j < n; j++ {
			fmt.Fscanf(r, "%d %d\n", &a, &b)
			scores = append(scores, []int{a, b})
		}
		sort.Slice(scores, func(i2, j int) bool {
			return scores[i2][0] < scores[j][0]
		})
		last := scores[0][1]
		for k := 1; k < n; k++ {
			if last < scores[k][1] {
				ans++
			} else {
				last = scores[k][1]
			}
		}
		fmt.Fprintln(w, n-ans)
	}
}

func mergeSort(arr [][]int) [][]int {
	if len(arr) <= 1 {
		return arr
	}

	mid := len(arr) / 2
	left := mergeSort(arr[:mid])
	right := mergeSort(arr[mid:])

	return merge(left, right)
}

func merge(left, right [][]int) [][]int {
	ret := make([][]int, len(left)+len(right))
	l, r := 0, 0

	for {
		if l < len(left) && r < len(right) {
			if left[l][0] < right[r][0] {
				ret[l+r] = left[l]
				l++
			} else {
				ret[l+r] = right[r]
				r++
			}
		} else if l < len(left) {
			ret[l+r] = left[l]
			l++
		} else if r < len(right) {
			ret[l+r] = right[r]
			r++
		} else {
			break
		}
	}
	return ret
}
