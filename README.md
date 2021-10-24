--------------------------------------------------

Author:      Zhipeng Wu  
Email:       763008300@qq.com  
Website:     https://wuzhipeng.cn/  
Create on:   2/14/2021 10:48 PM 

----------------------------------------------------

# LICSBAS for Windows
> Forked from the original [LICSBAS](https://github.com/yumorishita/LiCSBAS) and revised the code to support running on windows.

LiCSBAS is an open-source package in Python and bash to carry out InSAR time series analysis using LiCSAR products (i.e., unwrapped interferograms and coherence) which are freely available on the [COMET-LiCS web portal](https://comet.nerc.ac.uk/COMET-LiCS-portal/).

Users can easily derive the time series and velocity of the displacement if sufficient LiCSAR products are available in the area of interest. LiCSBAS also contains visualization tools to interactively display the time series of displacement to help investigation and interpretation of the results.

---

## Tutorial

1. Download and install [Python](https://www.python.org/).

2. Access [source code](https://github.com/Wu-Patrick/LiCSBAS) -> click `Code` -> click `Download ZIP`, and unzip it wherever you want, you need to provide its absolute path later. 

3. Open cmd and run the command to install python package.

   ~~~cmd~~
   cd LiCSBAS-master
   pip install -r LiCSBAS_requirements.txt
   ~~~

   If the GDAL installation fails, perform the following steps to install it manually.

   a. Download the appropriate GDAL installation file according to your computer system and python version from [http://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal](http://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal), such as GDAL-x.x.x-cpxx-cpxxm-win_amd64.whl

   b. Use the command `pip install GDAL-x.x.x-cpxx-cpxxm-win_amd64.whl` to install, note that xx needs to be replaced.

4. Download and install [MSYS2](https://www.msys2.org/).

5. Add three environment variables. Add the absolute path of `LiCSBAS-master\bin` to the environment variable `Path`; create a new environment variable `PYTHONPATH` with the value set to the absolute path of `LiCSBAS-master\LiCSBAS_lib`; create a new environment variable `MSYS2_PATH_TYPE` with the value set to `inherit`.

6. Run MSYS2 as **administrator** to use LiCSBAS.

---

## 教程

1. 下载并安装[Python](https://www.python.org/)。

2. 访问[源代码](https://github.com/Wu-Patrick/LiCSBAS)->点击`Code`->点击`Download ZIP`，然后解压到任意位置，后面需要提供其绝对路径。

3. 打开cmd，运行命令以安装python包：

   ~~~cmd~~
   cd LiCSBAS-master
   pip install -r LiCSBAS_requirements.txt
   ~~~

   如果GDAL安装失败，执行以下步骤手动安装：

   a. 根据你的计算机系统和python版本，从[http://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal](http://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal),下载合适的GDAL安装文件，如GDAL-x.x.x-cpxx-cpxxm-win_amd64.whl

   b. 使用`pip install GDAL-x.x.x-cpxx-cpxxm-win_amd64.whl`命令进行安装，注意xx需要被替换。

4. 下载并安装[MSYS2](https://www.msys2.org/).

5. 添加三个环境变量。将`LiCSBAS-master\bin`的绝对路径添加到环境变量`Path`中；新建环境变量`PYTHONPATH`，变量值设置为`LiCSBAS-master\LiCSBAS_lib`的绝对路径；新建环境变量`MSYS2_PATH_TYPE`，变量值设置为`inherit`。

6. 使用**管理员**身份运行MSYS2，即可使用LiCSBAS。
