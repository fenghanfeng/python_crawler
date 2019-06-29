#变量替换总结

1. ${变量#匹配规则}	：从头开始匹配，最短删除

2. ${变量##匹配规则}	：从头开始匹配，最长删除

3. ${变量%匹配规则}	：从尾开始匹配，最短删除

4. ${变量%%匹配规则}	：从尾开始匹配，最长删除

5. ${变量/旧字符串/新字符串}	：替换变量内旧字符串为新字符串，只替换一次

6. ${变量//旧字符串/新字符串}	：替换变量内旧字符串为新字符串，全部替换


##例子
	# 定义变量与赋值
	[root@iZ88ud1ufgymt5Z ~]# variable_1='I love you,Do you love me'
	[root@iZ88ud1ufgymt5Z ~]# echo $variable_1
	I love you,Do you love me

	# 变量的删除，从头匹配
	[root@iZ88ud1ufgymt5Z ~]# var1=${variable_1#*ov}
	[root@iZ88ud1ufgymt5Z ~]# echo $var1
	e you,Do you love me
	[root@iZ88ud1ufgymt5Z ~]# var2=${variable_1##*ov}
	[root@iZ88ud1ufgymt5Z ~]# echo $var2
	e me

	# 变量的删除，从尾匹配
	[root@iZ88ud1ufgymt5Z ~]# var3=${variable_1%ov*}
	[root@iZ88ud1ufgymt5Z ~]# echo $var3
	I love you,Do you l
	[root@iZ88ud1ufgymt5Z ~]# var3=${variable_1%%ov*}
	[root@iZ88ud1ufgymt5Z ~]# echo $var3
	I l

	# 变量的替换
	[root@iZ88ud1ufgymt5Z ~]# echo $PATH
	/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin
	[root@iZ88ud1ufgymt5Z ~]# var5=${PATH/bin/BIN}
	[root@iZ88ud1ufgymt5Z ~]# echo $var5
	/usr/local/sBIN:/usr/local/bin:/usr/sbin:/usr/bin
	[root@iZ88ud1ufgymt5Z ~]# var6=${PATH//bin/BIN}
	[root@iZ88ud1ufgymt5Z ~]# echo $var6
	/usr/local/sBIN:/usr/local/BIN:/usr/sBIN:/usr/BIN

![](https://python-class.oss-cn-shenzhen.aliyuncs.com/python-games/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20190606135348.png)
