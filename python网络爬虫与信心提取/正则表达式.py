'''
'PY'
'PYY'
'PYYY'
'PYYYY'
......
表达这个时要用正则表达式为PY+

-正则表达式是通用的字符串表达式
-简洁表达一组字符串的表达式
-针对字符串表达“简洁”和“特征”思想的工具
-判断某字符串的特征归属

作用：
    -表达文本类型的特征
    -同时查找和替换一组字符串
    -匹配字符串的全部或部分

使用：
    -编译

语法：
    -正则表达式由字符和操作符构成
    -常用操作符：
        .表示任何单个字符

        []字符集，对单个字符给出取值范围
            [abc]表示a,b,c,[a-z]表示a到z单个字符
        [^]非字符集，对单个字符给出排除范围
            [^abc]表示非a或b或c的单个字符
        *前一个字符0或无限次扩展
            abc*表示ab,abc,abcc,abccc等
        +前一个字符1次或无限次扩展
            abc+表示abc,abcc,abccc等
        ?表示前一个字符0次或1次扩展
            abc?表示ab,abc
        |表示左右的表达式任意一个
            abc|def表示abc,def
        {m}扩展前一个字符m次
            ab{2}c表示abbc
        {m,n}扩展前一个字符m至n次
            ab{1,2}c表示abc,abbc
        ^匹配字符串开头
            ^abc表示abc且在一个字符串的开头
        $匹配字符串结尾
            abc$表示abc且在一个字符串的结尾
        ()分组标记，内部只能使用|操作符
            (abc)表示abc,(abc|def)表示abc,def
        \d数字，等价于[0,9]

        \w单词字符，等价于[A-Za-z0-9_]
经典的正则表达式的实例：
    ^[A-Za-z]+$由26个字母组成的字符串
    ^[A-Za-z0-9]+$由26个字母和数字组成的字符串
    ^-?\d+$整数形式的字符串
    ^[0-9]*[1-9][0-9]*$正整数形式的字符串
    [1-9]\d{5}中国境内邮政编码,6位
    [\u4e00-\u9fa5]匹配中文字符
    \d{3}-\d{8}|\d{4}-\d{7}国内电话号码

正则字符串的表示类型
    raw string类型，即不含转义字符的字符串,用r'表示
    string类型

re库的主要函数
    re.search(pattern,string,flags = 0)
        -作用:从一个字符串中搜索匹配正则表达式的第一个位置，返回match对象
        -参数:
            pattern:正则表达式的字符串或原生字符串表示
            string:待匹配字符串
            flag:使用时的控制标记
                常用标记：
                re.l re.IGNORECASE忽略正则表达式的大小写，[A-Z]能够匹配小写字符
                re.M re.MULTILINE正则表达式中的^操作符能够将给定字符串的每行当作匹配开始
                re.S re.DOTALL正则表达式中的.操作符能够匹配所有字符，默认匹配除换行外的所有字符
    re.match(pattern,string,flags = 0)
        -作用:从一个字符串的开始位置起匹配正则表达式，返回match对象
        -参数：同search
    re.findall(pattern,string,flags = 0)
        -作用:搜索字符串，以列表类型返回全部能匹配的子串
        -参数：同search
    re.split(pattern,string,maxsplit = 0,flags = 0)
        -作用:将一个字符串按照正则表达式匹配结果进行分隔，返回列表类型
        -参数：
            pattern:正则表达式的字符串或原生字符串表示
            string:待匹配字符串
            maxsplit:最大分割数，剩余部分作为最后一个元素输出
            flag:使用时的控制标记
    re.finditer(pattern,string,flags = 0)
        -作用:搜索字符串，返回一个匹配结果的迭代类型，每个迭代元素是match类型
        -参数：同search
    re.sub(pattern,repl,string,count = 0,flags = 0)
        -作用:在一个字符串中替换所有匹配正则表达式的子串，返回替换后的字符串
        -参数：
            pattern:正则表达式的字符串或原生字符串表示
            repl:替换匹配字符串的字符串
            string:待匹配字符串
            count:匹配的最大次数
            flag:使用时的控制标记

re库的两种用法：
    -函数式用法：一次性操作
        rst = re.search(r'[1-9]{5}','BIT 100081')
    -面向对象用法：编译后的多次操作
        pat = re.compile(r'[1-9]{5}')
        rst = pat.search('BIT 100081')

regex = re.compile(pattern,flag = 0)
将正则表达式的字符串形式编译成正则表达式对象

match对象：
    -属性：
        .string:待匹配的文本
        .re:匹配时使用的pattern对象（正则表达式）
        .pos:正则表达式搜索文本的开始位置
        .endpos:正则表达式搜索文本的的结束位置
    -方法：
        .group(0):获得匹配后的字符串
        .start():匹配字符串在原始字符串的开始位置
        .end():匹配字符串在原始字符串的结束位置
        .span():返回(.start(),.end())

贪婪匹配和最小匹配
    re默认使用的是贪婪匹配，即输出最长的匹配的字符串
    若要用最小匹配，要加?
    实例：
        match = re.search(r'PY.*N','PYANBNCNDN')
        match.group(0)
        结果：'PYANBNCNDN'

        match = re.search(r'PY.*?N','PYANBNCNDN')
        match.group(0)
        结果：'PYAN'
    最小匹配操作符：
        *?前一个字符0次或无限次扩展，最小匹配
        +?前一个字符1次或无限次扩展，最小匹配
        ??前一个字符0次或1次扩展，最小匹配
        {m,n}?扩展前一个字符m至n次(含n),最小匹配
'''