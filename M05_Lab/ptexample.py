# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 19:04:09 2023

@author: mrapp
"""

#print("The bi-weekly pay schedule for 2023 and the allowance \n and savings amount based on a $2,000 dollar check.")
#print("Spending 25% on allowance bi-weekly and saving 15% bi-weekly.")
from prettytable import PrettyTable
byWeekly_payDates = ["1/13/23", "1/27/23", "2/10/23", "2/24/23", "3/10/23", "3/24/23","4/06/23", "4/21/23",
                     "5/05/23","5/19/23","6/02/23","6/16/23","6/30/23","7/14/23","7/28/23",
                     "8/11/23","8/25/23","9/08/23","9/22/23","10/06/23","10/20/23",
                     "11/03/23","11/17/23","12/01/23","12/15/23"]

print("The bi-weekly pay schedule for 2023 and the allowance \n and savings amount based on a $2,000 dollar check.")
print("Spending 25% on allowance bi-weekly and saving 15% bi-weekly.")
print("Made using PrettyTable in Python")





allowanceTable = PrettyTable(["Date","Paycheck amount", "Allowance %", "Amount"])
allowanceTable.add_row([byWeekly_payDates[0],"$2000" , "25%", "$500"])
allowanceTable.add_row([byWeekly_payDates[1],"$2000" , "25%", "$500"])
allowanceTable.add_row([byWeekly_payDates[2],"$2000" , "25%", "$500"])
allowanceTable.add_row([byWeekly_payDates[3],"$2000" , "25%", "$500"])
allowanceTable.add_row([byWeekly_payDates[4],"$2000" , "25%", "$500"])
allowanceTable.add_row([byWeekly_payDates[5],"$2000" , "25%", "$500"])
allowanceTable.add_row([byWeekly_payDates[6],"$2000" , "25%", "$500"])
allowanceTable.add_row([byWeekly_payDates[7],"$2000" , "25%", "$500"])
allowanceTable.add_row([byWeekly_payDates[7],"$2000" , "25%", "$500"])
allowanceTable.add_row([byWeekly_payDates[8],"$2000" , "25%", "$500"])
allowanceTable.add_row([byWeekly_payDates[9],"$2000" , "25%", "$500"])
allowanceTable.add_row([byWeekly_payDates[10],"$2000" , "25%", "$500"])
allowanceTable.add_row([byWeekly_payDates[11],"$2000" , "25%", "$500"])
allowanceTable.add_row([byWeekly_payDates[12],"$2000" , "25%", "$500"])
allowanceTable.add_row([byWeekly_payDates[13],"$2000" , "25%", "$500"])
allowanceTable.add_row([byWeekly_payDates[14],"$2000" , "25%", "$500"])
allowanceTable.add_row([byWeekly_payDates[15],"$2000" , "25%", "$500"])
allowanceTable.add_row([byWeekly_payDates[16],"$2000" , "25%", "$500"])
allowanceTable.add_row([byWeekly_payDates[17],"$2000" , "25%", "$500"])
allowanceTable.add_row([byWeekly_payDates[18],"$2000" , "25%", "$500"])
allowanceTable.add_row([byWeekly_payDates[19],"$2000" , "25%", "$500"])
allowanceTable.add_row([byWeekly_payDates[20],"$2000" , "25%", "$500"])
allowanceTable.add_row([byWeekly_payDates[21],"$2000" , "25%", "$500"])
allowanceTable.add_row([byWeekly_payDates[22],"$2000" , "25%", "$500"])
allowanceTable.add_row([byWeekly_payDates[23],"$2000" , "25%", "$500"])
allowanceTable.add_row([byWeekly_payDates[24],"$2000" , "25%", "$500"])
allowanceTable.add_row(["Yearly", "allowance", "total", "$12,000"] )


savingsTable = PrettyTable(["Date", "Paycheck amount", "Savings %", "Amount"])
savingsTable.add_row([byWeekly_payDates[1],"$2000" , "15%", "$300"])
savingsTable.add_row([byWeekly_payDates[0],"$2000" , "15%", "$300"])
savingsTable.add_row([byWeekly_payDates[1],"$2000" , "15%", "$300"])
savingsTable.add_row([byWeekly_payDates[2],"$2000" , "1%", "$300"])
savingsTable.add_row([byWeekly_payDates[3],"$2000" , "15%", "$300"])
savingsTable.add_row([byWeekly_payDates[4],"$2000" , "15%", "$300"])
savingsTable.add_row([byWeekly_payDates[5],"$2000" , "15%", "$300"])
savingsTable.add_row([byWeekly_payDates[6],"$2000" , "15%", "$300"])
savingsTable.add_row([byWeekly_payDates[7],"$2000" , "15%", "$300"])
savingsTable.add_row([byWeekly_payDates[7],"$2000" , "15%", "$300"])
savingsTable.add_row([byWeekly_payDates[8],"$2000" , "15%", "$300"])
savingsTable.add_row([byWeekly_payDates[9],"$2000" , "15%", "$300"])
savingsTable.add_row([byWeekly_payDates[10],"$2000" , "15%", "$300"])
savingsTable.add_row([byWeekly_payDates[11],"$2000" , "15%", "$300"])
savingsTable.add_row([byWeekly_payDates[12],"$2000" , "15%", "$300"])
savingsTable.add_row([byWeekly_payDates[13],"$2000" , "15%", "$300"])
savingsTable.add_row([byWeekly_payDates[14],"$2000" , "15%", "$300"])
savingsTable.add_row([byWeekly_payDates[15],"$2000" , "15%", "$300"])
savingsTable.add_row([byWeekly_payDates[16],"$2000" , "15%", "$300"])
savingsTable.add_row([byWeekly_payDates[17],"$2000" , "15%", "$300"])
savingsTable.add_row([byWeekly_payDates[18],"$2000" , "15%", "$300"])
savingsTable.add_row([byWeekly_payDates[19],"$2000" , "15%", "$300"])
savingsTable.add_row([byWeekly_payDates[20],"$2000" , "15%", "$300"])
savingsTable.add_row([byWeekly_payDates[21],"$2000" , "15%", "$300"])
savingsTable.add_row([byWeekly_payDates[22],"$2000" , "15%", "$300"])
savingsTable.add_row([byWeekly_payDates[23],"$2000" , "15%", "$300"])
savingsTable.add_row([byWeekly_payDates[24],"$2000" , "15%", "$300"])
savingsTable.add_row(["Yearly","savings" , "total", "$7,200"])
print(allowanceTable)
print(savingsTable)