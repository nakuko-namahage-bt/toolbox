# General settings
ARTIFACT = sample_app

# Program settings
SRC = sample_app.c
ASM = sample_app.s
OBJ = sample_app.o

# Build settings
CC = gcc
CFLAGS = -Wall
CFLAGS_release = -O2
CFLAGS_debug = -O0 -g2
CFLAGS += $(CFLAGS_debug)
INCLUDE = -I../sample_lib
LDFLAGS = -L../sample_lib
LIBS = -lsample

# NOTE: -o: Use only one output file.

all:$(ARTIFACT)

$(ARTIFACT):$(SRC)
	$(CC) $(SRC) -o $(ARTIFACT) $(CFLAGS) $(INCLUDE) $(LDFLAGS) $(LIBS)

asm:$(SRC)
	$(CC) $(SRC) -S -o $(ASM) $(CFLAGS) $(INCLUDE)

obj:$(SRC)
	$(CC) $(SRC) -c -o $(OBJ) $(CFLAGS) $(INCLUDE)

clean:
	rm -rf $(ASM) $(OBJ) $(ARTIFACT)
