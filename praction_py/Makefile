CC = gcc
CFLAGS = -Wall -Wextra -std=c99 -pedantic -I.

myfunc.o: myfunc.c myfunc.h
	$(CC) $(CFLAGS) -c myfunc.c -o myfunc.o

hw0301: hw0301.c myfunc.o
	$(CC) $(CFLAGS) hw0301.c myfunc.o -o hw0301

clean:
	rm -f *.o hw0301
