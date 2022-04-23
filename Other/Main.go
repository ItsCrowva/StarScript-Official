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
	"log"
	"os"
)

func main() {
	if err := os.MkdirAll("a/b/c/d", os.ModePerm); err != nil {
		log.Fatal(err)
	}
}
