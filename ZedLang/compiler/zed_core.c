#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void compile_to_asm(char* zed_file, char* asm_file) {
    FILE* in = fopen(zed_file, "r");
    FILE* out = fopen(asm_file, "w");
    char line[256];

    fprintf(out, ".section .data\nmsg: .ascii \"WhyzeD Sovereign Binary Active\\n\"\n\n");
    fprintf(out, ".section .text\n.global _start\n\n_start:\n");

    while (fgets(line, sizeof(line), in)) {
        if (line[0] == '#' || strlen(line) < 3) continue;

        // Command: Speak
        if (strncmp(line, "Speak", 5) == 0) {
            fprintf(out, "    mov x0, #1\n    adrp x1, msg\n    add x1, x1, :lo12:msg\n    mov x2, #30\n    mov x8, #64\n    svc #0\n");
        }
        // Command: Exit
        else if (strncmp(line, "Exit", 4) == 0) {
            fprintf(out, "    mov x0, #0\n    mov x8, #93\n    svc #0\n");
        }
    }
    fclose(in); fclose(out);
}

int main(int argc, char** argv) {
    if (argc < 3) return 1;
    compile_to_asm(argv[1], "temp.s");
    system("as temp.s -o temp.o && ld temp.o -o bin_out && rm temp.s temp.o");
    rename("bin_out", argv[2]);
    printf("ZeDc²: Sovereign Binary [%s] Generated.\n", argv[2]);
    return 0;
}
