خطوات تشغيل البرنامج
python detector.py --help
تدريب النموذج:

bash
نسخ الكود
python detector.py --train -m hog
التحقق من النموذج:

bash
نسخ الكود
python detector.py --validate -m hog
اختبار النموذج:

bash
نسخ الكود
python detector.py --test -f path/to/unknown_face_image.jpg -m hog