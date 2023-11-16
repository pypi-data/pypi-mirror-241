#ifndef TAJK_LIB_H
#define TAJK_LIB_H
#include <stdio.h>
#include <stdarg.h>
#include <stdlib.h>
#include <iconv.h>
#include "tajk_data2.h"

#ifdef __cplusplus
extern "C"  {
#endif

/*
使用简介如下。参数以后续定义为准，此处着重介绍调用函数的步骤、作用及要点等。
操作之前要初始化： tajk=tajk_init();   拿到的数据指针是后续所有调用函数的第一个参数
所有操作完成后释放资源   tajk_free(tajk);
用户需要在自己的代码中定义一个函数 tajk_exportmsg 发生非正常情况会调用这个函数，可以记录日志或者输出信息，也可以只定义一个空函数

写索引文件步骤：
tajk_setmode(tajk,isidx,版本，"OFI",发送者，接收者，日期） 初始化，清除以前的数据
tajk_writebegin(tajk,目录,0,NULL）   在一个目录下打开索引文件，写入文件头
tajk_writeidx（tajk,文件类别，批次号)，把文件写入索引文件
tajk_writeend(tajk,)结束写入 此函数可处理索引和数据文件

写数据文件步骤：
tajk_setmode(tajk,isidx,版本，"OFI",发送者，接收者，日期） 初始化，清除以前的数据
tajk_bindc tajk_bindd  把字符串、数字型变量和字段进行绑定
tajk_writebegin(tajk,目录,批次号,文件名）   在一个目录下打开数据文件，写入文件头
tajk_writedata(tajk)写入一行，在这之前应该设置各字段
tajk_writeend(tajk)结束写入  此函数可处理索引和数据文件

读索引文件步骤：
tajk_readfile(tajk,isidx,文件名） 读入索引文件头,此时设置sd数组，更新ver,mode,sender,recver,workday等
tajk_readidx(tajk)读入一行，解析得到绑定的文件名、批次号等

读数据文件步骤：
tajk_readfile(tajk,isidx,文件名）读入数据文件头，初始化sd数组，更新ver,mode,sender,recver,workday等
tajk_bindc tajk_bindd  把字符串、数字型变量和字段进行绑定
tajk_readdata(tajk)读入一行，解析得到各绑定的字段

bindd函数 indi可以置为NULL，读时如果相应字段读不出合法的数字则返回默认值，同时如果indi不为NULL，置*indi为-1， 如果可以读到合法的数字，且indi不为NULL，则*indi置0
写时如果indi为空或者*indi==0则将数据写入字段，否则用空格填充此字段
*/
extern int tajk_retcode;//记录最近的返回码
extern char tajk_retmsg[1000];//记录最近的返回信息

typedef struct {
    int ver;    //版本号，2.1版本设置21,2.2版本设置22，其它值表示错误
    int isidx;//写入文件尾时索引文件的处理和数据文件有些差异，所以需要区分是写入索引文件还是写入数据文件
    char mode[8];//模式，如索引文件中的OFI，数据文件中的01,03
    char sender[30],recver[30];//发送者，接收者
    char workday[10];//8位工作日期

    stru_fielddata sd[1000];//字段表
    int fieldnum;//sd的大小
    int recordcount,totalrecord;//记录数，总记录数
    int stdlinesize,linesize;//标准行长度，读到的行长度
    char linedata[100000];//行数据，用于写缓冲区
    char fname[100];//不包含目录信息的打开的文件名信息
    FILE *fjk;
    long totalrecordpos;//记录totalrecord的位置，用于结束的时候回写真正的记录数
}stru_tajk;

stru_tajk * tajk_init();//初始化
void tajk_free(stru_tajk *);//关闭所有资源
int tajk_closeall(stru_tajk * tajk);//关闭打开的文件等

void tajk_setmode(stru_tajk *,int isidx,int ver,const char * mode,const char *send,const char *recv,const char *rq);//初始化
int tajk_bind(stru_tajk *,const char *name,void * data,short *indi);//通用的绑定字段和数据的函数，计划淘汰掉另外两个
int tajk_bindc(stru_tajk *,const char *name,char * data);//把字符字段和数据绑定方便读、写数据，计划废弃，改用bind
int tajk_bindd(stru_tajk *,const char *name,double * data,double dft,short *indi);//把数字字段和数据绑定用于快速写数据，计划废弃，改用bind
int tajk_writebegin(stru_tajk *,const char * dirname,int batchnum,const char * fname);//开始写文件,fname为空则自动生成文件名
int tajk_writedata(stru_tajk *);//数据文件写入一行数据
int tajk_writeidx(stru_tajk *,const char *filemode,int batchnum);//索引文件写入一行，filemode为01,03这样
int tajk_writeend(stru_tajk *);//结束写文件，包括写文件尾、记录数处理、关闭文件等
int tajk_readfile(stru_tajk *,int isidx,const char * dirname,const char * filename);//读入文件头
int tajk_readfile2(stru_tajk *,int isidx,const char * dirname,const char * mode,const char * send,const char * recv,const char *rq,int batchnum);//读入文件头
int tajk_readidx(stru_tajk *,char *fname,char * fmode,int *batchnum);//读入一行索引文件
int tajk_readdata(stru_tajk *);//读入一行数据文件

int tajk_setd(stru_tajk * tajk,const char * colname,double val);//根据字段名设置浮点数据
int tajk_sets(stru_tajk * tajk,const char * colname,const char * val);//根据字段名设置字符串

char * tajk_findfile(const char *fdir,const char *fname);//在指定目录下查找文件名，忽略大小写

void tajk_exportmsg(stru_tajk *,int retcode,const char *retmsg);//setret里调用此函数，必须在外部定义一个函数记录日志，输出调试等

int tajk_readlinedata(int trim);//从fjk读入一行数据到lindata，去掉结尾的回车换行

#ifdef __cplusplus
}
#endif

#endif
