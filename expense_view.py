import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from db import get_expenses, create_tables
import csv
from datetime import datetime

# Category color mapping
CATEGORY_COLORS = {
    "Food": "#fff3e0",
    "Transport": "#e8f5e9",
    "Shopping": "#fce4ec",
    "Bills": "#e3f2fd",
    "Other": "#f5f5f5"
}

class ExpenseViewApp:
    def __init__(self, root, user_id):
        self.root = root
        self.root.title("💸 Advanced Expense Tracker")
        self.root.geometry("850x600")
        self.user_id = user_id

        # Header
        header = tk.Label(root, text="📊 Expense Dashboard", bg="#00bcd4", fg="white",
                          font=("Helvetica", 18, "bold"), pady=10)
        header.pack(fill="x")

        # Filter Section
        filter_frame = tk.Frame(root, bg="#f0f0f0")
        filter_frame.pack(fill="x", padx=20, pady=5)

        # Search
        tk.Label(filter_frame, text="🔍 Search:", bg="#f0f0f0", font=("Arial", 10)).grid(row=0, column=0, padx=5)
        self.search_var = tk.StringVar()
        self.search_var.trace("w", self.apply_filters)
        tk.Entry(filter_frame, textvariable=self.search_var, width=30).grid(row=0, column=1, padx=5)

        # Category filter
        tk.Label(filter_frame, text="📦 Category:", bg="#f0f0f0", font=("Arial", 10)).grid(row=0, column=2, padx=5)
        self.category_var = tk.StringVar()
        self.category_dropdown = ttk.Combobox(filter_frame, textvariable=self.category_var, state="readonly")
        self.category_dropdown.grid(row=0, column=3, padx=5)
        self.category_dropdown.bind("<<ComboboxSelected>>", lambda e: self.apply_filters())

        # Date range
        tk.Label(filter_frame, text="🗓️ From (YYYY-MM-DD):", bg="#f0f0f0").grid(row=1, column=0, padx=5, pady=5)
        self.from_date = tk.Entry(filter_frame, width=15)
        self.from_date.grid(row=1, column=1, padx=5)

        tk.Label(filter_frame, text="To:", bg="#f0f0f0").grid(row=1, column=2, padx=5)
        self.to_date = tk.Entry(filter_frame, width=15)
        self.to_date.grid(row=1, column=3, padx=5)

        # Apply filters
        ttk.Button(filter_frame, text="Apply", command=self.apply_filters).grid(row=1, column=4, padx=10)
        ttk.Button(filter_frame, text="Reset", command=self.reset_filters).grid(row=1, column=5, padx=5)

        # Table
        style = ttk.Style()
        style.configure("Treeview", font=("Arial", 10), rowheight=28)
        style.configure("Treeview.Heading", font=("Arial", 11, "bold"))

        self.tree = ttk.Treeview(root, columns=("Date", "Category", "Description", "Amount"), show="headings")
        for col in ("Date", "Category", "Description", "Amount"):
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center", width=150 if col != "Description" else 250)

        self.tree.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)

        scrollbar = ttk.Scrollbar(self.tree, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Footer
        bottom = tk.Frame(root)
        bottom.pack(fill="x", padx=20, pady=10)

        self.total_label = tk.Label(bottom, text="Total: Rs. 0", font=("Arial", 10, "italic"))
        self.total_label.pack(side="left")

        ttk.Button(bottom, text="Export to CSV", command=self.export_to_csv).pack(side="right", padx=10)
        ttk.Button(bottom, text="Clear Table", command=self.clear_table).pack(side="right")

        self.load_expenses()

    def load_expenses(self):
        self.expenses = get_expenses(self.user_id)
        self.populate_categories()
        self.show_expenses(self.expenses)

    def show_expenses(self, expenses):
        self.clear_table()
        total = 0
        for row in expenses:
            date, category, desc, amount = row
            color = CATEGORY_COLORS.get(category, "#ffffff")
            tag = category
            self.tree.insert("", tk.END, values=row, tags=(tag,))
            self.tree.tag_configure(tag, background=color)
            total += float(amount)
        self.total_label.config(text=f"Total: Rs. {total:.2f}")

    def apply_filters(self, *args):
        query = self.search_var.get().lower()
        category = self.category_var.get()
        from_d = self.from_date.get()
        to_d = self.to_date.get()

        try:
            from_date_obj = datetime.strptime(from_d, "%Y-%m-%d") if from_d else None
            to_date_obj = datetime.strptime(to_d, "%Y-%m-%d") if to_d else None
        except ValueError:
            messagebox.showerror("Invalid Date", "Please enter dates in YYYY-MM-DD format.")
            return

        def matches(row):
            date, cat, desc, _ = row
            if query and query not in desc.lower() and query not in cat.lower() and query not in date:
                return False
            if category and cat != category:
                return False
            try:
                date_obj = datetime.strptime(date, "%Y-%m-%d")
                if from_date_obj and date_obj < from_date_obj:
                    return False
                if to_date_obj and date_obj > to_date_obj:
                    return False
            except Exception:
                return False
            return True

        filtered = [row for row in self.expenses if matches(row)]
        self.show_expenses(filtered)

    def reset_filters(self):
        self.search_var.set("")
        self.category_var.set("")
        self.from_date.delete(0, tk.END)
        self.to_date.delete(0, tk.END)
        self.show_expenses(self.expenses)

    def populate_categories(self):
        categories = sorted(set(row[1] for row in self.expenses))
        self.category_dropdown["values"] = [""] + categories

    def clear_table(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

    def export_to_csv(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if not file_path:
            return
        with open(file_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Category", "Description", "Amount"])
            for row_id in self.tree.get_children():
                row = self.tree.item(row_id)["values"]
                writer.writerow(row)
        messagebox.showinfo("Exported", "Data exported to CSV successfully!")

# Run for testing
if __name__ == "__main__":
    create_tables()
    root = tk.Tk()
    app = ExpenseViewApp(root, user_id=1)
    root.mainloop()
