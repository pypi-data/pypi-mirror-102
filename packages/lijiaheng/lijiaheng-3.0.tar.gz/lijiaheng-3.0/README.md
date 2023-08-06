## setuptools本地安装
> 本项目用于演示setuptools的功能，需要注意目录结构，setup.py要与源码项目的根文件夹处于同一个路径下

1. 将本项目的test文件夹上传到服务器
2. cd到test的根目录，并执行python setup.py install，如果报错类似（__init__() takes exactly 2 arguments (4 give)），说明是setuptools的版本问题，执行pip3 uninstall setuptools、pip3 install setuptools即可。python会自动使用pip安装在install_requires中指定的依赖包
3. 由于在console_scripts指定了参数，所以在命令行中执行lijiaheng时，实际上会调用lijiaheng.py的main方法，最后执行pip list|grep lijiaheng，可以看到已经将模块安装到python的库中


## 上传到官方pip源
1. 在官网注册pypi账户：https://pypi.org/account/register/，并验证邮箱，已注册账户为：wefl/woaipython123
2. 安装twine：pip install twine
3. 按照前面的步骤在本地安装模块后，项目根目录下会多出3个目录，其中dist目录下有一个egg文件，将该文件上传到官方源即可，在文件夹test的根目录下执行：twine upload dist/* --username wefl --password woaipython123
4. 在其他计算机上执行：pip install lijiaheng -i https://pypi.org/simple，即可安装自己上传的模块
