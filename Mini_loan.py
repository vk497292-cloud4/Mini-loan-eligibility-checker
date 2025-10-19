import tkinter as tk
from tkinter import messagebox

def check_eligibility():
    try:
        age = int(age_entry.get())
        income = float(income_entry.get())
        credit = int(credit_entry.get())

        if age < 18:
            result = "Not eligible: Age must be at least 18."
        elif income < 10000:
            result = "Not eligible: Income must be at least ₹10,000."
        elif credit < 600:
            result = "Not eligible: Credit score must be 600 or above."
        else:
            result = "Eligible for mini loan!"

        messagebox.showinfo("Eligibility Result", result)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values.")

# Tkinter window setup
root = tk.Tk()
root.title("Mini Loan Eligibility Checker")
root.geometry("350x300")

# Labels and input fields
tk.Label(root, text="Mini Loan Eligibility Checker", font=('Arial', 14, 'bold')).pack(pady=10)

tk.Label(root, text="Enter Age:").pack()
age_entry = tk.Entry(root)
age_entry.pack(pady=5)

tk.Label(root, text="Enter Monthly Income (₹):").pack()
income_entry = tk.Entry(root)
income_entry.pack(pady=5)

tk.Label(root, text="Enter Credit Score:").pack()
credit_entry = tk.Entry(root)
credit_entry.pack(pady=5)

# Button to check eligibility
tk.Button(root, text="Check Eligibility", command=check_eligibility, bg='lightblue').pack(pady=20)

root.mainloop()  