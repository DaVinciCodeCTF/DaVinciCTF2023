#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char** argv) {
    srand(time(0));

    if (argc < 2){
        printf("./program <input>");
        return 0;
    } 

    int key = rand() % 0x424242;
    
    printf("Key: %d", key);

    char* input = argv[1];
    for(int i = 0; i < strlen(input); i++) {
        input[i] = (input[i] ^ (key + i)) & 0xFF;
    }

    FILE* fptr = fopen("enc.txt","w");

    if(fptr == NULL)
    {
        printf("Error!");   
        exit(1);             
    }

   fprintf(fptr,"%s", input);

   fclose(fptr);


}
