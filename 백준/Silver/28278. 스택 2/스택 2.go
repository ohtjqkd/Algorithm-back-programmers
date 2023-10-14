package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type stack struct {
	s []int
}

func (s *stack) push(i int) {
	s.s = append(s.s, i)
}

func (s *stack) pop() int {
	if len(s.s) == 0 {
		return -1
	}

	i := s.s[len(s.s)-1]
	s.s = s.s[:len(s.s)-1]
	return i
}

func (s *stack) size() int {
	return len(s.s)
}

func (s *stack) empty() int {
	if len(s.s) == 0 {
		return 1
	}
	return 0
}

func (s *stack) top() int {
	if len(s.s) == 0 {
		return -1
	}
	return s.s[len(s.s)-1]
}

func main() {
	var n int
	var s stack
	var cmd []string

	fmt.Scan(&n)
	scanner := bufio.NewScanner(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	for i := 0; i < n; i++ {
		scanner.Scan()
		cmd = strings.Split(scanner.Text(), " ")
		c, _ := strconv.ParseInt(cmd[0], 10, 64)
		switch c {
		case 1:
			v, _ := strconv.ParseInt(cmd[1], 10, 64)
			s.push(int(v))
		case 2:
			writer.WriteString(strconv.Itoa(s.pop()) + "\n")
		case 3:
			writer.WriteString(strconv.Itoa(s.size()) + "\n")
		case 4:
			writer.WriteString(strconv.Itoa(s.empty()) + "\n")
		case 5:
			writer.WriteString(strconv.Itoa(s.top()) + "\n")
		}
	}
    writer.Flush()
}
