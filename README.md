# Uyghur Text Processing Toolkit (维语文本处理工具)

[![Python Version](https://img.shields.io/badge/python-3.13%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

## 📖 简介
本工具包提供全面的现代维吾尔语（UEY）文本处理解决方案，支持文字转换、形态分析、语法检查等核心功能，适用于自然语言处理、教育科研、信息检索等领域。

## 🚀 核心功能

### 基础处理
1. **字符规范化**
   - `normalize()`: 将字符转换为基本形式
   - `denormalize()`: 将基本字符还原为原始形式

2. **文字转换**
   python converter = UyghurScriptConverter() uly_text = converter.to_uly("UEY文本") # 转拉丁维文 usy_text = converter.to_usy("UEY文本") # 转西里尔维文
3. **形态分析**
   - `stemmer.extract("كيتاب")`: 返回词根+词缀结构
   - `tagger.pos_tag(text)`: 词性标注

### 智能处理
4. **文本校验**
   - `detect_sentence_errors(text)`: 断句错误检测
   - `spell_check(text)`: 拼写检查与建议

5. **自动纠错**
``` python 
corrector = SpellCorrector()
corrected = corrector.correct("گوشخان") 
# 返回正确拼写 "گۆشخانا"
```
## 🔧 扩展功能

### 自定义处理
1. **词库管理**
``` python
lexicon = CustomLexicon()
lexicon.add_entry("新词", pos="NOUN") # 添加自定义词汇
```
2. **跨语言音译**
``` python
transliterator.transliterate("سلام", src="arabic", tgt="latin")
```
### 语义增强
3. **语义分析**
   - `find_synonyms("ياخشى")`: 查找近义词
   - `auto_expand("مەكتەپ")`: 生成相关短语

## ⚙️ 安装
`bash pip install uyghur-text-toolkit`
## 🛠️ 快速开始
``` python 
from uytext import UyghurProcessor
processor = UyghurProcessor()
# 文本转换示例
print(processor.convert_script("مەن پىروگرامما ئىجاد قىلدىم", target="ULY"))
# 输出：men programma ijad qildim
# 形态分析示例
analysis = processor.analyze_word("ئوقۇغۇچىلارنىڭ") 
print(f"词根: {analysis.stem}, 词缀: {analysis.suffixes}")
```
## 📌 注意事项
1. 需要安装维吾尔语字体支持包
2. 推荐使用Python 3.8+环境
3. 首次使用会自动下载语言模型（约300MB）

## 🤝 贡献指南
欢迎通过Issue提交建议或通过Pull Request贡献代码，请遵循PEP8编码规范。

## 🙏 致谢

本项目在开发过程中参考了以下优秀资源：

1. **维吾尔语资源**
   - [不同形式的维文字母](https://abkai.net/zh/uyghur/uyghur-script/) - UEY,UKY,UYY,ULY,IPA 之间的转换的依据
   - [维吾尔语字母表](https://nk2028.shn.hk/uyghur/alphabet/uyghur-alphabet-zhcn.pdf) - UEY字符链接规范依据
   - [维吾尔语UEY字符与Unicode映射](https://www.ukij.org/fonts/) - UEY字符链接规范依据

2. **学术研究**
   - 《现代维吾尔语形态分析研究》- 词根提取算法理论基础
   - 《多语言混合文本处理技术》- 跨语言音译实现参考

## 📜 许可证
MIT License © 2024 Uyghur Toolkit Project
> 提示：建议在文档中添加实际运行截图和使用场景示例。如需更详细的API文档，可运行 pdoc3 --html uytext 生成自动化文档。