# 🔍 Outline Verifier Skill (Hybrid Gatekeeper & Double-Blind Peer Review)

> **Autonomous 2-Tier Quality Assurance Engine for YouTube Video Outlines.**  
> *Động cơ thẩm định kịch bản khung YouTube tự động 2 tầng: Quét cú pháp cơ học cứng (0 token) kết hợp đánh giá song song chéo (Double-Blind Peer Review) giữa 2 Agent QA độc lập.*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.10+](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Antigravity: Skill](https://img.shields.io/badge/Antigravity-Agent%20Skill-brightgreen.svg)]()

---

## 🌟 TỔNG QUAN (OVERVIEW)

Trong quy trình sản xuất nội dung YouTube tự động bằng AI, **bước xây dựng Outline (kịch bản khung)** là mắt xích quyết định 80% thành bại của toàn bộ video. Một lỗi logic hoặc cấu trúc hỏng ở khâu outline sẽ làm lãng phí toàn bộ chi phí viết kịch bản chi tiết, thu âm giọng đọc AI (TTS), tạo hiệu ứng hình ảnh và dựng phim CapCut.

**Outline Verifier** giải quyết triệt để vấn đề này bằng kiến trúc **Hybrid Gatekeeper 2 Tầng**:
1. **Tầng 1 (Python Static Linter - 0 Token):** Quét kiểm tra cơ học cứng chỉ trong vài mili-giây (cấu trúc Part, độ dài từ ngữ, giới hạn câu TTS `<= 150 ký tự`, lọc từ rác AI).
2. **Tầng 2 (Dual QA Double-Blind Peer Review):** Điều phối 2 Agent QA độc lập đánh giá song song theo **Master Rubric 10 tiêu chuẩn** (8 tiêu chuẩn bất biến phổ quát + 2 tiêu chuẩn đặc thù kênh nạp từ `CHANNEL_PROFILE.md`).
3. **Cổng nghiệm thu đối chiếu bất đồng (Consensus Matrix):** Tự động so khớp kết quả chấm chéo, trích lục bằng chứng và xuất biên bản `OUTLINE_AUDIT_REPORT.md` trước khi cấp phép viết kịch bản chi tiết.

---

## 🏛️ KIẾN TRÚC ĐA KÊNH: DECOUPLED CORE + PLUGIN

```
+-----------------------------------------------------------------------------------+
|                        UNIVERSAL MASTER RUBRIC (10 TIÊU CHUẨN)                    |
+----------------------------------------------------+------------------------------+
|       70% UNIVERSAL CORE (BẤT BIẾN CHO MỌI KÊNH)   |  30% CHANNEL PROFILE PLUGIN  |
+----------------------------------------------------+------------------------------+
| [U-01] Master Hook 4.0 (0:00 - 0:45)               | [P-09] Khí chất Persona Kênh |
| [U-02] Focus Keyword Spoken Frequency (SEO)        |        (Marcus, Khắc kỷ,...) |
| [U-03] Nhịp thở Văn nói (Spoken Cadence)           |                              |
| [U-04] Curiosity Bridges (60-90s Zeigarnik Loops)  | [P-10] Bằng chứng Thẩm quyền |
| [U-05] Save / Share Trigger (50-60% Duration)      |        & Giá trị Hồi kết     |
| [U-06] End-Screen Watch Loop (Móc xích xem tiếp)   |        (SEC 10-K, Nature,...) |
| [U-07] Rào cản TTS (<= 150 kt) & Lọc từ rác AI     |                              |
| [U-08] Cấu trúc Timestamps Chương mục Tinh gọn     |                              |
+----------------------------------------------------+------------------------------+
```

---

## 📁 CẤU TRÚC THƯ MỤC (DIRECTORY STRUCTURE)

```
outline-verifier/
├── SKILL.md                               # Tệp chỉ dẫn thực thi cốt lõi của Agent Skill
├── README.md                              # Tài liệu hướng dẫn sử dụng và cài đặt
├── scripts/
│   └── linter.py                          # Python CLI static linter (0 token deterministic)
└── resources/
    ├── UNIVERSAL_MASTER_RUBRIC.md         # Bộ 10 tiêu chuẩn chấm thẩm định chi tiết
    ├── CHANNEL_PROFILE_TEMPLATE.md        # Tệp cấu hình mẫu bản sắc và quy chuẩn kênh
    └── OUTLINE_AUDIT_REPORT_TEMPLATE.md   # Mẫu biên bản nghiệm thu đối chiếu chéo
```

---

## 🚀 CÁCH CÀI ĐẶT (INSTALLATION)

### Cách 1: Cài đặt vào một Workspace cụ thể (Khuyên dùng)
Clone repository vào thư mục `.agents/skills/` trong project của bạn:
```bash
cd /path/to/your/project
mkdir -p .agents/skills
git clone https://github.com/tungdsvk-ctrl/outline-verifier.git .agents/skills/outline-verifier
```

### Cách 2: Cài đặt Toàn cục (Global Agent Skill)
Clone repository vào thư mục config của Antigravity để mọi project đều dùng được:
```bash
# Trên Windows:
git clone https://github.com/tungdsvk-ctrl/outline-verifier.git "%USERPROFILE%\.gemini\antigravity\skills\outline-verifier"

# Trên macOS/Linux:
git clone https://github.com/tungdsvk-ctrl/outline-verifier.git ~/.gemini/antigravity/skills/outline-verifier
```

---

## 🛠️ CÁCH SỬ DỤNG (USAGE WORKFLOW)

### Bước 1: Khai báo hồ sơ kênh (Một lần duy nhất)
Sao chép `resources/CHANNEL_PROFILE_TEMPLATE.md` thành `CHANNEL_PROFILE.md` và đặt tại thư mục gốc của kênh YouTube. Điền thông tin:
- Tên kênh, số lượng Hồi chuẩn (`target_parts`), số lượng từ chuẩn (`min_words`, `max_words`).
- Tính cách nhân vật dẫn dắt (`persona`), câu khẩu hiệu thương hiệu (`brand_slogan`).
- Nguồn tài liệu thẩm quyền và dạng giá trị hành động trao cho người xem ở Hồi kết.

### Bước 2: Ra lệnh cho Agent
Khi đã soạn thảo xong file `OUTLINE.md`, bạn chỉ cần nói với AI Agent:
> *"Hãy kiểm định outline tập 09 theo playbook"*  
> hoặc  
> *"Audit outline kịch bản EP09"*

AI Agent sẽ tự động:
1. Chạy `scripts/linter.py` để quét Tầng 1.
2. Điều phối 2 Agent QA độc lập đánh giá song song Tầng 2.
3. Tổng hợp bảng đối chiếu chéo và xuất ra tệp `OUTLINE_AUDIT_REPORT.md` kèm phán quyết cuối cùng.

---

## 🧪 CHẠY LINTER THỦ CÔNG (STANDALONE CLI)

Bạn cũng có thể chạy độc lập công cụ linter bằng dòng lệnh:
```bash
# Quét cơ bản
python scripts/linter.py path/to/OUTLINE.md

# Tùy chỉnh số Parts và giới hạn từ
python scripts/linter.py path/to/OUTLINE.md --parts 5 --min-words 800 --max-words 1400

# Xuất báo cáo dạng JSON cho CI/CD pipeline
python scripts/linter.py path/to/OUTLINE.md --json
```

---

## 📄 LICENSE

Dự án này được phát hành dưới giấy phép [MIT License](LICENSE). Tự do sử dụng, chỉnh sửa và tích hợp vào mọi workflow sáng tạo nội dung YouTube tự động.
