#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
小红书爆款文案策划工具
"""

import re
import random

class XiaohongshuCopywriter:
    def __init__(self):
        self.emojis = ["❤️", "✨", "🔥", "🌟", "💫", "🌸", "🌼", "🌺", "🍀", "🌈"]
        self.trending_tags = [
            "智能门锁", "智能家居", "好物分享", "种草", "家居生活", "生活好物",
            "智能好物", "实用好物", "家居改造", "生活小技巧", "好物推荐"
        ]

    def generate_title(self, product_name, key_feature):
        """生成标题"""
        templates = [
            f"{random.choice(self.emojis)} 解锁{product_name}新姿势，{key_feature}！",
            f"{random.choice(self.emojis)}{product_name}太香了！{key_feature}必备！",
            f"{random.choice(self.emojis)} 这个{product_name}绝了！{key_feature}！",
            f"{random.choice(self.emojis)} 终于找到{product_name}了！{key_feature}！",
            f"{random.choice(self.emojis)}{product_name}推荐！{key_feature}太实用了！"
        ]
        return random.choice(templates)

    def generate_content(self, product_name, key_features, user_scenarios):
        """生成内容"""
        content = []
        content.append("大家好！今天给大家分享一款超级实用的智能门锁配件！")
        content.append("🚪")

        for feature in key_features:
            content.append(f"{random.choice(self.emojis)} 特点：{feature}")

        content.append("")

        for scenario in user_scenarios:
            content.append(f"{random.choice(self.emojis)} 使用场景：{scenario}")

        content.append("")
        content.append("💰 价格：50-60元")
        content.append("📦 购买链接：点击下方链接即可购买")
        content.append("")
        content.append("👀 关注我，每天分享智能门锁好物！")

        return "\n".join(content)

    def generate_hashtags(self, product_name, key_features):
        """生成标签"""
        hashtags = [product_name, "智能门锁"]
        hashtags.extend(self.trending_tags)
        hashtags.extend(key_features)
        return " ".join([f"#{tag}" for tag in hashtags[:10]])

    def generate_copywriting(self, product_name, key_features, user_scenarios):
        """生成完整文案"""
        title = self.generate_title(product_name, key_features[0])
        content = self.generate_content(product_name, key_features, user_scenarios)
        hashtags = self.generate_hashtags(product_name, key_features)
        return {
            "title": title,
            "content": content,
            "hashtags": hashtags
        }

if __name__ == "__main__":
    copywriter = XiaohongshuCopywriter()

    product_name = "智能门锁锂电池"
    key_features = [
        "足容电芯，续航更长",
        "安全稳定，品质保障",
        "易于安装，兼容性强",
        "充电快速，使用寿命长"
    ]
    user_scenarios = [
        "家里智能门锁电量不足，紧急充电",
        "长时间外出，担心智能门锁电量耗尽",
        "智能门锁电池老化，需要更换"
    ]

    copywriting = copywriter.generate_copywriting(product_name, key_features, user_scenarios)

    print("--- 小红书爆款文案 ---")
    print("标题：", copywriting["title"])
    print("\n内容：")
    print(copywriting["content"])
    print("\n标签：")
    print(copywriting["hashtags"])
