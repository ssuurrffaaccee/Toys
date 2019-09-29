package main

import (
	"fmt"
	"sync"
)



var que=make(chan func(),100)



var mu sync.Mutex


func f1(){
	for true {
		fmt.Println("put cmd1")
		que <- func(){
			fmt.Println("do cmd1")
		}
		fmt.Println("put cmd2")
		que <- func(){
			fmt.Println("do cmd2")
		}
		mu.Lock()
		fmt.Println("lock")
		que <- func(){
			mu.Unlock()
			fmt.Println("unlock")
		}
		mu.Lock()
		fmt.Println("lock")
		mu.Unlock()
	}
}
func f2(){
	for true {
		fp:=<-que
		fp()
	}
}

func main(){
	go f2()
	f1()
}

