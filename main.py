#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tabulate import tabulate

FREE_MONEY_RATE = 0.04
INV_30_DAYS_RATE = 0.08
INV_90_DAYS_RATE = 0.092
INV_360_DAYS_RATE = 0.11

data = []

def print_data():
    print(tabulate(data, headers=['Year', 'Amount']))

def main():
    free_money = 7960
    inv_30_days = free_money
    inv_90_days = 7961.15
    inv_360_days = 23883.44
    initial_investment = free_money + inv_30_days + inv_90_days + inv_360_days
    data.append([0, f'${initial_investment:,.2f}'])

    years_invested = 40
    months_invested = years_invested * 12

    current_month = 1

    monthly_profit = lambda money, rate: money * rate / 12

    while current_month <= months_invested:
        interest_gained = monthly_profit(free_money, FREE_MONEY_RATE)
        interest_gained += monthly_profit(inv_30_days, INV_30_DAYS_RATE)
        interest_gained += monthly_profit(inv_90_days, INV_90_DAYS_RATE)
        interest_gained += monthly_profit(inv_360_days, INV_360_DAYS_RATE)

        current_total = free_money + inv_30_days + interest_gained

        if current_month % 12 == 0:
            current_total += inv_90_days + inv_360_days
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
            current_money = free_money + inv_30_days + inv_90_days + inv_360_days
            data.append([current_month / 12, f'${current_money:,.2f}'])

        current_month += 1

    print_data()

if __name__ == "__main__":
    main()
