#include <ctype.h>
#include <string.h>
#include <sys/stat.h>
#include <locale.h>
#include <iconv.h>
#include "tajk_modify.h"

static stru_ta_modify * tam;

static size_t convs(const char *to,const char * from,const char *sin,const size_t insize,char *sout,const size_t outsize){//代码转换
    size_t insize2,outsize2;
    char **cin,**cout,*c;
    iconv_t cv;
    cin=(char **)&sin;
    c=sout;
    cout=&c;
    cv=iconv_open(to,from);
    memset(sout,0,outsize);
    insize2=insize;
    outsize2=outsize;
    iconv(cv,(char **)cin,&insize2,cout,&outsize2);
    iconv_close(cv);
    return outsize2;
}

static void u2g(const char * utf8,char * gbk){  //转换utf8串到gbk
    char *outdata;
    outdata=(char *)malloc(strlen(utf8)+10);
    convs("GBK","UTF8",utf8,strlen(utf8),outdata,strlen(utf8)+5);
    strcpy(gbk,outdata);
    free(outdata);
}

static int rtn(int rtcode,const char *fmt,...){
   	char s[10000],savelocale[100];
	va_list ap;
	wchar_t ws[20000];
	if(rtcode==0){
	    return 0;
	};
	va_start(ap, fmt);
	vsnprintf(s,sizeof(s)-1,fmt,ap);
	va_end(ap);
	strcpy(savelocale,setlocale(LC_ALL,NULL));
	setlocale(LC_ALL, "zh_CN.utf8");
	mbstowcs(ws,s,sizeof(ws)/sizeof (wchar_t));
	setlocale(LC_ALL,"");
	tam->perrinfo(rtcode,ws);
	setlocale(LC_ALL,savelocale);
	return 0;
}

static char * srtrim(char *s){//清除字符串尾部的空白
    int i=strlen(s)-1;
    for(;i>=0;i--){
        if(isspace(s[i]))s[i]=0;
        else break;
    };
    return s;
}

static int readline(){//从源文件读入一行数据到lindata
    if(tam->fr==NULL)return rtn(__LINE__,"文件没打开不能读取");
    if(fgets(tam->linedata,sizeof(tam->linedata),tam->fr)==NULL)return rtn(__LINE__,"读文件错误");
    return 0;
}

static int readhead(char *t,int cd)   {//从缓冲区读入字符串，清空末尾的空格
    strcpy(t,"");
    if(readline())return 1;
    strncpy(t,tam->linedata,cd);
    t[cd-1]=0;
    srtrim(t);
    return tamodify_write();
}

static void default_perrinfo(int retcode,const wchar_t *errinfo){//用户可自定义一个输出错误信息的函数，不定义则使用这个空函数
}

int tamodify_open(const char * fnsrc,const char * fndst)    {//打开2个文件开始复制、修改
    char stemp[10000];
    int i;
    tam->errnum=0;
    strcpy(tam->errinfo,"");
    tam->totalcountpos=0;//设置为0可以在写文件时不累加writecount写入计数
    tam->fr=fopen(fnsrc,"r");
    if(tam->fr==NULL)return rtn(-1,"打开源文件%s错误",fnsrc);
    tam->fw=fopen(fndst,"w");
    if(tam->fw==NULL){
        return rtn(-1,"打开目标文件%s错误",fndst);
    };
    if(readhead(stemp,sizeof(stemp)))return __LINE__;
    if(strcmp(stemp,"OFDCFDAT")!=0)return rtn(__LINE__,"数据文件头应该是OFDCFDAT");
    if(readhead(stemp,sizeof(stemp)))return __LINE__;
    sscanf(tam->linedata,"%d",&tam->ver);
    if(tam->ver!=22)tam->ver=21;//实践中发现有些人还在使用2.0接口，就等同2.1处理吧
    if(readhead(tam->sender,sizeof(tam->sender)))return __LINE__;   //发送者
    if(readhead(tam->recver,sizeof(tam->recver)))return __LINE__;   //接收者
    if(readhead(tam->workday,sizeof(tam->workday)))return __LINE__; //日期
    if(readhead(stemp,sizeof(stemp)))return __LINE__;       //跳过
    if(readhead(tam->mode,sizeof(tam->mode)))return __LINE__;       //文件类型，如01，02，07这样
    if(readhead(stemp,sizeof(stemp)))return __LINE__;       //跳过
    if(readhead(stemp,sizeof(stemp)))return __LINE__;       //跳过
    if(readhead(stemp,sizeof(stemp)))return __LINE__;       //字段表行数
    sscanf(stemp,"%d",&tam->fieldnum);
    for(i=0,tam->linesize=0;i<tam->fieldnum;i++){
        if(readhead(stemp,sizeof(stemp)))return __LINE__;
        tam->sd[i].size=0;//供判断是否读到数据
        for(int j=0;tajk_datafile_field2[j].ver;j++){
            if(tajk_datafile_field2[j].ver!=tam->ver)continue;
            if(strcasecmp(tajk_datafile_field2[j].filemode,tam->mode)!=0)continue;
            if(strcasecmp(tajk_datafile_field2[j].name,stemp)!=0)continue;
            strcpy(tam->sd[i].name,tajk_datafile_field2[j].name);
            tam->sd[i].type=tajk_datafile_field2[j].type;
            tam->sd[i].size=tajk_datafile_field2[j].size;
            tam->sd[i].rratio=tam->sd[i].wratio=1.0;
            for(int k=0;k<tajk_datafile_field2[j].decpos;k++){
                tam->sd[i].rratio=tam->sd[i].rratio/10.0;
                tam->sd[i].wratio=tam->sd[i].wratio*10.0;
            };
            tam->sd[i].pos=tam->linesize;
            tam->linesize=tam->linesize+tam->sd[i].size;
            break;
        };
        if(tam->sd[i].size==0){//没有找到相应字段
            return rtn(__LINE__,"接口字段表中没有找到字段%s",stemp);
        };
    };
    tam->totalcountpos=ftell(tam->fw);//记录位置，最后要把数据条数回写此处
    if(readhead(stemp,sizeof(stemp)))return __LINE__;
    if(sscanf(stemp,"%d",&tam->totalcount)!=1)return rtn(__LINE__,"读数据文件行数出错");
    tam->totalcountwidth=strlen(stemp);
    tam->recordcount=0;
    tam->writecount=0;
    return 0;
}

int tamodify_read() {//读入一行内容，对应主结构里的read
    if(tam->recordcount==tam->totalcount)return 1;
    tam->recordcount++;
    return readline();
}

int tamodify_get(const char * colname,void * val){//根据字段名获取数据
    char data[3000];
    int i;
    for(i=0;i<tam->fieldnum;i++){
        if(strcasecmp(colname,tam->sd[i].name)!=0)continue;
        memcpy(data,tam->linedata+tam->sd[i].pos,tam->sd[i].size);//读入字段
        data[tam->sd[i].size]=0;//结尾清0
        srtrim(data);//清除结尾的空白
        if(tam->sd[i].type=='C' || tam->sd[i].type=='A'){//字符型
            strcpy(val,data);
        }else{
            if(sscanf(data,"%lf",(double *)val)==1){//正常读入数据
                *(double *)val=*(double *)val * tam->sd[i].rratio;
            }else{
                return 1;
            };
        };
        return 0;
    };
    return rtn(__LINE__,"字段名%s在接口文件中没找到",colname);
}

int tamodify_setd(const char * colname,double val){//根据字段名设置浮点数据
    int i;
    char temp[1000];
    for(i=0;i<tam->fieldnum;i++){
        if(strcasecmp(colname,tam->sd[i].name)!=0)continue;
        sprintf(temp,"%0*.0lf",tam->sd[i].size,val * tam->sd[i].wratio);
        memcpy(tam->linedata+tam->sd[i].pos,temp,tam->sd[i].size);
        return 0;
    };
    return rtn(__LINE__,"字段名%s在接口文件中没找到",colname);
}

int tamodify_sets(const char * colname,const char * val){//根据字段名设置字符串
    int i,k;
    for(i=0;i<tam->fieldnum;i++){
        if(strcasecmp(colname,tam->sd[i].name)!=0)continue;
        memset(tam->linedata+tam->sd[i].pos,' ',tam->sd[i].size);
        k=strlen(val);
        if(k>=tam->sd[i].size)k=tam->sd[i].size;
        memcpy(tam->linedata+tam->sd[i].pos,val,k);
        return 0;
    };
    return rtn(__LINE__,"字段名%s在接口文件中没找到",colname);
}

int tamodify_empty(int arg)    {//0清空所有字段，1清空所有，数值型置为0
    int i;
    for(i=0;i<tam->fieldnum;i++){
        
    };
    memset(tam->linedata,0,sizeof(tam->linedata));
    memset(tam->linedata,' ',tam->linesize);
    strcat(tam->linedata,"\r\n");
    return 0;
}

int tamodify_write()    {//读入一行内容，对应主结构里的write
    if(tam->fw==NULL)return rtn(-1,"未打开写文件");
    fprintf(tam->fw,"%s",tam->linedata);
    if(tam->totalcountpos>0)tam->writecount++;
    return 0;
}

int tamodify_close()    {//完成最后定稿，关闭文件，对应主结构里的close
    if(tam->errnum==0){//没有出错，则更新条数，写入文件尾
        fprintf(tam->fw,"OFDCFEND\r\n");
        fseek(tam->fw,tam->totalcountpos,SEEK_SET);
        fprintf(tam->fw,"%0*d\r\n",tam->totalcountwidth,tam->writecount);
    };
    if(tam->fr!=NULL){
        fclose(tam->fr);
        tam->fr=NULL;
    };
    if(tam->fw!=NULL){
        fclose(tam->fw);
        tam->fw=NULL;
    };
    return 0;
}

stru_ta_modify * tamodify_init(stru_ta_modify * ta_modify) {//初始化并切换一个实例
    if(ta_modify==NULL){
        ta_modify=(stru_ta_modify *)malloc(sizeof(stru_ta_modify));
    };
    tam=ta_modify;
    tam->errnum=0;
    strcpy(tam->errinfo,"");
    tam->fr=NULL;
    tam->fw=NULL;
    tam->fieldnum=0;
    tam->open=tamodify_open;
    tam->read=tamodify_read;
    tam->write=tamodify_write;
    tam->close=tamodify_close;
    tam->perrinfo=default_perrinfo;
    tam->get=tamodify_get;
    tam->setd=tamodify_setd;
    tam->sets=tamodify_sets;
    tam->empty=tamodify_empty;
    return ta_modify;
}

int tamodify_use(stru_ta_modify * ta_modify){//切换一个实例
    tam=ta_modify;
    return 0;
}
