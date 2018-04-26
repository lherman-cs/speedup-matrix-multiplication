CC= gcc
CFLAGS= -O0
PROG= matmul_opt
SRC= $(PROG).c
OBJECTS= $(PROG).o

$(PROG): $(OBJECTS)
	$(CC) -o $@ $?

$(OBJECTS): $(SRC)
	$(CC) $(CFLAGS) -c $?

