# General settings
ARTIFACT = libsample.so
RM = rm -rf

# Program settings
SRC = sample_lib.c
ASM = sample_lib.s
OBJ = sample_lib.o

# Build settings
CC = gcc
CFLAGS = -Wall
CFLAGS_release = -O2
CFLAGS_debug = -O0 -g2
CFLAGS += $(CFLAGS_debug)
INCLUDE = -I.
# LDFLAGS = -L./sample_lib
# LIBS = -lsample

# NOTE: -o: Use only one output file.

all:$(ARTIFACT)

$(ARTIFACT):$(SRC)
	$(CC) $(SRC) -shared -fPIC -o $(ARTIFACT) $(CFLAGS) $(INCLUDE) $(LDFLAGS) $(LIBS)

asm:$(SRC)
	$(CC) $(SRC) -S -o $(ASM) $(CFLAGS) $(INCLUDE)

obj:$(SRC)
	$(CC) $(SRC) -c -o $(OBJ) $(CFLAGS) $(INCLUDE)

clean:
	$(RM) $(ASM) $(OBJ) $(ARTIFACT)
