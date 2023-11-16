#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include "tajk_modify.h"
#include "tajk_lib.h"

static stru_ta_modify tm;
static stru_tajk *tajk,*taidx;

static char * srtrim(char *s){//清除字符串尾部的空白
    int i=strlen(s)-1;
    for(;i>=0;i--){
        if(isspace(s[i]))s[i]=0;
        else break;
    };
    return s;
}

void tajk_exportmsg(stru_tajk * tajk,int retcode,const char *retmsg){//必须要定义一个这样的函数，可以用来输出错误日志
    printf("%d|%s|\n",retcode,retmsg);
}

static PyObject *
p_open(PyObject *self, PyObject *args)
{
    PyObject * field;
    char *fnsrc,*fndst;//源文件名，目标文件名
    int jg,i;
    if (!PyArg_ParseTuple(args, "ss", &fnsrc,&fndst))return NULL;
    jg=tamodify_open(fnsrc,fndst);
    if(jg==0){
        field=PyList_New(0);
        for(i=0;i<tm.fieldnum;i++){
            PyList_Append(field,Py_BuildValue("s", tm.sd[i].name));
        };
        PyModule_AddObject(self,"field",field);
    };
    return PyLong_FromLong(jg);
}

static PyObject *
p_close()
{
    return PyLong_FromLong(tamodify_close());
}

static PyObject *
p_read()
{
    return PyLong_FromLong(tamodify_read());
}

static PyObject *
p_write()
{
    return PyLong_FromLong(tamodify_write());
}

static PyObject *
p_get(PyObject *self, PyObject *args)
{
    char data[3000];
    int i;
    char * colname;//字段名
    double dval;//数值型数据
    if (!PyArg_ParseTuple(args, "s", &colname))return NULL;
    for(i=0;i<tm.fieldnum;i++){
        if(strcasecmp(colname,tm.sd[i].name)!=0)continue;
        memcpy(data,tm.linedata+tm.sd[i].pos,tm.sd[i].size);//读入字段
        data[tm.sd[i].size]=0;//结尾清0
        srtrim(data);//清除结尾的空白
        if(tm.sd[i].type=='C' || tm.sd[i].type=='A'){//字符型
            return Py_BuildValue("s",data);
        }else{
            if(sscanf(data,"%lf",&dval)==1){//正常读入数据
                dval=dval * tm.sd[i].rratio;
                return Py_BuildValue("f",dval);
            }else{
                return Py_BuildValue("f",0);
            };
        };
        return NULL;//类型不对
    };
    return NULL;//字段名没找到
}

static PyObject *
p_set(PyObject *self, PyObject *args)
{
    PyObject * name,*data;
    char * sdata;
    char * colname;//字段名
    double dval;//数值型数据
    if(!PyArg_ParseTuple(args,"OO",&name,&data))return NULL;
    if(PyNumber_Check(data)){//如果参数是数值
        if (!PyArg_ParseTuple(args, "sd", &colname,&dval))return NULL;
        return PyLong_FromLong(tamodify_setd(colname,dval));
    }else{
        if (!PyArg_ParseTuple(args, "ss", &colname,&sdata))return NULL;
        return PyLong_FromLong(tamodify_sets(colname,sdata));
    };
}

static PyObject *
p_createindex(PyObject *self, PyObject *args)
{   //生成一个索引,参数是版本如22,类型如OFI,发送者,接收者,日期,数据目录如.
    int ver;//版本
    char *model,*sender,*recver,*rq;//类型，发送者，接收者，日期
    static char *datadir=".";//数据目录
    if (!PyArg_ParseTuple(args, "issss|s", &ver,&model,&sender,&recver,&rq,&datadir))return NULL;
    tajk_setmode(taidx,1,ver,model,sender,recver,rq);
    return PyLong_FromLong(tajk_writebegin(taidx,datadir,0,NULL));
}

static PyObject *
p_writeindex(PyObject *self, PyObject *args,PyObject *kw)
{   //写索引中的一行
    char * filemodel;//文件类别
    int batch_number=0;//批次号
    static char *kwlist[] = {"filemodel", "batch_number", NULL};
    if (!PyArg_ParseTupleAndKeywords(args,kw,"s|i",kwlist, &filemodel,&batch_number))return NULL;
    return PyLong_FromLong(tajk_writeidx(taidx,filemodel,batch_number));
}

static PyObject *
p_closeidx(PyObject *self, PyObject *args)
{
    return PyLong_FromLong(tajk_writeend(taidx));
}

static PyObject *
p_createdatafile(PyObject *self, PyObject *args)
{   //生成数据文件并写文件头
    int ver,batchnumber=0;//版本，批次号
    char *model,*sender,*recver,*rq;//类型，发送者，接收者，日期
    static char *datadir=".",*filename=NULL;//数据目录，指定文件名（为空则自动生成文件名)
    if (!PyArg_ParseTuple(args, "issss|sis", &ver,&model,&sender,&recver,&rq,&datadir,&batchnumber,filename))return NULL;
    tajk_setmode(tajk,0,ver,model,sender,recver,rq);
    return PyLong_FromLong(tajk_writebegin(tajk,datadir,batchnumber,filename));
}

static PyObject *
p_set2(PyObject *self, PyObject *args)
{
    PyObject * name,*data;
    char * sdata;
    char * colname;//字段名
    double dval;//数值型数据
    if(!PyArg_ParseTuple(args,"OO",&name,&data))return NULL;
    if(PyNumber_Check(data)){//如果参数是数值
        if (!PyArg_ParseTuple(args, "sd", &colname,&dval))return NULL;
        return PyLong_FromLong(tajk_setd(tajk,colname,dval));
    }else{
        if (!PyArg_ParseTuple(args, "ss", &colname,&sdata))return NULL;
        return PyLong_FromLong(tajk_sets(tajk,colname,sdata));
    };
}

static PyObject *
p_writedata(PyObject *self, PyObject *args)
{
    return PyLong_FromLong(tajk_writedata(tajk));
}

static PyObject *
p_closedatafile(PyObject *self, PyObject *args)
{
    return PyLong_FromLong(tajk_writeend(tajk));
}

static PyMethodDef pMethods[] = {
    {"open",  p_open, METH_VARARGS,"open(源文件名,目标文件名)\n指定源文件、目标文件开始复制、修改"},
    {"close",  p_close, METH_VARARGS,"close()\n最后一步操作：写文件尾，重置记录数量，关闭打开的文件"},
    {"read",  p_read, METH_VARARGS,"read()\n读入源文件中一行数据到缓冲区"},
    {"write",  p_write, METH_VARARGS,"read()\n把缓冲区中数据写入目标文件中"},
    {"get",  p_get, METH_VARARGS,"get(字段名)\n读取缓冲区中字段的值，根据字段类型返回字符串或者是数值"},
    {"set",  p_set, METH_VARARGS,"set(字段名,数据)\n更新缓冲区中字段的值"},
    {"createidx",p_createindex,METH_VARARGS,"nexidx(版本如22,类型如OFI,发送者,接收者,日期,数据目录如.)\n打开索引文件并写文件头"},
    {"widx",(PyCFunction)p_writeindex,METH_VARARGS | METH_KEYWORDS ,"nexidx(版本如22,类型如OFI,发送者,接收者,日期[,数据目录如.])\n索引文件写一行"},
    {"closeidx",p_closeidx,METH_VARARGS,"closeidx()\n写索引文件尾，结束写入"},
    {"createdatafile",p_createdatafile,METH_VARARGS,"createdatafile(版本如22,类型如01,发送者,接收者,日期,[数据目录如.,批次号,文件名])\n生成数据文件并写文件头"},
    {"set2", p_set2, METH_VARARGS,"set(字段名,数据)\n更新缓冲区中字段的值"},
    {"writedata", p_writedata, METH_VARARGS,"writedata()\n写一行数据到文件，注意要用set2设置各字段"},
    {"closedatafile",p_closedatafile,METH_VARARGS ,"closedatafile()\n写数据文件尾，结束写入"},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

static struct PyModuleDef pmodule = {
    PyModuleDef_HEAD_INIT,
    "tamodify",   /* name of module */
    PyDoc_STR("TA接口文件修改、生成、读取工具"),
    -1,       /* size of per-interpreter state of the module,
                 or -1 if the module keeps state in global variables. */
    pMethods
};

PyObject *
PyInit_tamodify(void){
    PyObject * m;
    tamodify_init(&tm);
    taidx=tajk_init();
    tajk=tajk_init();
    m=PyModule_Create(&pmodule);
    return m;
}
