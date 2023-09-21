//Program to find the duplicates in the array

/*

output:

Enter the length of array : 5
Enter the elements of the array : 1 1 2 2 3 
Duplicate pair 1 and the value is 1 and 1
Duplicate pair 2 and the value is 2 and 2
There are 2 duplicates in the array

*/


#include<stdio.h>

//Function to find the duplicates
int duplicatechecker(int arr[],int length)
{
    int count=0;
    for (int i=0;i<length;i++)
    {
        for (int j=0;j<length;j++)
            if (j>i)
                if (arr[i]==arr[j])
                {
                    count++;
                    printf("\nDuplicate pair %d and the value is %d and %d",count,arr[i],arr[j]);
                }
    }
    return count;
}

//main function
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