/*
字节跳动面试:流媒体服务器开发实习生-视频架构
N个数求和
***************************************
INPUT:
5
2/5 4/15 1/30 -2/60 8/3
OUTPUT:
3 1/3
*/
/* Note:Your choice is C IDE */
#include "stdio.h"
//最大公因数
long long g(long long m,long long n)
{
	if(n==0) return m;
	else return g(n,m%n);
}
//最小公倍数
long long h(long long m,long long n)
{
	long long max;
	max = m*n;
	max = max/(g(m,n));
	return max;
}
int main()
{
	
	int p;//输入的数量
	long long a,b;//第一对数字
	long long m,n;//后面的数字
	long long f,z,x;//分母，分子，结果的化简形式
	scanf("%d",&p);
	scanf("%lld/%lld",&a,&b);
	p--;
	while(p)
	{
		scanf("%lld/%lld",&m,&n);
		p--;
		//正常运算
		f =h(n,b);
		a = a*(f/b);
		m = m*(f/n);
		// 得出结果                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
		a = a+m;
		b = f;
		//约分结果
		x = g(a,b);
		a = a/x;
		b = b/x;
	}
	// 分子刚好被分母整除
	if(a%b==0)
	{
		printf("%lld",a/b);
	}
	//假分数
	else if(a>b)
	{
		int t;
		t = a/b;
		a = a-t*b;
		printf("%lld %lld/%lld",t,a,b);
	}
	else
	 printf("%lld/%lld",a,b);
 return 0;   
}
