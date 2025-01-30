#!/usr/bin/env python3
import random
import time

colors = ['\033[32m', '\033[92m', '\033[34m']  # سبز، سبز روشن، آبی
reset = '\033[0m'

def matrix_rain():
    print("\033[?25l")  # مخفی کردن مکان‌نما
    try:
        while True:
            print(
                "".join(
                    random.choice([chr(int(random.uniform(0x30A1, 0x30FA))) if random.random() > 0.7 else ' ' for _ in range(40)])
                    + random.choice(colors) 
                    + ('/' if random.random() > 0.5 else '\\') 
                    + reset
                )
                for _ in range(20)
            ), end='\r')
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\033[?25h")  # نمایش مجدد مکان‌نما

matrix_rain()
