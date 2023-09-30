import random
import time
import matplotlib.pyplot as plt

print("默认初始本金为5w")
print()
def baccarat_simulation():
    principal = 50000   # 初始本金
    bet = round(random.uniform(50, 350), 2) #下注金额范围
    balance = principal  # 当前余额
    total_profit = 0     # 总盈利
    round_count = 0      # 局数
    casino_profit = 0    # 赌场盈利
    max_balance = principal  # 赚到的最多的余额

    balances = [principal]  # 余额列表（初始余额为本金）
    num_of_rounds = [round_count]   # 赌博次数列表（初始局数）

    while balance > 0 and balance >= bet:
        round_count += 1
        result = random.choice(['闲家', '庄家', '和局'])  # 随机选择一种结果

        if result == '闲家':
            balance += round(bet * 1.0, 2)   # 闲家赔率为1:1
            total_profit += round(bet * 1.0, 2)
        elif result == '庄家':
            balance -= round(bet * 0.95, 2)  # 庄家赔率为1:0.95
            total_profit -= round(bet * 0.95, 2)
        else:
            balance -= round(bet * 8, 2)     # 和局赔率为1:8
            total_profit -= round(bet * 8, 2)

        player_points = random.randint(1, 13)   # 闲家点数，1到13之间的随机数
        banker_points = random.randint(1, 13)   # 庄家点数，1到13之间的随机数

        # 计算抽水
        commission = round(bet * 0.006, 2)
        balance -= commission
        casino_profit += commission

        print(f"局数: {round_count}  |  结果: {result}  |  闲家点数: {player_points}  |  庄家点数: {banker_points}  |  投注金额: {bet:.2f}  |  抽水: {commission:.2f}  |  余额: {max(balance, 0):.2f}  |  盈利: {total_profit:.2f}  |  赌场盈利: {casino_profit:.2f}") 
        
        time.sleep(1)  # 结果间隔1秒钟

        balances.append(max(balance, 0))
        num_of_rounds.append(round_count)

        if balance < principal and balance > max_balance:
            max_balance = balance

        bet *= 2   # 下一局使用倍投策略，下注金额翻倍

    # 绘制走势图
    fig, ax = plt.subplots(figsize=(12, 8))

    x = num_of_rounds
    y = balances
    
    for i in range(len(x) - 1):
        if y[i+1] > y[i]:
            ax.plot([x[i], x[i+1]], [y[i], y[i+1]], color='green', linewidth=1)
        elif y[i+1] < y[i]:
            ax.plot([x[i], x[i+1]], [y[i], y[i+1]], color='red', linewidth=1)
        else:
            ax.plot([x[i], x[i+1]], [y[i], y[i+1]], color='white', linewidth=1)
            
    ax.plot(x, y, 'black', linewidth=1)

    plt.xlabel('Rounds')
    plt.ylabel('Balance')
    plt.title('')
    plt.show()

    print("结束了，你的资产为0")

baccarat_simulation()