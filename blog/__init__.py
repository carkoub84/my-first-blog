import tkinter as tk
from tkinter import messagebox

class OmegaSoftGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("OmegaSoft Retail System")
        self.geometry("400x300")

        # Initialize OmegaSoft instance
        self.omega_soft = OmegaSoft()

        # Create GUI components
        self.create_widgets()

    def create_widgets(self):
        # Labels
        tk.Label(self, text="User Management").pack(pady=10)
        tk.Label(self, text="Username:").pack()
        tk.Label(self, text="Product Management").pack(pady=10)
        tk.Label(self, text="Product Name:").pack()
        tk.Label(self, text="Product Price:").pack()
        tk.Label(self, text="Product Category:").pack()
        tk.Label(self, text="Order Management").pack(pady=10)
        tk.Label(self, text="Select User:").pack()

        # Entry Widgets
        self.username_entry = tk.Entry(self)
        self.username_entry.pack()
        self.product_name_entry = tk.Entry(self)
        self.product_name_entry.pack()
        self.product_price_entry = tk.Entry(self)
        self.product_price_entry.pack()
        self.product_category_entry = tk.Entry(self)
        self.product_category_entry.pack()

        # Buttons
        tk.Button(self, text="Add User", command=self.add_user).pack()
        tk.Button(self, text="Add Product", command=self.add_product).pack()
        tk.Button(self, text="Create Order", command=self.create_order).pack()

    def add_user(self):
        username = self.username_entry.get()
        if username:
            user = User(username)
            self.omega_soft.add_user(user)
            messagebox.showinfo("Success", f"User '{username}' added successfully!")
        else:
            messagebox.showwarning("Warning", "Please enter a username.")

    def add_product(self):
        name = self.product_name_entry.get()
        price = self.product_price_entry.get()
        category = self.product_category_entry.get()

        if name and price and category:
            product = Product(name, float(price), category)
            self.omega_soft.add_product(product)
            messagebox.showinfo("Success", f"Product '{name}' added successfully!")
        else:
            messagebox.showwarning("Warning", "Please fill in all product details.")

    def create_order(self):
        selected_user = self.username_entry.get()
        products = self.omega_soft.products  # For simplicity, use all products as order items

        if selected_user and products:
            user = User(selected_user)
            self.omega_soft.create_order(user, products)
            messagebox.showinfo("Success", "Order created successfully!")
        else:
            messagebox.showwarning("Warning", "Please select a user and ensure there are products.")

    def run(self):
        self.mainloop()

# Instantiate and run the GUI
omega_soft_gui = OmegaSoftGUI()
omega_soft_gui.run()
