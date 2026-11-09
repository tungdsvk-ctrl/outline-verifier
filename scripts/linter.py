#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
OUTLINE STATIC LINTER (TẦNG 1: DETERMINISTIC FAST-PASS)
Skill: outline-verifier
Chức năng: Quét kiểm tra cấu trúc kỹ thuật cứng của file OUTLINE.md
           Độ trễ < 0.1 giây, chi phí 0 token.
Sử dụng: python scripts/linter.py <đường_dẫn_file_outline.md> [tùy_chọn]
=============================================================================
"""

import sys
import os
import re

# Bắt buộc UTF-8 cho stdout trên Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except Exception:
        pass

# Danh mục từ rác AI bị cấm tuyệt đối (Slop Words Zero-Tolerance)
BANNED_WORDS_EN = [
    r"\bdelve\b", r"\bunravel\b", r"\btapestry\b", r"\bbeacon\b",
    r"\btestament\b", r"\bnavigate\b", r"\blandscape\b", r"\bat its core\b",
    r"\bvital\b", r"\bgame-changer\b", r"\bever-evolving\b", r"\bshed light on\b",
    r"\brealm\b"
]

BANNED_WORDS_VI = [
    r"bức tranh toàn cảnh", r"vén màn bí mật", r"hãy cùng đi sâu vào",
    r"chìa khóa vạn năng", r"bước ngoặt lịch sử", r"khiến chúng ta phải suy ngẫm"
]

class OutlineLinter:
    def __init__(self, file_path: str, expected_parts: int = 5, min_words: int = 2700, max_words: int = 3500):
        self.file_path = file_path
        self.expected_parts = expected_parts
        self.min_words = min_words
        self.max_words = max_words
        self.errors = []
        self.warnings = []
        self.content = ""
        self.lines = []

    def load_file(self) -> bool:
        if not os.path.exists(self.file_path):
            self.errors.append(f"[LỖI FILE] Không tìm thấy file: {self.file_path}")
            return False
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                self.content = f.read()
            self.lines = self.content.splitlines()
            return True
        except Exception as e:
            self.errors.append(f"[LỖI ĐỌC FILE] Không thể đọc file: {str(e)}")
            return False

    def check_parts(self):
        """Tiêu chí 1: Đảm bảo có đủ đúng số tiêu đề Hồi từ PART 1 đến PART N (hỗ trợ ## hoặc ###)"""
        parts = re.findall(r"^#{2,3}\s+PART\s+([1-9]\d*):", self.content, re.MULTILINE | re.IGNORECASE)
        expected = [str(i) for i in range(1, self.expected_parts + 1)]
        if parts != expected:
            self.errors.append(
                f"[LỖI CẤU TRÚC HỒI] Danh sách các Hồi tìm thấy là {parts}. "
                f"Yêu cầu bắt buộc phải đủ và đúng thứ tự {self.expected_parts} Hồi: {expected}."
            )

    def check_word_count(self):
        """Tiêu chí 2: Kiểm tra dung lượng từ ngữ cho thời lượng chuẩn"""
        words = re.findall(r"\b\w+\b", self.content)
        total_words = len(words)
        
        if total_words < self.min_words:
            self.errors.append(
                f"[LỖI DUNG LƯỢNG] Kịch bản quá ngắn ({total_words} từ). "
                f"Yêu cầu tối thiểu {self.min_words} từ để đảm bảo thời lượng mục tiêu."
            )
        elif total_words > self.max_words:
            self.warnings.append(
                f"[CẢNH BÁO DUNG LƯỢNG] Kịch bản khá dài ({total_words} từ). "
                f"Nên kiểm soát dưới {self.max_words} từ để tránh video bị loãng."
            )

    def check_tts_line_length(self):
        """Tiêu chí 3: Rào cản TTS an toàn (100% câu độc lập len <= 150 ký tự)"""
        violating_lines = []
        for idx, line in enumerate(self.lines, start=1):
            stripped = line.strip()
            # Bỏ qua dòng trống, tiêu đề markdown, blockquote, bảng, hoặc dòng phân cách
            if not stripped or stripped.startswith("#") or stripped.startswith(">") or stripped.startswith("|") or stripped.startswith("---") or stripped.startswith("```"):
                continue
            
            # Kiểm tra độ dài câu thoại
            if len(stripped) > 150:
                if '"' in stripped or "'" in stripped or "*" in stripped:
                    violating_lines.append((idx, len(stripped), stripped[:60] + "..."))

        if violating_lines:
            sample_errors = violating_lines[:5]
            details = "\n  - ".join([f"Dòng {l[0]} ({l[1]} ký tự): {l[2]}" for l in sample_errors])
            msg = (
                f"[CẢNH BÁO TTS] Phát hiện {len(violating_lines)} dòng dài quá 150 ký tự "
                f"(gây nguy cơ méo tiếng / hụt hơi AI Voice ElevenLabs):\n  - {details}"
            )
            self.warnings.append(msg)

    def check_banned_slop_words(self):
        """Tiêu chí 4: Bộ lọc từ rác AI (Slop Zero-Tolerance)"""
        found_slop = []
        all_patterns = BANNED_WORDS_EN + BANNED_WORDS_VI
        for pattern in all_patterns:
            matches = re.finditer(pattern, self.content, re.IGNORECASE)
            for m in matches:
                line_no = self.content[:m.start()].count("\n") + 1
                found_slop.append((line_no, m.group()))

        if found_slop:
            details = ", ".join([f"'{s[1]}' (Dòng {s[0]})" for s in found_slop[:5]])
            self.errors.append(
                f"[LỖI TỪ RÁC AI] Phát hiện {len(found_slop)} từ rác AI bị cấm: {details}. "
                f"Yêu cầu xóa bỏ hoàn toàn theo quy chuẩn Trụ cột 5."
            )

    def run_all(self) -> bool:
        if not self.load_file():
            return False

        self.check_parts()
        self.check_word_count()
        self.check_tts_line_length()
        self.check_banned_slop_words()

        return len(self.errors) == 0

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Universal Outline Static Linter")
    parser.add_argument("file_path", help="Đường dẫn file OUTLINE.md cần quét")
    parser.add_argument("--parts", type=int, default=5, help="Số Hồi dự kiến (mặc định: 5)")
    parser.add_argument("--min-words", type=int, default=2700, help="Số từ tối thiểu (mặc định: 2700)")
    parser.add_argument("--max-words", type=int, default=3500, help="Số từ tối đa (mặc định: 3500)")

    args = parser.parse_args()
    target_file = args.file_path
    print(f"🔍 BẮT ĐẦU QUÉT UNIVERSAL STATIC LINTER: {target_file}")
    print(f"⚙️ CẤU HÌNH: {args.parts} Hồi | Dung lượng: {args.min_words} - {args.max_words} từ")
    print("=" * 70)

    linter = OutlineLinter(
        target_file,
        expected_parts=args.parts,
        min_words=args.min_words,
        max_words=args.max_words
    )
    is_passed = linter.run_all()

    if linter.warnings:
        print(f"⚠️ CÁC CẢNH BÁO ({len(linter.warnings)} mục):")
        for w in linter.warnings:
            print(f"  {w}")
        print("-" * 70)

    if not is_passed:
        print(f"❌ KẾT QUẢ: TẦNG 1 THẤT BẠI ({len(linter.errors)} LỖI CẤU TRÚC)")
        for err in linter.errors:
            print(f"  {err}")
        print("=" * 70)
        print("⛔ CHẶN CỔNG: Không đủ điều kiện chuyển sang Tầng 2 (Dual QA).")
        sys.exit(1)
    else:
        print("✅ KẾT QUẢ: TẦNG 1 HOÀN TOÀN ĐẠT CHUẨN (EXIT CODE: 0)")
        print("🚀 ĐỦ ĐIỀU KIỆN CHUYỂN TIẾP SANG TẦNG 2 (DUAL-AUDITOR CONSENSUS).")
        print("=" * 70)
        sys.exit(0)

if __name__ == "__main__":
    main()
