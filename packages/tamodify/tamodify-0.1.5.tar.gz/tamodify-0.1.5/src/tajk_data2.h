#ifndef	tajk_data_h
#define tajk_data_h

#ifdef __cplusplus
extern "C"  {
#endif

struct stru_tajk_datafile_field2	{//新版本的接口文件字段列表,不再使用数据字典表，直接使用字段列表，把字段名等内容也放在这里，去掉没使用的描述字段
    int ver;    //版本，目前支持2.0(仅部分文件：43、44（电子合同）)、2.1和2.2，对应取值为20、21和22
    char filemode[3];//文件类型,如01,02这样
    char name[50],type;     //字段名，类型（C、A、N）
    int size,decpos;        //大小，小数位置
};

extern struct stru_tajk_datafile_field2 tajk_datafile_field2[];//数据文件和字段对应关系版本2

typedef struct {
    char name[50],type;
    int size,pos;//大小,为0表示结构数组结束;在行中位置
    double rratio,wratio;//用于处理数据的小数乘数,分别用于读和写
    char *cdata;    //绑定字符型字段用
    double *ddata;  //绑定数据型字段用
    double valdft;//数值的默认值
    short *indi,ind;//读时，如果字段为空，置-1，否则置0。写时，为0正常设置字段，非0则用空格填充这个字段
}stru_fielddata;//字段表

#ifdef __cplusplus
}
#endif

#endif
