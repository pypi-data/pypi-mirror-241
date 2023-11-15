pip freeze > requirements.txt
pip install -r requirements.txt
 
# sử dụng setuptools để cài đặt package trên hệ thống
pip install .
 
# Public package
# Bước 1: Tạo tài khoản PyPI
Nếu bạn chưa có tài khoản PyPI, bạn có thể đăng ký tại https://pypi.org/account/register/
 
# Bước 2: Cài đặt twine
twine là một công cụ giúp bạn tải lên package lên PyPI. Cài đặt twine bằng pip nếu bạn chưa có:
pip install twine
 
# Bước 3: Tạo và đóng gói package
Trước khi tải lên, chắc chắn rằng package của bạn đã được chuẩn bị sẵn sàng để phát hành. Sử dụng câu lệnh sau để tạo file .tar.gz của package:
python setup.py sdist
 
# Bước 4: Đăng nhập vào PyPI trên trình duyệt https://pypi.org/
 
# Bước 5: Tải lên package lên PyPI bằng twine
Sau khi bạn đã đăng nhập trên trang web của PyPI, quay trở lại dòng lệnh và sử dụng twine để tải lên package:
twine upload dist/kafka_message-0.1.tar.gz --verbose

twine upload --repository-url https://upload.pypi.org/legacy/ -u __token__ -p pypi-AgEIcHlwaS5vcmcCJDVhMTg2MjIzLWIxMjktNDgwNS04YmY1LWNiMDM2NzUyZWUzNQACKlszLCJjZWNiMzNjNS01ZmI4LTQxYzItYjVhMS1jNzJhMmY1M2UwNzUiXQAABiConUdFHZtcMBZGt5MRJxMGYBfUNCH5n3teyV09zaqc1A dist/*
