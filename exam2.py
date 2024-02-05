# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 20:34:19 2024

@author: USER
"""

from banks import Banks,信義_Banks

bank1 = Banks('jay')                  # 定義Banks類別物件
print(bank1.bank_title())             # 列印銀行名稱
bank1.save_money(500)                   # 存錢
bank1.get_balance()                     # 列出存款金額
bank = 信義_Banks('Hung')             # 定義信義_Banks類別物件
print(bank.bank_title())                # 列印銀行名稱