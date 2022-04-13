/*
	This is the GoLang version of the StrScr Executer.

	Progress on this started on the 5th Recode of StrScr: Python and development for this is supposed to be worked on alongisde one another.
*/

// Timeline:
/* Alpha1 [
	30-03-22 - 12:47pm
	31-03-22 - 2:17pm
]
*/
package main

import (
	"fmt"
	"os"
	"path/filepath"
)

func main() {
	ex, err := os.Executable()
	if err != nil {
		panic(err)
	}
	exPath := filepath.Dir(ex)
	fmt.Println(exPath)
}
