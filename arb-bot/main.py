import time
from telegram import Bot

from config import BOT_TOKEN, CHAT_ID, FIXED_STAKE, SCAN_INTERVAL, MIN_PROFIT
from engine.arb import check_arb, calc_stake
from scraper.sporty import get_sporty
from scraper.xbet import get_xbet

bot = Bot(token=BOT_TOKEN)

def send(msg):
    bot.send_message(chat_id=CHAT_ID, text=msg)

while True:
    try:
        sporty_data = get_sporty()
        xbet_data = get_xbet()

        for match in sporty_data:

            if match in xbet_data:

                o1 = sporty_data[match]
                o2 = xbet_data[match]

                arb, profit = check_arb(o1, o2)

                if arb and profit >= MIN_PROFIT:

                    s1, s2 = calc_stake(FIXED_STAKE, o1, o2)

                    msg = f"""
🚨 ARBITRAGE FOUND

Match: {match}

Sporty: {o1}
1XBET: {o2}

Profit: {profit}%

Stake:
Book1: ₦{s1}
Book2: ₦{s2}
"""
                    send(msg)

        time.sleep(SCAN_INTERVAL)

    except Exception as e:
        print("Error:", e)
        time.sleep(5)
