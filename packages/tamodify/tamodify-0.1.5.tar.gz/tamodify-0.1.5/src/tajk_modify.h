#ifndef TAJK_MODIFY_H
#define TAJK_MODIFY_H
#include <stdio.h>
#include <stdarg.h>
#include <stdlib.h>
#include "tajk_data2.h"

#ifdef __cplusplus
extern "C"  {
#endif

/*
修改TA接口文件的库。未考虑线程安全

不在原文件上直接改写，只提供拷贝过程中的改写，即另一个文件进行复制，在复制的过程中可以改写数据，也可以忽略某行不再写入
仅修改文件内容，不修改文件头

大体操作流程如下：

stru_ta_modify tm;  //定义一个结构
tamodify_init(&tm);  //初始化并切换到这个结构来工作。如果需要在同一个程序中同时使用多个结构，需要用tm.use()切换。
tm.open(源文件，目标文件）   打开两个文件，源文件只读，目标文件只写，此时已经复制文件头完毕
while(tm.read()){//读入一行
    tm.get(列名,&浮点变量）;//从源文件中获取浮点数据
    tm.get(列名,字符串变量);//从源文件中获取数据
    tm.setd(列名,浮点变量）;//设置浮点数据以写入目标文件
    tm.set(列名,字符串变量);//设置数据以写入目标文件
    tm.write();//把当前修改过的行写入目标文件，如果没有这一句，则在目标文件中忽略这一行
};
if(tm.errno)说明刚刚的过程出现了错误，需要处理这个错误！
tm.close();//写入文件尾，更新条数，关闭两个文件

*/
typedef struct {
    int errnum;//最近的错误码
    char errinfo[1000];//最近的错误信息
    
    int (*open)(const char * fnsrc,const char * fndst);//打开2个文件开始复制、修改
    int (*read)();//读一行内容
    int (*write)();//将修改过的内容写入
    int (*close)();//结尾处理，关闭文件，如果有错误，则直接关闭文件。不管操作是否正常，最后都应该调用这个函数
    int (*get)(const char * colname,void * val);//根据字段名获取字符串
    int (*setd)(const char * colname,double val);//根据字段名设置浮点数据
    int (*sets)(const char * colname,const char * val);//根据字段名设置字符串
    int (*empty)(int arg);//0清空所有字段，1清空所有，数值型置为0
    
    void (*perrinfo)(int retcode,const wchar_t *errinfo);//用户可自定义一个输出错误信息的函数，不定义则使用一个空函数
    
    int ver;    //版本号，2.1版本设置21,2.2版本设置22，其它值表示错误
    int isidx;//写入文件尾时索引文件的处理和数据文件有些差异，所以需要区分是写入索引文件还是写入数据文件。。应该不需要了
    char mode[8];//模式，如索引文件中的OFI，数据文件中的01,03
    char sender[30],recver[30];//发送者，接收者
    char workday[10];//8位工作日期

    stru_fielddata sd[1000];//字段表
    int fieldnum;//sd的大小
    int recordcount,totalcount;//读入的记录数，总记录数
    int linesize;//根据文件头计算得到的行长度
    char linedata[10000];//行数据，用于读、写缓冲区
    char fname[100];//不包含目录信息的打开的文件名信息
    FILE *fjk,*fr,*fw;
    long totalcountpos;//记录totalcount的位置，用于结束的时候回写真正的记录数
    int totalcountwidth;//记录totalcount的宽度，用于回写时控制宽度
    int writecount;//写入计数    
    
    int stdlinesize;//废弃了
    int totalrecord;
    int totalrecordpos;
}stru_ta_modify;

stru_ta_modify * tamodify_init(stru_ta_modify *);//初始化并切换一个实例,用空指针则生成一个结构
int tamodify_use(stru_ta_modify *);//切换一个实例

int tamodify_open(const char * fnsrc,const char * fndst);//打开2个文件开始复制、修改,对应主结构里的open
int tamodify_read();//读入一行内容，对应主结构里的read
int tamodify_write();//写一行内容，对应主结构里的write
int tamodify_close();//最后关闭文件等处理，对应主结构里的close
int tamodify_get(const char * colname,void * val);//根据字段名获取数据
int tamodify_setd(const char * colname,double val);//根据字段名设置浮点数据
int tamodify_sets(const char * colname,const char * val);//根据字段名设置字符串
int tamodify_empty(int arg);//0清空所有字段，1清空所有，数值型置为0

#ifdef __cplusplus
}
#endif

#endif
