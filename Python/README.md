# GetPCLicense
通过python调用c++类，计算电脑的cpu，mac，disk的唯一标志符。

##使用
1. 生成 ipmodule.so
```
mkdir build&&cd build
cmake ..
make
```

2. 运行（注意，为了获取得到disk_serial_number一定要sudo）
sudo python test.py
可以看到
```
cpu_id_by_asm:  E9060900-FFFBEBBF-FEFBEBBF-0000
can not get mac id
disk_serial_number:  WD-WCC4M4DYZJV4
```
