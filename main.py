#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tabulate import tabulate

FREE_MONEY_RATE = 0.04
INV_30_DAYS_RATE = 0.08
INV_90_DAYS_RATE = 0.092
INV_360_DAYS_RATE = 0.11
MONTHLY_RATE = 0.1312
YEARS_INVESTED = 40
MONTHS_INVESTED = YEARS_INVESTED * 12

data = []

def print_data():
    print(tabulate(data, headers=['Year', 'Amount']))

def main():
    free_money = 6606.38
    inv_30_days = 9909.57
    inv_90_days = 15535.25
    inv_360_days = 32146.10
    initial_investment = free_money + inv_30_days + inv_90_days + inv_360_days
    data.append([0, f'${initial_investment:,.2f}'])

    monthly_profit = lambda money, rate: money * rate / 12

    outside_inv = 8000
    outside_inv_profit = lambda: monthly_profit(outside_inv, MONTHLY_RATE)
    monthly_deposits = outside_inv_profit()

    for current_month in range(1, MONTHS_INVESTED + 1):
        interest_gained = monthly_profit(free_money, FREE_MONEY_RATE)
        interest_gained += monthly_profit(inv_30_days, INV_30_DAYS_RATE)
        interest_gained += monthly_profit(inv_90_days, INV_90_DAYS_RATE)
        interest_gained += monthly_profit(inv_360_days, INV_360_DAYS_RATE)

        current_total = free_money + inv_30_days + interest_gained + monthly_deposits

        if current_month % 12 == 0:
            current_total += inv_90_days + inv_360_days
            invest = (monthly_deposits * 12 // 1000) * 1000
            current_total -= invest
            outside_inv += invest
            monthly_deposits = outside_inv_profit()
            free_money = current_total * 0.025
            inv_30_days = current_total * 0.075
            inv_90_days = current_total * 0.3
            inv_360_days = current_total * 0.6
        elif current_month % 3 == 0:
            current_total += inv_90_days
            free_money = current_total * 0.1
            inv_30_days = current_total * 0.3
            inv_90_days = current_total * 0.6
        else:
            free_money = current_total * 0.4
            inv_30_days = current_total * 0.6

        if current_month % 12 == 0:
            current_money = free_money + inv_30_days + inv_90_days + inv_360_days + outside_inv
            data.append([current_month / 12, f'${current_money:,.2f}'])

    print_data()

if __name__ == "__main__":
    main()
