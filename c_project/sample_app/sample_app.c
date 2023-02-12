/**********************************************************************
 * Includes
**********************************************************************/
#include <stdio.h>
// For getopt()
#include <unistd.h>
// For strtol()
#include <stdlib.h>
// For libsample.so
#include "sample_lib.h"


/**********************************************************************
 * Macros
**********************************************************************/
#define ARG_NUM (2)     // Number of arguments


/**********************************************************************
 * Enums
**********************************************************************/
typedef enum en_opreration {
    ADDITION,
    SUBTRACTION,
    MULTIPLICATION,
    DIVISION,
    INVALID
} EN_OPERATION;


int main(int argc, char *argv[]) {
    int opt;
    int a, b;
    int ret = 0;
    EN_OPERATION op = INVALID;

    // Parse options
    while ((opt = getopt(argc, argv, "o:")) != -1) {
        switch (opt) {
            case 'o':
                op = (EN_OPERATION)strtol(optarg, NULL, 10);
                break;
            default:
                break;
        }
    }

    // Search arguments location
    argc -= optind;     // Number of arguments
    argv += optind;     // Pointer of first atguments
    if (argc != ARG_NUM) {
        printf("Invalid arguments\n");
        ret = -1;
    } else {
        // Get arguments
        a = (int)strtol(argv[0], NULL, 10);
        b = (int)strtol(argv[1], NULL, 10);

        // Calculate
        switch(op) {
            case ADDITION:
                printf("%d + %d = %d\n", a, b, sample_add(a, b));
                break;
            case SUBTRACTION:
                printf("%d - %d = %d\n", a, b, sample_sub(a, b));
                break;
            case MULTIPLICATION:
                printf("%d * %d = %d\n", a, b, sample_mul(a, b));
                break;
            case DIVISION:
                printf("%d / %d = %f\n", a, b, sample_div(a, b));
                break;
            default:
                printf("Invalid operation\n");
                ret = -1;
                break;
        }
    }

    return ret;
}
