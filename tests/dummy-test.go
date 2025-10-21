package main

import (
	"fmt"
	"log"
	"os"
	"time"

	"github.com/tebeka/selenium"
	"github.com/tebeka/selenium/chrome"
)

func main() {
	executorURL := "http://localhost:8888/"
	if len(os.Args) > 1 {
		executorURL = os.Args[1]
	}

	caps := selenium.Capabilities{"browserName": "chrome"}
	chromeCaps := chrome.Capabilities{
		Args: []string{"--start-maximized"},
	}
	caps.AddChrome(chromeCaps)

	// Connect to Selenium server / remote driver
	driver, err := selenium.NewRemote(caps, executorURL)
	if err != nil {
		log.Fatalf("Failed to connect to WebDriver: %v", err)
	}
	defer driver.Quit()

	if err := driver.Get("https://www.example.com"); err != nil {
		log.Fatalf("Failed to open website: %v", err)
	}

	// Wait for <h1> tag up to 10 seconds
	var elem selenium.WebElement
	for i := 0; i < 10; i++ {
		elem, err = driver.FindElement(selenium.ByCSSSelector, "h1")
		if err == nil {
			break
		}
		time.Sleep(time.Second)
	}
	if err != nil {
		log.Fatalf("Timeout: <h1> not found: %v", err)
	}

	title, _ := driver.Title()
	if title != "Example Domain" {
		log.Fatalf("Test failed: expected title 'Example Domain', got '%s'", title)
	}

	link, err := driver.FindElement(selenium.ByCSSSelector, "a")
	if err != nil {
		log.Fatalf("Link not found: %v", err)
	}
	text, _ := link.Text()
	fmt.Println("Found link with text:", text)
	fmt.Println("✅ Test passed: Example.com loaded and title is as expected.")
}
