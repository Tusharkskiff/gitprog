//program to rotate an array elemnts

/*

output:


Enter the size of array : 5
Enter the elements of the array : 1 2 3 4 5
round 0 : 	 1 	 2 	 3 	 4 	 5 
Rotation starts
round 1 : 	 2 	 3 	 4 	 5 	 1 
round 2 : 	 3 	 4 	 5 	 1 	 2 
round 3 : 	 4 	 5 	 1 	 2 	 3 
round 4 : 	 5 	 1 	 2 	 3 	 4 
Rotation ends
round 5 : 	 1 	 2 	 3 	 4 	 5 

*/

#include<stdio.h>

//function to rotate the elements in the array
void rotate(int arr[],int length)
{
    int temp;
    
    for(int i=0;i<length;i++)
    {
        temp=arr[0];

        for(int j=0;j<length-1;j++)
        {
            arr[j]=arr[j+1];
        }
        arr[length-1]=temp;
        

        if(i==length-1)
            printf("\nRotation ends");


        printf("\nround %d : ",i+1);
        for(int k=0;k<length;k++)
            printf("\t %d ",arr[k]);
    }
}

//main function
int main()
{
    int arr[100],length;

    printf("Enter the size of array : ");
    scanf("%d",&length);

    printf("\nEnter the elements of the array : ");

    for(int i = 0 ; i < length ; i++)
        scanf("%d",&arr[i]);
    
    
    printf("\nround 0 : ");
        for(int i=0;i<length;i++)
            printf("\t %d ",arr[i]);
    printf("\nRotation starts");

    rotate(arr,length);
}