package main

import (
	"fmt"
	"math/rand"
)

func main() {
	var startGame int
	for {
		fmt.Println("--------0. Exit game--------------------")
		fmt.Println("--------1. Continue game--------------------")
		fmt.Scanf("%d\n", &startGame)
		if startGame == 0 {
			return
		}

		randomStart := rand.Intn(2)
		fmt.Println(randomStart)
		var x, y int
		initTableChess := [3][3]string{}

		if randomStart == 1 {
			startX := rand.Intn(3)
			startY := rand.Intn(3)
			initTableChess[startX][startY] = "X"
			displayChess(initTableChess)
			flag := 1
			for {
				for {
					fmt.Println("Player: ")
					fmt.Scanf("%d\n", &x)
					fmt.Scanf("%d\n", &y)
					if initTableChess[x][y] != "" {
						fmt.Println("Ô này đánh rồi cha nội")
						continue
					} else {
						initTableChess[x][y] = "O"
						break
					}
				}

				displayChess(initTableChess)
				flag++
				if CheckGameOver(initTableChess) != "" {
					fmt.Println(CheckGameOver(initTableChess))
					break
				}
				if flag == 9 {
					fmt.Println("Equal Game")
					break
				}

				initTableChess, _ = minimax(initTableChess, 1, true)

				displayChess(initTableChess)
				flag++
				if CheckGameOver(initTableChess) != "" {
					fmt.Println(CheckGameOver(initTableChess))
					break
				}
				if flag == 9 {
					fmt.Println("Equal Game")
					break
				}
			}
		} else {
			displayChess(initTableChess)
			flag := 1
			for {
				for {
					fmt.Println("Player: ")
					fmt.Scanf("%d\n", &x)
					fmt.Scanf("%d\n", &y)
					if initTableChess[x][y] != "" {
						fmt.Println("Ô này đánh rồi cha nội")
						continue
					} else {
						initTableChess[x][y] = "O"
						break
					}
				}

				displayChess(initTableChess)
				flag++
				if CheckGameOver(initTableChess) != "" {
					fmt.Println(CheckGameOver(initTableChess))
					break
				}
				if flag == 9 {
					fmt.Println("Equal Game")
					break
				}

				initTableChess, _ = minimax(initTableChess, 1, true)
				fmt.Println(initTableChess)

				displayChess(initTableChess)
				flag++
				if CheckGameOver(initTableChess) != "" {
					fmt.Println(CheckGameOver(initTableChess))
					break
				}
				if flag == 9 {
					fmt.Println("Equal Game")
					break
				}
			}
		}
	}
}

func CheckGameOver(initTableChess [3][3]string) string {
	if CheckWinNgang(initTableChess, "X") || CheckWinDoc(initTableChess, "X") || CheckWinCheoNguoc(initTableChess, "X") || CheckWinCheoXuoi(initTableChess, "X") {
		return "X Win"
	}
	if CheckWinNgang(initTableChess, "O") || CheckWinDoc(initTableChess, "O") || CheckWinCheoNguoc(initTableChess, "O") || CheckWinCheoXuoi(initTableChess, "O") {
		return "O Win"
	}
	return ""
}


func stateListFunc(tableChess [3][3]string, p string) []interface{} {
	temp := tableChess
	var stateList []interface{}
	for i := 0; i < len(temp); i++ {
		for j := 0; j < len(temp); j++ {
			if temp[i][j] == "" {
				temp[i][j] = p
				stateList = append(stateList, temp)
				temp[i][j] = ""
			}
		}
	}
	return stateList
}

func displayChess(tableChess [3][3]string) {
	viewChess := ""
	for i := 0; i < len(tableChess); i++ {
		viewChess += " - "
		for j := 0; j < len(tableChess); j++ {
			if tableChess[i][j] == "" {
				viewChess += " "
			}
			viewChess += tableChess[i][j] + " - "
		}
		viewChess += "\n"
	}
	fmt.Println(viewChess)
}

func CheckWinNgang(tableChess [3][3]string, p string) bool {
	for i := 0; i < len(tableChess); i++ {
		h := 0
		for j := 0; j < len(tableChess); j++ {
			if tableChess[i][j] == p {
				h += 1
			}
		}
		if h == 3 {
			return true
		}
	}
	return false
}

func CheckWinDoc(tableChess [3][3]string, p string) bool {
	for i := 0; i < len(tableChess); i++ {
		h := 0
		for j := 0; j < len(tableChess); j++ {
			if tableChess[j][i] == p {
				h += 1
			}
		}
		if h == 3 {
			return true
		}
	}
	return false
}

func CheckWinCheoXuoi(tableChess [3][3]string, p string) bool {
	h := 0
	for i := 0; i < len(tableChess); i++ {
		if tableChess[i][i] == p {
			h += 1
		}
	}
	if h == 3 {
		return true
	}
	return false
}

func CheckWinCheoNguoc(tableChess [3][3]string, p string) bool {
	h := 0
	for i := 0; i < len(tableChess); i++ {
		if tableChess[i][len(tableChess)-i-1] == p {
			h += 1
		}
	}
	if h == 3 {
		return true
	}
	return false
}


func minimax(tableChess [3][3]string, depth int, isMaximizingPlayer bool) ([3][3]string, int) {
	var bestValue int
	var stateRs [3][3]string
	if CheckGameOver(tableChess) == "X Win" {
		return tableChess, 10
	}
	if CheckGameOver(tableChess) == "O Win" {
		return tableChess, -10
	}
	if CheckGameOver(tableChess) == "" && FinishGame(tableChess) == 9 {
		return tableChess, 0
	}

	if isMaximizingPlayer {
		bestValue = -1000
		stateListWinX := stateListFunc(tableChess, "X")
		for i := 0; i < len(stateListWinX); i++ {
			_, value := minimax(stateListWinX[i].([3][3]string), depth+1, false)
			if value > bestValue {
				bestValue = value
				stateRs = stateListWinX[i].([3][3]string)
			}
		}
		return stateRs, bestValue
	} else {
		bestValue = 1000
		stateListLostO := stateListFunc(tableChess, "O")
		for i := 0; i < len(stateListLostO); i++ {
			_, value := minimax(stateListLostO[i].([3][3]string), depth+1, true)
			if value < bestValue {
				bestValue = value
				stateRs = stateListLostO[i].([3][3]string)
			}
		}
		return stateRs, bestValue
	}
}

func FinishGame(tableChess [3][3]string) int {
	flag := 0
	for i := 0; i < len(tableChess); i++ {
		for j := 0; j < len(tableChess); j++ {
			if tableChess[i][j] != "" {
				flag++
			}
		}
	}
	return flag
}