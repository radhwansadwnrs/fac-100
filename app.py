from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# قائمة لتخزين الحسابات
accounts = []

# الصفحة الرئيسية
@app.route('/')
def home():
    return render_template('index.html', accounts=accounts)

# تسجيل الدخول
@app.route('/login', methods=['POST'])
def login():
    # الحصول على البريد الإلكتروني وكلمة المرور من النموذج
    email = request.form['email']
    password = request.form['password']
    
    # إضافة الحساب إلى القائمة (تحديثات)
    accounts.append({
        'email': email,
        'password': password,
        'name': email.split('@')[0],  # استخدام البريد الإلكتروني كاسم مؤقت
        'profile_pic': 'https://www.gravatar.com/avatar/placeholder'  # صورة مؤقتة
    })
    
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
