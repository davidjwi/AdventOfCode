package main

import (
	"bufio"
	"fmt"
	"log"
	"math"
	"os"
	"strconv"
	"strings"
)

func check_difference(report []int) bool {
	for i := 0; i < len(report)-1; i++ {
		curr := report[i]
		next := report[i+1]
		diff := math.Abs(float64(curr - next))
		if diff < 1 || diff > 3 {
			return false
		}
	}
	return true
}

func main() {
	println("Hello World!")
	file, err := os.Open("day2_sample_input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	var reports [][]int

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		parts := strings.Fields(line)
		var report_line []int
		for _, n := range parts {
			int_num, err := strconv.Atoi(n)
			if err != nil {
				log.Fatalf("Failed to parse")
			}
			report_line = append(report_line, int_num)
		}
		reports = append(reports, report_line)
	}
	fmt.Println(reports)

	//	safe_reports = [][]int
	//	not_safe_reports = [][]int

	for _, r := range reports {
		if check_difference(r) {
			fmt.Println("Check Diff Returned True")
		}

	}

}
