# ============================================================
#                 XPath 语法结构总结
# ============================================================
#
# XPath (XML Path Language) 是用于在 XML/HTML 文档中选择节点的查询语言。
# 广泛应用于爬虫（Scrapy、lxml）、自动化测试（Selenium）、XSLT 等场景。
#
#
# 一、路径表达式（核心语法）
# ============================================================
#
# 表达式      含义                    示例
# ────────────────────────────────────────────────────────────
# /          从根节点选取            /html/body/div
# //         从任意位置选取          //div[@class='title']
# .          选取当前节点            ./p
# ..         选取父节点              ../span
# @          选取属性                //a/@href
# *          通配符（任意元素）      //div/*（div 下所有子元素）
# @*         通配符（任意属性）      //div/@*（div 的所有属性）
# node()     匹配任意节点             //div/node()
# text()     选取文本节点            //p/text()
#
#
# 二、谓语（Predicate）—— 筛选条件，用 [] 包裹
# ============================================================
#
# 谓语                        含义
# ────────────────────────────────────────────────────────────
# [x]                         第 x 个元素（从 1 开始计数）
# [last()]                    最后一个元素
# [last()-1]                  倒数第二个元素
# [position()<4]              前 3 个元素
# [position()>1]              第 2 个及之后所有元素
# [@attr]                     拥有某属性的元素
# [@attr='value']             属性等于某值
# [@attr!='value']            属性不等于某值
# [text()='xxx']              文本精确匹配
# [.='xxx']                   当前节点文本精确匹配
# [contains(@attr,'val')]     属性包含子串
# [contains(text(),'val')]    文本包含子串
# [starts-with(@attr,'val')]  属性以某值开头
# [ends-with(@attr,'val')]    属性以某值结尾（XPath 2.0+）
# [string-length(text())>n]   文本长度大于 n
# [not()]                     取反
# [not(contains(@class,'x'))] 不包含某 class
#
#
# 三、轴（Axes）—— 节点关系导航
# ============================================================
#
# 语法格式：轴名::节点名[谓语]
#
# 轴名                      选取方向
# ────────────────────────────────────────────────────────────
# child::                   子节点（默认轴，可省略）
# parent::                  父节点           等价于 ..
# self::                    当前节点          等价于 .
# ancestor::                所有祖先节点（父→祖→根）
# ancestor-or-self::        祖先 + 自身
# descendant::              所有后代节点（子→孙→...）
# descendant-or-self::      后代 + 自身      等价于 //
# following::               当前节点之后的所有节点
# following-sibling::       之后的同级节点
# preceding::               当前节点之前的所有节点
# preceding-sibling::       之前的同级节点
# attribute::               属性             等价于 @
# namespace::               命名空间节点
#
# 轴实用示例：
#   //h2/following-sibling::p[1]       —— h2 后面的第一个 p 兄弟
#   //p[@class]/preceding-sibling::*   —— 前面所有同级元素
#   //div/ancestor::body               —— 向上找到 body 祖先
#   //span/parent::div                 —— span 的父 div
#
#
# 四、运算符
# ============================================================
#
# 运算符            含义          示例
# ────────────────────────────────────────────────────────────
# |                 并集（合并）   //h1 | //h2 | //h3
# and               逻辑与         @class='a' and @id='b'
# or                逻辑或         @class='a' or @class='b'
# =                 等于
# !=                不等于
# <                 小于
# >                 大于
# <=                小于等于
# >=                大于等于
# +                 加
# -                 减
# *                 乘
# div               除
# mod               取余          position() mod 2 = 1（奇数行）
#
#
# 五、常用函数
# ============================================================
#
# 函数                        用途
# ────────────────────────────────────────────────────────────
# text()                      获取文本内容
# contains(a, b)              判断 a 是否包含 b
# starts-with(a, b)           判断 a 是否以 b 开头
# string-length(s)            字符串长度
# substring(s, start, len)    截取子串
# substring-before(s, sep)    分隔符前的部分
# substring-after(s, sep)     分隔符后的部分
# concat(a, b, ...)           拼接字符串
# normalize-space(s)          去除首尾空白并压缩中间空白
# translate(s, from, to)      字符替换
# not(expr)                   逻辑取反
# position()                  当前节点在结果集中的位置
# last()                      结果集大小
# count(expr)                 统计节点数量
# name()                      节点名称
# local-name()                去除命名空间的节点名称
# sum(expr)                   数值求和
# floor(n) / ceiling(n)       向下 / 向上取整
# round(n)                    四舍五入
#
#
# 六、实用速查
# ============================================================
#
# 场景                                  XPath 写法
# ────────────────────────────────────────────────────────────────
# 选取所有标题                          //h1 | //h2 | //h3 | //h4
# 选取 class='box' 的 div               //div[@class='box']
# 选取 class 包含 'box' 的 div          //div[contains(@class,'box')]
# 选取 id='main' 下所有 p               //*[@id='main']//p
# 选取 href 含 'google' 的链接          //a[contains(@href,'google')]
# 选取所有图片的 src                    //img/@src
# 选取空链接                            //a[not(@href) or @href='']
# 选取第三个 li                          //ul/li[3]
# 选取前5个 li                          //ul/li[position()<=5]
# 选取文本以"新闻"开头的 a              //a[starts-with(text(),'新闻')]
# 选取奇数行                            //tr[position() mod 2 = 1]
# 选取含某 data 属性的元素              //*[@data-xxx]
# 选取某元素后的全部同级                //h2[1]/following-sibling::*
# 选取某元素前的全部同级                //h2[3]/preceding-sibling::*
# 同时选多种元素                        //a | //button | //input
# 选取直接文本（非后代文本）            //p/text()
# 选取所有输入框                        //input | //textarea | //select
# 选取可见元素（排除 hidden）           //*[not(contains(@style,'display:none'))]
#
#
# 七、浏览器控制台测试
# ============================================================
#
# 在 Chrome DevTools Console 中可直接测试：
#
#   $x('//div[@class="title"]')
#   $x('//a[contains(text(),"更多")]')
#   $x('count(//img)')
#
# 返回匹配元素数组，可直接操作。
