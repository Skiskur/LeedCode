#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char * intToRoman(int num);
void appendChar(char * str, char c);

int main(int argc, char const *argv[]) {
    
    int input = 58;
    char* result = intToRoman(input);
    printf("%d morfs into -> \"%s\"\n", input, result);

    free(result);

    return 0;
}


char * intToRoman(int num) {

    char* result = (char*) calloc(30, sizeof(char));

    while (num > 0) {
        if (num >= 1000) {
            num = num - 1000;
            appendChar(result, 'M');
        } else if (num >= 900) {
            num = num - 900;
            appendChar(result, 'C');
            appendChar(result, 'M');
        } else if (num >= 500) {
            num = num - 500;
            appendChar(result, 'D');
        } else if (num >= 400) {
            num = num - 400;
            appendChar(result, 'C');
            appendChar(result, 'D');
        } else if (num >= 100) {
            num = num - 100;
            appendChar(result, 'C');
        } else if (num >= 90) {
            num = num - 90;
            appendChar(result, 'X');
            appendChar(result, 'C');
        } else if (num >= 50) {
            num = num - 50;
            appendChar(result, 'L');
        } else if (num >= 40) {
            num = num - 40;
            appendChar(result, 'X');
            appendChar(result, 'L');
        } else  if (num >= 10) {
            num = num - 10;
            appendChar(result, 'X');
        } else if (num >= 9) {
            num = num - 9;
            appendChar(result, 'I');
            appendChar(result, 'X');
        } else  if (num >= 5) {
            num = num - 5;
            appendChar(result, 'V');
        } else if (num >= 4) {
            num = num - 4;
            appendChar(result, 'I');
            appendChar(result, 'V');
        } else  if (num >= 1) {
            num = num - 1;
            appendChar(result, 'I');
        }
    }
    

    return result;
}

void appendChar(char * str, char c) {
    size_t len = strlen(str);
    str[len] = c;
    str[len + 1] = '\0';
}