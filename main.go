package main

import "fmt"

func main() {
	var n int 
	var age int
	var name string
    // fmt.Println("name:",name)
	// fmt.Println("age:",age)

	fmt.Scanf("%s %d",&name,&age)
	fmt.Println("updated age: ",age)
	fmt.Println("new name:",name)
	fmt.Println("new name:"+name+", updated age: ",age,", squared age: ",age*age)
	fmt.Printf("new name:%v , updated age: %v \n",name,age)
	fmt.Println("enter a number:")
	fmt.Scanf("%d",&n)
	if n%2==0{
		fmt.Println("number is divisible by 2")
	}else if n%3==0{
		fmt.Println("number is divisible by 3")
	}else {
		fmt.Println("number is not divisible by 2 and 3")
	}
	switch n{
	case 1:
		fmt.Println("number is 1")
	case 2:
		fmt.Println("number is 2")
	case 3:
		fmt.Println("number is 3")	
	case 4:
		fmt.Println("number is 4")
	case 5:
		fmt.Println("number is 5")	
	default:
		fmt.Println("number is greater than 5")
	}

	for i:=1;i<=5;i++{
		fmt.Println("value of i:",i)
	}

}
