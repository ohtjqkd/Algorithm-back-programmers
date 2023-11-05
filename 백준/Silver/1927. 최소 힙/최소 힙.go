package main

import (
	"bufio"
	"fmt"
	"os"
)

var (
	r *bufio.Reader = bufio.NewReader(os.Stdin)
	w *bufio.Writer = bufio.NewWriter(os.Stdout)
)

func main() {
	var n, cmd int

	defer w.Flush()

	fmt.Fscanf(r, "%d\n", &n)

	heap := NewHeap()

	for i := 0; i < n; i++ {
		fmt.Fscanf(r, "%d\n", &cmd)
		if cmd == 0 {
			fmt.Fprintln(w, heap.Pop().value)
		} else {
			heap.Push(NewNode(cmd))
		}
	}
}

type Node struct {
	value int
}

func NewNode(value int) *Node {
	return &Node{value}
}

func (n *Node) Less(a *Node) bool {
	return n.value <= a.value
}

type Heap struct {
	nodes []*Node
	size  int
}

func NewHeap() *Heap {
	return &Heap{}
}

func (h *Heap) Size() int {
	return h.size
}

func (h *Heap) swap(a, b int) {
	h.nodes[a], h.nodes[b] = h.nodes[b], h.nodes[a]
}

func (h *Heap) up(a int) {
	curr := a
	par := (curr - 1) / 2
	for curr != 0 && h.nodes[curr].Less(h.nodes[par]) {
		h.swap(curr, par)
		curr = par
		par = (curr - 1) / 2
	}
}

func (h *Heap) down() {
	var curr, left, right, nxt int
	curr = 0
	for left < h.size {
		left = curr*2 + 1
		right = curr*2 + 2
		nxt = left
		if left >= h.size {
			break
		}
		if right < h.size && h.nodes[right].Less(h.nodes[left]) {
			nxt = right
		}
		if !h.nodes[nxt].Less(h.nodes[curr]) {
			break
		}
		h.swap(curr, nxt)
		curr = nxt
	}
}

func (h *Heap) Push(n *Node) {
	h.nodes = append(h.nodes, n)
	h.size++
	h.up(len(h.nodes) - 1)
}

func (h *Heap) Pop() *Node {
	if h.size == 0 {
		return &Node{value: 0}
	}
	ret := h.nodes[0]
	h.swap(0, len(h.nodes)-1)
	h.nodes = h.nodes[:h.size-1]
	h.size--
	h.down()
	return ret
}
