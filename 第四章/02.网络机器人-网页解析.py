from lxml import html

#读取html文件
with open("img/斗破苍穹.html", "r", encoding="utf-8") as f:
    html_doc=f.read()

    #解析html的文本，将其转换为一个文档列表
    doc=html.fromstring(html_doc)

    #解析表头-xpath语法
    th_list=doc.xpath('//table/thead/tr/th/text()')
    print(th_list)

    # 解析表格中的数据-xpath语法
    # 获取第一行数据
    td_list=doc.xpath('//table/tbody/tr[1]/td/text()')
    print(td_list)

    # #获取所有行数据
    tr_list=doc.xpath('//table/tbody/tr')
    for tr in tr_list:
        td_list=tr.xpath('./td/text()')
        print(td_list)


