## C 语言学习笔记


### 视频课程
- [mooc 网](./docs/imooc/readme.md)
- [你好编程](./c_from_hello_code/README.md)
- [gcc](./docs/gcc/README.md)


### 教材

[<font color="orange">《C 程序设计语言》</font>](./docs/books/C_Programming_Language.md)


### 开源代码

#### Linux Kernel

- 在 Mac 上 clone 代码遇到了问题，有些文件会被自动修改：
```shell
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   include/uapi/linux/netfilter/xt_CONNMARK.h
	modified:   include/uapi/linux/netfilter/xt_dscp.h
	modified:   include/uapi/linux/netfilter/xt_mark.h
	modified:   include/uapi/linux/netfilter/xt_rateest.h
	modified:   include/uapi/linux/netfilter/xt_tcpmss.h
	modified:   include/uapi/linux/netfilter_ipv4/ipt_ecn.h
	modified:   include/uapi/linux/netfilter_ipv4/ipt_ttl.h
	modified:   include/uapi/linux/netfilter_ipv6/ip6t_hl.h
	modified:   net/netfilter/xt_dscp.c
	modified:   net/netfilter/xt_hl.c
	modified:   net/netfilter/xt_rateest.c
	modified:   net/netfilter/xt_tcpmss.c
	modified:   tools/memory-model/litmus-tests/Z6.0+pooncelock+poonceLock+pombonce.litmus
```
[网上有人问了这个问题](https://unix.stackexchange.com/questions/722233/why-the-linux-source-repo-modified-automatically-in-macos-12-5)
    - 问题似乎是仓库无法在不区分大小写的文件系统上进行检出。您可以创建一个区分大小写的单独分区，或者在Docker容器中进行操作。


