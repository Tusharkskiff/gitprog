#include<stdio.h>
//0 1 1 2 3 5 8 


void get_fibo(int n)
{
    int a,b,c,element_no=3;

    if(n==1)
        printf("The 1st element is 0");
    else if(n==2)
        printf("The 2nd element is 1 ");
    else
        {   
            a=0;
            b=1;
            while(element_no<=n)
            {
                c=a+b;
                a=b;
                b=c;
                element_no++;
            }
            
            printf("The %dth element is %d",n,c);
        }

}

int main()
{
    int n;

    printf("Series reference : 0, 1, 1, 2, 3, 5, 8, 13...");

    printf("\nEnter the Nth number : ");
    scanf("%d",&n);

    if(n<1)
    {
        printf("\nInvalid input");
        exit(0);
    }

    get_fibo(n);

    return 0;
}