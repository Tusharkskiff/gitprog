//Program to take a input from user, to see if we get the same when two elements of array are added
#include<stdio.h>

int check(int arr[],int tar,int leng);

int main()
{
    int arr[10],leng,tar,ans=0;
    printf("Enter the length of single array : ");
    scanf("%d",&leng);
    printf("Enter the elements : ");
    for(int i=0;i<leng;i++)
    {
        scanf("%d",&arr[i]);
    }

    printf("Enter the target elemnt : ");
    scanf("%d",&tar);

    ans=check(arr,tar,leng);
    
    if(ans>0)
    printf("\nwe got %d pairs",ans);
    else
    printf("\nNo pair found");

    return 0;

}


//Function to check

int check(int arr[],int tar,int leng)
{
    int a,b,count=0;
    for(int i=0;i<leng;i++)
    {
        for(int j=0;j<leng;j++)
        {
            if(j>i)
            {
                if((arr[i]+arr[j]==tar))
                {
                    a=arr[i];
                    b=arr[j];
                    printf("\nThe pair is %d,%d",a,b);
                    count++;
                }
                else
                {
                    continue;
                }
            }
        }
    }

    if(count>0)
    return count;
    else
    return 0;
}