//Program to find the duplicates in the array
#include<stdio.h>

int duplicatechecker(int arr[],int length);//function prototype

int main()
{
    int arr[100],length,count;

    printf("Enter the length of array : ");
    scanf("%d",&length);

    printf("Enter the elements of the array : ");
    for (int i=0;i<length;i++)
    {
        scanf("%d",&arr[i]);
    }

    count=duplicatechecker(arr,length);

    if (count>0)
        printf("\nThere are %d duplicates in the array",count);
    else
        printf("\nThere are no duplicates in the array");

    return 0;
}


//Function tom find the duplicates

int duplicatechecker(int arr[],int length)
{
    int count=0;
    for (int i=0;i<length;i++)
    {
        for (int j=0;j<length;j++)
        {
            if (j>i)
            {
                if (arr[i]==arr[j])
                {
                    count++;
                    printf("\nDuplicate pair %d and the value is %d and %d",count,arr[i],arr[j]);
                }
            }
        }
    }
    return count;
}