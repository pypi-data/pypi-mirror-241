import bitget.mix.order_api as maxOrderApi
from bitget import bitget_api as baseApi

from bitget.utils.exceptions import BitgetAPIException

if __name__ == '__main__':
    apiKey = "your apiKey"
    secretKey = "your secretKey"
    passphrase = "your passphrase"

    # Demo 1:place order
    maxOrderApi = maxOrderApi.OrderApi(apiKey, secretKey, passphrase)
    try:
        params = {}
        params["symbol"] = "BTCUSDT_UMCBL"
        params["marginCoin"] = "USDT"
        params["side"] = "open_long"
        params["orderType"] = "limit"
        params["price"] = "27012"
        params["size"] = "0.01"
        params["timInForceValue"] = "normal"
        response = maxOrderApi.placeOrder(params)
        print(response)
    except BitgetAPIException as e:
        print("error:" + e.message)

    # Demo 2:place order by post directly
    baseApi = baseApi.BitgetApi(apiKey, secretKey, passphrase)
    try:
        params = {}
        params["symbol"] = "BTCUSDT_UMCBL"
        params["marginCoin"] = "USDT"
        params["side"] = "open_long"
        params["orderType"] = "limit"
        params["price"] = "27012"
        params["size"] = "0.01"
        params["timInForceValue"] = "normal"
        response = baseApi.post("/api/mix/v1/order/placeOrder", params)
        print(response)
    except BitgetAPIException as e:
        print("error:" + e.message)

    # Demo 3:send get request
    try:
        params = {}
        params["productType"] = "umcbl"
        response = baseApi.get("/api/mix/v1/market/contracts", params)
        print(response)
    except BitgetAPIException as e:
        print("error:" + e.message)

    # Demo 4:send get request with no params
    try:
        response = baseApi.get("/api/spot/v1/account/getInfo", {})
        print(response)
    except BitgetAPIException as e:
        print("error:" + e.message)