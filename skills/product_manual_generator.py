#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
产品说明书生成工具
"""

class ProductManualGenerator:
    def __init__(self):
        self.sections = [
            "产品概述", "技术参数", "安装说明", "使用方法", "维护保养", "注意事项", "故障排除", "售后服务"
        ]

    def generate_manual(self, product_name, product_overview, technical_parameters, installation_instructions, usage_methods, maintenance, precautions, troubleshooting, after_sales):
        """生成产品说明书"""
        manual = []
        manual.append(f"# {product_name}说明书")
        manual.append("")

        manual.append("## 产品概述")
        manual.append(product_overview)
        manual.append("")

        manual.append("## 技术参数")
        for key, value in technical_parameters.items():
            manual.append(f"- {key}：{value}")
        manual.append("")

        manual.append("## 安装说明")
        manual.append(installation_instructions)
        manual.append("")

        manual.append("## 使用方法")
        manual.append(usage_methods)
        manual.append("")

        manual.append("## 维护保养")
        manual.append(maintenance)
        manual.append("")

        manual.append("## 注意事项")
        manual.append(precautions)
        manual.append("")

        manual.append("## 故障排除")
        for problem, solution in troubleshooting.items():
            manual.append(f"- **问题**：{problem}")
            manual.append(f"  **解决方法**：{solution}")
        manual.append("")

        manual.append("## 售后服务")
        manual.append(after_sales)
        manual.append("")

        manual.append("---")
        manual.append("本说明书仅供参考，如有变动，请以实物为准。")

        return "\n".join(manual)

if __name__ == "__main__":
    generator = ProductManualGenerator()

    product_name = "智能门锁锂电池"
    product_overview = "本产品是智能门锁专用的锂电池，适用于各种型号的智能门锁，具有续航时间长、安全稳定等特点。"
    technical_parameters = {
        "电压": "3.7V",
        "容量": "3000mAh",
        "尺寸": "100mm×50mm×10mm",
        "重量": "100g",
        "使用寿命": "3-5年"
    }
    installation_instructions = "1. 打开智能门锁电池盖\n2. 取出旧电池\n3. 插入新电池\n4. 关闭电池盖"
    usage_methods = "1. 插入电池后，智能门锁会自动开机\n2. 电池电量不足时，智能门锁会发出提示音\n3. 当电池电量耗尽时，智能门锁会自动锁定"
    maintenance = "1. 定期检查电池电量\n2. 避免电池接触水或其他液体\n3. 避免电池受到强烈冲击\n4. 当电池使用时间超过3年时，建议更换新电池"
    precautions = "1. 请勿将电池投入火中或高温环境\n2. 请勿将电池短路\n3. 请勿自行拆解电池\n4. 请勿使用非指定型号的电池"
    troubleshooting = {
        "智能门锁无法正常工作": "检查电池是否正确安装，电池电量是否充足",
        "电池电量显示不正确": "检查电池是否接触良好，或更换新电池",
        "电池无法充电": "检查充电器是否正常，充电接口是否接触良好"
    }
    after_sales = "本产品提供1年质保，在质保期内，如产品出现质量问题，可免费更换或维修。"

    manual = generator.generate_manual(product_name, product_overview, technical_parameters, installation_instructions, usage_methods, maintenance, precautions, troubleshooting, after_sales)

    print("--- 产品说明书 ---")
    print(manual)
