import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage

class FacebookAccountManager:
    def __init__(self, root):
        self.root = root
        self.root.title("إدارة الحسابات المتعددة")
        self.root.geometry("600x600")

        # الحسابات المخزنة (يمكن توسيعها لاحقًا لتخزين بيانات الحسابات)
        self.accounts = []
        
        # واجهة المستخدم لتسجيل الدخول في الأعلى
        self.login_frame = tk.Frame(root)
        self.login_frame.pack(pady=20)

        self.email_label = tk.Label(self.login_frame, text="البريد الإلكتروني")
        self.email_label.grid(row=0, column=0)
        self.email_entry = tk.Entry(self.login_frame)
        self.email_entry.grid(row=0, column=1)

        self.password_label = tk.Label(self.login_frame, text="كلمة المرور")
        self.password_label.grid(row=1, column=0)
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.grid(row=1, column=1)

        self.login_button = tk.Button(self.login_frame, text="تسجيل الدخول", command=self.login)
        self.login_button.grid(row=2, columnspan=2, pady=10)

        # مكان إضافة الحسابات في الأسفل
        self.account_frame = tk.Frame(root)
        self.account_frame.pack(pady=20)

        # إضافة حساب جديد
        self.add_account_button = tk.Button(root, text="إضافة حساب", command=self.add_account)
        self.add_account_button.pack(pady=10)

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        # التحقق من بيانات الحسابات
        account_image = PhotoImage()  # الصورة يمكن استبدالها بصورة حقيقية لحساب فيسبوك

        # إضافة الحساب إلى القائمة بعد تسجيل الدخول
        if email and password:  # في حالة كان الحساب المدخل صحيحًا
            account_data = {"email": email, "password": password, "image": account_image}
            self.accounts.append(account_data)
            self.show_accounts()  # تحديث عرض الحسابات
            messagebox.showinfo("تسجيل الدخول", f"تم تسجيل الدخول بنجاح باستخدام {email}")
        else:
            messagebox.showerror("خطأ", "البريد الإلكتروني أو كلمة المرور غير صحيحة")

    def show_accounts(self):
        # إخفاء واجهة تسجيل الدخول بعد تسجيل الدخول بنجاح
        for widget in self.login_frame.winfo_children():
            widget.grid_forget()

        # عرض الحسابات في الأسفل
        row = 0  # بدء الصف الأول لعرض الحسابات
        for account in self.accounts:
            account_frame = tk.Frame(self.account_frame)
            account_frame.grid(row=row, column=0, pady=10, padx=10)

            account_label = tk.Label(account_frame, text=account["email"])
            account_label.pack(side="left", padx=10)

            account_image_label = tk.Label(account_frame, image=account["image"])  # يمكن إضافة صورة حقيقية
            account_image_label.pack(side="left")

            open_button = tk.Button(account_frame, text="فتح الحساب", command=lambda email=account["email"]: self.open_account(email))
            open_button.pack(side="left", padx=10)

            row += 1  # الانتقال إلى الصف التالي

    def open_account(self, email):
        # هنا يمكن إضافة الوظيفة لفتح الحساب في نافذة جديدة
        messagebox.showinfo("فتح الحساب", f"تم فتح الحساب: {email}")

    def add_account(self):
        # هذه الوظيفة يمكن استخدامها لإضافة حسابات يدويا
        self.login_frame.pack(pady=20)  # إعادة عرض واجهة تسجيل الدخول
        self.email_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

# إنشاء نافذة Tkinter
root = tk.Tk()
app = FacebookAccountManager(root)
root.mainloop()
