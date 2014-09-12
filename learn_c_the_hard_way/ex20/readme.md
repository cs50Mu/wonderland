##可变参数为空的问题
看了好久都不明白头文件dbg.h中的定义` #define debug(M, ...) fprintf(stderr, "DEBUG %s:%d: " M "\n", __FILE__, __LINE__, ##__VA_ARGS__)`是怎么实现的，总感觉有点问题啊，我知道`__VA_ARGS__`和`##`的作用，但是如果可变参数是空字符的话，翻译出来的语句中最后会多了一个`,`的啊！

直到我在《Linux C编程一站式学习》的在线版中发现了这个：    

gcc有一种扩展语法，如果`##`运算符用在`__VA_ARGS__`前面，除了起连接作用之外还有特殊的含义，例如内核代码`net/netfilter/nf_conntrack_proto_sctp.c`中的：

`#define DEBUGP(format, ...) printk(format, ## __VA_ARGS__)`

printk这个内核函数相当于printf，也带有格式化字符串和可变参数，由于内核不能调用libc的函数，所以另外实现了一个打印函数。这个函数式宏定义可以这样调用：`DEBUGP("info no. %d", 1)`。也可以这样调用：`DEBUGP("info")`。后者相当于可变参数部分传了一个空参数，但展开后并不是`printk("info",)`，而是`printk("info")`，当`__VA_ARGS__`是空参数时，`##`运算符把它前面的`,`号“吃”掉了。

##make的no debug标志
在Makefile中添加-DNDEBUG标志等价于在文件中添加宏定义`#define NDEBUG`
