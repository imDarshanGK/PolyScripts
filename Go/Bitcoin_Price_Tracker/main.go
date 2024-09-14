package main

import (
	"encoding/json"
	"fmt"
	"net/http"
)

type PriceResponse struct {
	Bitcoin struct {
		USD float64 `json:"usd"`
	} `json:"bitcoin"`
}

func main() {
	giveCurrentPriceOfBitcoin()
}

func giveCurrentPriceOfBitcoin() {

	url := "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

	resp, err := http.Get(url)
	if err != nil {
		fmt.Printf("Error fetching price: %v\n", err)
		return
	}
	defer resp.Body.Close()

	var priceResp PriceResponse
	if err := json.NewDecoder(resp.Body).Decode(&priceResp); err != nil {
		fmt.Printf("Error decoding response: %v\n", err)
		return
	}

	fmt.Printf("1 BTC = $%.2f\n", priceResp.Bitcoin.USD)
}
