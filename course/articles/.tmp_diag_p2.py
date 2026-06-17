import re, os

base = '/Users/yiqi/nvidia-ecosystem/course/articles'
html_path = base + '/apoorv03_consumer_ai_p2.html'
raw_path = base + '/apoorv03_consumer_ai_p2_raw.html'
zh_path = base + '/apoorv03_consumer_ai_p2_zh.txt'

with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()
with open(raw_path, 'r', encoding='utf-8', errors='ignore') as f:
    raw = f.read()
with open(zh_path, 'r', encoding='utf-8', errors='ignore') as f:
    zh = f.read()

# figure order from raw
raw_imgs = re.findall(r'<img[^>]+src="([^"]+)"', raw)
print('raw imgs total', len(raw_imgs))
for i, u in enumerate(raw_imgs, 1):
    print(i, u)

# zh paras filter
junk = {
    '顺风','订阅','登录','消费级','分享','置顶','最新','讨论','更多3条评论...',
    '关于本文的讨论','评论','转发','准备好吗？','开始你的Substack','获取应用',
    'Substack是优秀文化的家园','本网站需要JavaScript才能正常运行。请启用JavaScript或解除脚本屏蔽。',
    '© 2026 Apoorv Agrawal','· 隐私','∙ 条款','∙ 收集通知',
}
paras=[]
for line in zh.splitlines():
    s=line.strip()
    if not s: continue
    if s in junk: continue
    if s.startswith('消费AI的现状。第二部分：参与度与留存率'): continue
    if s.startswith('Apoorv Agrawal') and '年' not in s: continue
    if re.match(r'^\d{4}年\d{1,2}月\d{1,2}日$', s): continue
    paras.append(s)
print('zh paras', len(paras))
