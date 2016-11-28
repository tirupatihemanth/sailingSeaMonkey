enc: encrypt.c aes_core.c aes.h
	gcc encrypt.c -o encrypt
	@echo "Compiled. To run use ./encrypt <ipfile> <keyfile> <encfile>"
dec: decrypt.c aes_core.c aes.h
	gcc decrypt.c -o decrypt
	@echo "Compiled. To run use ./decrypt <encfile> <keyfile> <decfile>"
encrypt: 
	./encrypt alice.txt aes.key alice.encrypt
	@echo "encrypted alice.txt using key=aes.key to alice.encrypt"
decrypt:
	./decrypt alice.encrypt aes.key alice.decrypt
	@echo "decrypted alice.encrypt using key=aes.key to alice.decrypt"
pic:
	./encrypt pic.jpg aes.key pic.encrypt
	@echo "encrypted pic.jpg using key=aes.key to pic.encrypt"
depic:
	./decrypt pic.encrypt aes.key pic.decrypt
	@echo "decrypted pic.encrypt using key=aes.key to pic.decrypt"
clean:
	rm -f encrypt decrypt *.encrypt *.decrypt

.PHONY: enc dec encrypt decrypt pic depic clean
