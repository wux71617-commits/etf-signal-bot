from strategy import get_signal

etfs = {
    "QQQ": "纳指ETF",
    "KWEB": "恒生科技ETF",
    "SOXX": "半导体ETF",
    "XLU": "电力ETF"
}

print("\n📊 ETF信号\n")

for code, name in etfs.items():
    signal, pos = get_signal(code)
    print(f"{name}：{signal}（仓位 {pos}）")
