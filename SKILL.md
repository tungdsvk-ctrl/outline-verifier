---
name: outline-verifier
description: "Tự động kiểm định kịch bản khung (Outline) đa kênh YouTube theo kiến trúc Hybrid Gatekeeper 2 tầng: Quét linter cơ học cứng (0 token) và điều phối 2 Agent QA độc lập (Double-Blind Peer Review) cùng chấm theo bộ Master Rubric 10 tiêu chuẩn để xuất biên bản nghiệm thu OUTLINE_AUDIT_REPORT.md trước khi viết kịch bản chi tiết."
---

# 📘 OUTLINE VERIFIER SKILL (HYBRID GATEKEEPER)

Skill này tự động hóa quy trình thẩm định kịch bản khung (`OUTLINE.md`) cho mọi kênh YouTube, đảm bảo video đạt chuẩn giữ chân thuật toán, logic dữ liệu và an toàn sản xuất trước khi viết kịch bản chi tiết.

---

## ⚡ CÁCH KÍCH HOẠT (TRIGGERS)

Skill sẽ tự động nhận diện và thực thi khi người dùng yêu cầu:
- *"Kiểm định outline tập X"*
- *"Audit outline kịch bản"*
- *"Verify outline [mã tập]"*
- *"Chạy kiểm tra outline theo playbook"*

---

## ⚙️ QUY TRÌNH THỰC THI 5 BƯỚC

```
[Bản thảo OUTLINE.md] ➔ [Tầng 1: Python Linter] ➔ [Tầng 2: Dual QA Song Song] ➔ [Đối Chiếu Bất Đồng] ➔ [Cổng Nghiệm Thu]
```

### BƯỚC 1: XÁC ĐỊNH FILE VÀ HỒ SƠ KÊNH
1. Tìm file `OUTLINE.md` trong thư mục tập phim cần kiểm định.
2. Kiểm tra file `CHANNEL_PROFILE.md` tại thư mục gốc của kênh (nếu chưa có, nạp cấu hình mặc định từ `resources/CHANNEL_PROFILE_TEMPLATE.md`).

### BƯỚC 2: QUÉT KỸ THUẬT TẦNG 1 (PYTHON LINTER - 0 TOKEN)
Chạy script linter bên trong skill:
```bash
python scripts/linter.py "đường_dẫn_file_outline.md"
```
- Nếu **Exit Code 1 (Thất bại)**: Dừng ngay lập tức, báo các dòng vi phạm (số Hồi, số từ, câu dài quá 150 ký tự, từ rác AI) để sửa tại chỗ. Không gọi LLM.
- Nếu **Exit Code 0 (Thành công)**: Tự động chuyển tiếp sang Bước 3.

### BƯỚC 3: THẨM ĐỊNH SONG SONG MÙ ĐÔI TẦNG 2 (DUAL QA PEER REVIEW)
Khởi chạy song song 2 Agent QA độc lập (hoặc 2 phiên thẩm định độc lập), cùng nạp chung **Bộ Master Rubric 10 Tiêu Chuẩn** (`resources/UNIVERSAL_MASTER_RUBRIC.md`) và file `OUTLINE.md`.

#### Mẫu Prompt Thẩm Định cho Từng Agent:
```text
Bạn là Giám định viên Kịch bản YouTube Độc lập.
Hãy đọc kỹ file OUTLINE.md và đối chiếu độc lập với 10 tiêu chuẩn sau:
1. U-01: Master Hook 4.0 trong 30-45s đầu (Đủ 4 yếu tố bẻ gãy trực giác cũ).
2. U-02: Focus Keyword Spoken SEO (Phát âm đúng 2 lần trong 30s đầu).
3. U-03: Nhịp thở Văn nói (Câu ngắn 1-5 từ đan xen câu dài, nhịp đọc 150 WPM).
4. U-04: Curiosity Bridges (Cầu nối tò mò chốt mở mỗi 60-90s, cấm liên từ luận văn).
5. U-05: Save / Share Trigger (Điểm dừng tại ~50-60% thời lượng).
6. U-06: End-Screen Watch Loop (Câu thoại dẫn sang tập tiếp theo).
7. U-07: Rào cản TTS & Lọc từ rác AI (100% câu <= 150 ký tự, 0 từ rác AI).
8. U-08: Timestamps Chuẩn (Đúng số dòng Hồi chính, không chia nhỏ sub-beats).
9. P-09: Khí chất Nhân vật Dẫn dắt (Đúng phong thái, khẩu hiệu khai báo trong CHANNEL_PROFILE.md).
10. P-10: Bằng chứng Chuyên môn & Giá trị (100% số liệu có nguồn kiểm chứng, trao giá trị thực chiến ở Hồi kết).

YÊU CẦU:
Trả về bảng chấm từng tiêu chí kèm số dòng trích dẫn cụ thể và phán quyết: PASS hoặc FAIL.
```

### BƯỚC 4: SO KHỚP ĐỐI CHIẾU CHÉO (CONSENSUS MATRIX)
Tổng hợp 2 báo cáo từ QA 1 và QA 2 thành bảng so sánh:
- Tiêu chí cả 2 cùng PASS ➔ ĐỒNG THUẬN (ĐẠT).
- Tiêu chí có 1 bên PASS và 1 bên FAIL ➔ BẤT ĐỒNG (Hệ thống tự động đứng về bên FAIL để bắt lỗi).
- Xuất file biên bản `OUTLINE_AUDIT_REPORT.md` lưu ngay trong thư mục tập phim.

### BƯỚC 5: CỔNG PHÁN QUYẾT XUẤT XƯỞNG (CIRCUIT BREAKER GATE)
1. **Cả 2 cùng PASS (10/10):** Cấp chứng nhận `STATUS: PRODUCTION READY` ➔ Cho phép viết Full Script và dựng Storyboard.
2. **Có Bất Đồng:** Chặn cổng sản xuất, chỉ định chính xác số dòng cần sửa theo phát hiện của bên đánh giá FAIL.
3. **Cả 2 cùng FAIL:** Ngắt mạch toàn diện, yêu cầu định hướng lại đề tài.
