#include"iostream"
int main(int argc,char**argv)
{
    std::cout<<"参数名字="<<argc<<std::endl;
    std::cout<<"程序名字="<<argv[0]<<std::endl;
    std::string argl=argv[1];
    if(argl =="--help")
    {
        std::cout<<"这里是程序帮助，但是这个程序什么用都没有"<<std::endl;
    }
    return 0;
}