package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

var (
	reader *bufio.Reader = bufio.NewReader(os.Stdin)
	writer *bufio.Writer = bufio.NewWriter(os.Stdout)
)

func main() {
	defer writer.Flush()

	// var tmp string
	var deq []string
	var N int

	fmt.Fscanln(reader, &N)
	for {
		line, _, _ := reader.ReadLine()
		l := string(line)
		cmds := strings.Split(l, " ")
		switch cmds[0] {
		case "push":
			push(&deq, cmds[1])
		case "pop":
			fmt.Fprintln(writer, pop(&deq))
		case "size":
			fmt.Fprintln(writer, size(&deq))
		case "empty":
			fmt.Fprintln(writer, empty(&deq))
		case "front":
			fmt.Fprintln(writer, front(&deq))
		case "back":
			fmt.Fprintln(writer, back(&deq))
		default:
			return
		}
	}
}

func push(arr *[]string, s string) {
	*arr = append(*arr, s)
}

func pop(arr *[]string) string {
	if len(*arr) == 0 {
		return "-1"
	}
	ret := (*arr)[0]
	*arr = (*arr)[1:]
	return ret
}

func empty(arr *[]string) string {
	if len(*arr) == 0 {
		return "1"
	}
	return "0"
}

func front(arr *[]string) string {
	if len(*arr) == 0 {
		return "-1"
	}
	return (*arr)[0]
}

func back(arr *[]string) string {
	if len(*arr) == 0 {
		return "-1"
	}
	return (*arr)[len(*arr)-1]
}

func size(arr *[]string) string {
	return fmt.Sprintf("%d", len(*arr))
}
