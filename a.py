import os
import subprocess
import time

# Đường dẫn thư mục tổng chứa tất cả các chapter
base_dir = r"F:\\JOB\Saka_Ejji\\test"  # Dùng raw string để tránh lỗi escape

# Lấy danh sách tất cả thư mục con (các chapter)
subdirs = [os.path.join(base_dir, d) for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]

try:
    for subdir in subdirs:
        print(f"📂 Đang xử lý thư mục: {subdir}")

        # Chạy launch.py cho từng chapter và đợi nó chạy xong trước khi tiếp tục
        process = subprocess.Popen(["python", "launch.py", "--headless", "--exec_dirs", subdir])

        # Chờ quá trình con kết thúc
        process.wait()

        print(f"✅ Hoàn thành: {subdir}")
        time.sleep(1)  # Nghỉ 1 giây để tránh quá tải CPU (tùy chọn)

except KeyboardInterrupt:
    print("\n⚠️ Nhận tín hiệu Ctrl+C! Đang dừng chương trình...")
    if process and process.poll() is None:  # Kiểm tra nếu tiến trình con vẫn đang chạy
        process.terminate()  # Yêu cầu dừng nhẹ nhàng
        try:
            process.wait(timeout=5)  # Chờ 5 giây để dừng hẳn
        except subprocess.TimeoutExpired:
            process.kill()  # Buộc dừng nếu vẫn chưa tắt
    print("🛑 Đã dừng chương trình.")
