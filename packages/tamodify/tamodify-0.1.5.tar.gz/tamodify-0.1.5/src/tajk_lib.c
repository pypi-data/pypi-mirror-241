#include <ctype.h>
#include <dirent.h>
#include <string.h>
#include <sys/stat.h>
#include "tajk_lib.h"

int tajk_retcode;//记录最近的返回码
char tajk_retmsg[1000];//记录最近的返回信息

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

static int setret(stru_tajk * tajk,int returncode,const char *fmt,...)  {//设置返回码、返回信息
    va_list ap;
    va_start(ap, fmt);
    vsnprintf(tajk_retmsg,sizeof(tajk_retmsg)-1,fmt,ap);
    va_end(ap);
    tajk_retcode=returncode;
    tajk_exportmsg(tajk,tajk_retcode,tajk_retmsg);
    return returncode;
}

static char * srtrim(char *s){//清除字符串尾部的空白
    int i=strlen(s)-1;
    for(;i>=0;i--){
        if(isspace(s[i]))s[i]=0;
        else break;
    };
    return s;
}

int tajk_closeall(stru_tajk * tajk){//关闭打开的文件等
	if(tajk==NULL)return setret(tajk,-1,"调用tajk_closeall的参数为空值");
    if(tajk->fjk!=NULL)fclose(tajk->fjk);
    tajk->fjk=NULL;
    return 0;
}

static int tajk_readline(stru_tajk * tajk,int trim){//从fjk读入一行数据到lindata，去掉结尾的回车换行
    if(tajk->fjk==NULL)return setret(tajk,1,"文件没打开不能读取");
    if(fgets(tajk->linedata,sizeof(tajk->linedata),tajk->fjk)==NULL)return setret(tajk,1,"读文件错误");
    for(int i=strlen(tajk->linedata)-1;i>=0;i--){
        if(tajk->linedata[i]==0xd)tajk->linedata[i]=0;
        else if(tajk->linedata[i]==0xa)tajk->linedata[i]=0;
        else break;
    };
    if(trim)srtrim(tajk->linedata);//清除末尾的空格
    return 0;
}

stru_tajk * tajk_init(){
	stru_tajk * tajk=(stru_tajk *)malloc(sizeof(stru_tajk));
	if(tajk==NULL)return NULL;
	tajk->fjk=NULL;
	return tajk;
}

void tajk_free(stru_tajk *tajk){
	tajk_closeall(tajk);
	free(tajk);
}

void tajk_setmode(stru_tajk *tajk,int isidx,int ver,const char * mode,const char *send,const char *recv,const char *rq){//初始化
    int idf;
    tajk_closeall(tajk);
    tajk->isidx=isidx;
    tajk->ver=ver;
    strcpy(tajk->mode,mode);
    strcpy(tajk->sender,send);
    strcpy(tajk->recver,recv);
    strcpy(tajk->workday,rq);
    tajk->totalrecord=0;
    tajk->totalrecordpos=0;
    if(tajk->isidx)   {
    }else{
        tajk->stdlinesize=0;
        for(idf=tajk->fieldnum=0;tajk_datafile_field2[idf].ver;idf++){
            if(tajk_datafile_field2[idf].ver!=ver)continue;
            if(strcmp(tajk_datafile_field2[idf].filemode,mode)!=0)continue;

            strcpy(tajk->sd[tajk->fieldnum].name,tajk_datafile_field2[idf].name);
            tajk->sd[tajk->fieldnum].type=tajk_datafile_field2[idf].type;
            tajk->sd[tajk->fieldnum].size=tajk_datafile_field2[idf].size;
            tajk->sd[tajk->fieldnum].rratio=tajk->sd[tajk->fieldnum].wratio=1.0;
            for(int k=0;k<tajk_datafile_field2[idf].decpos;k++){
                tajk->sd[tajk->fieldnum].rratio=tajk->sd[tajk->fieldnum].rratio/10.0;
                tajk->sd[tajk->fieldnum].wratio=tajk->sd[tajk->fieldnum].wratio*10.0;
            };
            tajk->sd[tajk->fieldnum].pos=tajk->stdlinesize;
            tajk->stdlinesize=tajk->stdlinesize+tajk->sd[tajk->fieldnum].size;
            tajk->sd[tajk->fieldnum].cdata=NULL;
            tajk->sd[tajk->fieldnum].ddata=NULL;
            tajk->fieldnum++;
        };
        memset(tajk->linedata,' ',tajk->stdlinesize);
        tajk->linedata[tajk->stdlinesize]=0;//初始化输出用行缓冲区
    };
}

int tajk_writebegin(stru_tajk *tajk,const char * dirname,int batchnum,const char * fname){//开始写文件
    char fn[1024];
    if(tajk->isidx){//索引文件
        if(fname!=NULL)strcpy(tajk->fname,fname);
        else snprintf(tajk->fname,sizeof(tajk->fname),"%s_%s_%s_%s.TXT",tajk->mode,tajk->sender,tajk->recver,tajk->workday);
        snprintf(fn,sizeof(fn),"%s/%s",dirname,tajk->fname);
        tajk->fjk=fopen(fn,"w");
        if(tajk->fjk==NULL)return setret(tajk,-1,"打开文件%s写失败",fn);
        if(tajk->ver==21){
            fprintf(tajk->fjk,"%8s\r\n","OFDCFIDX");
            fprintf(tajk->fjk,"%-4s\r\n","21");
            fprintf(tajk->fjk,"%-9s\r\n",tajk->sender);
            fprintf(tajk->fjk,"%-9s\r\n",tajk->recver);
            fprintf(tajk->fjk,"%8s\r\n",tajk->workday);
            tajk->totalrecordpos=ftell(tajk->fjk);//记录位置，最后回写此处
            fprintf(tajk->fjk,"%03d\r\n",0);
        }else{
            fprintf(tajk->fjk,"%8s\r\n","OFDCFIDX");
            fprintf(tajk->fjk,"%-8d\r\n",tajk->ver);
            fprintf(tajk->fjk,"%-20s\r\n",tajk->sender);
            fprintf(tajk->fjk,"%-20s\r\n",tajk->recver);
            fprintf(tajk->fjk,"%8s\r\n",tajk->workday);
            tajk->totalrecordpos=ftell(tajk->fjk);//记录位置，最后回写此处
            fprintf(tajk->fjk,"%08d\r\n",0);
        };
    }else{
        if(fname!=NULL)strcpy(tajk->fname,fname);
        else {
            if(batchnum==0)snprintf(tajk->fname,sizeof(tajk->fname),"OFD_%s_%s_%s_%s.TXT",tajk->sender,tajk->recver,tajk->workday,tajk->mode);
            else snprintf(tajk->fname,sizeof(tajk->fname),"OFD_%s_%s_%s_%s_%03d.TXT",tajk->sender,tajk->recver,tajk->workday,tajk->mode,batchnum);
        };
        snprintf(fn,sizeof(fn),"%s/%s",dirname,tajk->fname);
        tajk->fjk=fopen(fn,"w");
        if(tajk->fjk==NULL)return setret(tajk,-1,"打开文件%s写失败",fn);
        if(tajk->ver==21){
            fprintf(tajk->fjk,"%8s\r\n","OFDCFDAT");
            fprintf(tajk->fjk,"%-4s\r\n","21");
            fprintf(tajk->fjk,"%-9s\r\n",tajk->sender);
            fprintf(tajk->fjk,"%-9s\r\n",tajk->recver);
            fprintf(tajk->fjk,"%8s\r\n",tajk->workday);
            fprintf(tajk->fjk,"%-3s\r\n",""); //汇总表号，不知道有什么用，有填写000的，有填写3个空格的，有填写999的
            fprintf(tajk->fjk,"%2s\r\n",tajk->mode);
            fprintf(tajk->fjk,"%-8s\r\n","");//发送机构中的某人
            fprintf(tajk->fjk,"%-8s\r\n","");//接收机构中的某人
            fprintf(tajk->fjk,"%03d\r\n",tajk->fieldnum);
        }else{
            fprintf(tajk->fjk,"%8s\r\n","OFDCFDAT");
            fprintf(tajk->fjk,"%-8d\r\n",tajk->ver);
            fprintf(tajk->fjk,"%-20s\r\n",tajk->sender);
            fprintf(tajk->fjk,"%-20s\r\n",tajk->recver);
            fprintf(tajk->fjk,"%8s\r\n",tajk->workday);
            fprintf(tajk->fjk,"%-8s\r\n",""); //汇总表号，不知道有什么用，还扩到8位了
            fprintf(tajk->fjk,"%-8s\r\n",tajk->mode);
            fprintf(tajk->fjk,"%-8s\r\n","");//发送机构中的某人
            fprintf(tajk->fjk,"%-8s\r\n","");//接收机构中的某人
            fprintf(tajk->fjk,"%08d\r\n",tajk->fieldnum);
        };
        for(int i=0;i<tajk->fieldnum;i++)fprintf(tajk->fjk,"%s\r\n",tajk->sd[i].name);
        tajk->totalrecordpos=ftell(tajk->fjk);//记录位置，最后回写此处
        tajk->totalrecord=0;
        if(tajk->ver==21){
            fprintf(tajk->fjk,"%08d\r\n",0);
        }else{
            fprintf(tajk->fjk,"%016d\r\n",0);
        };
    };
    return 0;
}

int tajk_writeidx(stru_tajk *tajk,const char *filemode,int batchnum){//在索引文件中写入一行
    char fn[100];
    if(batchnum==0){
        sprintf(fn,"OFD_%s_%s_%s_%s.TXT",tajk->sender,tajk->recver,tajk->workday,filemode);
    }else{
        sprintf(fn,"OFD_%s_%s_%s_%s_%03d.TXT",tajk->sender,tajk->recver,tajk->workday,filemode,batchnum);
    };
    fprintf(tajk->fjk,"%s\r\n",fn);
    tajk->totalrecord++;
    return 0;
}

int tajk_readfile(stru_tajk *tajk,int isidx,const char * dirname,const char * filename){//读入文件头
    char fn[1024];
    tajk_closeall(tajk);
    tajk->isidx=isidx;
    sprintf(fn,"%s/%s",dirname,filename);
    strcpy(tajk->fname,filename);
    tajk->fjk=fopen(fn,"r+");
    tajk->recordcount=0;
    tajk_retcode=0;//清retcode，方便后续根据retcode判断读过程中是否有错误
    if(tajk->fjk==NULL)   {//打开文件失败,尝试打开文件名大小写有差异的文件
        DIR *sdir;
        struct dirent *ptr;
        sdir=opendir(dirname);
        if(sdir==NULL)return setret(tajk,1,"打开目录%s错误",dirname);
        while((ptr=readdir(sdir))!=NULL){
            if(strcasecmp(ptr->d_name,filename)==0){
                sprintf(fn,"%s/%s",dirname,ptr->d_name);
                strcpy(ptr->d_name,filename);
                tajk->fjk=fopen(fn,"rt");
                break;
            };
        };
        closedir(sdir);
    };
    if(tajk->fjk==NULL)return setret(tajk,1,"目录%s下未找到文件%s",dirname,filename);
    if(tajk->isidx){
        tajk_readline(tajk,0);
        if(strncmp(tajk->linedata,"OFDCFIDX",8)!=0){
            tajk_closeall(tajk);
            return setret(tajk,1,"索引文件头应该是OFDCFIDX");
        };
        tajk_readline(tajk,1);
        sscanf(tajk->linedata,"%d",&tajk->ver);
        if(tajk->ver!=22)tajk->ver=21;//实践中发现有些人还在使用2.0接口，就等同2.1处理吧
        tajk_readline(tajk,1);
        strncpy(tajk->sender,tajk->linedata,sizeof(tajk->sender));
        tajk->sender[sizeof(tajk->sender)-1]=0;
        tajk_readline(tajk,1);
        strncpy(tajk->recver,tajk->linedata,sizeof(tajk->recver));
        tajk->recver[sizeof(tajk->recver)-1]=0;
        tajk_readline(tajk,1);
        strncpy(tajk->workday,tajk->linedata,sizeof(tajk->workday));
        tajk->workday[sizeof(tajk->workday)-1]=0;
        tajk_readline(tajk,1);
        if(tajk_retcode)return setret(tajk,1,"读索引文件出错");
        if(sscanf(tajk->linedata,"%d",&tajk->totalrecord)!=1)return setret(tajk,1,"读索引文件数据文件个数出错");
    }else{
        tajk_readline(tajk,0);
        if(strncmp(tajk->linedata,"OFDCFDAT",8)!=0){
            tajk_closeall(tajk);
            return setret(tajk,1,"数据文件头应该是OFDCFDAT");
        };
        tajk_readline(tajk,1);
        sscanf(tajk->linedata,"%d",&tajk->ver);
        if(tajk->ver!=22)tajk->ver=21;//实践中发现有些人还在使用2.0接口，就等同2.1处理吧
        tajk_readline(tajk,1);
        strncpy(tajk->sender,tajk->linedata,sizeof(tajk->sender)-1);
        tajk->sender[sizeof(tajk->sender)-1]=0;
        tajk_readline(tajk,1);
        strncpy(tajk->recver,tajk->linedata,sizeof(tajk->recver)-1);
        tajk->recver[sizeof(tajk->recver)-1]=0;
        tajk_readline(tajk,1);
        strncpy(tajk->workday,tajk->linedata,sizeof(tajk->workday)-1);
        tajk->workday[sizeof(tajk->workday)-1]=0;
        tajk_readline(tajk,1);
        tajk_readline(tajk,1);
        strncpy(tajk->mode,tajk->linedata,sizeof(tajk->mode));
        tajk->mode[sizeof(tajk->mode)-1]=0;
        tajk_readline(tajk,1);
        tajk_readline(tajk,1);
        tajk_readline(tajk,1);
        if(sscanf(tajk->linedata,"%d",&tajk->fieldnum)!=1){
            tajk_closeall(tajk);
            return setret(tajk,1,"读数据文件出错，未能正确读入字段数量");
        };
        tajk->stdlinesize=0;
        for(int i=0;i<tajk->fieldnum;i++){
            tajk_readline(tajk,1);
            tajk->sd[i].size=0;//供判断是否读到数据
            for(int j=0;tajk_datafile_field2[j].ver;j++){
                if(tajk_datafile_field2[j].ver!=tajk->ver)continue;
                if(strcasecmp(tajk_datafile_field2[j].filemode,tajk->mode)!=0)continue;
                if(strcasecmp(tajk_datafile_field2[j].name,tajk->linedata)!=0)continue;
                
                strcpy(tajk->sd[i].name,tajk_datafile_field2[j].name);
                tajk->sd[i].type=tajk_datafile_field2[j].type;
                tajk->sd[i].size=tajk_datafile_field2[j].size;
                tajk->sd[i].rratio=tajk->sd[i].wratio=1.0;
                for(int k=0;k<tajk_datafile_field2[j].decpos;k++){
                    tajk->sd[i].rratio=tajk->sd[i].rratio/10.0;
                    tajk->sd[i].wratio=tajk->sd[i].wratio*10.0;
                };
                tajk->sd[i].pos=tajk->stdlinesize;
                tajk->stdlinesize=tajk->stdlinesize+tajk->sd[i].size;
                tajk->sd[i].cdata=NULL;
                tajk->sd[i].ddata=NULL;
                break;
            };
            if(tajk->sd[i].size==0){//没有找到相应字段
                tajk_closeall(tajk);
                return setret(tajk,1,"接口字段表中没有找到字段%s",tajk->linedata);
            };
        };
        if(tajk_retcode)return setret(tajk,1,"读数据文件出错");
        memset(tajk->linedata,' ',tajk->stdlinesize);
        tajk->linedata[tajk->stdlinesize]=0;//初始化输出用行缓冲区
        tajk->totalrecordpos=ftell(tajk->fjk);//记录位置，最后回写此处
        tajk_readline(tajk,1);
        if(sscanf(tajk->linedata,"%d",&tajk->totalrecord)!=1)return setret(tajk,1,"读数据文件数据行数出错");
        	//这里似乎要注意，如果原始文件不标准，会造成后续写入不正确！
    };
    return 0;
}

int tajk_readfile2(stru_tajk *tajk,int isidx,const char * dirname,const char * mode,const char * send,const char * recv,const char *rq,int batchnum){//读入文件头
    static char fn[1024];
    if(isidx){
        snprintf(fn,sizeof(fn),"%s_%s_%s_%s.TXT",mode,send,recv,rq);
    }else{
        if(batchnum){
            snprintf(fn,sizeof(fn),"OFD_%s_%s_%s_%s_%03d.TXT",send,recv,rq,mode,batchnum);
        }else{
            snprintf(fn,sizeof(fn),"OFD_%s_%s_%s_%s.TXT",send,recv,rq,mode);
        };
    };
    return tajk_readfile(tajk,isidx,dirname,fn);
}

int tajk_readidx(stru_tajk *tajk,char *fname,char * fmode,int *batchnum){//读入一行索引文件
    char t[10],s[100],r[100],rq[100],m[10];
    int b,i;
    tajk_readline(tajk,1);
    sscanf(tajk->linedata,"%50s",fname);
    i=sscanf(tajk->linedata,"%3[^_]_%10[^_]_%10[^_]_%10[^_]_%2[^_]_%d",t,s,r,rq,m,&b);
    if(i!=5 && i!=6)return setret(tajk,1,"索引中数据文件名%s错误",tajk->linedata);
    if(strcmp(s,tajk->sender)!=0)return setret(tajk,1,"索引中数据文件名%s错误,发送方不是%s",tajk->linedata,tajk->sender);
    if(strcmp(r,tajk->recver)!=0)return setret(tajk,1,"索引中数据文件名%s错误,接收方不是%s",tajk->linedata,tajk->recver);
    if(strcmp(rq,tajk->workday)!=0)return setret(tajk,1,"索引中数据文件名%s错误,日期不是%s",tajk->linedata,tajk->workday);
    strcpy(fmode,m);
    if(i==5)b=0;
    if(batchnum!=NULL){
        if(i==6)*batchnum=b;
        else *batchnum=0;
    };
    tajk->recordcount++;
    if(tajk->recordcount>=tajk->totalrecord){//已经处理完了
        tajk_readline(tajk,1);
        tajk_closeall(tajk);
        if(strcmp(tajk->linedata,"OFDCFEND")!=0)return setret(tajk,1,"索引文件结尾错误，第%d行不是'OFDCFEND',而是'%s'",tajk->recordcount,tajk->linedata);
    };
    return 0;
}

int tajk_bind(stru_tajk * tajk,const char *name,void * data,short *indi) {//通用的绑定字段和数据的函数，计划淘汰掉另外两个
    for(int i=0;i<tajk->fieldnum;i++){//
        if(strcasecmp(tajk->sd[i].name,name)==0){
            if(tajk->sd[i].type=='N')   {//字符型
                tajk->sd[i].ddata=data;
            }else{
                tajk->sd[i].cdata=data;
            };
            if(indi==NULL)tajk->sd[i].indi=&tajk->sd[i].ind;
            else tajk->sd[i].indi=indi;
            return 0;
        };
    };
    return setret(tajk,-1,"bind函数未找到%s字段",name);
}

int tajk_bindc(stru_tajk * tajk,const char *name,char * data){//把字段和数据绑定用于快速写数据
    for(int i=0;i<tajk->fieldnum;i++){//
        if(strcasecmp(tajk->sd[i].name,name)==0){
            tajk->sd[i].cdata=data;
            return 0;
        };
    };
    return setret(tajk,-1,"bind函数未找到%s字段",name);
}

int tajk_bindd(stru_tajk * tajk,const char *name,double * data,double dft,short *indi){//把字段和数据绑定用于快速写数据
    for(int i=0;i<tajk->fieldnum;i++){//
        if(strcasecmp(tajk->sd[i].name,name)==0){
            tajk->sd[i].ddata=data;
            tajk->sd[i].valdft=dft;
            if(indi==NULL)tajk->sd[i].indi=&tajk->sd[i].ind;
            else tajk->sd[i].indi=indi;
            return 0;
        };
    };
    return setret(tajk,-1,"bind函数未找到%s字段",name);
}

int tajk_setd(stru_tajk * tajk,const char * colname,double val){//根据字段名设置浮点数据
    int i;
    char temp[1000];
    for(i=0;i<tajk->fieldnum;i++){//
        if(strcasecmp(tajk->sd[i].name,colname)==0){
            sprintf(temp,"%0*.0lf",tajk->sd[i].size,val * tajk->sd[i].wratio);
            memcpy(tajk->linedata+tajk->sd[i].pos,temp,tajk->sd[i].size);
            return 0;
        };
    };
    return setret(tajk,-1,"字段名%s在接口文件中没找到",colname);
}

int tajk_sets(stru_tajk * tajk,const char * colname,const char * val){//根据字段名设置字符串
    int i,k;
    char sgbk[4000];
    for(i=0;i<tajk->fieldnum;i++){
        if(strcasecmp(colname,tajk->sd[i].name)!=0)continue;
        memset(tajk->linedata+tajk->sd[i].pos,' ',tajk->sd[i].size);
        u2g(val,sgbk);
        k=strlen(sgbk);
        if(k>=tajk->sd[i].size)k=tajk->sd[i].size;
        memcpy(tajk->linedata+tajk->sd[i].pos,sgbk,k);
        return 0;
    };
    return setret(tajk,-1,"字段名%s在接口文件中没找到",colname);
}

int tajk_readdata(stru_tajk * tajk){//读入一行数据文件
    char data[3000];
    tajk->recordcount++;
    tajk_readline(tajk,0);
    if((int)strlen(tajk->linedata)!=tajk->stdlinesize)return setret(tajk,1,"第%d行长度不对，应该是%d，实际是%d",tajk->recordcount,tajk->stdlinesize,strlen(tajk->linedata));
    for(int i=0;i<tajk->fieldnum;i++){
        if(tajk->sd[i].cdata==NULL && tajk->sd[i].ddata==NULL)continue;
        memcpy(data,tajk->linedata+tajk->sd[i].pos,tajk->sd[i].size);//读入字段
        data[tajk->sd[i].size]=0;//结尾清0
        srtrim(data);//清除结尾的空白
        if(tajk->sd[i].type=='C' || tajk->sd[i].type=='A'){//字符型
            if(tajk->sd[i].cdata!=NULL)strcpy(tajk->sd[i].cdata,data);
            if(data[0])*tajk->sd[i].indi=0;
            else *tajk->sd[i].indi=-1;
        }else{
            if(tajk->sd[i].ddata!=NULL){
                if(sscanf(data,"%lf",tajk->sd[i].ddata)==1){//正常读入数据
                    *tajk->sd[i].ddata=*tajk->sd[i].ddata * tajk->sd[i].rratio;
                    *tajk->sd[i].indi=0;
                }else{
//                    *tajk->sd[i].ddata=tajk->sd[i].valdft;//设置为默认值
                    *tajk->sd[i].ddata=0;//设置为0
                    *tajk->sd[i].indi=-1;
                };
            };
        };
    };
    if(tajk->recordcount>=tajk->totalrecord){//已经处理完了
        tajk_readline(tajk,1);
        tajk_closeall(tajk);
        if(strcmp(tajk->linedata,"OFDCFEND")!=0)return setret(tajk,1,"数据文件结尾错误，第%d行不是'OFDCFEND',而是'%s'",tajk->recordcount,tajk->linedata);
    };
    return 0;
}

int tajk_writedata(stru_tajk * tajk){//数据文件写入一行数据
    int i,k;
    char temp[10000];
    for(i=0;i<tajk->fieldnum;i++){
        if(tajk->sd[i].cdata==NULL && tajk->sd[i].ddata==NULL)continue;
        memset(tajk->linedata+tajk->sd[i].pos,' ',tajk->sd[i].size);
        if(tajk->sd[i].type=='C' || tajk->sd[i].type=='A'){//字符型
            k=strlen(tajk->sd[i].cdata);
            if(k>=tajk->sd[i].size)k=tajk->sd[i].size;
            memcpy(tajk->linedata+tajk->sd[i].pos,tajk->sd[i].cdata,k);
        }else {//数字型
            if(tajk->sd[i].indi==NULL || *tajk->sd[i].indi==0){//未指定指示变量
                sprintf(temp,"%0*.0lf",tajk->sd[i].size,*tajk->sd[i].ddata * tajk->sd[i].wratio);
                memcpy(tajk->linedata+tajk->sd[i].pos,temp,tajk->sd[i].size);
            }else{
                memset(tajk->linedata+tajk->sd[i].pos,0x20,tajk->sd[i].size);
            };
        };
    };
    fprintf(tajk->fjk,"%s\r\n",tajk->linedata);
    tajk->totalrecord++;
    return 0;
}

int tajk_writeend(stru_tajk * tajk){//结束写文件，包括写文件尾、记录数处理、关闭文件等
    fprintf(tajk->fjk,"OFDCFEND\r\n");
    fseek(tajk->fjk,tajk->totalrecordpos,SEEK_SET);
    if(tajk->isidx){
        if(tajk->ver==21){
            fprintf(tajk->fjk,"%03d",tajk->totalrecord);
        }else{
            fprintf(tajk->fjk,"%08d",tajk->totalrecord);
        };
    }else{
        if(tajk->ver==21){
            fprintf(tajk->fjk,"%08d",tajk->totalrecord);
        }else{
            fprintf(tajk->fjk,"%016d",tajk->totalrecord);
        };
    };
    fclose(tajk->fjk);
    tajk->fjk=NULL;
    return 0;
}
