# هذا الملف هو نقطة تشغيل التطبيق
from app import create_app, db
from app.models import seed_data

app = create_app()

# عند تشغيل التطبيق، نقوم بإنشاء الجداول وتعبئتها ببيانات مبدئية
with app.app_context():
    db.create_all()
    seed_data()  # تعبئة بيانات مبدئية

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
