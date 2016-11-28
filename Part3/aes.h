#ifndef AES_H
#define AES_H

#define BYTE_SIZE sizeof(unsigned char)


/*block size = 4 bytes*/
#define BLOCK_SIZE (BYTE_SIZE*4)
/*128 bit key*/
#define KEY_SIZE (sizeof(unsigned char)*16)
#define NUM_ROUNDS 10
/*2x2 MDS matrix*/
#define MDS_SIZE 2

typedef unsigned char byte;

void xorState(byte *, byte *);
void shiftRows(byte *);
void rKeyGen(byte *mKey, byte rKey[][BLOCK_SIZE]);

#endif