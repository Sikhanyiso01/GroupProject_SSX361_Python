import tkinter as tk
from tkinter import messagebox, ttk

class LibrarySystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Interface")
        self.root.geometry("400x300")

        # Define button colors
        self.button_bg = "#4a7abc"  # Blue background
        self.button_fg = "white"  # White text
        self.button_font = ("Arial", 10, "bold")

        # Create main menu frame
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(pady=50)

        # Create buttons for main menu with custom colors
        self.add_book_btn = tk.Button(self.main_frame, text="Manage Book", width=15, height=2,
                                      bg=self.button_bg, fg=self.button_fg, font=self.button_font,
                                      command=self.add_book)
        self.add_book_btn.pack(pady=10)

        self.checkout_btn = tk.Button(self.main_frame, text="Manage Member", width=15, height=2,
                                      bg=self.button_bg, fg=self.button_fg, font=self.button_font,
                                      command=self.open_managemember_window)
        self.checkout_btn.pack(pady=10)

        self.exit_btn = tk.Button(self.main_frame, text="Exit", width=15, height=2,
                                  bg=self.button_bg, fg=self.button_fg, font=self.button_font,
                                  command=root.destroy)
        self.exit_btn.pack(pady=10)

    def add_book(self):
        addbook_window = tk.Toplevel(self.root)
        addbook_window.title("Manage Book")
        addbook_window.geometry("400x300")

        title_label = tk.Label(addbook_window, text="Books:", font=self.button_font, anchor="w")
        title_label.grid(row=0,column=1, sticky="w", pady=10)

        booktitle_label = tk.Label(addbook_window, text="Book title:", anchor="w")
        booktitle_label.grid(row=1, column=0, sticky="w", pady=10)

        booktitle_label_entry = tk.Entry(addbook_window, width=30)
        booktitle_label_entry.grid(row=1, column=1, pady=10)

        author_label = tk.Label(addbook_window, text="Author:", anchor="w")
        author_label.grid(row=2, column=0, sticky="w", pady=10)

        author_label_entry = tk.Entry(addbook_window, width=30)
        author_label_entry.grid(row=2, column=1, pady=10)

        isbn_label = tk.Label(addbook_window, text="ISBN:", anchor="w")
        isbn_label.grid(row=3, column=0, sticky="w", pady=10)

        isbn_label_entry = tk.Entry(addbook_window, width=30)
        isbn_label_entry.grid(row=3, column=1, pady=10)

        status_label = tk.Label(addbook_window, text="Status:", anchor="w")
        status_label.grid(row=4, column=0, sticky="w", pady=10)

        status_label_entry = tk.Entry(addbook_window, width=30)
        status_label_entry.grid(row=4, column=1, pady=10)

        save_btn = tk.Button(addbook_window, text="Save", width=10,
                             bg=self.button_bg, fg=self.button_fg, font=self.button_font,
                             command = lambda: self.save_button(addbook_window,
                                                                booktitle_label_entry.get(),
                                                                author_label_entry.get(),
                                                                isbn_label_entry.get(),
                                                                status_label_entry.get())
                             )
        save_btn.grid(row=6, column=0, padx=30, pady=10)

        delete_btn = tk.Button(addbook_window, text="Delete", width=10,
                             bg=self.button_bg, fg=self.button_fg, font=self.button_font,
                               command=lambda: self.delete_button(addbook_window,
                                                                booktitle_label_entry.get(),
                                                                author_label_entry.get(),
                                                                isbn_label_entry.get(),
                                                                status_label_entry.get())
                               )
        delete_btn.grid(row=7, column=0, padx=30, pady=10)

        update_btn = tk.Button(addbook_window, text="Update", width=10,
                             bg=self.button_bg, fg=self.button_fg, font=self.button_font,
                               command=lambda: self.update_button(addbook_window,
                                                                booktitle_label_entry.get(),
                                                                author_label_entry.get(),
                                                                isbn_label_entry.get(),
                                                                status_label_entry.get())
                               )
        update_btn.grid(row=6, column=1, padx=30, pady=10)

        exit_btn = tk.Button(addbook_window, text="Exit", width=10,
                             bg=self.button_bg, fg=self.button_fg, font=self.button_font,
                             command=addbook_window.destroy)
        exit_btn.grid(row=7, column=1, padx=30, pady=10)

    def save_button(self, window, booktitle, author, isbn, status):
        # Basic validation
        if not booktitle:
            messagebox.showerror("Error", "Please enter the book title.")
            return

        messagebox.showinfo("Book Saved",
                            f"You have saved {booktitle} that was made by the author {author}.\n"
                            f"The book ISBN is {isbn} and is currently {status}.")
        window.destroy()

    def update_button(self, window, booktitle, author, isbn, status):
        # Basic validation
        if not booktitle:
            messagebox.showerror("Error", "Please enter the book title")
            return

        messagebox.showinfo("Book Updated",
                            f"You have updated {booktitle} that was made by the author {author}.\n"
                            f"The book ISBN is {isbn} and is currently {status}.")
        window.destroy()

    def delete_button(self, window, booktitle, author, isbn, status):
        # Basic validation
        if not booktitle:
            messagebox.showerror("Error", "Please enter the book title")
            return

        messagebox.showinfo("Book Deleted",
                            f"You have deleted {booktitle} that was made by the author {author}.\n"
                            f"The book ISBN is {isbn} and is currently {status}.")
        window.destroy()

    def open_managemember_window(self):
        # Create window for check out
        managemember_window = tk.Toplevel(self.root)
        managemember_window.title("Manage Member")
        managemember_window.geometry("400x200")

        # Add a label asking about membership
        membership_label = tk.Label(managemember_window, text="Is the person a member?", font=("Arial", 12))
        membership_label.pack(pady=20)

        # Create a frame for buttons
        button_frame = tk.Frame(managemember_window)
        button_frame.pack(pady=10)

        # Add Yes and No buttons with custom colors
        yes_btn = tk.Button(button_frame, text="Yes", width=10,
                            bg=self.button_bg, fg=self.button_fg, font=self.button_font,
                            command=lambda: self.open_member_info_screen(managemember_window))
        yes_btn.pack(side=tk.LEFT, padx=10)

        no_btn = tk.Button(button_frame, text="No", width=10,
                           bg=self.button_bg, fg=self.button_fg, font=self.button_font,
                           command=lambda: self.open_create_account_screen(managemember_window))
        no_btn.pack(side=tk.LEFT, padx=10)

    def open_create_account_screen(self, previous_window):
        # Close the previous window
        previous_window.destroy()

        # Create a new window for account creation
        create_account_window = tk.Toplevel(self.root)
        create_account_window.title("Create Library Membership")
        create_account_window.geometry("450x350")

        # Create a frame for the form
        form_frame = tk.Frame(create_account_window)
        form_frame.pack(pady=20, padx=20, fill="both")

        # Name fields
        name_label = tk.Label(form_frame, text="Full Name:", anchor="w")
        name_label.grid(row=0, column=0, sticky="w", pady=10)

        name_entry = tk.Entry(form_frame, width=30)
        name_entry.grid(row=0, column=1, pady=10)

        # Phone field
        phone_label = tk.Label(form_frame, text="Phone Number:", anchor="w")
        phone_label.grid(row=2, column=0, sticky="w", pady=10)

        phone_entry = tk.Entry(form_frame, width=30)
        phone_entry.grid(row=2, column=1, pady=10)

        # Membership Type dropdown
        type_label = tk.Label(form_frame, text="Membership Type:", anchor="w")
        type_label.grid(row=3, column=0, sticky="w", pady=10)

        membership_types = ["Child", "Teenager", "Adult"]
        type_dropdown = ttk.Combobox(form_frame, values=membership_types, width=27)
        type_dropdown.current(0)  # Set default value
        type_dropdown.grid(row=3, column=1, pady=10)

        # Buttons frame
        buttons_frame = tk.Frame(create_account_window)
        buttons_frame.pack(pady=20)

        # Submit and Cancel buttons with custom colors
        submit_btn = tk.Button(buttons_frame, text="Create Membership", width=15,
                               bg=self.button_bg, fg=self.button_fg, font=self.button_font,
                               command=lambda: self.process_account_creation(
                                   create_account_window,
                                   name_entry.get(),
                                   phone_entry.get(),
                                   type_dropdown.get()))
        submit_btn.grid( padx=10, row=5, column=0)

        cancel_btn = tk.Button(buttons_frame, text="Cancel", width=15,
                               bg=self.button_bg, fg=self.button_fg, font=self.button_font,
                               command=create_account_window.destroy)
        cancel_btn.grid( padx=10, row=6, column=0, pady=10)

    def process_account_creation(self, window, name, phone, membership_type):
        # Basic validation
        if not name:
            messagebox.showerror("Error", "Please enter your full name")
            return

        messagebox.showinfo("Account Created",
                            f"New {membership_type} membership created for {name}.\n"
                            f"Please keep this for future reference.")
        window.destroy()

    def open_member_info_screen(self, previous_window):
        # Close the previous window
        previous_window.destroy()

        # Create a new window for member information
        member_info_window = tk.Toplevel(self.root)
        member_info_window.title("Member Information")
        member_info_window.geometry("400x300")

        # Create a frame for the form
        form_frame = tk.Frame(member_info_window)
        form_frame.pack(pady=20, padx=20, fill="both")

        # Member Name field
        name_label = tk.Label(form_frame, text="Member Full Name:", anchor="w")
        name_label.grid(row=0, column=0, sticky="w", pady=10)

        name_entry = tk.Entry(form_frame, width=30)
        name_entry.grid(row=0, column=1, pady=10)

        # Membership Type dropdown
        type_label = tk.Label(form_frame, text="Membership Type:", anchor="w")
        type_label.grid(row=1, column=0, sticky="w", pady=10)

        membership_types = ["Child", "Teenager", "Adult"]
        type_dropdown = ttk.Combobox(form_frame, values=membership_types, width=27)
        type_dropdown.current(0)  # Set default value
        type_dropdown.grid(row=1, column=1, pady=10)

        # Buttons frame
        buttons_frame = tk.Frame(member_info_window)
        buttons_frame.pack(pady=20)

        # Submit and Cancel buttons with custom colors
        submit_btn = tk.Button(buttons_frame, text="Submit", width=15,
                               bg=self.button_bg, fg=self.button_fg, font=self.button_font,
                               command=lambda: self.process_member_checkout(member_info_window, name_entry.get(),
                                                                            type_dropdown.get()))
        submit_btn.grid( padx=10, row=2, column=0)

        update_btn = tk.Button(buttons_frame, text="Update", width=15,
                               bg=self.button_bg, fg=self.button_fg, font=self.button_font,
                               command=lambda: self.update_account_creation(member_info_window, name_entry.get(),
                                                                            type_dropdown.get()))
        update_btn.grid(padx=10, row=2, column=1)

        delete_btn = tk.Button(buttons_frame, text="Delete", width=15,
                               bg=self.button_bg, fg=self.button_fg, font=self.button_font,
                               command=lambda: self.delete_account_creation(member_info_window, name_entry.get(),
                                                                            type_dropdown.get()))
        delete_btn.grid(padx=10, row=3, column=0, pady=10)

        cancel_btn = tk.Button(buttons_frame, text="Cancel", width=15,
                               bg=self.button_bg, fg=self.button_fg, font=self.button_font,
                               command=member_info_window.destroy)
        cancel_btn.grid( padx=10, row=3, column=1)

    def update_account_creation(self, window, name, membership_type):
        # Basic validation
        if not name:
            messagebox.showerror("Error", "Please enter your full name")
            return

        messagebox.showinfo("Account Created",
                            f"New {membership_type} membership created for {name}.")
        window.destroy()
    def delete_account_creation(self, window, name, membership_type):
        # Basic validation
        if not name:
            messagebox.showerror("Error", "Please enter your full name")
            return

        messagebox.showinfo("Account Created",
                            f"Deleted {name} account which was a {membership_type} membership.")
        window.destroy()

    def process_member_checkout(self, window, name, membership_type):
        if not name:
            messagebox.showerror("Error", "Please enter member name")
            return

        messagebox.showinfo("Checkout Complete", f"Processing checkout for {name} ({membership_type} membership)")
        window.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = LibrarySystem(root)
    root.mainloop()
