# 📋 BẢNG CHECKLIST ĐỐI SOÁT THẨM ĐỊNH KỊCH BẢN KHUNG 2 TẦNG
## (HYBRID GATEKEEPER AUDIT CHECKLIST FOR OUTLINE)

> **Mục đích:** Cung cấp bộ tiêu chí kiểm tra chi tiết từng dòng, từng thông số kỹ thuật để người sáng lập (Creator) và AI Agent cùng đối soát chất lượng kịch bản khung trước khi sản xuất chi tiết.

---

## ⚙️ TẦNG 1: CHECKLIST QUÉT CƠ HỌC CỨNG (PYTHON STATIC LINTER - 0 TOKEN)

*Tầng này quét định lượng siêu tốc (< 50ms) bằng mã máy tính, đảm bảo 100% không có lỗi cú pháp hoặc rủi ro kỹ thuật.*

| STT | Hạng Mục Kiểm Tra | Điều Kiện ĐẠT CHUẨN (PASS) | Hậu Quả Nếu Bị Trượt (FAIL) | Trạng Thái Đối Soát |
| :---: | :--- | :--- | :--- | :---: |
| **1.1** | **Cấu trúc đủ 5 Hồi (5-Act Structure)** | Xuất hiện đầy đủ và đúng thứ tự 5 tiêu đề Hồi từ Part 1 đến Part 5 (hoặc Act 1 đến Act 5). Hỗ trợ định dạng: `## PART X:`, `## ACT X:`, `## PHẦN X (ACT X):`. | Kịch bản gãy mạch phim, thiếu cấu trúc 5 Hồi chuẩn của kênh. | `[ ]` |
| **1.2** | **Ngưỡng dung lượng từ ngữ (Word Budget)** | Tổng số từ nằm trong khoảng **2,700 – 3,500 từ** (tương ứng video dài 18–22 phút ở tốc độ đọc 150 WPM). *Lưu ý: Nếu có phân cảnh chỉ đạo mỹ thuật thì nội dung thoại thoại không vượt quá 3,500 từ.* | Kịch bản quá ngắn làm video hụt thời lượng, hoặc quá dài làm loãng nhịp phim. | `[ ]` |
| **1.3** | **An toàn mô hình AI Voice (TTS Limit)** | **100% câu thoại độc lập có độ dài $\le$ 150 ký tự** (`len(line) <= 150`). Không có câu ghép 3-4 mệnh đề phụ. | Giọng đọc AI (ElevenLabs) bị méo tiếng, hụt hơi, hoặc sinh tạp âm lạ ở đuôi câu. | `[ ]` |
| **1.4** | **Lọc sạch từ rác AI (AI Slop Words Filter)** | Tuyệt đối sạch **0 từ** trong danh mục cấm: `delve`, `tapestry`, `testament`, `beacon`, `landscape`, `bustling`, `unravel`, `at its core`, `vital`, `game-changer`, `ever-evolving`, `shed light on`, `realm`, `vén màn bí mật`, `hãy cùng`. | Kịch bản sặc mùi AI học vẹt, mất tính chân thực và tính thuyết phục của điều tra pháp y. | `[ ]` |

---

## 🧠 TẦNG 2: CHECKLIST ĐÁNH GIÁ CHẤT LƯỢNG NỘI DUNG (COGNITIVE AUDIT - 10 TIÊU CHUẨN)

*Tầng này đánh giá nhận thức, logic tâm lý giữ chân người xem và giá trị bảo vệ tài chính do 2 Agent QA chấm độc lập.*

### PHẦN A: 8 TIÊU CHUẨN PHỔ QUÁT (UNIVERSAL CORE - 70%)

| Mã TC | Tên Tiêu Chuẩn | Dấu Hiệu Nhận Biết & Tiêu Chí Bắt Buộc | Dòng Trích Dẫn Đối Soát | Kết Quả |
| :---: | :--- | :--- | :--- | :---: |
| **U-01** | **Master Hook 4.0 (0:00 - 0:45)** | Trong 45 giây đầu bắt buộc hội tụ đủ 4 yếu tố:<br>1. *Curiosity Gap:* Mở ra câu hỏi nghịch lý hóc búa.<br>2. *Shocking Metric:* Số liệu gây sốc định lượng.<br>3. *Visual Contrast:* Hình ảnh thị giác tương phản mạnh.<br>4. *Contrarian Claim:* Lật ngược niềm tin phổ thông của đám đông.<br>• *Quy tắc phụ:* Không đưa Mascot Marcus vào 30s đầu (Zero-Persona Rule). | `Dòng ________` | `[ ] PASS`<br>`[ ] FAIL` |
| **U-02** | **Spoken SEO Keyword Frequency** | Từ khóa hạt giống chính phải được phát âm tự nhiên **đúng 2 lần trong 30–45 giây đầu** của Part 1 để YouTube nhận diện chủ đề qua audio transcript. Phân bổ tự nhiên, không nhồi nhét máy móc. | `Dòng ________` | `[ ] PASS`<br>`[ ] FAIL` |
| **U-03** | **Nhịp thở Văn nói (Spoken Cadence)** | • Viết cho TAI NGHE, không viết cho MẮT ĐỌC.<br>• Đan xen câu ngắn đanh thép (1–5 từ: *"Case closed."*, *"Sounds simple. It is not."*) và câu dẫn giải (10–15 từ).<br>• Dùng đại từ xưng hô trực diện (You, We, I).<br>• Ẩn dụ đời thường hóa các thuật ngữ kinh tế phức tạp. | `Dòng ________` | `[ ] PASS`<br>`[ ] FAIL` |
| **U-04** | **Curiosity Bridges (60–90s)** | • Cứ mỗi 60–90 giây hoặc tại cuối mỗi Hồi phải có một câu chốt mở nút thắt tiếp theo (Zeigarnik Open Loops).<br>• Tuyệt đối cấm các liên từ viết văn khô cứng (*"Furthermore"*, *"In addition"*, *"Mặt khác"*).<br>• Câu chuyển ý kích thích: *"Here is the contrarian truth."*, *"Here is where the real money lives."* | `Dòng ________` | `[ ] PASS`<br>`[ ] FAIL` |
| **U-05** | **Save / Share Trigger** | • Nằm ở khoảng **50% – 60% thời lượng video** (khoảng giữa Part 3 hoặc đầu Part 4, phút 10:15 – 11:00).<br>• Đặt ngay sau khi kịch bản giải thích xong một bài toán giá trị cao hoặc một cú shock kiến thức.<br>• Lời kêu gọi ngắn gọn, đánh trúng tâm lý bảo vệ túi tiền cá nhân để đạt tỷ lệ Save-to-View > 1.2%. | `Dòng ________` | `[ ] PASS`<br>`[ ] FAIL` |
| **U-06** | **End-Screen Watch Loop** | • Câu thoại cuối cùng không cảm ơn sáo rỗng (*"Cảm ơn các bạn đã xem, hãy bấm like..."*).<br>• Mở ra một câu hỏi bỏ lửng kết nối logic trực tiếp sang một tập phim khác cùng vũ trụ kênh (Binge-watching loop). | `Dòng ________` | `[ ] PASS`<br>`[ ] FAIL` |
| **U-07** | **Rào cản TTS & Lọc sạch Từ rác** | • Xác nhận lại lần 2 bằng đọc hiểu: Toàn bộ các câu punchline, thoại dẫn đều an toàn cho việc ngắt nhịp voice.<br>• Không sót các cấu trúc sáo rỗng văn mẫu. | `Dòng ________` | `[ ] PASS`<br>`[ ] FAIL` |
| **U-08** | **Cấu trúc Timestamps Tinh gọn** | • Danh sách Timestamps ở cuối file chỉ gồm **đúng 5 dòng** tương ứng với 5 Hồi chính.<br>• Định dạng chuẩn: `mm:ss - Part X: [Tên Hồi Ngắn Gọn]`.<br>• Tuyệt đối cấm chia vụn các sub-beats con làm loãng giao diện YouTube Player. | `Dòng ________` | `[ ] PASS`<br>`[ ] FAIL` |

---

### PHẦN B: 2 TIÊU CHUẨN ĐẶC THÙ KÊNH (CHANNEL PLUGIN - 30%)
*Nạp từ `CHANNEL_PROFILE.md` của kênh Main Street Economics / Dark Economics.*

| Mã TC | Tên Tiêu Chuẩn | Dấu Hiệu Nhận Biết & Tiêu Chí Bắt Buộc | Dòng Trích Dẫn Đối Soát | Kết Quả |
| :---: | :--- | :--- | :--- | :---: |
| **P-09** | **Khí chất Nhân vật Kênh (Host Persona - Marcus)** | • Đúng chuẩn Giám định viên Pháp y Tài chính: Lạnh lùng, mỉa mai, điềm đạm, không đạo đức giả.<br>• Xuất hiện đúng câu khẩu hiệu thương hiệu: *"Dissecting corporate greed. One receipt at a time. I'm Marcus. Case closed."*<br>• Tần suất xuất hiện mascot Marcus được kiểm soát $\le$ 20% tổng số phân cảnh. | `Dòng ________` | `[ ] PASS`<br>`[ ] FAIL` |
| **P-10** | **Bằng chứng Chuyên môn & 3 Khiên Tự Vệ** | • **100% Bằng chứng kiểm chứng:** Trích dẫn từ nguồn thẩm quyền (Báo cáo thường niên SEC Form 10-K, DEF 14A, trát phạt FTC, điều luật thuế IRS Section 168(k), dữ liệu FAA). Cấm bịa đặt số liệu.<br>• **3 Khiên Tự Vệ Thực Chiến:** Hồi kết phải trao trọn vẹn đúng 3 công cụ tự vệ giúp người xem bảo vệ tiền túi hoặc danh mục hưu trí cá nhân. | `Dòng ________` | `[ ] PASS`<br>`[ ] FAIL` |

---

## 📊 BẢNG TỔNG KẾT & QUY TẮC CẤP CHỨNG NHẬN (VERDICT SCORECARD)

| Tổng Số Tiêu Chuẩn | Phán Quyết | Điều Kiện & Ý Nghĩa |
| :---: | :---: | :--- |
| **10 / 10 PASS** | 🟢 **PRODUCTION READY** | **Đạt chuẩn xuất sắc toàn diện.** Cấp phép chuyển giao ngay sang khâu viết kịch bản thoại chi tiết (`script_en.txt`, `script_en_styled.md`) và dựng storyboard CapCut. |
| **9 / 10 PASS** | 🟡 **NEEDS REVISION (CONDITIONAL PASS)** | **Đạt có điều kiện.** Chỉ chấp nhận lỗi hình thức nhẹ (như thiếu khối Timestamps U-08 hoặc từ khóa SEO U-02 có thể bổ sung trong vòng 1-2 phút). Sau khi sửa xong, tự động nâng lên Production Ready. |
| **$\le$ 8 / 10 PASS** | 🔴 **REJECTED (CIRCUIT BREAKER)** | **Bị từ chối xuất xưởng.** Trượt các tiêu chí cốt lõi (Hook U-01, Nhịp văn U-03, Bridge U-04, Persona P-09, Bằng chứng P-10). Writer bắt buộc phải biên tập lại bản thảo và nộp tái thẩm định. |
